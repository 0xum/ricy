#!/usr/bin/env python3
"""Aplica os dois archives corrigidos ao kit, antes de preparar o destino."""
from pathlib import Path
import hashlib
import json
import shutil

base = Path(__file__).resolve().parent
kit = base.parents[1]
entries = json.loads((base / 'manifest.json').read_text())

# Verifique tudo antes da primeira alteração. Não substitua ajustes desconhecidos.
for entry in entries:
    original = kit / entry['target']
    replacement = base / entry['replacement']
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    if digest(replacement) != entry['replacement_sha256']:
        raise SystemExit('Correção com hash inesperado: ' + str(replacement))
    if digest(original) not in {entry['original_sha256'], entry['replacement_sha256']}:
        raise SystemExit('Arquivo já modificado; revise o patch: ' + str(original))

for entry in entries:
    shutil.copy2(base / entry['replacement'], kit / entry['target'])
    print('Correção aplicada:', entry['target'])

print('Prepare o destino com a contribuição noctalia-kde-integracao-e-menus.')
