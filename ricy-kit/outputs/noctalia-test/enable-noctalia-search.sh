#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 printf 'Start the Noctalia test first.\n' >&2
 exit 1
fi
systemctl --user stop plasma-krunner.service
if ! systemctl --user is-active --quiet noctalia-busca-desktop.service; then
 if ! systemd-run --user --unit=noctalia-busca-desktop --collect --property=Type=dbus --property=BusName=org.kde.krunner --property=BindsTo=noctalia-teste.service --property=After=noctalia-teste.service /usr/bin/python "$base_dir/desktop-search.py"; then
  systemctl --user start plasma-krunner.service
  exit 1
 fi
fi
