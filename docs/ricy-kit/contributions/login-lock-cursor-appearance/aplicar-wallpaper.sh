#!/usr/bin/env bash
set -euo pipefail
test -f /usr/local/share/ricy/limine-splash.png
# A API enumera os desktops do destino; não transporta IDs de monitores.
exec qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript '
var ds = desktops();
for (var i = 0; i < ds.length; ++i) {
    ds[i].wallpaperPlugin = "org.kde.image";
    ds[i].currentConfigGroup = ["Wallpaper", "org.kde.image", "General"];
    ds[i].writeConfig("Image", "file:///usr/local/share/ricy/limine-splash.png");
    ds[i].writeConfig("FillMode", 2);
}'
