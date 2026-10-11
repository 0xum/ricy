#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
workspace_dir="$(dirname "$(dirname "$base_dir")")"
export NOCTALIA_CONFIG_HOME="$workspace_dir/work/noctalia-profile/config"
export NOCTALIA_STATE_HOME="$workspace_dir/work/noctalia-profile/state"
noctalia config validate
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 systemctl --user reset-failed noctalia-teste.service 2>/dev/null || true
 systemd-run --user --unit=noctalia-test --collect --setenv="NOCTALIA_CONFIG_HOME=$NOCTALIA_CONFIG_HOME" --setenv="NOCTALIA_STATE_HOME=$NOCTALIA_STATE_HOME" /usr/bin/noctalia
fi
ready=false
for i in {1..30}; do
 if noctalia msg status >/dev/null 2>&1; then ready=true; break; fi
 sleep 0.3
done
if [ "$ready" != true ]; then
 systemctl --user stop noctalia-teste.service || true
 printf 'Noctalia did not start; Plasma panels were preserved.\n' >&2
 exit 1
fi
noctalia msg bar-hide search_edge >/dev/null
mkdir -p "$HOME/.local/share/applications" "$HOME/.config/autostart"
cp "$base_dir/codex-noctalia-menu.desktop" "$base_dir/codex-noctalia-return.desktop" "$base_dir/codex-noctalia-clipboard.desktop" "$HOME/.local/share/applications/"
cp "$base_dir/codex-noctalia-recover.desktop" "$HOME/.config/autostart/"
kbuildsycoca6 --noincremental >/dev/null 2>&1
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.doRegister '["codex-noctalia-menu.desktop", "_launch", "Noctalia Menu (test)", "Noctalia Menu (test)"]' >/dev/null
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.setShortcut '["codex-noctalia-menu.desktop", "_launch", "Noctalia Menu (test)", "Noctalia Menu (test)"]' '[268435488]' 2 >/dev/null
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "$(cat "$base_dir/restaurar-wallpaper.js")"
touch "$base_dir/teste-ativo"
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'panels().forEach(p => p.remove()); print("Plasma panels hidden for the test.")'
"$base_dir/enable-noctalia-search.sh"
python "$base_dir/configure-super.py"
python "$base_dir/configure-clipboard.py"
printf 'Test started. To return, run return-to-plasma.sh in this folder.\n'
