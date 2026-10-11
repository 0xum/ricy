#!/usr/bin/env python3
"""Registers in Noctalia the common background of Plasma desktops for Home card."""
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
from urllib.parse import unquote, urlparse


def main():
    if os.geteuid() == 0:
        raise SystemExit('Run as session user without sudo.')
    script = '''var ds = desktops(); var paths = [];
for (var i = 0; i < ds.length; ++i) {
    if (ds[i].wallpaperPlugin != "org.kde.image") { throw new Error("Plasma wallpaper is not a static image."); }
    ds[i].currentConfigGroup = ["Wallpaper", "org.kde.image", "General"];
    paths.push(ds[i].readConfig("Image", ""));
} print(JSON.stringify(paths));'''
    result = subprocess.check_output(['qdbus6', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript', script], text=True)
    images = json.loads(result.strip())
    resolved = set()
    for image in images:
        url = urlparse(image)
        if url.scheme not in ('', 'file') or url.netloc not in ('', 'localhost'):
            raise SystemExit('Background is not a local file: manually configure the image.')
        path = Path(unquote(url.path)).expanduser().resolve()
        if not path.is_file():
            raise SystemExit('Image not found; no preference changed.')
        resolved.add(path)
    if len(resolved) != 1:
        raise SystemExit('Desktops with different backgrounds: Choose card image manually; no preference changed.')
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
    print('Image from registered Plasma to Home card; backup: ' + str(backup))


if __name__ == '__main__':
    main()
