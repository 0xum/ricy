#!/usr/bin/env python3
"""Install user integration on the destination, saving destination-only backups."""
from pathlib import Path
from datetime import datetime
import json
import os
import shutil
import subprocess

KIT = Path(__file__).resolve().parent
MIMES = ['application/vnd.debian.binary-package', 'application/x-debian-package', 'application/x-rpm']
TARGETS = ['.local/share/cachyos-package-installer',
           '.local/share/applications/cachyos-local-package-installer.desktop',
           '.local/share/kio/servicemenus/cachyos-install-package.desktop',
           '.config/mimeapps.list', '.local/share/applications/mimeapps.list',
           '.config/kde-mimeapps.list', '.local/share/applications/kde-mimeapps.list']


def desktop_quote(value):
    for old, new in [('\\', '\\\\'), ('"', '\\"'), ('`', '\\`'), ('$', '\\$')]:
        value = value.replace(old, new)
    return '"' + value.replace('%', '%%') + '"'


def main():
    if os.geteuid() == 0:
        raise SystemExit('Run as normal user in the destination KDE session without sudo.')
    for command in ['python', 'pacman', 'dpkg-deb', 'rpm', 'rpm2archive', 'pkgfile',
                    'fakeroot', 'zstd', 'pkexec', 'update-desktop-database', 'kbuildsycoca6']:
        if not shutil.which(command):
            raise SystemExit('Absent dependence: ' + command)
    import PyQt6.QtWidgets  # fail before mutation when unavailable
    home = Path.home()
    state = home / '.local/state/cachyos-package-installer-backups'
    backup = state / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    backup.chmod(0o700)
    manifest = {}
    for relative in TARGETS:
        path = home / relative
        exists = path.exists() or path.is_symlink()
        manifest[relative] = exists
        if exists:
            dest = backup / 'files' / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            if path.is_dir() and not path.is_symlink():
                shutil.copytree(path, dest, symlinks=True)
            else:
                shutil.copy2(path, dest, follow_symlinks=False)
    (backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (backup / 'manifest.json').chmod(0o600)
    versions = subprocess.run(['pacman', '-Q'], capture_output=True, text=True, check=True)
    (backup / 'packages-before.txt').write_text(versions.stdout)
    (backup / 'packages-before.txt').chmod(0o600)
    defaults = {mime: subprocess.run(['xdg-mime', 'query', 'default', mime],
                capture_output=True, text=True).stdout.strip() for mime in MIMES}
    (backup / 'mime-defaults-before.json').write_text(json.dumps(defaults, indent=2) + '\n')
    (backup / 'mime-defaults-before.json').chmod(0o600)
    print('Backup local do destino:', backup, flush=True)
    app = home / TARGETS[0]
    app.mkdir(parents=True, exist_ok=True)
    for source in (KIT / 'app').iterdir():
        shutil.copy2(source, app / source.name)
    shutil.copy2(KIT / 'LICENSE-debtap-GPL-2.0', app / 'LICENSE-debtap-GPL-2.0')
    shutil.copy2(KIT / 'README.md', app / 'README-migracao.md')
    for relative in TARGETS[1:3]:
        destination = home / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        model = KIT / 'desktop' / (destination.name + '.in')
        destination.write_text(model.read_text().replace('@INSTALLER@', desktop_quote(str(app / 'installer.py'))))
        destination.chmod(0o755 if '/servicemenus/' in relative else 0o644)
    subprocess.run(['update-desktop-database', str(home / '.local/share/applications')], check=True)
    # Update only the requested MIME defaults, leaving unrelated entries intact.
    config = home / '.config/mimeapps.list'
    config.parent.mkdir(parents=True, exist_ok=True)
    import configparser
    parser = configparser.ConfigParser(interpolation=None, strict=False)
    parser.optionxform = str
    if config.exists():
        parser.read(config)
    if not parser.has_section('Default Applications'):
        parser.add_section('Default Applications')
    for mime in MIMES:
        parser.set('Default Applications', mime, 'cachyos-local-package-installer.desktop')
    with config.open('w') as stream:
        parser.write(stream, space_around_delimiters=False)
    subprocess.run(['kbuildsycoca6', '--noincremental'], check=True)
    print('Integration installed. To undo:')
    print('python restore-integration.py "' + str(backup) + '"')


if __name__ == '__main__':
    main()
