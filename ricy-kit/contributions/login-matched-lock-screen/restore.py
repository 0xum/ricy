#!/usr/bin/env python3
"""Restores the explicit backup created by apply.py."""
import json
from pathlib import Path
import shutil
import sys

backup = Path(sys.argv[1]).resolve()
manifest = json.loads((backup / 'manifest.json').read_text())
rc = Path.home() / '.config/kscreenlockerrc'
local = Path.home() / '.local/share/plasma/shells/org.kde.plasma.desktop'
if local.exists():
    if not (local / '.ricy-bloqueio').exists():
        raise SystemExit('Local shell without Ricy marker; restore aborted.')
    shutil.rmtree(local)
if manifest.get('shell_exists'):
    shutil.copytree(backup / 'shell', local, symlinks=True)
if manifest['kscreenlockerrc_exists']:
    shutil.copy2(backup / 'kscreenlockerrc', rc)
else:
    rc.unlink(missing_ok=True)
print('Previous lock restored. The next opening will use this setting.')
