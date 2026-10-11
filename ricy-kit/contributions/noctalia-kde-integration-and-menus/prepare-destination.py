#!/usr/bin/env python3
"""Generates DESTINATION backups and local paths. It does not start or apply the test."""
from pathlib import Path
import tarfile, configparser, re, json, shutil, hashlib
root=Path(__file__).resolve().parent;home=Path.home()
base=root/'outputs/noctalia-test';style=root/'outputs/kde-outlines'
backup=base/'plasma-antes.tar.gz'
if backup.exists() or (style/'estado-antes.json').exists():
 raise SystemExit('Destination already prepared. Do not replace the original backup.')
for rel in ['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc']:
 if not (home/rel).is_file():raise SystemExit('Open a Plasma session with panels before preparing: missing '+rel)
backup.touch(mode=0o600)
rels=['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc','.config/plasmarc','.config/kdeglobals','.config/kwinrc','.config/kglobalshortcutsrc','.config/Kvantum/kvantum.kvconfig','.config/Kvantum/KDE-Noctalia']
manifest={}
with tarfile.open(backup,'w:gz') as t:
 for rel in rels:
  p=home/rel
  if p.exists():
   t.add(p,arcname=rel);manifest[rel]='directory' if p.is_dir() else hashlib.sha256(p.read_bytes()).hexdigest()
  else:manifest[rel]=None
(base/'backup-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(base/'backup-manifest.json').chmod(0o600)
style_backup=style/'kde-antes-contornos.tar.gz';shutil.copy2(backup,style_backup);style_backup.chmod(0o600)
def read(rel):
 c=configparser.ConfigParser(interpolation=None,strict=False);c.optionxform=str;c.read(home/rel);return c
kg=read('.config/kdeglobals');kw=read('.config/kwinrc')
keys=[('kdeglobals','KDE','widgetStyle'),('kdeglobals','General','menuFont'),('kwinrc','Plugins','blurEnabled'),('kwinrc','Effect-blur','BlurStrength'),('kwinrc','Effect-blur','NoiseStrength')]
state={'keys':[[f,g,k,(kg if f=='kdeglobals' else kw).get(g,k,fallback=None)] for f,g,k in keys], 'existing_paths':{rel:(home/rel).exists() for rel in rels}}
(style/'estado-antes.json').write_text(json.dumps(state,indent=2)+'\n');(style/'estado-antes.json').chmod(0o600)
c=read('.config/plasma-org.kde.plasma.desktop-appletsrc');lines=[]
for section in c.sections():
 m=re.fullmatch(r'Containments\]\[(\d+)\]\[Wallpaper\]\[org.kde.image\]\[General',section)
 if m and 'Image' in c[section]:
  lines.append(f'var d=desktopById({int(m[1])}); if(d){{d.currentConfigGroup=["Wallpaper","org.kde.image","General"];d.writeConfig("Image",{json.dumps(c[section]["Image"])});}}')
(base/'restaurar-wallpaper.js').write_text('\n'.join(lines)+'\n');(base/'restaurar-wallpaper.js').chmod(0o600)
profile=root/'work/noctalia-profile/config/noctalia';(profile/'palettes').mkdir(parents=True)
shutil.copy2(base/'config.toml',profile/'config.toml');shutil.copy2(base/'KDE-Current.json',profile/'palettes/KDE-Current.json')
(root/'work/noctalia-profile/state').mkdir(parents=True)
for name,script in [('menu','open-menu.sh'),('return','return-to-plasma.sh'),('recover','recover-at-login.sh'),('clipboard','open-clipboard.sh')]:
 p=base/f'codex-noctalia-{name}.desktop';p.write_text(re.sub(r'^Exec=.*$',lambda _:f'Exec="{base/script}"',p.read_text(),flags=re.M))
print('Prepared:',root,'\nPrivate DESTINATION backup:',backup)
