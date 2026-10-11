#!/usr/bin/env python3
"""Regressions without changing session: preserved content and ID collisions."""
import ast
from pathlib import Path
from panels import capture, merge, panel_groups, sections

base = Path(__file__).resolve().parent
for p in base.glob('*.py'):
    ast.parse(p.read_text(), str(p))
source = '''[Containments][23]
plugin=org.kde.panel

[Containments][23][Applets][43]
plugin=org.kde.plasma.volume

[Containments][23][General]
AppletOrder=43

[Containments][43]
plugin=org.kde.plasma.folder

[Containments][43][Wallpaper][org.kde.image][General]
Image=file:///chosen-wallpaper.png
FillMode=2
'''
views = '[PlasmaViews][Panel 23]\nthickness=44\n\n[Updates]\nKeep=yes\n'
saved = capture(source, views)
assert saved['panels'] == ['23']
assert 'chosen-wallpaper' not in saved['applets']
without = ''.join(b for h, b in sections(source) if not h.startswith('[Containments][23]'))
a, v = merge(without, views, saved)
assert panel_groups(a)[0] == {'23'}
assert '[Containments][43]\nplugin=org.kde.plasma.folder' in a
assert '[Applets][43]' not in a and '[Applets][44]' in a
assert 'AppletOrder=44' in a
for h, b in sections(without):
    assert b.strip() in a
assert '[Updates]\nKeep=yes' in v
assert merge(without, '# preserved comment\n' + views, saved)[1].startswith('# preserved comment\n')
assert merge(source, views, saved) == (source, views)
tray = '''[Containments][9]
plugin=org.kde.panel

[Containments][9][General]
AppletOrder=11;12
SystrayContainmentId=10

[Containments][10]
plugin=org.kde.plasma.private.systemtray

[Containments][10][Applets][11]
plugin=org.kde.plasma.volume

[Containments][10][Applets][12]
plugin=org.kde.plasma.networkmanagement
'''
s = capture(tray, '[PlasmaViews][Panel 9]\nthickness=44\n')
assert '[Containments][10]' in s['applets']
x, y = merge('[Containments][9]\nplugin=org.kde.plasma.folder\n[Containments][9][Wallpaper][custom]\nImage=user-choice\n', '[Unrelated]\nKeep=yes\n', s)
assert 'Image=user-choice' in x and '[Unrelated]\nKeep=yes' in y
assert '[PlasmaViews][Panel 13]' in y and '[Containments][13]\nplugin=org.kde.panel' in x
assert 'SystrayContainmentId=10' in x
try:
    merge('', '', {'panels': [], 'applets': '', 'views': ''})
except ValueError:
    pass
else:
    raise AssertionError('Backup vazio deveria ser recusado.')
print('Regressions passed: wallpaper, desktops, widgets, separate tray, references/IDs, views, idempotence, and empty backup; valid Python syntax.')
