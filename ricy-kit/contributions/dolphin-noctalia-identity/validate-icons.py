#!/usr/bin/env python3
"""Offline overlay scope, provenance and Qt SVG painting checks; never install."""
import configparser
import hashlib
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent / 'icons/Ricy-Dolphin'
provenance = json.loads((root / 'provenance.json').read_text())
assert provenance['license'] == 'MIT'
assert 'Permission is hereby granted' in (root / 'LICENSE').read_text()
config = configparser.ConfigParser(interpolation=None)
config.read(root / 'index.theme')
assert config['Icon Theme']['Inherits'] == 'breeze-dark,breeze,hicolor'
assert config['Icon Theme']['Directories'] == 'scalable/actions'
assert config['scalable/actions']['Context'] == 'Actions'
expected = {item['kde_name'] for item in provenance['assets']}
assert len(expected) == 13
assert {p.stem for p in root.rglob('*.svg')} == expected
assert all(p.parent == root / 'scalable/actions' for p in root.rglob('*.svg'))
for item in provenance['assets']:
    path = root / 'scalable/actions' / (item['kde_name'] + '.svg')
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['asset_sha256']
    assert provenance['commit'] in item['source']
    assert item['source'].endswith('/' + item['tabler_glyph'] + '.svg')
    svg = ET.parse(path).getroot()
    assert svg.attrib['viewBox'] == '0 0 24 24'
    assert svg.attrib['stroke-width'] == '2'
print('PASS only selected action glyphs, native inheritance, pinned provenance/license and SVG XML')
try:
    from PyQt6.QtSvg import QSvgRenderer
    from PyQt6.QtGui import QImage, QPainter
    from PyQt6.QtCore import Qt
except ImportError:
    print('NOT RUN SVG painting: PyQt6 QtSvg unavailable')
    sys.exit(2)
for path in root.rglob('*.svg'):
    renderer = QSvgRenderer(str(path))
    assert renderer.isValid(), path
    image = QImage(48, 48, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    renderer.render(painter)
    painter.end()
    ink = [image.pixelColor(x, y) for y in range(48) for x in range(48)
           if image.pixelColor(x, y).alpha() > 20]
    assert len(ink) > 20, path
    assert all(pixel.lightness() > 100 for pixel in ink), path
print('PASS all 13 SVGs paint visible strokes on the dark surface')
print('NOT RUN live native loader/modes, content providers, missing-overlay fallback and Recovery')
