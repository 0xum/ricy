#!/usr/bin/env bash
set -euo pipefail
kit_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
[[ -f "$kit_dir/outputs/kde-outlines/estado-antes.json" ]] || { printf 'Execute preparar-destino.py primeiro.\n' >&2; exit 1; }
mkdir -p "$HOME/.config/Kvantum"
cp -a -- "$kit_dir/outputs/kde-outlines/KDE-Noctalia" "$HOME/.config/Kvantum/"
kvantummanager --set KDE-Noctalia
kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle kvantum
# Preserva a família de fonte do destino; ajusta apenas o tamanho dos menus.
python - <<'PY'
import subprocess
font=subprocess.check_output(['kreadconfig6','--file','kdeglobals','--group','General','--key','menuFont'],text=True).strip()
if not font:font=subprocess.check_output(['kreadconfig6','--file','kdeglobals','--group','General','--key','font'],text=True).strip()
if font:
 fields=font.split(',')
 if len(fields)>2:
  fields[1]='10';fields[2]='-1'
  subprocess.run(['kwriteconfig6','--file','kdeglobals','--group','General','--key','menuFont',','.join(fields)],check=True)
else:print('Escolha a fonte dos menus em Fontes do KDE; não foi presumida uma família.')
PY
python "$kit_dir/recarregar-estilo.py"
printf 'Estilo aplicado. Feche e abra os menus; se necessário, reabra os aplicativos.\n'
