#!/usr/bin/env python3
from pathlib import Path
import os,re,shlex,shutil,subprocess
base=Path(__file__).resolve().parent
version=re.search(r'KWIN_PLUGIN_VERSION_STRING\s+"([^"]+)"',Path('/usr/include/kwin/config-kwin.h').read_text()).group(1)
if version!='6.7.5': raise SystemExit('Compatibility: KWin 6.7.5. Review the API before compiling another version.')
work=Path(os.environ.get('XDG_CACHE_HOME',Path.home()/'.cache'))/'ricy-dolphin-corners-build-6.7.5'; work.mkdir(parents=True,exist_ok=True)
for name in ['corners.cpp','metadata.json']: shutil.copy2(base/name,work/name)
packages=['Qt6Core','Qt6Gui','Qt6Widgets','Qt6Quick','Qt6DBus','KF6CoreAddons','KF6WindowSystem','epoxy','libdrm','wayland-server']
flags=shlex.split(subprocess.check_output(['pkg-config','--cflags',*packages],text=True))+['-I/usr/include/kwin','-I/usr/include/KF6/KConfig','-I/usr/include/KF6/KConfigCore','-I/usr/include/KF6/KConfigGui','-I/usr/include/KDecoration3']
if not Path('/usr/include/vulkan/vulkan_core.h').exists():
 extra=os.environ.get('RICY_VULKAN_HEADERS')
 if not extra: raise SystemExit('Instale vulkan-headers ou defina RICY_VULKAN_HEADERS.')
 flags+=['-I'+extra]
libs=shlex.split(subprocess.check_output(['pkg-config','--libs',*packages],text=True))
subprocess.run(['/usr/lib/qt6/moc',*flags,'corners.cpp','-o','corners.moc'],cwd=work,check=True)
subprocess.run(['g++','-std=c++20','-O2','-fPIC','-fvisibility=hidden','-shared',*flags,'corners.cpp','-o','ricydolphinrounding.so','-lkwin','-lKF6ConfigGui','-lKF6ConfigCore','-lkdecorations3',*libs],cwd=work,check=True)
print(work/'ricydolphinrounding.so')
