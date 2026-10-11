#!/usr/bin/env python3
"""Selects the compatible Ricy blur; retains the native effect as fallback."""
import subprocess

def effect(method, name):
    result = subprocess.run(['qdbus6', 'org.kde.KWin', '/Effects', 'org.kde.kwin.Effects.' + method, name], text=True, capture_output=True, timeout=10)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()

def main():
    version = subprocess.check_output(['kwin_wayland', '--version'], text=True).strip()
    if version.split()[-1] != '6.7.5':
        print('KWin updated: Maintaining native blur until the Ricy variant is recompiled.')
        return
    if effect('isEffectLoaded', 'ricyblur') == 'true':
        return
    if effect('isEffectSupported', 'ricyblur') != 'true':
        print('Unavailable variant: keeping native blur.')
        return
    native = effect('isEffectLoaded', 'blur') == 'true'
    if native:
        effect('unloadEffect', 'blur')
    try:
        if effect('loadEffect', 'ricyblur') != 'true':
            raise RuntimeError('KWin recusou a variante Ricy.')
        print('Ricy Continuous Blur Charged.')
    except Exception:
        if native:
            effect('loadEffect', 'blur')
        raise

if __name__ == '__main__':
    main()
