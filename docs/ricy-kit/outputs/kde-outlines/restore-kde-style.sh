#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$base_dir/menuFont-antes.txt" ]]; then
  kwriteconfig6 --file kdeglobals --group General --key menuFont "$(cat -- "$base_dir/menuFont-antes.txt")"
fi
# The original user config had no widgetStyle key; restore the inherited Breeze style.
if [[ -s "$base_dir/widgetStyle-antes.txt" ]]; then
  kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle "$(cat -- "$base_dir/widgetStyle-antes.txt")"
else
  kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle --delete
fi
if [[ -f "$base_dir/kvantum-config-antes" ]]; then
  cp -- "$base_dir/kvantum-config-antes" "$HOME/.config/Kvantum/kvantum.kvconfig"
elif [[ -f "$base_dir/kvantum-ausente-antes" ]]; then
  rm -f -- "$HOME/.config/Kvantum/kvantum.kvconfig"
fi
python - <<'PY'
from gi.repository import Gio, GLib
Gio.bus_get_sync(Gio.BusType.SESSION,None).emit_signal(None,'/KGlobalSettings','org.kde.KGlobalSettings','notifyChange',GLib.Variant('(ii)',(2,0)))
Gio.bus_get_sync(Gio.BusType.SESSION,None).emit_signal(None,'/KDEPlatformTheme','org.kde.KDEPlatformTheme','refreshFonts',None)
PY
systemctl --user restart plasma-plasmashell.service
printf '%s\n' 'Previous style restored. Reopen old applications to update controls.'
