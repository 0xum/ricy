#!/usr/bin/env python3
"""Link the Night Light regression against the selected compiled Noctalia objects."""
import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=Path, required=True)
source = parser.parse_args().source
build = source / 'build-ricy'
entry = next(x for x in json.loads((build / 'compile_commands.json').read_text())
             if x['file'].endswith('/gamma_service.cpp'))
args = shlex.split(entry['command'])
args = args[:args.index('-MD')]
lines = (build / 'build.ninja').read_text().splitlines()
index = next(i for i, line in enumerate(lines) if line.startswith('build noctalia: '))
objects = shlex.split(lines[index].split('cpp_LINKER_RSP ', 1)[1].split(' | ', 1)[0])
objects = [x for x in objects if x != 'noctalia.p/src_main.cpp.o']
link = shlex.split(lines[index + 1].split(' = ', 1)[1])
with tempfile.TemporaryDirectory(prefix='ricy-nightlight-test-') as temporary:
    temp = Path(temporary)
    obj, binary = temp / 'test.o', temp / 'test'
    subprocess.run(args + ['-std=c++23', '-c', str(Path(__file__).with_suffix('.cpp').resolve()),
                           '-o', str(obj)], cwd=build, check=True)
    subprocess.run(['c++', '-o', str(binary), str(obj), *objects, *link], cwd=build, check=True)
    env = os.environ.copy()
    for key in ['XDG_CONFIG_HOME', 'XDG_CACHE_HOME', 'XDG_STATE_HOME', 'XDG_RUNTIME_DIR']:
        env[key] = str(temp)
    env['WAYLAND_DISPLAY'] = 'ricy-test-unconnected'
    subprocess.run(['dbus-run-session', '--', str(binary)], env=env, check=True)
