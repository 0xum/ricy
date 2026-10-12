#!/usr/bin/env python3
"""Install the optional Dolphin chrome overlay and existing helper with rollback."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

here = Path(__file__).resolve().parent
home = Path.home()
source = here / 'icons/Ricy-Dolphin'
provenance = json.loads((source / 'provenance.json').read_text())
for asset in provenance['assets']:
    path = source / 'scalable/actions' / (asset['kde_name'] + '.svg')
    ET.parse(path)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['asset_sha256']
assert {p.stem for p in (source / 'scalable/actions').glob('*.svg')} == {a['kde_name'] for a in provenance['assets']}
environment = dict(os.environ, XDG_CACHE_HOME=str(home / '.cache/ricy-dolphin-identity-motion/iconography'))
library = Path(subprocess.check_output([sys.executable, str(here.parent / 'dolphin-blur-corners/build-ui.py')],
                                       env=environment, text=True).strip())
overlay = home / '.local/share/icons/Ricy-Dolphin'
helper = home / '.local/share/ricy-dolphin/plugins/generic/libricydolphinui.so'
backup = home / '.local/state/ricy-dolphin-backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
manifest = []
for number, path in enumerate((overlay, helper)):
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
for path in source.rglob('*'):
    if not path.is_file():
        continue
    destination = overlay / path.relative_to(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.ricy-icons-', dir=destination.parent)
    os.close(fd)
    try:
        shutil.copy2(path, temporary)
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
fd, temporary = tempfile.mkstemp(prefix='.ricy-icons-', dir=helper.parent)
os.close(fd)
try:
    shutil.copy2(library, temporary)
    os.replace(temporary, helper)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)
print('Applied. New Dolphin processes select the optional overlay; missing overlay keeps the system theme.')
print('Rollback: apply.py --restaurar BACKUP; reopen Dolphin. Global KDE theme and dolphinrc are unchanged.')
