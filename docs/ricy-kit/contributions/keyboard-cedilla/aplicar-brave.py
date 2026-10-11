#!/usr/bin/env python3
"""Seleciona XWayland no Brave para respeitar a composição de cedilha."""
from datetime import datetime
import os
from pathlib import Path
import shutil


def main():
    if os.geteuid() == 0:
        raise SystemExit("Execute como o usuário da sessão, sem sudo.")
    home = Path.home()
    config = Path(os.environ.get("XDG_CONFIG_HOME", home / ".config"))
    target = config / "brave-flags.conf"
    old = target.read_text(encoding="utf-8") if target.exists() else ""
    lines = old.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.strip().startswith("--ozone-platform=")]
    if indexes:
        lines[indexes[0]] = "--ozone-platform=x11"
        lines = [line for i, line in enumerate(lines) if i not in indexes[1:]]
    else:
        lines.append("--ozone-platform=x11")
    content = "\n".join(lines) + "\n"
    if content == old:
        print("Brave já configurado; nenhuma alteração.")
        return
    state = Path(os.environ.get("XDG_STATE_HOME", home / ".local/state"))
    backup = state / "ricy-teclado-backups" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True, mode=0o700)
    if target.exists():
        shutil.copy2(target, backup / "brave-flags.conf")
    else:
        (backup / "brave-flags.conf.ausente").touch(mode=0o600)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"Configurado: {target}\nBackup: {backup}")
    print("Reabra completamente o Brave. O KDE continua em Wayland.")


if __name__ == "__main__":
    main()
