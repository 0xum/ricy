#!/usr/bin/env python3
"""Instala a integração persistente no usuário de uma sessão Plasma preparada."""
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
script_names = ['iniciar-teste.sh', 'ativar-busca-noctalia.sh',
                'recuperar-no-login.sh', 'voltar-ao-plasma.sh', 'configurar-super.py']

if os.geteuid() == 0:
    raise SystemExit('Execute como usuário do desktop, sem sudo.')
if not (scripts / 'plasma-antes.tar.gz').is_file():
    raise SystemExit('Prepare primeiro a contribuição Noctalia no destino.')
if os.environ.get('XDG_SESSION_TYPE') != 'wayland':
    raise SystemExit('Execute na sessão Plasma Wayland do destino.')

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
    '@ADAPTER@': quote(scripts / 'busca-desktop.py'),
    '@START@': quote(base / 'iniciar-automatico.sh'),
}
units.mkdir(parents=True, exist_ok=True)
for name in names:
    text = (base / (name + '.in')).read_text()
    for key, value in replacements.items():
        text = text.replace(key, value)
    (units / name).write_text(text)
for name in script_names:
    shutil.copy2(base / name, scripts / name)
    (scripts / name).chmod(0o755)
(base / 'iniciar-automatico.sh').chmod(0o755)

# Caso esteja migrando do teste transitório, descarregue essas duas unidades.
for name in ['noctalia-busca-desktop.service', 'noctalia-teste.service']:
    subprocess.run(['systemctl', '--user', 'stop', name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
subprocess.run(['systemctl', '--user', 'daemon-reload'], check=True)
subprocess.run(['systemd-analyze', '--user', 'verify',
                *(str(units / name) for name in names)], check=True)
subprocess.run(['systemctl', '--user', 'enable',
                'ricy-noctalia-integracao.service'], check=True)
subprocess.run(['systemctl', '--user', 'restart',
                'ricy-noctalia-integracao.service'], check=True)
print('Início automático habilitado. Backup local:', backup)
