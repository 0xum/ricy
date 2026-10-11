#!/usr/bin/env python3
"""Registra no Noctalia o fundo comum dos desktops Plasma para o cartão Home."""
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
from urllib.parse import unquote, urlparse


def main():
    if os.geteuid() == 0:
        raise SystemExit('Execute como usuário da sessão, sem sudo.')
    script = '''var ds = desktops(); var paths = [];
for (var i = 0; i < ds.length; ++i) {
    if (ds[i].wallpaperPlugin != "org.kde.image") { throw new Error("Wallpaper Plasma não é uma imagem estática."); }
    ds[i].currentConfigGroup = ["Wallpaper", "org.kde.image", "General"];
    paths.push(ds[i].readConfig("Image", ""));
} print(JSON.stringify(paths));'''
    result = subprocess.check_output(['qdbus6', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript', script], text=True)
    images = json.loads(result.strip())
    resolved = set()
    for image in images:
        url = urlparse(image)
        if url.scheme not in ('', 'file') or url.netloc not in ('', 'localhost'):
            raise SystemExit('Fundo não é um arquivo local: configure a imagem manualmente.')
        path = Path(unquote(url.path)).expanduser().resolve()
        if not path.is_file():
            raise SystemExit('Imagem não encontrada; nenhuma preferência alterada.')
        resolved.add(path)
    if len(resolved) != 1:
        raise SystemExit('Desktops com fundos diferentes: escolha a imagem do cartão manualmente; nenhuma preferência alterada.')
    image = resolved.pop()
    home = Path.home()
    # This is the profile used by the permanent integration in this kit.
    settings = home / 'Projects/ricy/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/state/noctalia/settings.toml'
    state = Path(os.environ.get('XDG_STATE_HOME', home / '.local/state'))
    backup = state / 'ricy-menu-wallpaper-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    (backup / 'manifest.json').write_text(json.dumps({'settings_existed': settings.exists(), 'settings_path': str(settings)}) + '\n')
    if settings.exists():
        shutil.copy2(settings, backup / 'settings.toml')
        (backup / 'settings.toml').chmod(0o600)
    response = subprocess.check_output(['/usr/bin/noctalia', 'msg', 'wallpaper-set', str(image)], text=True).strip()
    if response != 'ok':
        raise SystemExit('Noctalia recusou a imagem: ' + response)
    print('Imagem do Plasma registrada para o cartão Home; backup: ' + str(backup))


if __name__ == '__main__':
    main()
