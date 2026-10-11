#!/usr/bin/env python3
"""Alinha o bloqueio nativo do Plasma 6.7 ao login mocha-limine local."""
import configparser
import datetime
import json
from pathlib import Path
import shutil
import subprocess

home = Path.home()
system = Path('/usr/share/plasma/shells/org.kde.plasma.desktop')
local = home / '.local/share/plasma/shells/org.kde.plasma.desktop'
marker = local / '.ricy-bloqueio'
if local.exists() and not marker.exists():
    raise SystemExit('There is already a local shell. Preserve it before applying this contribution.')
theme = configparser.ConfigParser()
theme.read('/etc/sddm.conf.d/95-mocha-limine.conf')
name = theme.get('Theme', 'Current', fallback='mocha-limine')
config = configparser.ConfigParser()
config.read(f'/usr/share/sddm/themes/{name}/theme.conf')
image = Path(config.get('General', 'background'))
if not image.is_file():
    raise SystemExit('Login Wallpaper not found.')

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise SystemExit(f'KDE Layout changed: missing or ambiguous expected snippet: {old!r}')
    return text.replace(old, new, 1)

ui = (system / 'contents/lockscreen/LockScreenUi.qml').read_text()
ui = replace_once(ui, 'uiVisible = seenPositionChange;', 'uiVisible = true;')
ui = replace_once(ui, '        onExited: {\n            uiVisible = false;\n        }\n', '')
ui = replace_once(ui, 'interval: 10000', 'interval: 60000\n            running: true')
ui = replace_once(ui, 'Component.onCompleted: launchAnimation.start();',
                  'Component.onCompleted: {\n            launchAnimation.start();\n            // The transition after mounting starts native authentication.\n            Qt.callLater(() => { lockScreenRoot.uiVisible = true; });\n            console.info("Ricy: lock screen with mocha-limine presentation loaded");\n        }')
main = (system / 'contents/lockscreen/MainBlock.qml').read_text()
main = replace_once(main, 'id: passwordBox', 'id: passwordBox\n            rightActions: [] // Same password field as the mocha-limine login')

backup = home / '.local/state/ricy-lockscreen-backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
rc = home / '.config/kscreenlockerrc'
manifest = {'kscreenlockerrc_exists': rc.exists(), 'shell_exists': local.exists()}
if rc.exists():
    shutil.copy2(rc, backup / 'kscreenlockerrc')
    (backup / 'kscreenlockerrc').chmod(0o600)
if local.exists():
    shutil.copytree(local, backup / 'shell', symlinks=True)
(backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(backup / 'manifest.json').chmod(0o600)

local.mkdir(parents=True, exist_ok=True)
contents = local / 'contents'
contents.mkdir(exist_ok=True)
for child in system.iterdir():
    if child.name != 'contents':
        target = local / child.name
        if child.is_file():
            if target.is_symlink():
                target.unlink()
            shutil.copy2(child, target)
        elif not target.exists():
            target.symlink_to(child, target_is_directory=child.is_dir())
for child in (system / 'contents').iterdir():
    if child.name != 'lockscreen':
        target = contents / child.name
        if not target.exists():
            target.symlink_to(child, target_is_directory=child.is_dir())
lock = contents / 'lockscreen'
lock.mkdir(exist_ok=True)
for child in (system / 'contents/lockscreen').iterdir():
    if child.is_file():
        shutil.copy2(child, lock / child.name)
(lock / 'LockScreenUi.qml').write_text(ui)
(lock / 'MainBlock.qml').write_text(main)
marker.write_text('Adapted KDE lock installed; the other components use links to the system.\n')

def setting(groups, key, value):
    args = ['kwriteconfig6', '--file', str(rc)]
    for group in groups:
        args += ['--group', group]
    subprocess.run(args + ['--key', key, value], check=True)

setting(['Greeter'], 'WallpaperPlugin', 'org.kde.image')
setting(['Greeter', 'Wallpaper', 'org.kde.image', 'General'], 'Image', image.as_uri())
setting(['Greeter', 'Wallpaper', 'org.kde.image', 'General'], 'FillMode', '2')
setting(['Greeter', 'LnF', 'General'], 'alwaysShowClock', 'true')
setting(['Greeter', 'LnF', 'General'], 'hideClockWhenIdle', 'false')
setting(['Greeter', 'LnF', 'General'], 'showMediaControls', 'false')
print(f'Bloqueio aplicado. Backup: {backup}')
