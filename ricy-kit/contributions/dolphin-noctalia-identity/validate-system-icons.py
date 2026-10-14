#!/usr/bin/env python3
"""Check system icon inheritance and theme changes in isolated Qt fixtures."""
from pathlib import Path
import os
import shlex
import shutil
import subprocess
import tempfile

here = Path(__file__).resolve().parent
helper = here.parent / 'dolphin-blur-corners'
with tempfile.TemporaryDirectory(prefix='ricy-system-icons-') as temporary:
    work = Path(temporary)
    config = work / 'config'
    config.mkdir()
    data = work / 'data'
    # A stale, valid legacy overlay must not override the system selection.
    for name in ('Ricy-Test-One', 'Ricy-Test-Two', 'Ricy-Dolphin'):
        theme = data / 'icons' / name
        actions = theme / 'scalable/actions'
        actions.mkdir(parents=True)
        (theme / 'index.theme').write_text(
            f'[Icon Theme]\nName={name}\nInherits=breeze,hicolor\nDirectories=scalable/actions\n'
            '[scalable/actions]\nSize=24\nType=Scalable\nMinSize=8\nMaxSize=256\nContext=Actions\n')
        for icon in ('go-next', 'dialog-close'):
            (actions / f'{icon}.svg').write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24">'
                '<path d="M4 4L20 20M20 4L4 20" stroke="white" stroke-width="2"/></svg>')
    for name in ('ui.cpp', 'ui.json', 'motion.h'):
        shutil.copy2(helper / name, work / name)
    (work / 'check.cpp').write_text(r'''
#include "ui.cpp"
#include <KIconTheme>
#include <KIconLoader>
#include <cstdio>
int main(int argc, char **argv) {
    QCoreApplication::setApplicationName("dolphin");
    QApplication app(argc, argv);
    RicyDolphinUi helper;
    auto check = [](const QString &theme) {
        if (KIconTheme::current() != theme) return false;
        for (const auto &name : {QStringLiteral("go-next"), QStringLiteral("dialog-close")}) {
            const QString path = KIconLoader::global()->iconPath(name, -24, true);
            if (!path.contains("/icons/" + theme + "/")) return false;
            if (QIcon::fromTheme(name).pixmap(24,24).isNull()) return false;
        }
        return true;
    };
    if (!check("Ricy-Test-One")) { fprintf(stderr,"FAIL initial native theme resolution\n"); return 1; }
    auto globals = KSharedConfig::openConfig("kdeglobals");
    KConfigGroup(globals, "Icons").writeEntry("Theme", "Ricy-Test-Two");
    globals->sync();
    // Simulate the Qt platform theme update without broadcasting on the user's bus.
    QIcon::setThemeName("Ricy-Test-Two");
    KIconTheme::reconfigure();
    KIconLoader::global()->reconfigure("dolphin", {});
    if (!check("Ricy-Test-Two")) {
        fprintf(stderr,"FAIL native theme reconfiguration\n"); return 1;
    }
    fprintf(stderr,"PASS system icons ignore the legacy overlay and follow native theme reconfiguration\n");
    return 0;
}
''')
    flags = shlex.split(subprocess.check_output(
        ['pkg-config', '--cflags', '--libs', 'Qt6Widgets'], text=True))
    includes = [f'-I{path}' for path in Path('/usr/include/KF6').iterdir() if path.is_dir()]
    moc_flags = shlex.split(subprocess.check_output(['pkg-config', '--cflags', 'Qt6Widgets'], text=True))
    subprocess.run(['/usr/lib/qt6/moc', *includes, *moc_flags, str(work / 'ui.cpp'),
                    '-o', str(work / 'ui.moc')], check=True)
    subprocess.run(['g++', '-std=c++17', '-fPIC', *includes, str(work / 'check.cpp'),
                    '-o', str(work / 'check'), *flags, '-lKF6IconThemes', '-lKF6ConfigCore', '-lKF6WindowSystem'], check=True)
    (config / 'kdeglobals').write_text('[Icons]\nTheme=Ricy-Test-One\n')
    environment = dict(os.environ, QT_QPA_PLATFORM='offscreen', QT_QPA_PLATFORMTHEME='kde',
                       XDG_CONFIG_HOME=str(config), XDG_DATA_HOME=str(data),
                       XDG_STATE_HOME=str(work / 'state'), XDG_CACHE_HOME=str(work / 'cache'))
    subprocess.run([str(work / 'check')], env=environment, check=True)
print('NOT RUN live system settings notification, compositor and Plasma Recovery')
