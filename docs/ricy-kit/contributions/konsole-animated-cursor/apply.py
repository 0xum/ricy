#!/usr/bin/env python3
"""Instala/restaura the Konsole profile with animated text cursor."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parent / 'login-lock-cursor-appearance'))
from common import apply, merge_ini, read_text, restore, target

ASSETS = {
    '.local/share/konsole/PlasmaBlur.profile': BASE / 'assets/PlasmaBlur.profile',
    '.local/share/konsole/PlasmaBlur.colorscheme': BASE / 'assets/PlasmaBlur.colorscheme',
    '.local/bin/konsole': BASE / 'assets/konsole',
    '.local/share/applications/org.kde.konsole.desktop': BASE / 'assets/org.kde.konsole.desktop',
}
CONFIG = '.config/konsolerc'


def settings(text):
    text = merge_ini(text, {'Desktop Entry': {'DefaultProfile': 'PlasmaBlur.profile'}})
    first_group = next((i for i, line in enumerate(text.splitlines(keepends=True)) if line.strip().startswith('[')), None)
    lines = text.splitlines(keepends=True)
    first_group = len(lines) if first_group is None else first_group
    prefix = ''.join(line for line in lines[:first_group] if not re.match(r'^\s*MenuBar\s*=', line))
    return prefix.rstrip() + '\nMenuBar=Disabled\n\n' + ''.join(lines[first_group:])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='Disposable home for testing application/restoration')
    parser.add_argument('--restaurar', type=Path, metavar='BACKUP')
    args = parser.parse_args()
    home = args.home.resolve()
    real = home == Path.home().resolve()
    if real and os.geteuid() == 0:
        parser.error('Run as a desktop user without sudo.')
    allowed = list(ASSETS) + [CONFIG]
    if args.restaurar:
        restore(home, args.restaurar.resolve(), 'konsole', allowed)
    else:
        if real:
            if not Path('/usr/bin/konsole').exists():
                parser.error('Install the konsole package in the destination before continuing.')
            result = subprocess.run(['/usr/bin/konsole', '--list-profile-properties'], capture_output=True, text=True, check=True)
            if 'AnimatingCursorEnabled : bool' not in result.stdout:
                parser.error('This version Konsole does not recognize AnimatingCursorEnabled; no preference has been changed.')
        operations = list(ASSETS.items())
        operations.append((CONFIG, settings(read_text(target(home, CONFIG)))))
        apply(home, operations, home / '.local/state/ricy-konsole-backups', 'konsole')
    if real and shutil.which('kbuildsycoca6'):
        subprocess.run(['kbuildsycoca6', '--noincremental'], check=True)
    print('Done. Close Konsole and open a new window to load the profile.')


if __name__ == '__main__':
    main()
