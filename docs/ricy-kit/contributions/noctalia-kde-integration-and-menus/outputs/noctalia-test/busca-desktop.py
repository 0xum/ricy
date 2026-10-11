#!/usr/bin/env python3
"""Adaptador da interface de ativação KRunner para o Noctalia no KDE."""
import subprocess
import json
import time
from gi.repository import Gio, GLib

xml = '''<node><interface name="org.kde.krunner.App">
<method name="query"><arg type="s" direction="in"/></method>
<method name="display"/>
<method name="toggleDisplay"/>
<method name="displayWithClipboardContents"/>
<method name="displaySingleRunner"><arg type="s" direction="in"/></method>
<method name="querySingleRunner"><arg type="s" direction="in"/><arg type="s" direction="in"/></method>
</interface></node>'''

def handle(connection, sender, path, interface, method, parameters, invocation):
    values = parameters.unpack()
    term = ''
    if method == 'ActivateAction':
        action, values, platform_data = values
        if action.lower() == 'query' and values:
            term = str(values[0])
    elif method == 'query':
        term = values[0]
    elif method == 'querySingleRunner':
        term = values[1]
    elif method == 'displayWithClipboardContents':
        try:
            term = subprocess.run(['wl-paste', '--no-newline'], capture_output=True, text=True, check=True, timeout=2).stdout
        except (OSError, subprocess.SubprocessError):
            pass
    args = ['/usr/bin/noctalia', 'msg', 'panel-toggle' if method == 'toggleDisplay' else 'panel-open', 'launcher']
    if term:
        args.append(term)
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        if status.get('activePanelId') != 'launcher':
            # O Noctalia também resolve o monitor da busca por activeOutputName.
            output = connection.call_sync(
                'org.kde.KWin', '/KWin', 'org.kde.KWin', 'activeOutputName',
                None, GLib.VariantType.new('(s)'), Gio.DBusCallFlags.NONE, 2000, None,
            ).unpack()[0].strip()
            if not output:
                raise ValueError('KWin não informou o monitor ativo')
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, check=True, timeout=2)
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-show', 'search_edge', output], capture_output=True, check=True, timeout=2)
            time.sleep(0.25)
        subprocess.run(args, capture_output=True, check=True, timeout=5)
        invocation.return_value(GLib.Variant('()', ()))
    except (OSError, subprocess.SubprocessError, GLib.Error, ValueError):
        try:
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, timeout=2)
        except (OSError, subprocess.SubprocessError):
            pass
        invocation.return_dbus_error('org.kde.krunner.NoctaliaUnavailable', 'Noctalia não está disponível')

freedesktop_xml = '<node><interface name="org.freedesktop.Application"><method name="ActivateAction"><arg type="s" direction="in"/><arg type="av" direction="in"/><arg type="a{sv}" direction="in"/></method><method name="Activate"><arg type="a{sv}" direction="in"/></method></interface></node>'
connection = Gio.bus_get_sync(Gio.BusType.SESSION, None)
info = Gio.DBusNodeInfo.new_for_xml(xml)
registration = connection.register_object('/App', info.interfaces[0], handle, None, None)
freedesktop_info = Gio.DBusNodeInfo.new_for_xml(freedesktop_xml)
freedesktop_registration = connection.register_object('/org/kde/krunner', freedesktop_info.interfaces[0], handle, None, None)
result = connection.call_sync('org.freedesktop.DBus', '/org/freedesktop/DBus', 'org.freedesktop.DBus', 'RequestName', GLib.Variant('(su)', ('org.kde.krunner', 4)), GLib.VariantType.new('(u)'), Gio.DBusCallFlags.NONE, 5000, None).unpack()[0]
if result != 1:
    raise SystemExit('O nome D-Bus do KRunner já está em uso')
# A barra de apoio não reage ao ponteiro: só os comandos de abertura a mostram.
# Ao fechar a busca (Escape, clique externo ou escolha de app), recolhemos a barra.
search_was_open = False

def sync_search_edge():
    global search_was_open
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        search_open = status.get('activePanelId') == 'launcher'
        if search_was_open and not search_open:
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, check=True, timeout=2)
        search_was_open = search_open
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return True

subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, timeout=2)
GLib.timeout_add(250, sync_search_edge)
GLib.MainLoop().run()
