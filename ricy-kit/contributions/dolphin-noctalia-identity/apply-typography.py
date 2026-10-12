#!/usr/bin/env python3
"""Explicit one-shot KDE/Qt font inheritance and official Noctalia family sync.

Builds and installs only the existing Dolphin helper/QSS, changes only the three
UseSystemFont flags and shell.font_family, and preserves a restorer manifest.
Never changes KDE fonts, launchers, services, tokens, or shell size/scale.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--noctalia-config', type=Path, required=True,
                    help='Explicit active Noctalia config.toml (private; never committed)')
args = parser.parse_args()
here = Path(__file__).resolve().parent
home = Path.home()
config = args.noctalia_config.resolve(strict=True)
original = config.read_text()
settings = tomllib.loads(original)
if 'font_family' not in settings.get('shell', {}):
    parser.error('Expected an existing official shell.font_family entry')
# Query the current desktop platform integration, not a captured token value.
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase, QFontInfo
app = QApplication(['ricy-typography-sync'])
if app.platformName() != 'wayland' or os.environ.get('QT_SCALE_FACTOR'):
    raise SystemExit('Use the active Wayland desktop without a process-scale override; no files changed')
font = app.font()
family = QFontInfo(font).family()
if not family or family != font.family() or family not in QFontDatabase.families():
    raise SystemExit('UNKNOWN active Qt font resolution; no files changed')
section = re.search(r'(?ms)^\[shell\][^\n]*\n.*?(?=^\[|\Z)', original)
if not section:
    parser.error('Expected an existing [shell] table')
updated, count = re.subn(r'(?m)^font_family\s*=.*$',
                         'font_family = ' + json.dumps(family), section.group())
if count != 1:
    parser.error('Expected exactly one shell.font_family assignment')
updated = original[:section.start()] + updated + original[section.end():]
expected = tomllib.loads(original)
expected['shell']['font_family'] = family
assert tomllib.loads(updated) == expected
root = home / '.local/share/ricy-dolphin'
backup = home / '.local/state/ricy-dolphin-backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
# Keep the earlier source/cache/binary as rollback material.
environment = dict(os.environ, XDG_CACHE_HOME=str(home / '.cache/ricy-dolphin-identity-motion/typography'))
library = Path(subprocess.check_output([sys.executable, str(here.parent / 'dolphin-blur-corners/build-ui.py')],
                                       env=environment, text=True).strip())
targets = [root / 'dolphin.qss', root / 'plugins/generic/libricydolphinui.so', home / '.config/dolphinrc', config]
backup.mkdir(parents=True, mode=0o700)
manifest = []
for number, path in enumerate(targets):
    exists = path.exists()
    if exists:
        shutil.copy2(path, backup / str(number))
    manifest.append(dict(path=str(path), exists=exists, saved=str(number)))
(backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

def atomic_copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.ricy-typography-', dir=destination.parent)
    os.close(fd)
    try:
        shutil.copy2(source, name)
        os.replace(name, destination)
    finally:
        if os.path.exists(name):
            os.unlink(name)

print('Backup:', backup, flush=True)
atomic_copy(here / 'dolphin.qss', targets[0])
atomic_copy(library, targets[1])
for group in ('IconsMode', 'CompactMode', 'DetailsMode'):
    subprocess.run(['kwriteconfig6', '--file', str(targets[2]), '--group', group,
                    '--key', 'UseSystemFont', 'true'], check=True)
# Preserve file permissions and all unrelated TOML data.
with tempfile.TemporaryDirectory() as temporary:
    staged = Path(temporary) / 'config.toml'
    shutil.copy2(config, staged)
    staged.write_text(updated)
    atomic_copy(staged, config)
print('KNOWN Qt application font:', font.toString())
print('Noctalia shell.font_family:', family)
print('New Dolphin processes load the updated helper. Existing windows are preserved.')
print('Reload Noctalia through its official msg config-reload command in its active environment.')
print('Rollback: apply.py --restaurar BACKUP, then reload Noctalia and reopen Dolphin.')
