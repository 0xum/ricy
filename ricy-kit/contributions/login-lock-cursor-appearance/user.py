#!/usr/bin/env python3
"""Apply/restore cursor and KDE/GTK appearance with a local destination backup."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from common import BASE, apply, merge_ini, read_text, restore, target

INTEGRATION = BASE.parent / 'noctalia-kde-integration-and-menus/outputs/kde-outlines'
ASSETS = {
    '.local/share/icons/Bibata-Modern-Classic': BASE / 'assets/icons/Bibata-Modern-Classic',
    '.local/share/plasma/desktoptheme/mocha-blur': BASE / 'assets/plasma/desktoptheme/mocha-blur',
    '.local/share/plasma/look-and-feel/Catppuccin-Mocha-Mauve': BASE / 'assets/plasma/look-and-feel/Catppuccin-Mocha-Mauve',
    '.config/fontconfig/fonts.conf': BASE / 'assets/fontconfig/fonts.conf',
    '.config/Kvantum/KDE-Noctalia': INTEGRATION / 'KDE-Noctalia',
    '.local/share/color-schemes/KDE-Noctalia.colors': INTEGRATION / 'KDE-Noctalia.colors',
}
EXTRA = ['.config/Kvantum/kvantum.kvconfig', '.config/environment.d/20-cursor.conf',
         '.local/share/icons/default/index.theme', '.icons/default/index.theme', '.gtkrc-2.0']
KWIN = {
    '.local/share/kwin/scripts/adaptivepanelwidth': BASE / 'assets/kwin/scripts/adaptivepanelwidth',
    '.local/share/kwin/scripts/windowsarrows': BASE / 'assets/kwin/scripts/windowsarrows',
    '.local/share/kwin/effects/smoothwindowgeometry': BASE / 'assets/kwin/effects/smoothwindowgeometry',
}


def gtk2(text, settings):
    for key, value in settings.items():
        text = re.sub(r'^\s*' + re.escape(key) + r'\s*=.*\n?', '', text, flags=re.M)
        if key in ['gtk-application-prefer-dark-theme', 'gtk-enable-animations']:
            value = '1' if value.lower() in ['true', '1'] else '0'
        elif not value.isdigit():
            value = json.dumps(value)
        text = text.rstrip() + f'\n{key}={value}\n'
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='Disposable home for testing')
    parser.add_argument('--restaurar', type=Path, metavar='BACKUP')
    parser.add_argument('--extensoes-kwin', action='store_true', help='Includes local efeitos/scripts and recompiles the arrow module in the destination KWin')
    args = parser.parse_args()
    home = args.home.resolve()
    real = home == Path.home().resolve()
    if real and os.geteuid() == 0:
        parser.error('Run as a desktop user without sudo.')
    preferences = json.loads((BASE / 'preferences.json').read_text())
    kwin_preferences = json.loads((BASE / 'kwin-preferences.json').read_text())
    allowed = list(ASSETS) + list(preferences) + EXTRA + list(KWIN) + list(kwin_preferences)
    if args.restaurar:
        restore(home, args.restaurar.resolve(), 'usuario', allowed)
    else:
        if real:
            # Validates dependencies before writing preferences.
            required = ['/usr/share/themes/adw-gtk3-dark', '/usr/share/icons/breeze-dark',
                        '/usr/share/sounds/ocean', '/usr/local/share/ricy/limine-splash.png']
            missing = [p for p in required if not Path(p).exists()]
            if missing:
                parser.error('Install dependencies and run system.py before: ' + ', '.join(missing))
        operations = list(ASSETS.items())
        # The native module depends on KWin's ABI; we never carry the .so.
        temporary = tempfile.TemporaryDirectory(prefix='ricy-kwin-')
        build = Path(temporary.name) / 'windowsarrows'
        if args.extensoes_kwin:
            shutil.copytree(KWIN['.local/share/kwin/scripts/windowsarrows'], build)
            if real:
                subprocess.run(['bash', str(build / 'contents/native/build.sh')], check=True)
            operations += [(relative, build if relative.endswith('/windowsarrows') else source) for relative, source in KWIN.items()]
            preferences['.config/kwinrc']['Plugins'].update({
                'adaptivepanelwidthEnabled': 'true', 'windowsarrowsEnabled': 'true',
                'smoothwindowgeometryEnabled': 'true', 'maximizeEnabled': 'false',
            })
            preferences.update(kwin_preferences)
        for relative, groups in preferences.items():
            operations.append((relative, merge_ini(read_text(target(home, relative)), groups)))
        operations += [
            ('.config/Kvantum/kvantum.kvconfig', merge_ini(read_text(target(home, EXTRA[0])), {'General': {'theme': 'KDE-Noctalia'}})),
            ('.config/environment.d/20-cursor.conf', 'XCURSOR_THEME=Bibata-Modern-Classic\nXCURSOR_SIZE=16\n'),
            ('.local/share/icons/default/index.theme', '[Icon Theme]\nName=Default\nInherits=Bibata-Modern-Classic\n'),
            ('.icons/default/index.theme', '[Icon Theme]\nName=Default\nInherits=Bibata-Modern-Classic\n'),
            ('.gtkrc-2.0', gtk2(read_text(target(home, '.gtkrc-2.0')), preferences['.config/gtk-3.0/settings.ini']['Settings'])),
        ]
        # The palette must pass the KDE API; we do not copy full kdeglobals.
        backup = apply(home, operations, home / '.local/state/ricy-appearance-backups', 'usuario')
        temporary.cleanup()
        if real:
            try:
                subprocess.run(['plasma-apply-colorscheme', 'KDE-Noctalia'], check=True)
            except Exception:
                restore(home, backup, 'usuario', allowed)
                raise
    if real:
        subprocess.run(['fc-cache', '-f'], check=True)
        if shutil.which('kbuildsycoca6'):
            subprocess.run(['kbuildsycoca6', '--noincremental'], check=True)
    print('Done. Do a new session to load all preferences.')
    print('Lock: apply also ../login-matched-lock-screen/apply.py without sudo.')


if __name__ == '__main__':
    main()
