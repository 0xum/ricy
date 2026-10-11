"""Local operations with backup for Ricy's appearance contribution."""
import datetime
import json
import os
from pathlib import Path
import re
import shutil

BASE = Path(__file__).resolve().parent


def merge_ini(text, groups):
    """Replace only the given keys; preserve groups and comments from others."""
    lines = text.splitlines(keepends=True)
    for group, values in groups.items():
        header = '[' + group + ']'
        matches = [i for i, line in enumerate(lines) if line.strip() == header]
        if len(matches) > 1:
            raise ValueError('Grupo duplicado: ' + header)
        if not matches:
            if lines and not lines[-1].endswith('\n'):
                lines[-1] += '\n'
            lines += ['\n', header + '\n']
            start = len(lines)
        else:
            start = matches[0] + 1
        end = next((i for i in range(start, len(lines)) if lines[i].lstrip().startswith('[')), len(lines))
        body = lines[start:end]
        for key, value in values.items():
            pattern = re.compile(r'^\s*' + re.escape(key) + r'\s*=')
            # GTK gerado por nwg-look pode ter a mesma chave repetida.
            body = [line for line in body if not pattern.match(line)]
            if body and not body[-1].endswith('\n'):
                body[-1] += '\n'
            body.append(f'{key}={value}\n')
        lines[start:end] = body
    return ''.join(lines)


def read_text(path):
    return path.read_text() if path.exists() else ''


def target(root, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Invalid path: ' + relative)
    path = root / rel
    # It prevents --root/--home from writing out of destination by a link.
    for parent in path.parents:
        if parent == root:
            break
        if parent.is_symlink():
            raise ValueError('Destination directory is a link: ' + str(parent))
    return path


def remove(path):
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_symlink():
        destination.symlink_to(os.readlink(source))
    elif source.is_dir():
        shutil.copytree(source, destination, symlinks=True)
    else:
        shutil.copy2(source, destination)


def apply(root, operations, backup_parent, scope):
    """Validate fonts, save the state of destination and apply a finite list."""
    paths = []
    for relative, content in operations:
        paths.append(target(root, relative))
        if isinstance(content, Path) and not content.exists():
            raise FileNotFoundError(content)
    backup = backup_parent / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    manifest = {'root': str(root), 'scope': scope, 'entries': []}
    for index, ((relative, _), path) in enumerate(zip(operations, paths)):
        exists = path.exists() or path.is_symlink()
        entry = {'path': relative, 'exists': exists, 'item': str(index)}
        if exists:
            copy(path, backup / 'items' / str(index))
            if os.geteuid() == 0:
                members = [path] + (list(path.rglob('*')) if path.is_dir() and not path.is_symlink() else [])
                entry['owners'] = {
                    str(member.relative_to(path)): [member.lstat().st_uid, member.lstat().st_gid]
                    for member in members
                }
        manifest['entries'].append(entry)
    manifest_path = backup / 'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    manifest_path.chmod(0o600)
    try:
        for (_, content), path in zip(operations, paths):
            remove(path)
            if isinstance(content, Path):
                copy(content, path)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    except Exception:
        restore(root, backup, scope, [relative for relative, _ in operations])
        raise
    print('Backup:', backup)
    return backup


def restore(root, backup, scope, allowed):
    manifest = json.loads((backup / 'manifest.json').read_text())
    if manifest['root'] != str(root) or manifest['scope'] != scope:
        raise ValueError('Backup pertence a outro destino ou escopo.')
    for entry in manifest['entries']:
        if entry['path'] not in allowed or not entry['item'].isdigit():
            raise ValueError('Invalid backup input.')
        target(root, entry['path'])
        if entry['exists']:
            source = backup / 'items' / entry['item']
            if not (source.exists() or source.is_symlink()):
                raise FileNotFoundError(source)
    for entry in reversed(manifest['entries']):
        path = target(root, entry['path'])
        remove(path)
        if entry['exists']:
            copy(backup / 'items' / entry['item'], path)
            if os.geteuid() == 0:
                for relative, owner in entry.get('owners', {}).items():
                    child = Path(relative)
                    if child.is_absolute() or '..' in child.parts:
                        raise ValueError('Invalid path in ownership backup.')
                    os.chown(path / child, *owner, follow_symlinks=False)
    print('Previous status restored from', backup)
