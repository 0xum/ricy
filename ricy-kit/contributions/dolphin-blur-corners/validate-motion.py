#!/usr/bin/env python3
"""Compile/run isolated native Qt/KIO motion checks without installation/settings writes."""
from pathlib import Path
import os
import shlex
import shutil
import subprocess
import sys
import tempfile

here = Path(__file__).resolve().parent
if not all(shutil.which(tool) for tool in ('g++', 'pkg-config')):
    print('NOT RUN motion component checks: g++/pkg-config unavailable')
    sys.exit(2)
try:
    qt = shlex.split(subprocess.check_output(
        ['pkg-config', '--cflags', '--libs', 'Qt6Widgets', 'Qt6Test', 'Qt6Xml'], text=True))
except subprocess.CalledProcessError:
    print('NOT RUN motion component checks: Qt6 development dependencies unavailable')
    sys.exit(2)
with tempfile.TemporaryDirectory(prefix='ricy-motion-validation-') as temporary:
    work = Path(temporary)
    config = work / 'config'
    config.mkdir()
    (config / 'kdeglobals').write_text('[KDE]\nAnimationDurationFactor=1\n')
    close_assets = work / 'data/icons/Ricy-Dolphin/scalable/actions'
    close_assets.mkdir(parents=True)
    shutil.copy2(here.parent / 'dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/dialog-close.svg',
                 close_assets / 'dialog-close.svg')
    includes = [f'-I{path}' for path in Path('/usr/include/KF6').iterdir() if path.is_dir()]
    for name in ('validate-motion.cpp', 'motion.h', 'ui.cpp', 'ui.json'):
        shutil.copy2(here / name, work / name)
    flags = shlex.split(subprocess.check_output(['pkg-config', '--cflags', 'Qt6Widgets'], text=True))
    subprocess.run(['/usr/lib/qt6/moc', *includes, *flags, str(work / 'ui.cpp'),
                    '-o', str(work / 'ui.moc')], check=True)
    subprocess.run(['g++', '-std=c++17', '-fPIC', *includes, str(work / 'validate-motion.cpp'),
                    '-o', str(work / 'validate-motion'), *qt, '-lKF6ConfigCore',
                    '-lKF6KIOFileWidgets', '-lKF6KIOCore', '-lKF6KIOWidgets', '-lKF6IconThemes'], check=True)
    environment = dict(os.environ, QT_QPA_PLATFORM='offscreen', XDG_CONFIG_HOME=str(config),
                       XDG_DATA_HOME=str(work / 'data'), XDG_STATE_HOME=str(work / 'state'))
    subprocess.run([str(work / 'validate-motion'),
                    str(here.parent / 'dolphin-noctalia-identity/dolphin.qss')], env=environment, check=True)
    # Loading through Qt's factory exercises ownership that direct fixtures miss.
    generic = work / 'plugins/generic'
    generic.mkdir(parents=True)
    subprocess.run(['g++', '-std=c++17', '-fPIC', '-shared', *includes,
                    str(work / 'ui.cpp'), '-o', str(generic / 'libricydolphinui.so'),
                    *qt, '-lKF6ConfigCore', '-lKF6IconThemes'], check=True)
    subprocess.run(['g++', '-std=c++17', str(here / 'validate-plugin-lifetime.cpp'),
                    '-o', str(work / 'validate-plugin-lifetime'), *qt], check=True)
    environment['QT_PLUGIN_PATH'] = str(work / 'plugins')
    subprocess.run([str(work / 'validate-plugin-lifetime'), '-plugin', 'ricydolphinui'],
                   env=environment, check=True)
    print('PASS generic plugin creation and application shutdown without double deletion')

print('NOT RUN live Dolphin/compositor, large directory repaint/CPU, native KDE disable and Recovery')
