#!/usr/bin/env python3
"""Desfaz somente archives da instalação, preservando o layout vivo."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

if os.geteuid() == 0:
    raise SystemExit('Execute como usuário do desktop, sem sudo.')
if subprocess.run(['systemctl', '--user', 'is-active', '--quiet', 'noctalia-teste.service']).returncode == 0:
    raise SystemExit('Execute ricy plasma antes de restaurar os scripts.')
backup = Path(sys.argv[1]).resolve()
home = Path.home()
manifest = json.loads((backup / 'manifest.json').read_text())
for rel, existed in manifest.items():
    target = home / rel
    if not target.resolve().is_relative_to(home) or Path(rel).is_absolute():
        raise SystemExit('Caminho fora da home: ' + rel)
    if rel in ['.config/plasma-org.kde.plasma.desktop-appletsrc', '.config/plasmashellrc']:
        continue
    source = backup / rel
    if existed:
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            target.unlink(missing_ok=True)
            target.symlink_to(os.readlink(source))
        else:
            shutil.copy2(source, target)
            if target.suffix == '.sh' or target.parent.name == 'bin':
                target.chmod(0o755)
    else:
        target.unlink(missing_ok=True)
subprocess.run(['kbuildsycoca6', '--noincremental'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print('Instalação da alternância desfeita; desktop atual preservado.')
