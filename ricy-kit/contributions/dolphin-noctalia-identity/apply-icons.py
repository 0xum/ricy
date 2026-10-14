#!/usr/bin/env python3
"""Install system icon inheritance and retire the Dolphin overlay with rollback."""
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
environment = dict(os.environ, XDG_CACHE_HOME=str(home / '.cache/ricy-dolphin-identity-motion/iconography'))
library = Path(subprocess.check_output([sys.executable, str(here.parent / 'dolphin-blur-corners/build-ui.py')],
                                       env=environment, text=True).strip())
overlay = home / '.local/share/icons/Ricy-Dolphin'
helper = home / '.local/share/ricy-dolphin/plugins/generic/libricydolphinui.so'
wrapper = home / '.local/bin/ricy-dolphin'
backup = home / '.local/state/ricy-dolphin-backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
manifest = []
for number, path in enumerate((overlay, helper, wrapper)):
    if path.exists():
        if path.is_dir():
            shutil.copytree(path, backup / str(number))
        else:
            shutil.copy2(path, backup / str(number))
    manifest.append(dict(path=str(path), exists=path.exists(), saved=str(number)))
(backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print('Backup:', backup, flush=True)
# Update only the selected payload. Files are atomic; previously mapped helper
# inodes remain valid. The manifest can restore previous files/absence exactly.
for source, destination in ((library, helper), (here / 'launch.py', wrapper)):
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.ricy-icons-', dir=destination.parent)
    os.close(fd)
    try:
        shutil.copy2(source, temporary)
        os.chmod(temporary, 0o755)
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
if overlay.exists():
    shutil.rmtree(overlay)
print('Applied. Dolphin follows the KDE system icon theme. The retired Tabler overlay is backed up and removed.')
print('Rollback: apply.py --restaurar BACKUP; reopen Dolphin. Global KDE theme and dolphinrc are unchanged.')
