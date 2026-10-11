#!/usr/bin/env python3
"""Troca somente shell, painéis e atalhos; configurações visuais são compartilhadas."""
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from paineis import capture, merge, panel_groups

BASE = Path(__file__).resolve().parent
SCRIPTS = BASE.parent / 'noctalia-kde-integration-and-menus/outputs/noctalia-test'
PROFILE = SCRIPTS.parents[1] / 'work/noctalia-profile'
HOME = Path.home()
STATE = Path(os.environ.get('XDG_STATE_HOME', HOME / '.local/state')) / 'ricy-alternancia'
APPLETS = HOME / '.config/plasma-org.kde.plasma.desktop-appletsrc'
VIEWS = HOME / '.config/plasmashellrc'
SHELL = 'noctalia-teste.service'
ADAPTER = 'noctalia-busca-desktop.service'
PLASMA = 'plasma-plasmashell.service'
KEYS = [16777250, 268435488, 268435542]
ACTIONS = [(['codex-noctalia-menu.desktop', '_launch', 'Menu Noctalia', 'Menu Noctalia'], KEYS[:2]),
           (['codex-noctalia-clipboard.desktop', '_launch', 'Área de transferência Noctalia', 'Área de transferência Noctalia'], KEYS[2:])]


def run(*args, check=True):
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check).stdout.strip()


def ctl(*args):
    return run('systemctl', '--user', *args)


def active(name):
    return subprocess.run(['systemctl', '--user', 'is-active', '--quiet', name]).returncode == 0


def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.ricy-tmp')
    tmp.write_text(data)
    tmp.chmod(0o600)
    os.replace(tmp, path)


def save(name, obj):
    atomic(STATE / name, json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def plasma(script):
    return run('qdbus6', 'org.kde.plasmashell', '/PlasmaShell', 'org.kde.PlasmaShell.evaluateScript', script)


def wait_plasma():
    for _ in range(100):
        try:
            if 'ready' in plasma('print("ready")'):
                return
        except subprocess.CalledProcessError:
            pass
        time.sleep(.2)
    raise RuntimeError('Plasma não respondeu ao D-Bus.')


def shortcut_call(method, signature, args):
    from gi.repository import Gio, GLib
    bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)
    return bus.call_sync('org.kde.kglobalaccel', '/kglobalaccel', 'org.kde.KGlobalAccel', method,
                         GLib.Variant(signature, args), None, Gio.DBusCallFlags.NONE, 5000, None).unpack()


def capture_shortcuts():
    originals = {}
    for key in KEYS:
        for e in shortcut_call('getGlobalShortcutsByKey', '(i)', (key,))[0]:
            if e[2] in [a[0][0] for a in ACTIONS]:
                continue
            entry = {'id': [e[2], e[0], e[3], e[1]], 'keys': list(e[6])}
            originals[(e[2], e[0])] = entry
    save('atalhos.json', list(originals.values()))


def transfer_shortcuts():
    for e in json.loads((STATE / 'atalhos.json').read_text()):
        shortcut_call('setForeignShortcut', '(asai)', (e['id'], [k for k in e['keys'] if k not in KEYS]))
    for action, keys in ACTIONS:
        for _ in range(20):
            shortcut_call('doRegister', '(as)', (action,))
            shortcut_call('setShortcut', '(asaiu)', (action, keys, 2))
            shortcut_call('setForeignShortcut', '(asai)', (action, keys))
            if all(any(e[2] == action[0] for e in shortcut_call('getGlobalShortcutsByKey', '(i)', (k,))[0]) for k in keys):
                break
            time.sleep(.1)
        else:
            raise RuntimeError('Não foi possível registrar os atalhos do Noctalia.')


def restore_shortcuts():
    if not (STATE / 'troca-ativa').exists():
        return
    for action, _ in ACTIONS:
        shortcut_call('setForeignShortcut', '(asai)', (action, []))
    for e in json.loads((STATE / 'atalhos.json').read_text()):
        shortcut_call('setForeignShortcut', '(asai)', (e['id'], e['keys']))
    for action, _ in ACTIONS:
        shortcut_call('unregister', '(ss)', (action[0], action[1]))


def snapshot_panels():
    ids = json.loads(plasma('print(JSON.stringify(panels().map(function(p){return p.id;})))'))
    if not ids:
        if not (STATE / 'paineis.json').exists():
            raise RuntimeError('Nenhum painel disponível para preservar. Execute o instalador antes de alternar.')
        return False
    # Parar apenas plasmashell garante o flush do KConfig; apps e KWin continuam.
    ctl('stop', PLASMA)
    try:
        saved = capture(APPLETS.read_text(), VIEWS.read_text() if VIEWS.exists() else '')
        if set(saved['panels']) != {str(i) for i in ids}:
            raise RuntimeError('O layout salvo difere dos painéis vivos; nenhuma remoção realizada.')
        save('paineis.json', saved)
    finally:
        ctl('start', PLASMA)
        wait_plasma()
    return True


def restore_panels():
    if json.loads(plasma('print(JSON.stringify(panels().map(function(p){return p.id;})))')):
        return
    saved = json.loads((STATE / 'paineis.json').read_text())
    ctl('stop', PLASMA)
    try:
        current = APPLETS.read_text()
        views = VIEWS.read_text() if VIEWS.exists() else ''
        new_applets, new_views = merge(current, views, saved)
        atomic(APPLETS, new_applets)
        atomic(VIEWS, new_views)
    finally:
        ctl('start', PLASMA)
        wait_plasma()
    if len(json.loads(plasma('print(JSON.stringify(panels().map(function(p){return p.id;})))'))) != len(saved['panels']):
        raise RuntimeError('Os painéis restaurados não apareceram como esperado.')


def restore():
    ctl('stop', ADAPTER)
    ctl('stop', SHELL)
    wait_plasma()
    restore_panels()
    restore_shortcuts()
    ctl('start', 'plasma-krunner.service')
    for name in ['codex-noctalia-menu.desktop', 'codex-noctalia-clipboard.desktop', 'codex-noctalia-voltar.desktop']:
        (HOME / '.local/share/applications' / name).unlink(missing_ok=True)
    (HOME / '.config/autostart/codex-noctalia-recuperar.desktop').unlink(missing_ok=True)
    run('kbuildsycoca6', '--noincremental')
    (SCRIPTS / 'teste-ativo').unlink(missing_ok=True)
    (STATE / 'troca-ativa').unlink(missing_ok=True)
    print('Plasma ativo. Painéis atuais restaurados; wallpaper e personalizações preservados.')


def start():
    os.environ['NOCTALIA_CONFIG_HOME'] = str(PROFILE / 'config')
    os.environ['NOCTALIA_STATE_HOME'] = str(PROFILE / 'state')
    run('/usr/bin/noctalia', 'config', 'validate')
    wait_plasma()
    snapshot_panels()
    if not (STATE / 'troca-ativa').exists():
        capture_shortcuts()
    try:
        ctl('stop', 'plasma-krunner.service')
        ctl('reset-failed', SHELL, ADAPTER)
        ctl('start', SHELL)
        for _ in range(50):
            try:
                run('/usr/bin/noctalia', 'msg', 'status')
                break
            except subprocess.CalledProcessError:
                time.sleep(.2)
        else:
            raise RuntimeError('Noctalia não ficou pronto.')
        run('/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge')
        import shutil
        for name in ['codex-noctalia-menu.desktop', 'codex-noctalia-clipboard.desktop']:
            dest = HOME / '.local/share/applications' / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(SCRIPTS / name, dest)
        dest = HOME / '.config/autostart/codex-noctalia-recuperar.desktop'
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SCRIPTS / dest.name, dest)
        run('kbuildsycoca6', '--noincremental')
        atomic(STATE / 'troca-ativa', 'noctalia\n')
        transfer_shortcuts()
        run(str(SCRIPTS / 'ativar-busca-noctalia.sh'))
        atomic(SCRIPTS / 'teste-ativo', 'noctalia\n')
        plasma('panels().forEach(function(p){p.remove();});print("Painéis recolhidos.")')
        if not active(SHELL) or not active(ADAPTER):
            raise RuntimeError('Shell ou adaptador parou durante a troca.')
    except Exception:
        restore()
        raise
    print('Noctalia ativo. Perfil, wallpaper e personalizações preservados.')


def main():
    if os.geteuid() == 0:
        raise SystemExit('Execute como usuário do desktop, sem sudo.')
    STATE.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (STATE / 'integracao.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        {'iniciar': start, 'restaurar': restore}[sys.argv[1]]()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Falha na alternância: ' + str(e), file=sys.stderr)
        raise SystemExit(1)
