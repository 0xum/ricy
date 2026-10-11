#!/usr/bin/env python3
"""Instala comandos e corrige entradas antigas sem alternar o ambiente atual."""
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
from paineis import capture

base = Path(__file__).resolve().parent
kit = base.parents[1]
home = Path.home()
scripts = base.parent / 'noctalia-kde-integration-and-menus/outputs/noctalia-test'
state = Path(os.environ.get('XDG_STATE_HOME', home / '.local/state')) / 'ricy-alternancia'
if os.geteuid() == 0:
    raise SystemExit('Execute como usuário da sessão, sem sudo.')
if not (scripts / 'plasma-antes.tar.gz').is_file():
    raise SystemExit('Prepare a integração Noctalia e instale seu início automático primeiro.')
subprocess.run(['systemctl', '--user', 'cat', 'ricy-noctalia-integracao.service'], check=True, stdout=subprocess.DEVNULL)
state.mkdir(parents=True, exist_ok=True, mode=0o700)
backup = state / 'backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True, mode=0o700)
manifest = {}


def remember(path):
    rel = str(path.relative_to(home))
    if rel in manifest:
        return
    manifest[rel] = path.exists() or path.is_symlink()
    if manifest[rel]:
        dest = backup / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.is_symlink():
            dest.symlink_to(os.readlink(path))
        else:
            shutil.copy2(path, dest)
            dest.chmod(0o600)


def write(path, text, executable=False):
    remember(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    path.chmod(0o755 if executable else 0o644)


def quote(path):
    return '"' + str(path).replace('\\', '\\\\').replace('"', '\\"').replace('`', '\\`').replace('$', '\\$') + '"'


for name in ['plasma-org.kde.plasma.desktop-appletsrc', 'plasmashellrc']:
    remember(home / '.config' / name)
for name in ['paineis.json', 'atalhos.json', 'troca-ativa']:
    remember(state / name)
# Seed apenas para migração de uma sessão antiga que já está sem painéis.
if not (state / 'paineis.json').exists():
    with tarfile.open(scripts / 'plasma-antes.tar.gz') as archive:
        applets = archive.extractfile('.config/plasma-org.kde.plasma.desktop-appletsrc').read().decode()
        views = archive.extractfile('.config/plasmashellrc').read().decode()
    seed = capture(applets, views)
    if not seed['panels']:
        raise SystemExit('Backup antigo não contém painéis; instalação interrompida.')
    (state / 'paineis.json').write_text(json.dumps(seed, ensure_ascii=False, indent=2) + '\n')
    (state / 'paineis.json').chmod(0o600)
    if (scripts / 'teste-ativo').exists():
        old = []
        for name in ['super-atalho-original.json', 'clipboard-atalho-original.json']:
            path = scripts / name
            if path.exists():
                old.extend(json.loads(path.read_text()))
        (state / 'atalhos.json').write_text(json.dumps(old, indent=2) + '\n')
        (state / 'atalhos.json').chmod(0o600)
        (state / 'troca-ativa').write_text('migracao\n')
        (state / 'troca-ativa').chmod(0o600)

start = '#!/usr/bin/env bash\nset -euo pipefail\nexec python ' + quote(base / 'integracao.py') + ' iniciar\n'
back = ('#!/usr/bin/env bash\nset -euo pipefail\n'
        'if [[ "${RICY_RECUPERACAO_INTERNA:-0}" == 1 ]]; then\n exec python ' + quote(base / 'integracao.py') + ' restaurar\nfi\n'
        'exec ' + quote(base / 'ricy') + ' plasma\n')
for target in [scripts, base.parent / 'noctalia-autostart', kit / 'outputs/noctalia-test']:
    write(target / 'iniciar-teste.sh', start, True)
    write(target / 'voltar-ao-plasma.sh', back, True)
for name, mode in [('ricy', ''), ('voltar-ao-noctalia', 'noctalia'), ('voltar-ao-plasma', 'plasma')]:
    write(home / '.local/bin' / name,
          '#!/usr/bin/env bash\nexec ' + quote(base / 'ricy') + (' "$@"\n' if not mode else ' ' + mode + '\n'), True)
for name, mode in [('iniciar.sh', 'noctalia'), ('voltar.sh', 'plasma'), ('alternar.sh', 'alternar')]:
    write(home / 'ricy' / name, '#!/usr/bin/env bash\nexec ' + quote(base / 'ricy') + ' ' + mode + '\n', True)
for name, title, mode, icon in [('noctalia', 'Voltar ao Noctalia', 'noctalia', 'noctalia'),
                                ('plasma', 'Voltar ao Plasma', 'plasma', 'preferences-desktop'),
                                ('alternar', 'Alternar Plasma e Noctalia', 'alternar', 'preferences-desktop')]:
    write(home / '.local/share/applications' / f'ricy-{name}.desktop',
          '[Desktop Entry]\nType=Application\nName=' + title + '\n'
          'Comment=Preserva wallpaper, painéis e perfil personalizado; vale também no próximo login\n'
          'Exec=' + quote(base / 'ricy') + ' ' + mode + '\nIcon=' + icon + '\nCategories=Utility;\nTerminal=false\n')
for name in ['ricy', 'integracao.py']:
    (base / name).chmod(0o755)
(backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(backup / 'manifest.json').chmod(0o600)
subprocess.run(['kbuildsycoca6', '--noincremental'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print('Alternância instalada. Ambiente atual mantido. Backup privado:', backup)
