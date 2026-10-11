#!/usr/bin/env python3
"""Instala o seletor na sessão sem substituir o compositor ou encerrar apps."""
from datetime import datetime
from pathlib import Path
import os
import shutil
import subprocess

home = Path.home()
base = Path(__file__).resolve().parent
if os.geteuid() == 0:
    raise SystemExit('Execute a integração como usuário da sessão, sem sudo.')
helper = home / '.local/lib/ricy-blur/iniciar.py'
unit = home / '.config/systemd/user/ricy-blur-continuidade.service'
backup = home / '.local/state/ricy-blur-backups' / datetime.now().strftime('%Y%m%d-%H%M%S')
backup.mkdir(parents=True, mode=0o700)
for path in (helper, unit):
    if path.exists():
        shutil.copy2(path, backup / path.name)
helper.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(base / 'iniciar.py', helper)
unit.parent.mkdir(parents=True, exist_ok=True)
escaped = str(helper).replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%')
unit.write_text(f'''[Unit]
Description=Ricy continuous Noctalia blur with native KWin fallback
After=plasma-kwin_wayland.service
Before=noctalia-teste.service
PartOf=graphical-session.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python "{escaped}"
RemainAfterExit=yes

[Install]
WantedBy=graphical-session.target
''')
subprocess.run(['systemctl', '--user', 'daemon-reload'], check=True)
subprocess.run(['systemctl', '--user', 'enable', '--now', 'ricy-blur-continuidade.service'], check=True)
print(f'Backup da integração: {backup}')
