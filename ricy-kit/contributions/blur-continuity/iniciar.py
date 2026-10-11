#!/usr/bin/env python3
"""Seleciona o blur Ricy compatível; conserva o efeito nativo como fallback."""
import subprocess

def effect(method, name):
    result = subprocess.run(['qdbus6', 'org.kde.KWin', '/Effects', 'org.kde.kwin.Effects.' + method, name], text=True, capture_output=True, timeout=10)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()

def main():
    version = subprocess.check_output(['kwin_wayland', '--version'], text=True).strip()
    if version.split()[-1] != '6.7.5':
        print('KWin atualizado: mantendo blur nativo até recompilar a variante Ricy.')
        return
    if effect('isEffectLoaded', 'ricyblur') == 'true':
        return
    if effect('isEffectSupported', 'ricyblur') != 'true':
        print('Variante indisponível: mantendo blur nativo.')
        return
    native = effect('isEffectLoaded', 'blur') == 'true'
    if native:
        effect('unloadEffect', 'blur')
    try:
        if effect('loadEffect', 'ricyblur') != 'true':
            raise RuntimeError('KWin recusou a variante Ricy.')
        print('Blur contínuo Ricy carregado.')
    except Exception:
        if native:
            effect('loadEffect', 'blur')
        raise

if __name__ == '__main__':
    main()
