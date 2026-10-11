#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'clipboard-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=268435542
mine=['codex-noctalia-clipboard.desktop','_launch','Área de transferência Noctalia (teste)','Área de transferência Noctalia (teste)']
call('doRegister','(as)',(mine,))
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
 call('setForeignShortcut','(asai)',(mine,[]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setShortcut','(asaiu)',(mine,[meta],2))
 call('setForeignShortcut','(asai)',(mine,[meta]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Não foi possível registrar Super+V para o Noctalia')
print('Super+V restaurado.' if restore else 'Super+V registrado para o Noctalia.')
