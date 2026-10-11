#!/usr/bin/env python3
"""Datas em inglês; localização fixa Cosmópolis/SP; clima e calendário Noctalia."""
from datetime import datetime
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tomllib

PREFERENCES = {
    'shell': {'lang': 'en'},
    'location': {'auto_locate': False, 'address': 'Cosmopolis, Sao Paulo, Brazil'},
    'weather': {'enabled': True, 'unit': 'metric'},
    'calendar': {'enabled': True},
}


def update_toml(text):
    """Edit only owned scalar keys, retaining account tables and other preferences."""
    tomllib.loads(text)
    for section, values in PREFERENCES.items():
        headers = list(re.finditer(r'(?m)^\[[^\n]+\][ \t]*$', text))
        header = next((m for m in headers if m.group().strip() == '[' + section + ']'), None)
        if header is None:
            text = text.rstrip() + '\n\n[' + section + ']\n'
            start, end = len(text), len(text)
        else:
            start = header.end()
            end = next((m.start() for m in headers if m.start() > header.start()), len(text))
        body = text[start:end]
        for key, value in values.items():
            encoded = str(value).lower() if isinstance(value, bool) else json.dumps(value, ensure_ascii=False)
            line = key + ' = ' + encoded
            pattern = re.compile(r'(?m)^' + re.escape(key) + r'[ \t]*=[^\n]*$')
            if pattern.search(body):
                body = pattern.sub(lambda _: line, body)
            else:
                body = body.rstrip() + '\n' + line + '\n\n'
        text = text[:start] + body + text[end:]
    parsed = tomllib.loads(text)
    for section, values in PREFERENCES.items():
        for key, value in values.items():
            assert parsed[section][key] == value
    return text


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    temporary = path.with_name(path.name + '.ricy-novo')
    temporary.write_text(content)
    temporary.chmod(mode)
    temporary.replace(path)


def main():
    if os.geteuid() == 0:
        raise SystemExit('Execute como usuário da sessão, sem sudo.')
    locales = subprocess.check_output(['locale', '-a'], text=True).lower().replace('-', '')
    if 'en_us.utf8' not in locales:
        raise SystemExit('Gere a locale en_US.UTF-8 antes de aplicar.')
    home = Path.home()
    integration = home / 'ricy-kit/contributions/noctalia-kde-integration-and-menus'
    profile = integration / 'work/noctalia-profile'
    config = profile / 'config/noctalia/config.toml'
    settings = profile / 'state/noctalia/settings.toml'
    if not config.is_file():
        raise SystemExit('Prepare primeiro o perfil da integração permanente deste kit.')
    unit = Path(os.environ.get('XDG_CONFIG_HOME', home / '.config')) / 'systemd/user/noctalia-teste.service.d/60-ricy-idioma-localizacao.conf'
    paths = {'config.toml': config, 'settings.toml': settings, '60-ricy-idioma-localizacao.conf': unit}
    originals = {name: path.read_text() if path.exists() else None for name, path in paths.items()}
    updated = {name: update_toml(originals[name] or '') for name in ('config.toml', 'settings.toml')}
    state = Path(os.environ.get('XDG_STATE_HOME', home / '.local/state'))
    backup = state / 'ricy-idioma-localizacao-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    for name, path in paths.items():
        if path.exists():
            shutil.copy2(path, backup / name)
            (backup / name).chmod(0o600)
    (backup / 'manifest.json').write_text(json.dumps({name: {'path': str(path), 'existed': originals[name] is not None} for name, path in paths.items()}) + '\n')
    env = dict(os.environ, NOCTALIA_CONFIG_HOME=str(profile / 'config'), NOCTALIA_STATE_HOME=str(profile / 'state'))
    try:
        for name in ('config.toml', 'settings.toml'):
            atomic_write(paths[name], updated[name])
        subprocess.run(['/usr/bin/noctalia', 'config', 'validate'], env=env, check=True)
        atomic_write(unit, '[Service]\nEnvironment="LC_TIME=en_US.UTF-8" "TZ=America/Sao_Paulo"\nUnsetEnvironment=LC_ALL\n')
    except Exception:
        for name, path in paths.items():
            if originals[name] is None:
                path.unlink(missing_ok=True)
            else:
                atomic_write(path, originals[name])
        raise
    # Use the existing activation helper's temporary KillMode=process override.
    helper = home / 'ricy-kit/contributions/notification-continuity/ativar.py'
    spec = importlib.util.spec_from_file_location('ricy_preservar_aplicativos', helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.restart_preserving_apps()
    print('Datas em inglês; Cosmópolis/SP; clima métrico e eventos habilitados.')
    print('Backup: ' + str(backup))


if __name__ == '__main__':
    main()
