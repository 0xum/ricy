#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
workspace_dir="$(dirname "$(dirname "$base_dir")")"
export NOCTALIA_CONFIG_HOME="$workspace_dir/work/noctalia-profile/config"
export NOCTALIA_STATE_HOME="$workspace_dir/work/noctalia-profile/state"
noctalia config validate
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 systemctl --user reset-failed noctalia-teste.service 2>/dev/null || true
 if [[ -f "$HOME/.config/systemd/user/noctalia-teste.service" ]]; then
  systemctl --user stop plasma-krunner.service
  systemctl --user start noctalia-teste.service
 else
 systemd-run --user --unit=noctalia-test --collect --setenv="NOCTALIA_CONFIG_HOME=$NOCTALIA_CONFIG_HOME" --setenv="NOCTALIA_STATE_HOME=$NOCTALIA_STATE_HOME" /usr/bin/noctalia
 fi
fi
ready=false
for i in {1..30}; do
 if noctalia msg status >/dev/null 2>&1; then ready=true; break; fi
 sleep 0.3
done
if [ "$ready" != true ]; then
 systemctl --user stop noctalia-teste.service || true
 printf 'Noctalia não iniciou; os painéis do Plasma foram preservados.\n' >&2
 exit 1
fi
noctalia msg bar-hide search_edge >/dev/null
mkdir -p "$HOME/.local/share/applications" "$HOME/.config/autostart"
cp "$base_dir/codex-noctalia-menu.desktop" "$base_dir/codex-noctalia-voltar.desktop" "$base_dir/codex-noctalia-clipboard.desktop" "$HOME/.local/share/applications/"
cp "$base_dir/codex-noctalia-recuperar.desktop" "$HOME/.config/autostart/"
kbuildsycoca6 --noincremental >/dev/null 2>&1
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.doRegister '["codex-noctalia-menu.desktop", "_launch", "Menu Noctalia", "Menu Noctalia"]' >/dev/null
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.setShortcut '["codex-noctalia-menu.desktop", "_launch", "Menu Noctalia", "Menu Noctalia"]' '[268435488]' 2 >/dev/null
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "$(cat "$base_dir/restaurar-wallpaper.js")"
touch "$base_dir/teste-ativo"
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'panels().forEach(p => p.remove()); print("Painéis do Plasma substituídos pelo Noctalia.")'
"$base_dir/ativar-busca-noctalia.sh"
python "$base_dir/configurar-super.py"
python "$base_dir/configurar-clipboard.py"
printf 'Noctalia iniciado. Para voltar, execute voltar-ao-plasma.sh nesta pasta.\n'
