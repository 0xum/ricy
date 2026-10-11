#!/usr/bin/env python3
"""Install the local minimize/restore effect without restarting the compositor."""
import argparse,configparser,json,os,shutil,subprocess
from pathlib import Path
from datetime import datetime
home=Path.home();base=Path(__file__).resolve().parent
config=Path(os.environ.get('XDG_CONFIG_HOME',home/'.config'))/'kwinrc'
data=Path(os.environ.get('XDG_DATA_HOME',home/'.local/share'))
state=Path(os.environ.get('XDG_STATE_HOME',home/'.local/state'))
target=data/'kwin/effects/ricywindowactions'
settings={('Plugins','ricywindowactionsEnabled'):'true',('Plugins','squashEnabled'):'false',('Plugins','magiclampEnabled'):'false',('Plugins','scaleEnabled'):'true',('Plugins','fadeEnabled'):'false',('Effect-scale','Duration'):'180',('Effect-scale','InScale'):'0.92',('Effect-scale','OutScale'):'0.92'}
def dbus(method,*args):
 return subprocess.check_output(['qdbus6','org.kde.KWin','/Effects','org.kde.kwin.Effects.'+method,*args],text=True).strip()
def config_write(group,key,value):
 cmd=['kwriteconfig6','--file',str(config),'--group',group,'--key',key]
 cmd+=['--delete'] if value is None else [str(value)]
 subprocess.run(cmd,check=True)
def reconfigure():subprocess.run(['qdbus6','org.kde.KWin','/KWin','org.kde.KWin.reconfigure'],check=True,capture_output=True)
def main():
 if os.geteuid()==0:raise SystemExit('Run in session as a user without sudo.')
 parser=argparse.ArgumentParser();parser.add_argument('--restaurar',type=Path);args=parser.parse_args()
 if args.restaurar:
  m=json.loads((args.restaurar/'manifest.json').read_text());dbus('unloadEffect','ricywindowactions')
  if target.exists():shutil.rmtree(target)
  if m['had_effect']:shutil.copytree(args.restaurar/'effect',target)
  for row in m['settings']:config_write(row['group'],row['key'],row['value'])
  reconfigure();print('Previous effect and preferences restored.');return
 before=configparser.ConfigParser(interpolation=None,strict=False);before.optionxform=str;before.read(config)
 backup=state/'ricy-indicador-animacoes-backups'/datetime.now().strftime('%Y%m%d-%H%M%S-%f');backup.mkdir(parents=True,mode=0o700)
 m={'had_effect':target.exists(),'settings':[{'group':g,'key':k,'value':before.get(g,k,fallback=None)} for g,k in settings]}
 if target.exists():shutil.copytree(target,backup/'effect')
 (backup/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
 shutil.copytree(base/'assets/kwin/effects/ricywindowactions',target,dirs_exist_ok=True)
 for (g,k),v in settings.items():config_write(g,k,v)
 dbus('unloadEffect','squash');dbus('unloadEffect','magiclamp');dbus('unloadEffect','fade');dbus('unloadEffect','ricywindowactions')
 reconfigure()
 loaded=dbus('loadEffect','ricywindowactions');dbus('loadEffect','scale');dbus('reconfigureEffect','scale')
 if dbus('isEffectLoaded','ricywindowactions')!='true':raise SystemExit('Effect did not load; backup preserved: '+str(backup))
 print('Backup: '+str(backup));print('Animations loaded, no restart KWin.')
if __name__=='__main__':main()
