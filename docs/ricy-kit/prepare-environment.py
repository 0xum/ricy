#!/usr/bin/env python3
"""Prepare the kit on the target computer BEFORE you start testing."""
from pathlib import Path
import tarfile, shutil, json, configparser, re, hashlib
kit=Path(__file__).resolve().parent
home=Path.home(); base=kit/'outputs/noctalia-test'; style=kit/'outputs/kde-outlines'
backup=base/'plasma-antes.tar.gz'
if backup.exists():
    raise SystemExit('Backup already exists. Use start-test.sh to repeat; do not replace your original backup.')
paths=['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc','.config/plasmarc','.config/kdeglobals','.config/kwinrc','.config/kwinoutputconfig.json','.config/kglobalshortcutsrc','.config/kscreenlockerrc','.config/klipperrc','.config/kcminputrc','.config/gtk-3.0/settings.ini','.config/gtk-4.0/settings.ini','.config/autostart','.config/noctalia','.local/state/noctalia','.config/Kvantum']
manifest={}
with tarfile.open(backup,'w:gz') as archive:
    for rel in paths:
        p=home/rel
        if p.exists():
            archive.add(p,arcname=rel)
            manifest[rel]='directory' if p.is_dir() else hashlib.sha256(p.read_bytes()).hexdigest()
        else: manifest[rel]=None
backup.chmod(0o600)
(base/'backup-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
shutil.copy2(backup,style/'kde-antes-contornos.tar.gz')
# The wallpaper restoration is generated with DESTINATION IDs and images.
cfg=configparser.ConfigParser(interpolation=None,strict=False);cfg.optionxform=str
cfg.read(home/'.config/plasma-org.kde.plasma.desktop-appletsrc')
lines=[]
for section in cfg.sections():
    match=re.fullmatch(r'Containments\]\[(\d+)\]\[Wallpaper\]\[org.kde.image\]\[General',section)
    if match and 'Image' in cfg[section]:
        i=int(match[1]); image=json.dumps(cfg[section]['Image'])
        lines.append(f'var d=desktopById({i}); if(d){{d.currentConfigGroup=["Wallpaper","org.kde.image","General"];d.writeConfig("Image",{image});}}')
(base/'restaurar-wallpaper.js').write_text('\n'.join(lines)+'\n')
# Capture the previous style before applying the local variant.
kg=configparser.ConfigParser(interpolation=None,strict=False);kg.optionxform=str;kg.read(home/'.config/kdeglobals')
(style/'menuFont-antes.txt').write_text(kg.get('General','menuFont',fallback=''))
(style/'widgetStyle-antes.txt').write_text(kg.get('KDE','widgetStyle',fallback=''))
kv=home/'.config/Kvantum/kvantum.kvconfig'
if kv.exists():shutil.copy2(kv,style/'kvantum-config-antes')
else:(style/'kvantum-ausente-antes').touch()
profile=kit/'work/noctalia-profile/config/noctalia';(profile/'palettes').mkdir(parents=True,exist_ok=True)
shutil.copy2(base/'config.toml',profile/'config.toml')
shutil.copy2(base/'KDE-Current.json',profile/'palettes/KDE-Current.json')
(kit/'work/noctalia-profile/state').mkdir(parents=True,exist_ok=True)
for name,script in [('menu','open-menu.sh'),('clipboard','open-clipboard.sh'),('return','return-to-plasma.sh'),('recover','recover-at-login.sh')]:
    p=base/f'codex-noctalia-{name}.desktop'
    p.write_text(re.sub(r'^Exec=.*$',f'Exec="{base/script}"',p.read_text(),flags=re.M))
print('Kit prepared in',kit)
print('Destination backup:',backup)
