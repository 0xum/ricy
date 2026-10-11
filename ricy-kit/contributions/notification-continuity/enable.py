#!/usr/bin/env python3
"""Ativa/restaura local variant without closing shell child applications."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess

home = Path.home()
config = Path(os.environ.get('XDG_CONFIG_HOME', home / '.config'))
state = Path(os.environ.get('XDG_STATE_HOME', home / '.local/state'))
cache = Path(os.environ.get('XDG_CACHE_HOME', home / '.cache'))
binary = home / '.local/lib/ricy-noctalia/noctalia'
override = config / 'systemd/user/noctalia-teste.service.d/50-notificacoes-ricy.conf'
paths = {'binary': binary, 'override': override}


def systemctl(*args):
    subprocess.run(['systemctl', '--user', *args], check=True)


def replace_file(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + '.ricy-novo')
    shutil.copy2(source, temporary)
    temporary.replace(destination)


def restart_preserving_apps():
    # Temporary Override: the control-group pattern would also close applications
    # released by the Noctalia menu as a browser and editor.
    runtime = Path(os.environ['XDG_RUNTIME_DIR']) / 'systemd/user/noctalia-teste.service.d/99-ricy-preservar-aplicativos.conf'
    if runtime.exists():
        raise SystemExit(f'Temporary Override already exists; review: {runtime}')
    runtime.parent.mkdir(parents=True, exist_ok=True)
    runtime.write_text('[Service]\nKillMode=process\n')
    try:
        systemctl('daemon-reload')
        systemctl('restart', 'noctalia-teste.service')
        systemctl('start', 'noctalia-busca-desktop.service')
    finally:
        runtime.unlink(missing_ok=True)
        systemctl('daemon-reload')


def main():
    if os.geteuid() == 0:
        raise SystemExit('Run as session user without sudo.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--bin', type=Path, default=cache / 'ricy-noctalia-src-5.2.1/build-ricy/noctalia')
    parser.add_argument('--restaurar', type=Path)
    args = parser.parse_args()
    if args.restaurar:
        manifest = json.loads((args.restaurar / 'manifest.json').read_text())
        for key, path in paths.items():
            if manifest[key]:
                replace_file(args.restaurar / key, path)
            else:
                path.unlink(missing_ok=True)
    else:
        if not args.bin.is_file():
            raise SystemExit('Compile the binary first.')
        subprocess.run([str(args.bin), '--version'], check=True)
        if not (config / 'systemd/user/noctalia-teste.service').exists():
            raise SystemExit('First install permanent integration Noctalia.')
        backup = state / 'ricy-notificacoes-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
        backup.mkdir(parents=True, mode=0o700)
        manifest = {}
        for key, path in paths.items():
            manifest[key] = path.exists()
            if path.exists():
                shutil.copy2(path, backup / key)
        (backup / 'manifest.json').write_text(json.dumps(manifest) + '\n')
        replace_file(args.bin, binary)
        binary.chmod(0o755)
        override.parent.mkdir(parents=True, exist_ok=True)
        escaped = str(binary).replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%')
        override.write_text(f'[Service]\nExecStart=\nExecStart="{escaped}"\n')
        print(f'Backup: {backup}', flush=True)
    restart_preserving_apps()
    print('Shell e adaptador reiniciados; aplicativos preservados.')


if __name__ == '__main__':
    main()
