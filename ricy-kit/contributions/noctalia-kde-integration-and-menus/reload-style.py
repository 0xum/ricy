#!/usr/bin/env python3
"""Reloads Kvantum after editing the same theme; does not close the applications."""
from gi.repository import Gio,GLib
import subprocess,time
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
bus.emit_signal(None,'/KDEPlatformTheme','org.kde.KDEPlatformTheme','refreshFonts',None);bus.flush_sync(None)
original=subprocess.check_output(['kreadconfig6','--file','kdeglobals','--group','KDE','--key','widgetStyle'],text=True).strip()
if original.lower()!='kvantum':raise SystemExit('Active style is not Kvantum; nothing has been alternated.')
try:
 subprocess.run(['kwriteconfig6','--file','kdeglobals','--group','KDE','--key','widgetStyle','Breeze'],check=True)
 bus.emit_signal(None,'/KGlobalSettings','org.kde.KGlobalSettings','notifyChange',GLib.Variant('(ii)',(2,0)));bus.flush_sync(None);time.sleep(.5)
finally:
 subprocess.run(['kwriteconfig6','--file','kdeglobals','--group','KDE','--key','widgetStyle',original],check=True)
 bus.emit_signal(None,'/KGlobalSettings','org.kde.KGlobalSettings','notifyChange',GLib.Variant('(ii)',(2,0)));bus.flush_sync(None)
