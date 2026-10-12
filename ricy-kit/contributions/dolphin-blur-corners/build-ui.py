#!/usr/bin/env python3
from pathlib import Path
import os,shlex,shutil,subprocess
base=Path(__file__).resolve().parent
work=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-dolphin-ui-build';work.mkdir(parents=True,exist_ok=True)
for name in ['ui.cpp','ui.json','motion.h']:shutil.copy2(base/name,work/name)
flags=shlex.split(subprocess.check_output(['pkg-config','--cflags','Qt6Widgets'],text=True))
libs=shlex.split(subprocess.check_output(['pkg-config','--libs','Qt6Widgets'],text=True))
# Dolphin already uses this native KDE icon loader. The helper selects an
# optional process-local overlay while retaining its inherited content providers.
flags += ['-I/usr/include/KF6/KIconThemes', '-I/usr/include/KF6/KConfigCore', '-I/usr/include/KF6/KConfig']
libs += ['-lKF6IconThemes', '-lKF6ConfigCore']
subprocess.run(['/usr/lib/qt6/moc',*flags,'ui.cpp','-o','ui.moc'],cwd=work,check=True)
subprocess.run(['g++','-std=c++17','-O2','-fPIC','-shared',*flags,'ui.cpp','-o','libricydolphinui.so',*libs],cwd=work,check=True)
print(work/'libricydolphinui.so')
