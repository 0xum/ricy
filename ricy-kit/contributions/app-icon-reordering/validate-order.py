#!/usr/bin/env python3
"""Validates the actual order logic of the C++ font without changing the session."""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--fonte', type=Path, default=Path(os.environ.get('XDG_CACHE_HOME', Path.home() / '.cache')) / 'ricy-noctalia-src-5.2.1')
args = parser.parse_args()
with tempfile.TemporaryDirectory(prefix='ricy-taskbar-order-') as directory:
    binary = Path(directory) / 'validate-order'
    subprocess.run(['c++', '-std=c++23', '-O1', '-Wall', '-Wextra', '-I' + str(args.fonte / 'src'), str(Path(__file__).with_suffix('.cpp')), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)
