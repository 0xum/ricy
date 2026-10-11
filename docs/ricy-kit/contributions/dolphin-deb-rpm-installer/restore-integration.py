#!/usr/bin/env python3
"""Restore a destination backup; does not remove system packages or applications."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys


def main():
    if os.geteuid() == 0 or len(sys.argv) != 2:
        raise SystemExit('Usage, without sudo: python restore-integration.py /path/to/local-backup')
    backup = Path(sys.argv[1]).resolve(strict=True)
    home = Path.home()
    root = (home / '.local/state/cachyos-package-installer-backups').resolve()
    if backup.parent != root:
        raise SystemExit('Use only one backup generated in this user by the kit installer.')
    manifest = json.loads((backup / 'manifest.json').read_text())
    import runpy
    allowed = set(runpy.run_path(str(Path(__file__).with_name('install-integration.py')))['TARGETS'])
    if set(manifest) != allowed:
        raise SystemExit('Manifesto does not match the targets of this contribution.')
    if input('Restore previous files, replacing later changes to those files? [y/N] ').lower() != 'y':
        return
    for relative, existed in manifest.items():
        target = home / relative
        if target.is_dir() and not target.is_symlink():
            shutil.rmtree(target)
        elif target.exists() or target.is_symlink():
            target.unlink()
        if existed:
            source = backup / 'files' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir() and not source.is_symlink():
                shutil.copytree(source, target, symlinks=True)
            else:
                shutil.copy2(source, target, follow_symlinks=False)
    subprocess.run(['update-desktop-database', str(home / '.local/share/applications')], check=True)
    subprocess.run(['kbuildsycoca6', '--noincremental'], check=True)
    print('Restored files. Packages, installed applications and caches have not been removed.')


if __name__ == '__main__':
    main()
