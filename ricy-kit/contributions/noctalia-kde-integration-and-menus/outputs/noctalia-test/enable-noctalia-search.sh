#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 printf 'Start Noctalia integration first.\n' >&2
 exit 1
fi
systemctl --user stop plasma-krunner.service
if ! systemctl --user is-active --quiet noctalia-busca-desktop.service; then
 if [[ -f "$HOME/.config/systemd/user/noctalia-busca-desktop.service" ]]; then
  launch=(systemctl --user start noctalia-busca-desktop.service)
 else
  launch=(systemd-run --user --unit=noctalia-busca-desktop --collect --property=Type=dbus --property=BusName=org.kde.krunner --property=BindsTo=noctalia-teste.service --property=After=noctalia-teste.service /usr/bin/python "$base_dir/desktop-search.py")
 fi
 if ! "${launch[@]}"; then
  systemctl --user start plasma-krunner.service
  exit 1
 fi
fi

# Type=exec evita disputar com a unidade nativa do KRunner por BusName.
# Aguarde o adaptador realmente assumir o nome antes de declarar sucesso.
ready=false
for i in {1..30}; do
 adapter_pid=$(systemctl --user show noctalia-busca-desktop.service --property=MainPID --value)
 owner_pid=$(qdbus6 org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.GetConnectionUnixProcessID org.kde.krunner 2>/dev/null || true)
 if [[ "$adapter_pid" != 0 && "$owner_pid" == "$adapter_pid" ]]; then
  ready=true
  break
 fi
 sleep 0.1
done
if [[ "$ready" != true ]]; then
 systemctl --user stop noctalia-busca-desktop.service || true
 systemctl --user start plasma-krunner.service
 printf 'The adapter did not assume desktop search.\n' >&2
 exit 1
fi
