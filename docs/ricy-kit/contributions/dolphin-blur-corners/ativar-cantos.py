#!/usr/bin/env python3
from pathlib import Path
import configparser,datetime,json,subprocess,sys
key='ricydolphinroundingEnabled';effect='ricydolphinrounding'
def run(args):return subprocess.check_output(args,text=True).strip()
def load():
 result=run(['qdbus6','org.kde.KWin','/Effects','org.kde.kwin.Effects.loadEffect',effect])
 if result!='true':raise RuntimeError('KWin não carregou o efeito; confira plugin/ABI.')
if len(sys.argv)>1:
 if len(sys.argv)!=3 or sys.argv[1]!='--restaurar':raise SystemExit('Uso: ativar-cantos.py [--restaurar BACKUP]')
 data=json.loads((Path(sys.argv[2])/'manifest.json').read_text())
 run(['qdbus6','org.kde.KWin','/Effects','org.kde.kwin.Effects.unloadEffect',effect])
 args=['kwriteconfig6','--file','kwinrc','--group','Plugins','--key',key]
 subprocess.run(args+(['--delete'] if data['key'] is None else [data['key']]),check=True)
 if data['loaded']:load()
 print('Estado anterior restaurado; raios nativos repostos.');raise SystemExit
cfg=configparser.ConfigParser(interpolation=None);cfg.optionxform=str;cfg.read(Path.home()/'.config/kwinrc')
loaded=effect in run(['qdbus6','org.kde.KWin','/Effects','org.kde.kwin.Effects.loadedEffects']).splitlines()
b=Path.home()/'.local/state/ricy-dolphin-corners-backups'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f');b.mkdir(parents=True,mode=0o700)
(b/'manifest.json').write_text(json.dumps({'key':cfg.get('Plugins',key,fallback=None),'loaded':loaded},indent=2)+'\n');(b/'manifest.json').chmod(0o600)
load()
subprocess.run(['kwriteconfig6','--file','kwinrc','--group','Plugins','--key',key,'true'],check=True)
print('Backup:',b)
