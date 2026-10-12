#!/usr/bin/env python3
"""Build/install only the existing Dolphin Qt helper, preserving phase rollback."""
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

here = Path(__file__).resolve().parent
home = Path.home()
helper = home / '.local/share/ricy-dolphin/plugins/generic/libricydolphinui.so'
if not helper.is_file():
    raise SystemExit('Existing Dolphin adaptation required; run its established installer first.')
environment = dict(os.environ, XDG_CACHE_HOME=str(home / '.cache/ricy-dolphin-identity-motion/motion'))
library = Path(subprocess.check_output(
    [sys.executable, '-B', str(here.parent / 'dolphin-blur-corners/build-ui.py')],
    env=environment, text=True).strip())
backup = home / '.local/state/ricy-dolphin-backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
shutil.copy2(helper, backup / '0')
(backup / 'manifest.json').write_text(json.dumps([
    dict(path=str(helper), exists=True, saved='0')], indent=2) + '\n')
print('Backup:', backup, flush=True)
fd, temporary = tempfile.mkstemp(prefix='.ricy-motion-', dir=helper.parent)
os.close(fd)
try:
    shutil.copy2(library, temporary)
    os.replace(temporary, helper)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)
print('Applied to new Dolphin processes. Existing mapped helpers remain valid.')
print('Rollback: apply.py --restaurar BACKUP; reopen Dolphin.')
