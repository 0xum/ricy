#!/usr/bin/env python3
"""Apply the two corrected files to the kit before preparing the destination."""
from pathlib import Path
import hashlib
import json
import shutil

base = Path(__file__).resolve().parent
kit = base.parents[1]
entries = json.loads((base / 'manifest.json').read_text())

# Check everything before the first change. Do not replace unknown settings.
for entry in entries:
    original = kit / entry['target']
    replacement = base / entry['replacement']
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    if digest(replacement) != entry['replacement_sha256']:
        raise SystemExit('Unexpected hash correction: ' + str(replacement))
    if digest(original) not in {entry['original_sha256'], entry['replacement_sha256']}:
        raise SystemExit('File already modified; review patch: ' + str(original))

for entry in entries:
    shutil.copy2(base / entry['replacement'], kit / entry['target'])
    print('Correction applied:', entry['target'])

print('Prepare the destination with the noctalia-kde-integration-and-menus contribution.')
