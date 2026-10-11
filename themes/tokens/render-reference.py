#!/usr/bin/env python3
"""Render the existing identity board without installing or activating anything."""
import argparse
from decimal import Decimal
from html import escape
import json
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent
REFERENCE = BASE.parents[1] / 'ricy-kit/contributions/noctalia-visual-identity/reference.svg'


def render(tokens, template):
    if tokens['schema_version'] != 1 or tokens['contract_version'].split('.')[0] != '1':
        raise ValueError('Unsupported Ricy token contract')
    geometry = tokens['geometry']
    scale = Decimal(str(geometry['shell_corner_radius_scale'])) * Decimal(str(tokens['typography']['ui_scale']))
    alpha = tokens['materials']['attached_shell_background']['opacity']
    derived = {
        'radius': {name: Decimal(str(value)) * scale
                   for name, value in geometry['native_radius_logical_px'].items()},
        'shell_alpha_svg': format(alpha, 'g').replace('0.', '.', 1) if 0 < alpha < 1 else format(alpha, 'g'),
        'shell_alpha_label': format(alpha, '.2f'),
        'card_alpha_label': format(tokens['materials']['cards']['opacity'], '.2f'),
    }
    values = dict(tokens, derived=derived)

    def substitute(match):
        value = values
        for part in match[1].split('.'):
            value = value[part]
        if isinstance(value, (dict, list, bool)) or value is None:
            raise ValueError(f'Expected a scalar token: {match[1]}')
        if isinstance(value, Decimal):
            value = format(value.normalize(), 'f')
        elif isinstance(value, float):
            value = format(value, 'g')
        return escape(str(value), quote=True)

    return re.sub(r'\$\{([a-zA-Z0-9_.]+)\}', substitute, template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tokens', type=Path, default=BASE / 'tokens.json')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Compare with the retained board; never write')
    mode.add_argument('--output', type=Path, help='Write only this explicitly selected SVG path')
    args = parser.parse_args()
    try:
        output = render(json.loads(args.tokens.read_text()), (BASE / 'reference.svg.in').read_text()).encode('utf-8')
        if args.check:
            if output != REFERENCE.read_bytes():
                raise ValueError('Generated board differs from reference.svg')
            print('PASS token-generated SVG is byte-for-byte identical to the retained board')
        elif args.output:
            args.output.write_bytes(output)
        else:
            sys.stdout.buffer.write(output)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        parser.exit(1, f'FAIL {error}\n')


if __name__ == '__main__':
    main()
