#!/usr/bin/env python3
"""Instala/restaura tema SDDM, cursor, fonte e wallpaper na próxima instalação."""
import argparse
import json
import os
import pwd
from pathlib import Path
import subprocess
from comum import BASE, apply, merge_ini, read_text, restore, target

ASSETS = {
    'usr/share/sddm/themes/mocha-limine': 'sddm/mocha-limine',
    'usr/share/icons/Bibata-Modern-Classic': 'icons/Bibata-Modern-Classic',
    'usr/local/share/fonts/ricy': 'fonts',
    'usr/local/share/ricy/limine-splash.png': 'wallpapers/limine-splash.png',
}
CONFIGS = ['etc/sddm.conf', 'etc/sddm.conf.d/95-mocha-limine.conf']
THEME = {'Current': 'mocha-limine', 'CursorSize': '16',
         'CursorTheme': 'Bibata-Modern-Classic', 'Font': 'JetBrainsMono Nerd Font'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('/'), help='Raiz descartável para testar sem alterar o sistema')
    parser.add_argument('--restaurar', type=Path, metavar='BACKUP')
    args = parser.parse_args()
    root = args.root.resolve()
    if root == Path('/') and os.geteuid() != 0:
        parser.error('Execute este script com sudo para instalar no sistema.')
    greeter = json.loads((BASE / 'greeter-preferencias.json').read_text())
    greeter_paths = ['var/lib/sddm/.config/' + name for name in greeter]
    allowed = list(ASSETS) + CONFIGS + greeter_paths
    account = pwd.getpwnam('sddm') if root == Path('/') else None
    if args.restaurar:
        restore(root, args.restaurar.resolve(), 'sistema', allowed)
    else:
        operations = [(relative, BASE / 'assets' / asset) for relative, asset in ASSETS.items()]
        for relative in CONFIGS:
            # sddm.conf tem precedência sobre os drop-ins. Mantém sessões,
            # autenticação e autologin existentes; altera só Theme e lembrança.
            text = merge_ini(read_text(target(root, relative)), {'Theme': THEME})
            if relative == 'etc/sddm.conf':
                text = merge_ini(text, {'Users': {'RememberLastSession': 'true'}})
            operations.append((relative, text))
        for name, groups in greeter.items():
            relative = 'var/lib/sddm/.config/' + name
            operations.append((relative, merge_ini(read_text(target(root, relative)), groups)))
        backup = apply(root, operations, root / 'var/lib/ricy-appearance-backups', 'sistema')
        theme = root / 'usr/share/sddm/themes/mocha-limine/theme.conf'
        try:
            theme.write_text(merge_ini(theme.read_text(), {'General': {'background': '/usr/local/share/ricy/limine-splash.png'}}))
            # Assets copiados de origens diferentes devem ser legíveis pelo SDDM.
            for relative in ASSETS:
                path = target(root, relative)
                if path.is_dir():
                    path.chmod(0o755)
                    for child in path.rglob('*'):
                        if not child.is_symlink():
                            child.chmod(0o755 if child.is_dir() else 0o644)
                else:
                    path.chmod(0o644)
            for relative in greeter_paths:
                path = target(root, relative)
                path.chmod(0o600)
                if account:
                    os.chown(path, account.pw_uid, account.pw_gid)
                    os.chown(path.parent, account.pw_uid, account.pw_gid)
        except Exception:
            restore(root, backup, 'sistema', allowed)
            raise
    if root == Path('/'):
        subprocess.run(['fc-cache', '-f'], check=True)
    print('Concluído. O SDDM usará a configuração na próxima tela de login.')
    print('Este script não reinicia o SDDM nem encerra a sessão.')


if __name__ == '__main__':
    main()
