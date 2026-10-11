#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# An explicit return to Plasma is also valid in the next logins.
# Internal recovery avoids stopping your own drive during the rollback.
if [[ "${RICY_RECUPERACAO_INTERNA:-0}" != 1 ]]; then
 systemctl --user disable --now ricy-noctalia-integracao.service 2>/dev/null || true
fi
python "$base_dir/configure-super.py" restore
python "$base_dir/configure-clipboard.py" restore
systemctl --user stop noctalia-busca-desktop.service 2>/dev/null || true
systemctl --user start plasma-krunner.service
systemctl --user stop noctalia-teste.service 2>/dev/null || true
systemctl --user stop plasma-plasmashell.service
python - "$base_dir" <<'PY'
import sys,tarfile,os
from pathlib import Path
base=Path(sys.argv[1]); home=Path.home()
with tarfile.open(base/'plasma-antes.tar.gz') as t:
 for rel in ['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc']:
  data=t.extractfile(rel).read(); dest=home/rel
  tmp=dest.with_name(dest.name+'.noctalia-restore'); tmp.write_bytes(data); os.replace(tmp,dest)
PY
systemctl --user start plasma-plasmashell.service
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.unregister codex-noctalia-menu.desktop _launch >/dev/null 2>&1 || true
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.unregister codex-noctalia-clipboard.desktop _launch >/dev/null 2>&1 || true
rm -f "$HOME/.local/share/applications/codex-noctalia-clipboard.desktop" "$HOME/.local/share/applications/codex-noctalia-menu.desktop" "$HOME/.local/share/applications/codex-noctalia-return.desktop" "$HOME/.config/autostart/codex-noctalia-recover.desktop"
kbuildsycoca6 --noincremental >/dev/null 2>&1
rm -f "$base_dir/teste-ativo"
printf 'restored original Plasma Panels.\n'
