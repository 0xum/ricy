#!/usr/bin/env python3
"""Compila apenas o plugin sobre o código oficial do KWin 6.7.5."""
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess

base = Path(__file__).resolve().parent
cache = Path(os.environ.get('XDG_CACHE_HOME', Path.home() / '.cache'))
source = cache / 'ricy-kwin-src-6.7.5'
work = cache / 'ricy-blur-build-6.7.5'
commit = 'ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7'

def run(args, cwd=None):
    subprocess.run(args, cwd=cwd, check=True)

def output(args, cwd=None):
    return subprocess.check_output(args, cwd=cwd)

header = Path('/usr/include/kwin/config-kwin.h').read_text()
if re.search(r'KWIN_PLUGIN_VERSION_STRING\s+"([^"]+)"', header).group(1) != '6.7.5':
    raise SystemExit('Adaptação para KWin 6.7.5: revise/rebaseie antes de compilar outra versão.')
if not source.exists():
    cache.mkdir(parents=True, exist_ok=True)
    run(['git', 'clone', '--depth', '1', '--branch', 'v6.7.5', '--filter=blob:none', '--sparse', 'https://github.com/KDE/kwin.git', str(source)])
    run(['git', '-C', str(source), 'sparse-checkout', 'set', 'src/plugins/blur'])
if output(['git', 'rev-parse', 'HEAD'], source).decode().strip() != commit:
    raise SystemExit('Fonte com commit inesperado.')
patch = base / 'blur-continuidade.patch'
diff = output(['git', 'diff', '--binary'], source)
if not diff:
    run(['git', 'apply', '--check', str(patch)], source)
    run(['git', 'apply', str(patch)], source)
elif diff != patch.read_bytes():
    raise SystemExit('Fonte contém alterações desconhecidas; confira o diff antes de continuar.')
shutil.copytree(source / 'src/plugins/blur', work, dirs_exist_ok=True)
packages = ['Qt6Core', 'Qt6Gui', 'Qt6Widgets', 'Qt6Quick', 'Qt6DBus', 'KF6CoreAddons', 'KF6WindowSystem', 'epoxy', 'libdrm', 'wayland-server']
flags = shlex.split(output(['pkg-config', '--cflags', *packages]).decode())
flags += ['-I/usr/include/kwin', '-I/usr/include/KF6/KConfig', '-I/usr/include/KF6/KConfigCore', '-I/usr/include/KF6/KConfigGui', '-I/usr/include/KDecoration3']
# Optional cached official headers; a regular Arch installation can use vulkan-headers.
extra_headers = os.environ.get('RICY_VULKAN_HEADERS')
if extra_headers:
    flags += ['-I' + str(Path(extra_headers).resolve())]
elif not Path('/usr/include/vulkan/vulkan_core.h').exists():
    raise SystemExit('Instale vulkan-headers ou indique sua pasta include em RICY_VULKAN_HEADERS.')
run(['/usr/lib/kf6/kconfig_compiler_kf6', 'blur.kcfg', 'blurconfig.kcfgc'], work)
run(['/usr/lib/qt6/rcc', '-name', 'ricyblur', 'blur.qrc', '-o', 'qrc_ricyblur.cpp'], work)
run(['/usr/lib/qt6/moc', *flags, 'blur.h', '-o', 'moc_blur.cpp'], work)
run(['/usr/lib/qt6/moc', *flags, 'main.cpp', '-o', 'main.moc'], work)
libs = shlex.split(output(['pkg-config', '--libs', *packages]).decode())
run(['g++', '-std=c++20', '-O2', '-fPIC', '-fvisibility=hidden', '-shared', *flags, 'blur.cpp', 'main.cpp', 'blurconfig.cpp', 'qrc_ricyblur.cpp', '-o', 'ricyblur.so', '-lkwin', '-lKF6ConfigGui', '-lKF6ConfigCore', '-lkdecorations3', *libs], work)
print(f'Plugin pronto: {work / "ricyblur.so"}')
