#!/usr/bin/env python3
from pathlib import Path
import os,shlex,shutil,subprocess
base=Path(__file__).resolve().parent
work=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-dolphin-ui-build';work.mkdir(parents=True,exist_ok=True)
for name in ['ui.cpp','ui.json']:shutil.copy2(base/name,work/name)
flags=shlex.split(subprocess.check_output(['pkg-config','--cflags','Qt6Widgets'],text=True))
libs=shlex.split(subprocess.check_output(['pkg-config','--libs','Qt6Widgets'],text=True))
subprocess.run(['/usr/lib/qt6/moc',*flags,'ui.cpp','-o','ui.moc'],cwd=work,check=True)
subprocess.run(['g++','-std=c++17','-O2','-fPIC','-shared',*flags,'ui.cpp','-o','libricydolphinui.so',*libs],cwd=work,check=True)
print(work/'libricydolphinui.so')
