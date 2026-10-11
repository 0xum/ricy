#!/usr/bin/env bash
set -euo pipefail
root_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
base_dir="$(dirname "$root_dir")/noctalia-kde-integration-and-menus/outputs/noctalia-test"

recuperar() {
 local resultado=$?
 trap - ERR
 printf 'Failed to start Noctalia; restoring Plasma.\n' >&2
 RICY_RECUPERACAO_INTERNA=1 "$base_dir/return-to-plasma.sh" || true
 exit "$resultado"
}
trap recuperar ERR

# The unit has After=plasmashell, and the D-Bus calls check for real readiness.
ready=false
for i in {1..100}; do
 if qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'print("ready")' >/dev/null 2>&1 &&
    gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.getGlobalShortcutsByKey 16777250 >/dev/null 2>&1; then
  ready=true
  break
 fi
 sleep 0.3
done
if [[ "$ready" != true ]]; then
 printf 'Plasma/KGlobalAccel were not ready for integration.\n' >&2
 false
fi

"$base_dir/start-test.sh"
systemctl --user is-active --quiet noctalia-teste.service
systemctl --user is-active --quiet noctalia-busca-desktop.service
printf 'Noctalia integration initiated; autostart enabled.\n'
