#!/usr/bin/env python3
"""Instala/restaura o perfil Konsole com cursor de texto animado."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.parent / 'login-lock-cursor-appearance'))
from comum import apply, merge_ini, read_text, restore, target

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
    parser.add_argument('--home', type=Path, default=Path.home(), help='Home descartável para verificar aplicação/restauração')
    parser.add_argument('--restaurar', type=Path, metavar='BACKUP')
    args = parser.parse_args()
    home = args.home.resolve()
    real = home == Path.home().resolve()
    if real and os.geteuid() == 0:
        parser.error('Execute como usuário do desktop, sem sudo.')
    allowed = list(ASSETS) + [CONFIG]
    if args.restaurar:
        restore(home, args.restaurar.resolve(), 'konsole', allowed)
    else:
        if real:
            if not Path('/usr/bin/konsole').exists():
                parser.error('Instale o pacote konsole no destino antes de continuar.')
            result = subprocess.run(['/usr/bin/konsole', '--list-profile-properties'], capture_output=True, text=True, check=True)
            if 'AnimatingCursorEnabled : bool' not in result.stdout:
                parser.error('Esta versão Konsole não reconhece AnimatingCursorEnabled; nenhuma preferência foi alterada.')
        operations = list(ASSETS.items())
        operations.append((CONFIG, settings(read_text(target(home, CONFIG)))))
        apply(home, operations, home / '.local/state/ricy-konsole-backups', 'konsole')
    if real and shutil.which('kbuildsycoca6'):
        subprocess.run(['kbuildsycoca6', '--noincremental'], check=True)
    print('Concluído. Feche o Konsole e abra uma nova janela para carregar o perfil.')


if __name__ == '__main__':
    main()
