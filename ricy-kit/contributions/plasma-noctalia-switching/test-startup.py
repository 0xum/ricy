#!/usr/bin/env python3
"""Exercise cold-login preparation and real-start failure without a desktop session."""
from contextlib import ExitStack, redirect_stdout
import io
import os
from pathlib import Path
import subprocess
import tempfile
from unittest.mock import patch
import integration


def scenario(shell_fails=False):
    calls = []
    with tempfile.TemporaryDirectory(prefix='ricy-startup-test-') as temporary, ExitStack() as stack:
        root = Path(temporary)
        scripts = root / 'scripts'
        scripts.mkdir()
        for name in ('codex-noctalia-menu.desktop', 'codex-noctalia-clipboard.desktop',
                     'codex-noctalia-recover.desktop'):
            (scripts / name).write_text('[Desktop Entry]\nType=Application\n')
        for name, value in {'HOME': root / 'home', 'STATE': root / 'state',
                            'SCRIPTS': scripts, 'PROFILE': root / 'profile'}.items():
            stack.enter_context(patch.object(integration, name, value))
        stack.enter_context(patch.dict(os.environ))
        for name in ('wait_plasma', 'snapshot_panels', 'capture_shortcuts',
                     'transfer_shortcuts', 'plasma'):
            stack.enter_context(patch.object(integration, name))
        stack.enter_context(patch.object(integration, 'active', return_value=True))
        recovered = stack.enter_context(patch.object(integration, 'restore'))

        def run(*args, check=True):
            calls.append(args)
            if args[:3] == ('systemctl', '--user', 'reset-failed'):
                if check:
                    raise subprocess.CalledProcessError(1, args, stderr='Unit not loaded')
                return ''
            if shell_fails and args == ('systemctl', '--user', 'start', integration.SHELL):
                raise subprocess.CalledProcessError(1, args, stderr='Shell startup failed')
            return ''

        stack.enter_context(patch.object(integration, 'run', side_effect=run))
        with redirect_stdout(io.StringIO()):
            if shell_fails:
                try:
                    integration.start()
                except subprocess.CalledProcessError as error:
                    assert error.cmd == ('systemctl', '--user', 'start', integration.SHELL)
                else:
                    raise AssertionError('Shell startup failure must propagate')
                recovered.assert_called_once_with()
            else:
                integration.start()
                recovered.assert_not_called()
                assert (root / 'state/troca-ativa').exists()
                assert (scripts / 'teste-ativo').exists()
        assert ('systemctl', '--user', 'start', integration.SHELL) in calls


if __name__ == '__main__':
    scenario()
    print('PASS cold startup proceeds when reset-failed reports unloaded units')
    scenario(shell_fails=True)
    print('PASS a real shell-start failure still restores Plasma and propagates')
