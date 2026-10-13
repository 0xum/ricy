#!/usr/bin/env python3
"""Exercise session-specific Dolphin shortcuts without contacting the desktop."""
from pathlib import Path
import json
import tempfile
from unittest.mock import patch
import integration

NATIVE = ['org.kde.dolphin-plasma.desktop', '_launch', 'Dolphin (Plasma)', 'Dolphin (Plasma)']
MENU = ['plasmashell', 'activate application launcher', 'Plasma', 'Application Launcher']
CLIPBOARD = ['plasmashell', 'clipboard', 'Plasma', 'Clipboard']
EXTRA = 150994992


class Shortcuts:
    def __init__(self, native=True):
        self.actions = {}
        self.unregistered = []
        for action, keys in ((MENU, [integration.KEYS[0], EXTRA]),
                             (CLIPBOARD, [integration.KEYS[2]]),
                             (NATIVE, [integration.KEYS[3]] if native else []),
                             (integration.DOLPHIN_ACTION, [])):
            self.actions[tuple(action[:2])] = [action, keys]

    def call(self, method, signature, arguments):
        if method == 'getComponent':
            return ('/component/org_kde_dolphin_desktop' if tuple(integration.DOLPHIN_ACTION[:2]) in self.actions else '/',)
        if method == 'getGlobalShortcutsByKey':
            return ([tuple([action[1], action[3], action[0], action[2], 'default', 'Default', keys[:], []])
                     for action, keys in self.actions.values() if arguments[0] in keys],)
        if method == 'shortcut':
            return (self.actions.get(tuple(arguments[0][:2]), [arguments[0], []])[1][:],)
        if method == 'doRegister':
            self.actions.setdefault(tuple(arguments[0][:2]), [arguments[0], []])
            return ()
        if method in ('setShortcut', 'setForeignShortcut'):
            action, keys = arguments[:2]
            identity = tuple(action[:2])
            assert not any(key in other for owner, (_, other) in self.actions.items()
                           if owner != identity for key in keys), 'duplicate key ownership'
            self.actions[identity] = [action, keys[:]]
            return (keys[:],) if method == 'setShortcut' else ()
        if method == 'unregister':
            self.unregistered.append(arguments)
            self.actions.pop(tuple(arguments), None)
            return (True,)
        raise AssertionError(method)

    def run(self, *arguments, **kwargs):
        assert arguments == ('qdbus6', 'org.kde.kglobalaccel', '/component/org_kde_dolphin_desktop',
                             'org.kde.kglobalaccel.Component.cleanUp')
        self.actions.pop(tuple(integration.DOLPHIN_ACTION[:2]), None)
        return 'true'

    def keys(self, action):
        return self.actions[tuple(action[:2])][1]


def scenario(native=True, migrate=False, partial=False):
    backend = Shortcuts(native)
    with tempfile.TemporaryDirectory(prefix='ricy-shortcuts-test-') as temporary:
        state = Path(temporary)
        (state / 'troca-ativa').write_text('noctalia\n')
        with patch.object(integration, 'STATE', state), patch.object(integration, 'shortcut_call', backend.call), \
                patch.object(integration, 'run', backend.run):
            if migrate:
                old = [{'id': MENU, 'keys': backend.keys(MENU)[:]},
                       {'id': CLIPBOARD, 'keys': backend.keys(CLIPBOARD)[:]}]
                if partial:
                    old.append({'id': NATIVE, 'keys': [integration.KEYS[3]]})
                    backend.actions[tuple(NATIVE[:2])][1] = []
                    backend.actions[tuple(integration.DOLPHIN_ACTION[:2])][1] = [integration.KEYS[3]]
                integration.save('atalhos.json', old)
                assert integration.ensure_dolphin_shortcut_snapshot()
                assert json.loads((state / 'atalhos.json').read_text())[:2] == old[:2]
            else:
                integration.capture_shortcuts()
            original = (state / 'atalhos.json').read_bytes()
            integration.transfer_shortcuts()
            assert backend.keys(integration.DOLPHIN_ACTION) == [integration.KEYS[3]]
            assert backend.keys(NATIVE) == []
            assert backend.keys(MENU) == [EXTRA]
            assert backend.keys(integration.ACTIONS[1][0]) == [integration.KEYS[2]]
            assert not integration.ensure_dolphin_shortcut_snapshot()
            assert (state / 'atalhos.json').read_bytes() == original
            integration.transfer_shortcuts()  # Reentry retains Plasma's original owner.
            integration.restore_shortcuts()
            assert backend.keys(NATIVE) == ([integration.KEYS[3]] if native else [])
            assert backend.keys(integration.DOLPHIN_ACTION) == []
            assert backend.keys(MENU) == [integration.KEYS[0], EXTRA]
            assert backend.keys(CLIPBOARD) == [integration.KEYS[2]]
            assert tuple(integration.DOLPHIN_ACTION[:2]) not in backend.unregistered
            integration.transfer_shortcuts()  # New cycle keeps the persistent Dolphin action.
            assert backend.keys(integration.DOLPHIN_ACTION) == [integration.KEYS[3]]


if __name__ == '__main__':
    scenario()
    scenario(native=False)
    scenario(migrate=True)
    scenario(migrate=True, partial=True)
    print('PASS Dolphin shortcut transfer/restore, unbound original, older/partial snapshot migration, reentry and menu/clipboard preservation')
