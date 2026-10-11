#!/usr/bin/env python3
"""Restaura os valores capturados no destino; não restaura painéis nem cores opcionais."""
from pathlib import Path
import json,subprocess,tarfile,shutil
from gi.repository import Gio,GLib
root=Path(__file__).resolve().parent;style=root/'outputs/kde-outlines';home=Path.home()
state=json.loads((style/'estado-antes.json').read_text())
for f,g,k,v in state['keys']:
 args=['kwriteconfig6','--file',f,'--group',g,'--key',k]
 subprocess.run(args+(['--delete'] if v is None else [v]),check=True)
with tarfile.open(style/'kde-antes-contornos.tar.gz') as t:
 for rel in ['.config/Kvantum/kvantum.kvconfig','.config/Kvantum/KDE-Noctalia']:
  dest=home/rel
  if dest.is_dir():shutil.rmtree(dest)
  elif dest.exists():dest.unlink()
  if state['existing_paths'].get(rel):
   for member in t.getmembers():
    if member.name==rel or member.name.startswith(rel+'/'):t.extract(member,path=home,filter='data')
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
bus.emit_signal(None,'/KDEPlatformTheme','org.kde.KDEPlatformTheme','refreshFonts',None)
bus.emit_signal(None,'/KGlobalSettings','org.kde.KGlobalSettings','notifyChange',GLib.Variant('(ii)',(2,0)));bus.flush_sync(None)
effective=subprocess.check_output(['kreadconfig6','--file','kdeglobals','--group','KDE','--key','widgetStyle'],text=True).strip()
if effective.lower()=='kvantum':subprocess.run(['python',str(root/'recarregar-estilo.py')],check=True)
subprocess.run(['qdbus6','org.kde.KWin','/KWin','org.kde.KWin.reconfigure'],check=True)
print('Estilo, fonte e blur restaurados aos valores capturados. Reabra aplicativos se necessário.')
