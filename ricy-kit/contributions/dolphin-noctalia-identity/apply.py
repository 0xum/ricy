#!/usr/bin/env python3
"""Dolphin appearance itself, with backup and restoration. No sudo."""
from pathlib import Path
import configparser, datetime, json, shutil, subprocess, sys, re, os, tempfile
home=Path.home(); here=Path(__file__).resolve().parent
name='Ricy-Dolphin'; theme=home/'.config/Kvantum'/name
root=home/'.local/share/ricy-dolphin'; wrapper=home/'.local/bin/ricy-dolphin'
config=home/'.config/Kvantum/kvantum.kvconfig'
desktop=home/'.local/share/applications/org.kde.dolphin.desktop'
drop=home/'.config/systemd/user/plasma-dolphin.service.d/70-ricy-aparencia.conf'
service=home/'.local/share/dbus-1/services/org.freedesktop.FileManager1.service'
targets=[theme,root,wrapper,config,desktop,drop,service,home/".config/dolphinrc"]
def refresh():
 subprocess.run(['systemctl','--user','daemon-reload'],check=True)
 subprocess.run(['kbuildsycoca6','--noincremental'],check=True,stdout=subprocess.DEVNULL)
if len(sys.argv)>1:
 if len(sys.argv)!=3 or sys.argv[1]!='--restaurar': raise SystemExit('Usage: apply.py [--restaurar BACKUP]')
 backup=Path(sys.argv[2]); manifest=json.loads((backup/'manifest.json').read_text())
 for item in manifest:
  path=Path(item['path'])
  if path.is_dir(): shutil.rmtree(path)
  elif path.exists(): path.unlink()
  if item['exists']:
   path.parent.mkdir(parents=True,exist_ok=True)
   source=backup/item['saved']
   if source.is_dir(): shutil.copytree(source,path)
   else: shutil.copy2(source,path)
 refresh(); print('Restaurado. Reabra Dolphin.'); raise SystemExit
base=home/'.config/Kvantum/KDE-Noctalia'
if not base.exists(): raise SystemExit('Aplique primeiro KDE-Noctalia do kit.')
ui=Path(subprocess.check_output([sys.executable,str(here.parent/'dolphin-blur-corners/build-ui.py')],text=True).strip())
backup=home/'.local/state/ricy-dolphin-backups'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
backup.mkdir(parents=True,mode=0o700); manifest=[]
for n,path in enumerate(targets):
 exists=path.exists(); saved=str(n)
 if exists:
  if path.is_dir(): shutil.copytree(path,backup/saved)
  else: shutil.copy2(path,backup/saved)
 manifest.append(dict(path=str(path),exists=exists,saved=saved))
(backup/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
theme.mkdir(parents=True,exist_ok=True)
svg=(base/'KDE-Noctalia.svg').read_text()
for old,new in [('#1E1E2E','#181825'),('#45475A','#46485c'),('#9399B2','#a6adc8')]: svg=re.sub(re.escape(old),new,svg,flags=re.I)
(theme/f'{name}.svg').write_text(svg)
cfg=configparser.ConfigParser(interpolation=None); cfg.optionxform=str; cfg.read(base/'KDE-Noctalia.kvconfig')
for section,values in {'%General':{'comment':'Ricy Dolphin — Noctalia reference','translucent_windows':'true','blurring':'true','reduce_window_opacity':'30','animate_states':'true','layout_spacing':'8','layout_margin':'8','toolbar_icon_size':'22','tree_branch_line':'false'},'GeneralColors':{'window.color':'#181825','base.color':'transparent','alt.base.color':'transparent','light.color':'#46485c','mid.light.color':'#46485c','disabled.text.color':'#a6adc8'},'Hacks':{'transparent_dolphin_view':'true'},'ItemView':{'text.focus.color':'#cdd6f4'},'StatusBar':{'font.bold':'false'}}.items():
 for key,value in values.items(): cfg[section][key]=value
with (theme/f'{name}.kvconfig').open('w') as f: cfg.write(f,space_around_delimiters=False)
shutil.copy2(here/'LICENSE',theme/'LICENSE')
cfg=configparser.ConfigParser(interpolation=None); cfg.optionxform=str; cfg.read(config)
if not cfg.has_section('Applications'): cfg.add_section('Applications')
for key in list(cfg['Applications']):
 apps=[a.strip() for a in cfg['Applications'][key].split(',') if a.strip() and a.strip()!='dolphin']
 if apps: cfg['Applications'][key]=','.join(apps)
 else: del cfg['Applications'][key]
cfg['Applications'][name]='dolphin'
with config.open('w') as f: cfg.write(f,space_around_delimiters=False)
root.mkdir(parents=True,exist_ok=True); shutil.copy2(here/'dolphin.qss',root/'dolphin.qss')
wrapper.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(here/'launch.py',wrapper); wrapper.chmod(0o755)
plugin=root/'plugins/generic'; plugin.mkdir(parents=True,exist_ok=True)
# Never overwrite a shared-library inode mapped by an existing Dolphin process.
fd,temporary=tempfile.mkstemp(prefix='.ricydolphinui-',suffix='.so',dir=plugin)
os.close(fd)
try:
 shutil.copy2(ui,temporary)
 os.replace(temporary,plugin/'libricydolphinui.so')
finally:
 if os.path.exists(temporary): os.unlink(temporary)
desktop.parent.mkdir(parents=True,exist_ok=True)
source=desktop.read_text() if desktop.exists() else Path('/usr/share/applications/org.kde.dolphin.desktop').read_text()
source=re.sub(r'^Exec=.*$',f'Exec="{wrapper}" %u',source,flags=re.M); desktop.write_text(source)
drop.parent.mkdir(parents=True,exist_ok=True)
drop.write_text(f'[Service]\nExecStart=\nExecStart="{wrapper}" --daemon\n')
service.parent.mkdir(parents=True,exist_ok=True)
service.write_text(f'[D-BUS Service]\nName=org.freedesktop.FileManager1\nExec="{wrapper}" --daemon\nSystemdService=plasma-dolphin.service\n')
for group in ['IconsMode','CompactMode','DetailsMode']:
 subprocess.run(['kwriteconfig6','--file','dolphinrc','--group',group,'--key','UseSystemFont','true'],check=True)
 # Preserve dormant personal ViewFont values; UseSystemFont selects KDE/Qt.
for group,key,value in [('General','ShowSelectionToggle','false'),
                        ('General','BrowseThroughArchives','true'),
                        ('DetailsMode','ExpandableFolders','true'),
                        ('DetailsMode','LeftPadding','20')]:
 subprocess.run(['kwriteconfig6','--file','dolphinrc','--group',group,'--key',key,value],check=True)
refresh(); print('Backup:',backup)
# Typography and controls in open instances, without closing them.
services=subprocess.check_output(['qdbus6'],text=True).splitlines()
for bus in services:
 bus=bus.strip()
 if bus.startswith('org.kde.dolphin-'):
  subprocess.run(['qdbus6',bus,'/MainApplication','org.qtproject.Qt.QApplication.setStyleSheet',(root/'dolphin.qss').read_text()],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) # The instance may close between listing it and sending the command.
print('Applied. New windows also load the Kvantum variant.')
