#!/usr/bin/env python3
"""Install the selector in the session without replacing the composer or terminating apps."""
from datetime import datetime
from pathlib import Path
import os
import shutil
import subprocess

home = Path.home()
base = Path(__file__).resolve().parent
if os.geteuid() == 0:
    raise SystemExit('Run integration as a session user without sudo.')
helper = home / '.local/lib/ricy-blur/start.py'
unit = home / '.config/systemd/user/ricy-blur-continuidade.service'
backup = home / '.local/state/ricy-blur-backups' / datetime.now().strftime('%Y%m%d-%H%M%S')
backup.mkdir(parents=True, mode=0o700)
for path in (helper, unit):
    if path.exists():
        shutil.copy2(path, backup / path.name)
helper.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(base / 'start.py', helper)
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
print(f'Integration backup: {backup}')
