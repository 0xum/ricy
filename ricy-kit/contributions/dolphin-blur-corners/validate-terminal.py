#!/usr/bin/env python3
"""Validate native embedded Konsole rendering/input in isolated local state."""
from pathlib import Path
import os
import shlex
import shutil
import subprocess
import tempfile

here = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='ricy-terminal-validation-') as temporary:
    work = Path(temporary)
    for name in ('ui.cpp', 'ui.json', 'motion.h', 'validate-terminal.cpp'):
        shutil.copy2(here / name, work / name)
    includes = [f'-I{path}' for path in Path('/usr/include/KF6').iterdir() if path.is_dir()]
    flags = shlex.split(subprocess.check_output(['pkg-config', '--cflags', 'Qt6Widgets', 'Qt6Test'], text=True))
    libs = shlex.split(subprocess.check_output(['pkg-config', '--libs', 'Qt6Widgets', 'Qt6Test'], text=True))
    for source in ('ui', 'validate-terminal'):
        subprocess.run(['/usr/lib/qt6/moc', *includes, *flags, str(work / f'{source}.cpp'),
                        '-o', str(work / f'{source}.moc')], check=True)
    subprocess.run(['g++', '-std=c++17', '-fPIC', *includes, *flags,
                    str(work / 'validate-terminal.cpp'), '-o', str(work / 'validate-terminal'),
                    *libs, '-lKF6Parts', '-lKF6CoreAddons', '-lKF6IconThemes', '-lKF6ConfigCore', '-lKF6WindowSystem'], check=True)
    environment = dict(os.environ, QT_QPA_PLATFORM='offscreen', XDG_CONFIG_HOME=str(work / 'config'),
                       XDG_DATA_HOME=str(work / 'data'), XDG_STATE_HOME=str(work / 'state'),
                       XDG_CACHE_HOME=str(work / 'cache'))
    subprocess.run(['dbus-run-session', '--', str(work / 'validate-terminal'),
                    str(here.parent / 'dolphin-noctalia-identity/dolphin.qss')], env=environment, check=True)
print('NOT RUN live compositor, sustained terminal output/CPU and Recovery')
