#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'super-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=16777250
mine=['codex-noctalia-menu.desktop','_launch','Menu Noctalia (teste)','Menu Noctalia (teste)']
if not saved.exists():
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 old=[]
 for e in entries:
  if e[2]==mine[0]:continue
  old.append({'id':[e[2],e[0],e[3],e[1]],'keys':list(e[6])})
 saved.write_text(json.dumps(old,indent=2)+'\n')
original=json.loads(saved.read_text())
restore=len(sys.argv)>1 and sys.argv[1]=='restore'
if restore:
 call('setForeignShortcut','(asai)',(mine,[268435488]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setForeignShortcut','(asai)',(mine,[meta,268435488]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Não foi possível registrar Super para o Noctalia')
print('Atalho Super restaurado.' if restore else 'Super e Super+Espaço registrados para o Noctalia.')
