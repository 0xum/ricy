#!/usr/bin/env python3
"""Check token structure, provenance and migration equivalence offline."""
import configparser
import hashlib
import json
import math
from pathlib import Path
import re
import runpy
import sys
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate token key: {key}')
        result[key] = value
    return result


def walk(value, path=''):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk(item, f'{path}.{key}' if path else key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, f'{path}.{index}')
    else:
        yield path, value


def validate_documented_paths(tokens, documents):
    """Resolve documentary token paths without implementing semantic aliases."""
    pattern = re.compile(
        r'`((?:colors|materials|typography|geometry|motion|blur|application_adaptations)\.[a-z0-9_.]+)`'
    )
    count = 0
    for document in documents:
        paths = set(pattern.findall(document.read_text(encoding='utf-8')))
        require(paths, f'No canonical token references in {document.name}')
        for path in sorted(paths):
            target = tokens
            for part in path.split('.'):
                require(isinstance(target, dict) and part in target,
                        f'{document.name}: unresolved canonical token path {path}')
                target = target[part]
        count += len(paths)
    return count


def main():
    tokens = json.loads((BASE / 'tokens.json').read_text(), object_pairs_hook=unique_object)
    require(type(tokens['schema_version']) is int and tokens['schema_version'] == 1,
            'Unsupported schema_version')
    require(tokens['contract_version'] == '1.0.0', 'Review the validator for a new contract version')
    for group in ('colors', 'materials', 'typography', 'geometry', 'motion', 'blur', 'application_adaptations'):
        require(isinstance(tokens[group], dict) and tokens[group], f'Missing token group: {group}')
    colors = tokens['colors']
    for name, value in colors.items():
        require(re.fullmatch(r'#[0-9a-f]{6}', value), f'Invalid sRGB color: {name}')
    for path, value in walk(tokens):
        key = path.rsplit('.', 1)[-1]
        if isinstance(value, (float, int)) and not isinstance(value, bool):
            require(math.isfinite(value), f'Non-finite number: {path}')
            if key == 'opacity':
                require(0 <= value <= 1, f'Opacity outside [0, 1]: {path}')
            if key.endswith('alpha_255'):
                require(type(value) is int and 0 <= value <= 255, f'Invalid 8-bit alpha: {path}')
            if key.endswith('_ms') or key.endswith('_logical_px'):
                require(value >= 0, f'Negative duration/dimension: {path}')
        if key == 'color' or (key in {'outline', 'neutral', 'active', 'active_text', 'hover', 'hover_text',
                                     'selected', 'highlighted_text', 'border', 'background', 'foreground',
                                     'secondary_text'} and path.startswith('application_adaptations.')):
            require(value in colors or re.fullmatch(r'#[0-9a-f]{6}', value), f'Unresolved color role: {path}')
        if key.endswith('_ref'):
            target = tokens
            for part in value.split('.'):
                target = target[part]
            require(isinstance(target, (str, int, float)), f'Invalid scalar reference: {path}')
    print('PASS contract version, groups, color references, finite numbers and alpha units')

    count = validate_documented_paths(tokens, [
        BASE / 'SEMANTICS.md', ROOT / 'docs/NOCTALIA-VISUAL-GROUNDING.md',
    ])
    print(f'PASS {count} documentary canonical token references (semantic roles/Noctalia grounding)')

    provenance = tokens['provenance']
    reference = ROOT / provenance['reference']
    require(hashlib.sha256(reference.read_bytes()).hexdigest() == provenance['reference_sha256'],
            'Retained identity snapshot changed; audit its provenance')
    legacy = json.loads(reference.read_text())
    for group in ('colors', 'materials', 'typography', 'motion'):
        require(tokens[group] == legacy[group], f'Existing values changed in {group}')
    geometry = dict(legacy['geometry'])
    del geometry['native_radius_at_ui_scale_1_logical_px']
    require(tokens['geometry'] == geometry, 'Existing geometry changed')

    def resolve_colors(value):
        if isinstance(value, dict):
            return {key: resolve_colors(item) for key, item in value.items()}
        if isinstance(value, list):
            return [resolve_colors(item) for item in value]
        return colors.get(value, value) if isinstance(value, str) else value

    dolphin = dict(tokens['application_adaptations']['dolphin'])
    selection = dolphin.pop('file_selection')
    # The user approved the search-result Places adaptation on 2026-10-11.
    # Retain exact promotion equivalence for the other legacy adaptations.
    places = dolphin.pop('places_buttons')
    # Requested 2026-10-11: scoped row radius and padded navigation treatment.
    dolphin.pop('navigation')
    dolphin.pop('toolbar')
    # Scoped native popup, scrollbar and panel treatments requested 2026-10-11.
    for adaptation in ('context_menu', 'scrollbars', 'rubber_band', 'panel_layout', 'launch'):
        dolphin.pop(adaptation)
    require(dolphin['rows']['radius_max'] == tokens['geometry']['native_radius_logical_px']['medium'],
            'Dolphin rows must use the native medium radius')
    dolphin['rows'] = dict(dolphin['rows'])
    dolphin['rows']['radius_max'] = legacy['application_adaptations']['dolphin']['rows']['radius_max']
    legacy_dolphin = dict(legacy['application_adaptations']['dolphin'])
    legacy_dolphin.pop('places_buttons')
    require(resolve_colors(dolphin) == legacy_dolphin,
            'Existing Dolphin adaptation outside Places changed')
    require(places['style'] == 'search_results'
            and places['neutral_alpha_255'] == 0 and places['border_alpha_255'] == 0,
            'Places results must remain borderless with transparent normal rows')
    helper = (ROOT / selection['source']).read_text()
    require('fill.setAlpha(selected ? 170 : 95)' in helper and 'fill.setAlpha(195)' in helper,
            'Audit Dolphin selection alpha changes')
    require([selection[key] for key in ('hover_alpha_255', 'selected_alpha_255', 'selected_hover_alpha_255')]
            == [95, 170, 195], 'Dolphin selection alpha differs from its source')
    config = configparser.ConfigParser()
    konsole = tokens['application_adaptations']['konsole']
    config.read(ROOT / konsole['source'])
    require(config.getfloat('General', 'Opacity') == konsole['opacity'], 'Konsole opacity differs')
    background = tuple(int(value) for value in config['Background']['Color'].split(','))
    require('#%02x%02x%02x' % background == konsole['background'], 'Konsole background differs')
    require(config.getboolean('General', 'Blur') == konsole['compositor_blur'], 'Konsole blur intent differs')
    preferences = json.loads((ROOT / 'ricy-kit/contributions/login-lock-cursor-appearance/preferences.json').read_text())
    settings = preferences['.config/kwinrc']['Effect-blur']
    require(tokens['blur']['settings']['strength'] == int(settings['BlurStrength'])
            and tokens['blur']['settings']['noise_strength'] == int(settings['NoiseStrength']),
            'KWin reference settings differ')
    print('PASS existing identity values, scoped adaptations and retained snapshot SHA-256')

    renderer = runpy.run_path(str(BASE / 'render-reference.py'))
    template = (BASE / 'reference.svg.in').read_text()
    svg = renderer['render'](tokens, template)
    ET.fromstring(svg)
    require(svg.encode('utf-8') == renderer['REFERENCE'].read_bytes(), 'Generated board differs')
    # Exercise consumption: a changed semantic accent must reach the rendered SVG.
    variant = json.loads(json.dumps(tokens))
    variant['colors']['accent'] = '#010203'
    changed = renderer['render'](variant, template)
    require('#010203' in changed and colors['accent'] not in changed, 'SVG does not consume the accent token')
    require('${' not in svg, 'Unresolved SVG template placeholder')
    print('PASS SVG XML, exact before/after bytes and semantic token propagation')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ET.ParseError, configparser.Error) as error:
        print(f'FAIL {error}', file=sys.stderr)
        sys.exit(1)
