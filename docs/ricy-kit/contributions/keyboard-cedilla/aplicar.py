#!/usr/bin/env python3
"""Corrige cedilha no teclado US internacional sem mudar o idioma da sessão."""
from datetime import datetime
import os
from pathlib import Path
import shutil

BEGIN = "# BEGIN Ricy: cedilha US internacional"
END = "# END Ricy: cedilha US internacional"
BLOCK = '''# BEGIN Ricy: cedilha US internacional
<dead_acute> <c> : "ç" ccedilla
<dead_acute> <C> : "Ç" Ccedilla
# END Ricy: cedilha US internacional
'''


def main():
    if os.geteuid() == 0:
        raise SystemExit("Execute como o usuário da sessão, sem sudo.")
    home = Path.home()
    target = home / ".XCompose"
    old = target.read_text(encoding="utf-8") if target.exists() else 'include "%L"\n'
    if old.count(BEGIN) != old.count(END) or old.count(BEGIN) > 1:
        raise SystemExit("Marcadores Ricy inconsistentes em .XCompose; revise o arquivo.")
    if BEGIN in old:
        start, end = old.index(BEGIN), old.index(END) + len(END)
        if end < start:
            raise SystemExit("Marcadores Ricy fora de ordem; revise o arquivo.")
        old = old[:start] + old[end:].lstrip("\n")
    content = old.rstrip("\n") + "\n\n" + BLOCK
    if target.exists() and target.read_text(encoding="utf-8") == content:
        print("Cedilha já configurada; nenhuma alteração.")
        return
    state = Path(os.environ.get("XDG_STATE_HOME", home / ".local/state"))
    backup = state / "ricy-teclado-backups" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True, mode=0o700)
    if target.exists():
        shutil.copy2(target, backup / "XCompose")
    else:
        (backup / "XCompose.ausente").touch(mode=0o600)
    target.write_text(content, encoding="utf-8")
    print(f"Configurado: {target}\nBackup: {backup}")
    print("Reabra completamente os aplicativos para recarregar a composição.")


if __name__ == "__main__":
    main()
