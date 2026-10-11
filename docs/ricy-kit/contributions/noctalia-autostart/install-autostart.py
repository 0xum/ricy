#!/usr/bin/env python3
"""Installs persistent integration into the user of a prepared Plasma session."""
from pathlib import Path
from datetime import datetime
import os
import shutil
import subprocess
import json

base = Path(__file__).resolve().parent
integration = base.parent / 'noctalia-kde-integration-and-menus'
scripts = integration / 'outputs/noctalia-test'
home = Path.home()
units = home / '.config/systemd/user'
names = ['noctalia-teste.service', 'noctalia-busca-desktop.service',
         'ricy-noctalia-integracao.service']
script_names = ['start-test.sh', 'enable-noctalia-search.sh',
                'recover-at-login.sh', 'return-to-plasma.sh', 'configure-super.py']

if os.geteuid() == 0:
    raise SystemExit('Run as a desktop user without sudo.')
if not (scripts / 'plasma-antes.tar.gz').is_file():
    raise SystemExit('Prepare first the Noctalia contribution to the destination.')
if os.environ.get('XDG_SESSION_TYPE') != 'wayland':
    raise SystemExit('Run at the Plasma Wayland session of destination.')

backup = home / '.local/state/ricy-inicio-automatico-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
manifest = {}
for path in [*(units / name for name in names), *(scripts / name for name in script_names)]:
    relative = str(path.relative_to(home))
    manifest[relative] = path.exists()
    if path.exists():
        target = backup / 'files' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
(backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(backup / 'manifest.json').chmod(0o600)

def quote(value):
    return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%') + '"'

replacements = {
    '@CONFIG_ENV@': quote('NOCTALIA_CONFIG_HOME=' + str(integration / 'work/noctalia-profile/config')),
    '@STATE_ENV@': quote('NOCTALIA_STATE_HOME=' + str(integration / 'work/noctalia-profile/state')),
    '@ADAPTER@': quote(scripts / 'desktop-search.py'),
    '@START@': quote(base / 'start-automatically.sh'),
}
units.mkdir(parents=True, exist_ok=True)
for name in names:
    template_names = {
        'noctalia-teste.service': 'noctalia-test.service.in',
        'noctalia-busca-desktop.service': 'noctalia-desktop-search.service.in',
        'ricy-noctalia-integracao.service': 'ricy-noctalia-integration.service.in',
    }
    text = (base / template_names[name]).read_text()
    for key, value in replacements.items():
        text = text.replace(key, value)
    (units / name).write_text(text)
for name in script_names:
    shutil.copy2(base / name, scripts / name)
    (scripts / name).chmod(0o755)
(base / 'start-automatically.sh').chmod(0o755)

# If you're migrating from the transient test, download these two units.
for name in ['noctalia-busca-desktop.service', 'noctalia-teste.service']:
    subprocess.run(['systemctl', '--user', 'stop', name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
subprocess.run(['systemctl', '--user', 'daemon-reload'], check=True)
subprocess.run(['systemd-analyze', '--user', 'verify',
                *(str(units / name) for name in names)], check=True)
subprocess.run(['systemctl', '--user', 'enable',
                'ricy-noctalia-integracao.service'], check=True)
subprocess.run(['systemctl', '--user', 'restart',
                'ricy-noctalia-integracao.service'], check=True)
print('Autostart enabled. Local backup:', backup)
