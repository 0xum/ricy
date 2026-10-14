#!/usr/bin/env python3
"""Compile an isolated native Configure fixture without installing or saving preferences."""
from pathlib import Path
import os
import shlex
import shutil
import subprocess
import tempfile

here = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='ricy-configure-validation-') as temporary:
    work = Path(temporary)
    config = work / 'config'
    config.mkdir()
    (config / 'kdeglobals').write_text('[Icons]\nTheme=breeze-dark\n')
    for name in ('ui.cpp', 'ui.json', 'motion.h', 'validate-configure.cpp'):
        shutil.copy2(here / name, work / name)
    flags = shlex.split(subprocess.check_output(['pkg-config', '--cflags', 'Qt6Widgets', 'Qt6Test'], text=True))
    libs = shlex.split(subprocess.check_output(['pkg-config', '--libs', 'Qt6Widgets', 'Qt6Test'], text=True))
    includes = [f'-I{path}' for path in Path('/usr/include/KF6').iterdir() if path.is_dir()]
    for source in ('ui', 'validate-configure'):
        subprocess.run(['/usr/lib/qt6/moc', *includes, *flags, str(work / f'{source}.cpp'),
                        '-o', str(work / f'{source}.moc')], check=True)
    subprocess.run(['g++', '-std=c++17', '-fPIC', *includes, *flags, str(work / 'validate-configure.cpp'),
                    '-o', str(work / 'validate-configure'), *libs, '-lKF6WidgetsAddons', '-lKF6ConfigCore', '-lKF6WindowSystem'], check=True)
    environment = dict(os.environ, QT_QPA_PLATFORM='offscreen', QT_QPA_PLATFORMTHEME='kde',
                       XDG_CONFIG_HOME=str(config), XDG_DATA_HOME=str(work / 'data'),
                       XDG_STATE_HOME=str(work / 'state'), XDG_CACHE_HOME=str(work / 'cache'))
    subprocess.run([str(work / 'validate-configure'),
                    str(here.parent / 'dolphin-noctalia-identity/dolphin.qss')], env=environment, check=True)
print('NOT RUN actual Dolphin setting persistence, live compositor/multiple monitors and Plasma Recovery')
