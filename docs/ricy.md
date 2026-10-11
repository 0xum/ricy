# Ricy — KDE Plasma playback with Noctalia in CachyOS

> **organization 11/10/2026:** project in `$HOME/Projects/ricy`; active kit in `$HOME/Projects/ricy/ricy-kit`; scripts `start.sh`, `return.sh` and `switch.sh` at the project root. Documentation and transportable kit in `docs/`; original file in `archives/ricy.zip`. The old paths in the record below are historical. The current lock is `$HOME/.local/state/ricy/documentacao.lock`.


> **Status in force in this destination (10/10/2026):** Permanent noctalia on login, active kit in `$HOME/ricy-kit`, full appearance and selected SDDM for the next restart. Use `REINSTALL.md` and the final contribution of this record. Previous excerpts on test mode are historical.

> **Reference of the next visual adjustments:** consult [IDENTITY-VISUAL.md](VISUAL-IDENTITY.md). The guide and tokens capture the language of Noctalia to harmonize other components, with distinction between already applied appearance and future work.

Log 8 of October 2026. Document of the final status of this session, with explanation of the decisions and migration script. The archive kit is in `~/ricy-kit`, next to this document. **Transfer the document and kit together.**

## Instructions for the other chats of this session

This file is the shared record of changes made in this CachyOS. Each chat must document the changes it has effectively made, so that another agent or user can play them in another installation. `/home/delta/ricy-kit`.

To enlarge the appearance of the system, read first `VISUAL-IDENTITY.md` and `ricy-kit/contributions/noctalia-visual-identity/tokens.json`. Use the visual language registered there as a reference for the next components; preserve approved behaviors and record the really applied adaptations.

### How to contribute

1. Read the document before writing and check out your own current files, commands, and settings. Do not present intent, abandoned attempt or hypothesis as applied change.
2. Preserve existing content. Add your contribution to the end, under `## Contribuição — <tema> — <data e hora>`. Identify chat by title, if known; otherwise use a job description without inventing an identifier.
3. Explain the goal, the previous state and the final result. Separate completed changes, discarded attempts and pending work. Also register changes from other themes besides Noctalia.
4. Include paths, packages and observed versions, final settings, running order commands, dependencies, services, autostart and effects on the rest of the system. Explain how to test and undo each change.
5. Distinguish the paths of this portable path machine. `$HOME` in commands intended for another installation. Desktop IDs, monitor, user, shortcuts and backups need to be captured in the destination, not reused blindly.
6. If you depend on binary scripts, themes or archives, copy only the necessary materials for `/home/delta/ricy-kit/contributions/<tema>/` and describe how to install them. Preserve the license of third party files. Do not move active archives or change services to prepare documentation.
7. Do not overwrite files from another chat in the kit. Do not include passwords, tokens, keys, clipboard history, private conversations or complete personal backups. Inform the location of existing backups and provide a procedure to generate new ones in the destination.
8. If your change replaces a documented configuration, explicitly record what has been replaced and what is the final state. Fix only the required snippet with evidence; do not rewrite the report of another chat by assumption.
9. Register the tests actually executed and their limitations. If there is not enough evidence in the context available, enter the gap; do not invent commands or results. The documented migration does not mean that it has already been tested on another computer.
10. When finished, please inform the topic added and the files included in the kit. Do not run the system changes again: this contribution is documentation.

### Avoid Chat Conflict

Prepare your section in a temporary file and add it without rerecording the entire document. Use the same lock for any writing in the record:

```bash
# Replace by the actual path of the file with your ready contribution:
contribuicao="/tmp/ricy-contribuicao-TEMA.md"
flock "$HOME/.ricy-documentacao.lock" bash -c 'cat -- "$1" >> "$2"' _ "$contribuicao" "$HOME/ricy.md"
```

The lock coordinates only the chats that follow this instruction. For a punctual fix, reread the file inside the lock before saving. Use distinct subfolders in the kit. If you include new files, update `SHA256SUMS` under the same lock, keeping the existing inputs; check the hashes before considering the materials ready. The migration preparer changes the paths of the `.desktop`, therefore its hashes must be checked before performing the preparation.

### Suggested structure of the contribution

```markdown
## Contribution — THEME — DATE AND TIME

Chat/work: ...
Objective and final result: ...

### Applied changes
- File/service/package: previous status, change and motive.

### Play in another CachyOS
Prerequisites, observed versions, local backups and commands in order.
Final settings and materials in ricy-kit/contributions/TEMA/.

### Verification
Tests performed, results and limitations.

### Restore
Commands and necessary archives; what restoration covers.

### Attempts discarded and pending
Only when relevant to avoid repeating a mistake or assuming something incomplete.
```

---

## 1. Result and scope

We have maintained the KDE Plasma/Wayland session and KWin. Noctalia replaces the panels, menu and search while Plasma remains responsible for the desktop and wallpaper. The goal was visual continuity, sobriety, readable icons and accessible controls without recompiling or changing the Noctalia source code.

| Element | Final State |
|---|---|
| Taskbar | Lower, 44 px, reserved area; maximized windows respect their height |
| Visibility | Always visible; auto-hide and smart-auto-hide off |
| Applications | Left icons, active indicator, current workspace only, no titles |
| Tray | To the right; drawer with 3 columns and icons of 24 px |
| Network and volume | Icons only; no SSID and no percentage |
| Search | Super, Super+space and desktop typing; central top, embedded on the edge |
| Search support | Empty top bar 10 px, without space reserve; only appears with shortcut search/adapter |
| Pointer on top | Does not reveal the support bar |
| Clipboard | Super+V Opens/Historical Close of Noctalia in the Center |
| colors | KDE/Catppuccin Mocha palette with Mauve accent |
| Blur | KWin at the dark background of the compatible bar and panels, opacity 0,70  |
| Qt/KDE Menus | Variant Kvantum KDE-Noctalia, compact, rounded, opaque |
| Wallpaper | Preserved by Plasma; Noctalia wallpaper disabled |

The initial request for an adaptive bar has been tested, but the approved state keeps the lower bar fixed with a reserved area. Do not describe this state as smart concealment. The launcher button of the bar can still use its own bottom anchor; the opening at the top is guaranteed by the shortcuts and the typing adapter.

## 2. Reference environment

Versions observed on this computer: `noctalia 5.2.1-1.1`, `plasma-desktop 6.7.5-1.1`, `kwin 6.7.5-3.1`, `kvantum 1.1.8-1.1`, `python-gobject 3.58.0-1`, `qt6-tools 6.12.0-1.1`. They are reference versions, not a promise of compatibility with future versions. The Noctalia used here is the binary of the CachyOS package; old QML-based versions settings should not be mixed with this TOML.

The package `qt6-tools` provides `qdbus6`; `glib2` provides `gdbus`; Python with PyGObject provides `Gio` and `GLib`. `wl-clipboard` is optional for the adapter method that reads the text already copied; the normal history is from Noctalia itself. Noto Sans is the source of Noctalia; JetBrainsMono Nerd Font de 10 pt was the source of KDE, Papirus-Dark the icon theme and Breeze the decoration of windows. These last three were the existing visual base, no changes required for integration.

## 3. Installation and preparation in the new CachyOS

Use a KDE Plasma session **Wayland**. Copy `ricy-kit` for the home of the destination user. Do not copy the restore backup of the old machine, monitor IDs, desktop IDs or JSONs from old shortcuts to the destination. The delivered kit does not include these personal files.

Install the available components in your CachyOS repositories:

```bash
sudo pacman -Syu
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts papirus-icon-theme
# Optional for displayWithClipboardContents:
sudo pacman -S --needed wl-clipboard
```

If the repository does not offer `noctalia`, resolve the availability of the package corresponding to the documented version before continuing. Do not automatically replace with another shell implementation.

Prepare the kit **before changing the style or starting the test**:

```bash
cd "$HOME/ricy-kit"
python prepare-environment.py
```

The preparer creates a backup of DESTINO, registers hashes, generates wallpaper restoration with local IDs, copies the isolated profile, saves the previous style and recalculates `Exec=` from shortcuts to the current user. It refuses to overwrite an existing backup. After starting the test, use `start-test.sh` to repeat it.

If the destination wallpaper is already desired, it will be preserved. To play the image of this computer, choose previously on Plasma `/usr/share/wallpapers/cachyos-wallpapers/limine-splash.png`, if this image exists in the installation. The initial desktop also had an old reference to `north.png`; it should not be applied indiscriminately to all monitors.

## 4. Colors, KDE style and menus

The Noctalia palette was extracted from the active KDE colors. Main values:

| Role | Color |
|---|---|
| Dark background |  `#181825`  |
| Text |  `#cdd6f4`  |
| Cards/menus |  `#313244`  |
| Secondary text |  `#a6adc8`  |
| I'll do it. |  `#cba6f7`  |
| Selection/hover |  `#977dba`, black text |
| Outline |  `#46485c`  |
| Success |  `#a6e3a1`  |
| Error |  `#f38ba8`  |

Kit contains `KDE-Noctalia.colors`, exported only from the effective active color groups, and the Kvantum variant completes. So it is not necessary to import the whole `kdeglobals` old with personal preferences.

```bash
mkdir -p "$HOME/.local/share/color-schemes" "$HOME/.config/Kvantum"
cp "$HOME/ricy-kit/outputs/kde-outlines/KDE-Noctalia.colors" "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
cp -a "$HOME/ricy-kit/outputs/kde-outlines/KDE-Noctalia" "$HOME/.config/Kvantum/"
printf '[General]\ntheme=KDE-Noctalia\n' > "$HOME/.config/Kvantum/kvantum.kvconfig"
kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle kvantum
```

Reopen Qt applications to update style; a new session also applies the change. The variant starts from [Catppuccin Kvantum](https://github.com/catppuccin/kvantum), with MIT license included. We modified SVG from `menu-normal` for corners of 12 px, background `#313244` and border `#46485c`; `menuitem-normal` It won corners of 6 px and fill `#977dba`No. No. `.kvconfig`, vertical margins of text are zero, vertical frame of items 4 px, lateral 6 px, side margin of the text 2 px, minimum height 24 and separator 5 px. `popup_blurring=false`, `reduce_menu_opacity=0` and `shadowless_popup=true` avoid the blur rectangle out of the corners.

The source of the menus was maintained/restored for 10 If you want the same font, install JetBrainsMono Nerd Font and select it in KDE; do not force a missing font. Qt menus rendered by the application and Noctalia's own menus are distinct components. Kvantum adjusts the first ones; does not itself reduce menus designed internally by Noctalia.

The script `generate-kvantum-variant.py` records how the variant was built. To regenerate it, place the Catppuccin checkout in `work/catppuccin-kvantum`, run the script in the kit root and check out the result. It also installs the local variant; it is not necessary to run it to use the ready files.

## 5. Isolated profile of Noctalia

Kit structure:

```text
~/ricy-kit/
  prepare-environment.py
  generate-kvantum-variant.py
  outputs/nottalia-test/ scripts, TOML, palette, shortcuts and destination backup
  outputs/kde-outlines/ SVG, Kvantum, KDE palette and style restoration
  work/noctalia-profile/
    config/noctalia/config.toml
    config/noctalia/palettes/KDE-Current.json
    state/ isolated state generated at destination
```

`NOCTALIA_CONFIG_HOME` points to `work/noctalia-profile/config`; `NOCTALIA_STATE_HOME` points to `work/noctalia-profile/state`. Using the default item “Noctalia” of the package can open another profile. Use the kit script.

The JSON palette must also contain the object `terminal`, required by the validator of the version used, even with terminal templates disabled.

### Complete Final TOML Configuration

```toml
[shell]
font_family = "Noto Sans"
setup_wizard_enabled = false
clipboard_enabled = true
screen_time_enabled = false
polkit_agent = false
corner_radius_scale = 1.3

[shell.launcher]
compact = true
sort_by_usage = true
fetch_exchange_rates = false

[bar.default]
position = "bottom"
layer = "top"
thickness = 44
scale = 1.5
font_scale = 0.85
auto_hide = false
smart_auto_hide = false
reserve_space = true
show_on_workspace_switch = false
margin_ends = 0
margin_edge = 0
radius = 6
radius_top_left = 6
radius_top_right = 6
radius_bottom_left = 0
radius_bottom_right = 0
concave_edge_corners = false
background_opacity = 0.70
compositor_blur = true
start = ["launcher", "taskbar"]
center = []
end = ["tray", "volume", "network", "clock", "control-center"]

[widget.taskbar]
scale = 0.666667
icon_scale = 1.725
item_spacing = 6
only_active_workspace = true
show_all_outputs = false
show_active_indicator = true
show_window_title = false

[wallpaper]
enabled = false

[backdrop]
enabled = false

[desktop_widgets]
enabled = false

[dock]
enabled = false

[lockscreen]
enabled = false

[osd]
enabled = false

[weather]
enabled = false

[theme]
mode = "dark"
source = "custom"
custom_palette = "KDE-Current"
builtin = "Noctalia"

[theme.templates]
enable_builtin_templates = false
enable_community_templates = false
builtin_ids = []
community_ids = []

[widget.network]
show_label = false

[widget.volume]
show_label = false

[shell.panel]
clipboard_placement = "floating"
clipboard_position = "center"
launcher_placement = "attached"
launcher_position = "auto"
open_near_click_launcher = false
transparency_mode = "solid"
control_center_placement = "attached"
control_center_position = "auto"
open_near_click_control_center = true

[widget.tray]
drawer = true
drawer_columns = 3
drawer_item_size = 24
detached_panel = false

[bar]
order = ["search_edge", "default"]

[bar.search_edge]
position = "top"
enabled = true
thickness = 10
auto_hide = false
smart_auto_hide = false
reserve_space = false
show_on_workspace_switch = false
layer = "overlay"
background_opacity = 0.70
compositor_blur = true
margin_ends = 0
margin_edge = 0
padding = 0
radius = 0
radius_top_left = 0
radius_top_right = 0
radius_bottom_left = 0
radius_bottom_right = 0
concave_edge_corners = false
shadow = false
start = []
center = []
end = []
```

## 6. Explanation of adjustments and problems solved

**Bar on windows:** We're doing it. `reserve_space=true` And we kept it `layer="top"` in the main bar. The previous overlay layer placed it above overlays as screenshot; the reserved area makes KWin discount 44 px of maximized windows. The upper support range is overlay for the launcher, but does not reserve space.

**App icons and context menu:** global bar scale 1,5 improved readability, but also expanded the context menu. `widget.taskbar.scale=0.666667` compensates for the menu scale, and `icon_scale=1.725` keeps the icons around 28 px. `corner_radius_scale=1.3` left the rectangle of the rounded selection. The minimum width was approximately 240 px; the menu can grow according to the text.

**Tray and excessive texts:**  `network.show_label=false` hidden SSID; `volume.show_label=false` hides the percentage. Tray drawer uses three columns and icons 24 px, offering a more compact presentation for the items. We do not promise uniformity of application menus that use own rendering.

**Continuity of the plant:**  `control_center_placement="attached"`, position `auto` and `open_near_click_control_center=true` make the center follow the opening bar/anchore and draw the native union.

**Blur only in the dark background:**  `background_opacity=0.70`, `compositor_blur=true` and `shell.panel.transparency_mode="solid"`. KWin applies blur behind the surface; it is not text blur. Cards and buttons remain opaque. Taskbar context menus use fixed internal opacity and do not expose the same native blur in this version. We decided not to modify/recompile Noctalia to change that.

KWin settings used:

```bash
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
```

In this environment the Wayland protocol of background effects was available. If the blur does not appear in the destination, check first the effect of KWin and support between compositor and version of Noctalia; do not assume that only transparency equals blur.

**Desktop typing:** just swap the search shortcut doesn't intercept Plasma's action. `plasma-krunner.service` and an adapter assumes `org.kde.krunner` in the session D-Bus. `/App` (`org.kde.krunner.App`) and `/org/kde/krunner` (`org.freedesktop.Application`). The second interface, especially `ActivateAction("Query", ...)`, it was necessary for Plasma 6.7. Consultations are forwarded to `noctalia msg panel-open launcher <texto>`; are not recorded in log by the adapter. The adapter is connected to the life cycle of the test service.

**Super alone:** an attempt with `kwinrc/ModifierOnlyShortcuts` did not work on this Plasma. We use KGlobalAccel and transfer Meta from the action `plasmashell / activate application launcher` for `codex-noctalia-menu.desktop / _launch`. `setForeignShortcut` is required to change an action belonging to another component. The Qt codes used are Meta `16777250`, Meta+Space `268435488` and Meta+V `268435542`. In the new clipboard shortcut we record the action and use also `setShortcut` before `setForeignShortcut`. The original JSONs are created in the destination before transferring the shortcuts.

**Search at the top and visual union:** the floating/top_center mode left the aspect of a window loose. We switched to attached/auto and created the empty bar `search_edge` as the first bar in the order. It provides the top anchor without dislocating the windows. Initially it used auto-hide and reappeared by touching the top with the pointer. The final solution disables auto-hide, hides the bar by `bar-hide search_edge`, show it before opening the search and hide it again after closing. So the hidden surface does not receive pointer entry. The wrapper waits 250 ms by revelation before opening; the adapter checks the state for each 250 ms to collect the bar after Escape, external click or app opening.

**Clipboard:**  `clipboard_enabled=true` and the Super+V shortcut calls `panel-toggle clipboard`. The panel is floating/center. History starts to be retained from activation; we do not matter the old Klipper history. The original Plasma shortcut is saved for restoration.

## 7. Start, test and return

After preparation and visual adjustments:

```bash
cd "$HOME/ricy-kit"
./outputs/noctalia-test/start-test.sh
```

Script validates TOML, starts `noctalia-teste.service` via user systemd, waits IPC available, hides the top support, installs the menu items, restores wallpaper and only then removes the Plasma panels from the test layout. The plasmashell process remains active. Then initiates the adapter and configures the shortcuts. The backup allows you to recover the removed panels.

Check:

1. Maximized windows stop above the bottom bar.
2. Icons and tray are readable; Wi-Fi and volume do not display text.
3. Super and Super+Space open the search at the top with visual union.
4. By focusing on the desktop and typing, the query goes to Noctalia.
5. Close search collects the support track; passing the pointer at the top does not reveal it.
6. Super+V opens the history; copy a new text to check the record.
7. The center is still connected to the bottom bar and the wallpaper has been preserved.

Diagnosis:

```bash
systemctl --user status noctalia-teste.service noctalia-busca-desktop.service
noctalia msg status
journalctl --user -u noctalia-teste.service -u noctalia-busca-desktop.service -n 80 --no-pager
```

To reload after editing the effective profile:

```bash
noctalia msg config-reload
# A reload can recreate the top bar; keep it hidden when the search is closed:
noctalia msg bar-hide search_edge
```

`outputs/noctalia-test/config.toml` is the distributed copy; the service reads `work/noctalia-profile/config/noctalia/config.toml`. When making permanent adjustments, update both.

To return to Plasma panels and shortcuts:

```bash
"$HOME/ricy-kit/outputs/noctalia-test/return-to-plasma.sh"
```

Quick restoration only restores `plasma-org.kde.plasma.desktop-appletsrc` and `plasmashellrc` from the local backup, closes the adapter/Noctalia, reactivates KRunner and restores the shortcuts. It does not automatically undo palette, fonts, blur or Kvantum. To restore application style:

```bash
"$HOME/ricy-kit/outputs/kde-outlines/restore-kde-style.sh"
```

This second script restores widgetStyle, menu font and Kvantum selection stored in destination. To also undo palette and blur, recover selectively `kdeglobals` and `kwinrc` backup, considering any subsequent changes; do not import complete configuration of another machine.

The test uses transitory services, not a persistent installation in the login. There is a recovery autostart item: in the next login if the tag `teste-ativo` exist and the service is inactive, restores Plasma. To reproduce exactly the test, do not simultaneously enable the default Noctalia autostart. A definitive login setting remains out of what we did.

## 8. Integration archives — audit and re-creation content

The archives below accompany the kit. `.desktop` point to the actual destination directory; `prepare-environment.py` The backups, markers and shortcut history are not included in the kit because they should be generated locally.

### prepare-environment.py

```python
#!/usr/bin/env python3
"""Prepare the kit on the target computer BEFORE you start testing."""
from pathlib import Path
import tarfile, shutil, json, configparser, re, hashlib
kit=Path(__file__).resolve().parent
home=Path.home(); base=kit/'outputs/noctalia-test'; style=kit/'outputs/kde-outlines'
backup=base/'plasma-antes.tar.gz'
if backup.exists():
    raise SystemExit('Backup already exists. Use start-test.sh to repeat; do not replace your original backup.')
paths=['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc','.config/plasmarc','.config/kdeglobals','.config/kwinrc','.config/kwinoutputconfig.json','.config/kglobalshortcutsrc','.config/kscreenlockerrc','.config/klipperrc','.config/kcminputrc','.config/gtk-3.0/settings.ini','.config/gtk-4.0/settings.ini','.config/autostart','.config/noctalia','.local/state/noctalia','.config/Kvantum']
manifest={}
with tarfile.open(backup,'w:gz') as archive:
    for rel in paths:
        p=home/rel
        if p.exists():
            archive.add(p,arcname=rel)
            manifest[rel]='directory' if p.is_dir() else hashlib.sha256(p.read_bytes()).hexdigest()
        else: manifest[rel]=None
backup.chmod(0o600)
(base/'backup-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
shutil.copy2(backup,style/'kde-antes-contornos.tar.gz')
# The wallpaper restoration is generated with DESTINATION IDs and images.
cfg=configparser.ConfigParser(interpolation=None,strict=False);cfg.optionxform=str
cfg.read(home/'.config/plasma-org.kde.plasma.desktop-appletsrc')
lines=[]
for section in cfg.sections():
    match=re.fullmatch(r'Containments\]\[(\d+)\]\[Wallpaper\]\[org.kde.image\]\[General',section)
    if match and 'Image' in cfg[section]:
        i=int(match[1]); image=json.dumps(cfg[section]['Image'])
        lines.append(f'var d=desktopById({i}); if(d){{d.currentConfigGroup=["Wallpaper","org.kde.image","General"];d.writeConfig("Image",{image});}}')
(base/'restaurar-wallpaper.js').write_text('\n'.join(lines)+'\n')
# Capture the previous style before applying the local variant.
kg=configparser.ConfigParser(interpolation=None,strict=False);kg.optionxform=str;kg.read(home/'.config/kdeglobals')
(style/'menuFont-antes.txt').write_text(kg.get('General','menuFont',fallback=''))
(style/'widgetStyle-antes.txt').write_text(kg.get('KDE','widgetStyle',fallback=''))
kv=home/'.config/Kvantum/kvantum.kvconfig'
if kv.exists():shutil.copy2(kv,style/'kvantum-config-antes')
else:(style/'kvantum-ausente-antes').touch()
profile=kit/'work/noctalia-profile/config/noctalia';(profile/'palettes').mkdir(parents=True,exist_ok=True)
shutil.copy2(base/'config.toml',profile/'config.toml')
shutil.copy2(base/'KDE-Current.json',profile/'palettes/KDE-Current.json')
(kit/'work/noctalia-profile/state').mkdir(parents=True,exist_ok=True)
for name,script in [('menu','open-menu.sh'),('clipboard','open-clipboard.sh'),('voltar','return-to-plasma.sh'),('recuperar','recover-at-login.sh')]:
    p=base/f'codex-noctalia-{name}.desktop'
    p.write_text(re.sub(r'^Exec=.*$',f'Exec="{base/script}"',p.read_text(),flags=re.M))
print('Kit prepared in',kit)
print('Destination backup:',backup)
```

### outputs/noctalia-test/KDE-Current.json

```json
{
  "dark": {
    "mPrimary": "#cba6f7",
    "mOnPrimary": "#11111b",
    "mSecondary": "#cba6f7",
    "mOnSecondary": "#11111b",
    "mTertiary": "#a6e3a1",
    "mOnTertiary": "#11111b",
    "mError": "#f38ba8",
    "mOnError": "#11111b",
    "mSurface": "#181825",
    "mOnSurface": "#cdd6f4",
    "mSurfaceVariant": "#313244",
    "mOnSurfaceVariant": "#a6adc8",
    "mOutline": "#46485c",
    "mShadow": "#000000",
    "mHover": "#977dba",
    "mOnHover": "#000000",
    "terminal": {
      "background": "#181825",
      "foreground": "#cdd6f4",
      "cursor": "#cba6f7",
      "cursorText": "#181825",
      "selectionBg": "#977dba",
      "selectionFg": "#000000",
      "normal": {
        "black": "#181825",
        "red": "#f38ba8",
        "green": "#a6e3a1",
        "yellow": "#f9e2af",
        "blue": "#89b4fa",
        "magenta": "#cba6f7",
        "cyan": "#94e2d5",
        "white": "#cdd6f4"
      },
      "bright": {
        "black": "#181825",
        "red": "#f38ba8",
        "green": "#a6e3a1",
        "yellow": "#f9e2af",
        "blue": "#89b4fa",
        "magenta": "#cba6f7",
        "cyan": "#94e2d5",
        "white": "#cdd6f4"
      }
    }
  }
}
```

### outputs/noctalia-test/open-menu.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
if ! /usr/bin/noctalia msg status | /usr/bin/python -c 'import json,sys; s=json.load(sys.stdin); sys.exit(0 if s.get("activePanelId")=="launcher" else 1)'; then
 /usr/bin/noctalia msg bar-show search_edge >/dev/null
 sleep 0.25
fi
exec /usr/bin/noctalia msg panel-toggle launcher
```

### outputs/noctalia-test/open-clipboard.sh

```bash
#!/usr/bin/env bash
exec /usr/bin/noctalia msg panel-toggle clipboard
```

### outputs/noctalia-test/enable-noctalia-search.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 printf 'Inicie o teste Noctalia primeiro.\n' >&2
 exit 1
fi
systemctl --user stop plasma-krunner.service
if ! systemctl --user is-active --quiet noctalia-busca-desktop.service; then
 if ! systemd-run --user --unit=noctalia-busca-desktop --collect --property=Type=dbus --property=BusName=org.kde.krunner --property=BindsTo=noctalia-teste.service --property=After=noctalia-teste.service /usr/bin/python "$base_dir/desktop-search.py"; then
  systemctl --user start plasma-krunner.service
  exit 1
 fi
fi
```

### outputs/noctalia-test/desktop-search.py

```python
#!/usr/bin/env python3
"""Temporary KRunner activation interface adapter for Noctalia."""
import subprocess
import json
import time
from gi.repository import Gio, GLib

xml = '''<node><interface name="org.kde.krunner.App">
<method name="query"><arg type="s" direction="in"/></method>
<method name="display"/>
<method name="toggleDisplay"/>
<method name="displayWithClipboardContents"/>
<method name="displaySingleRunner"><arg type="s" direction="in"/></method>
<method name="querySingleRunner"><arg type="s" direction="in"/><arg type="s" direction="in"/></method>
</interface></node>'''

def handle(connection, sender, path, interface, method, parameters, invocation):
    values = parameters.unpack()
    term = ''
    if method == 'ActivateAction':
        action, values, platform_data = values
        if action.lower() == 'query' and values:
            term = str(values[0])
    elif method == 'query':
        term = values[0]
    elif method == 'querySingleRunner':
        term = values[1]
    elif method == 'displayWithClipboardContents':
        try:
            term = subprocess.run(['wl-paste', '--no-newline'], capture_output=True, text=True, check=True, timeout=2).stdout
        except (OSError, subprocess.SubprocessError):
            pass
    args = ['/usr/bin/noctalia', 'msg', 'panel-toggle' if method == 'toggleDisplay' else 'panel-open', 'launcher']
    if term:
        args.append(term)
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        if status.get('activePanelId') != 'launcher':
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-show', 'search_edge'], capture_output=True, check=True, timeout=2)
            time.sleep(0.25)
        subprocess.run(args, capture_output=True, check=True, timeout=5)
        invocation.return_value(GLib.Variant('()', ()))
    except (OSError, subprocess.SubprocessError):
        invocation.return_dbus_error('org.kde.krunner.NoctaliaUnavailable', 'Noctalia is not available')

freedesktop_xml = '<node><interface name="org.freedesktop.Application"><method name="ActivateAction"><arg type="s" direction="in"/><arg type="av" direction="in"/><arg type="a{sv}" direction="in"/></method><method name="Activate"><arg type="a{sv}" direction="in"/></method></interface></node>'
connection = Gio.bus_get_sync(Gio.BusType.SESSION, None)
info = Gio.DBusNodeInfo.new_for_xml(xml)
registration = connection.register_object('/App', info.interfaces[0], handle, None, None)
freedesktop_info = Gio.DBusNodeInfo.new_for_xml(freedesktop_xml)
freedesktop_registration = connection.register_object('/org/kde/krunner', freedesktop_info.interfaces[0], handle, None, None)
result = connection.call_sync('org.freedesktop.DBus', '/org/freedesktop/DBus', 'org.freedesktop.DBus', 'RequestName', GLib.Variant('(su)', ('org.kde.krunner', 4)), GLib.VariantType.new('(u)'), Gio.DBusCallFlags.NONE, 5000, None).unpack()[0]
if result != 1:
    raise SystemExit('KRunner's D-Bus name is already in use')
# The support bar does not react to the pointer: only the opening commands show it.
# When closing the search (Escape, external click or app choice), we collect the bar.
search_was_open = False

def sync_search_edge():
    global search_was_open
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        search_open = status.get('activePanelId') == 'launcher'
        if search_was_open and not search_open:
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, check=True, timeout=2)
        search_was_open = search_open
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return True

subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, timeout=2)
GLib.timeout_add(250, sync_search_edge)
GLib.MainLoop().run()
```

### outputs/noctalia-test/configure-super.py

```python
#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'super-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=16777250
mine=['codex-noctalia-menu.desktop','_launch','Noctalia Menu (test)','Noctalia Menu (test)']
if not saved.exists():
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 old=[]
 for e in entries:
  if e[2]==mine[0]:continue
  old.append({'id':[e[2],e[0],e[3],e[1]],'keys':list(e[6])})
 saved.write_text(json.dumps(old,indent=2)+'\n')
original=json.loads(saved.read_text())
restore=len(sys.argv)>1 and sys.argv[1]=='restore'
if restore:
 call('setForeignShortcut','(asai)',(mine,[268435488]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setForeignShortcut','(asai)',(mine,[meta,268435488]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Unable to register Super for Noctalia')
print('Super shortcut restored.' if restore else 'Super and Super+ Space registered for Noctalia.')
```

### outputs/noctalia-test/configure-clipboard.py

```python
#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'clipboard-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=268435542
mine=['codex-noctalia-clipboard.desktop','_launch','Noctalia Clipboard (test)','Noctalia Clipboard (test)']
call('doRegister','(as)',(mine,))
if not saved.exists():
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 old=[]
 for e in entries:
  if e[2]==mine[0]:continue
  old.append({'id':[e[2],e[0],e[3],e[1]],'keys':list(e[6])})
 saved.write_text(json.dumps(old,indent=2)+'\n')
original=json.loads(saved.read_text())
restore=len(sys.argv)>1 and sys.argv[1]=='restore'
if restore:
 call('setForeignShortcut','(asai)',(mine,[]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setShortcut','(asaiu)',(mine,[meta],2))
 call('setForeignShortcut','(asai)',(mine,[meta]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Unable to register Super+V for Noctalia')
print('Super+V restored.' if restore else 'Super+V registered to Noctalia.')
```

### outputs/noctalia-test/start-test.sh

```bash
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
```

### outputs/noctalia-test/return-to-plasma.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
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
printf 'Original Plasma panels restored.\n'
```

### outputs/noctalia-test/recover-at-login.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$base_dir/teste-ativo" ] && ! systemctl --user is-active --quiet noctalia-teste.service; then
 "$base_dir/return-to-plasma.sh"
fi
```

### outputs/noctalia-test/codex-noctalia-menu.desktop

```ini
[Desktop Entry]
Type=Application
Name=Noctalia Menu (test)
Exec="/home/delta/ricy-kit/outputs/noctalia-test/open-menu.sh"
Icon=noctalia
Categories=Utility;
X-KDE-Shortcuts=Meta+Space
```

### outputs/noctalia-test/codex-noctalia-clipboard.desktop

```ini
[Desktop Entry]
Type=Application
Name=Noctalia Clipboard (test)
Exec="/home/delta/ricy-kit/outputs/noctalia-test/open-clipboard.sh"
Icon=edit-paste
Categories=Utility;
X-KDE-Shortcuts=Meta+V
```

### outputs/noctalia-test/codex-noctalia-return.desktop

```ini
[Desktop Entry]
Type=Application
Name=Return to Plasma
Exec="/home/delta/ricy-kit/outputs/noctalia-test/return-to-plasma.sh"
Icon=noctalia
Categories=Utility;
```

### outputs/noctalia-test/codex-noctalia-recover.desktop

```ini
[Desktop Entry]
Type=Application
Name=Restore Plasma after the Noctalia test
Exec="/home/delta/ricy-kit/outputs/noctalia-test/recover-at-login.sh"
OnlyShowIn=KDE;
X-KDE-autostart-phase=2
```

## 9. Origins and historical record

Code consulted to confirm behavior: [Noctalia](https://github.com/noctalia-dev/noctalia), [Kvantum](https://github.com/tsujan/Kvantum), [Catppuccin Kvantum](https://github.com/catppuccin/kvantum), in addition to the local Plasma/KWin interfaces. The documentation here records what was observed and configured in this session; the links are the origins of the projects, not a verification of the latest version of the web.

On this computer, the original active archives are in `/home/delta/Documents/Codex/2026-10-08/no-x20/outputs/noctalia-test` and the active profile in `work/noctalia-profile` from the same folder. The kit files are a migration copy: creating them did not move or reconfigure the current session.

Steps taken: test with backup → wallpaper preservation and active Plasma → layer correction/exclusive zone → icon enlargement → KDE palette → menu compaction and rounding → SSID/volume concealment → central attached → background blur → Qt/Kvantum → tray menus with drawer → desktop search replacement → Super key correction by KGlobalAccel → search at the top with continuity → no pointer reaction support → Super+V.

The intermediate tests of central search and floating/top_center were replaced by the attached arrangement described here. The final opacity is 0,70, no 0,80. We did not profoundly modify the shell or recompile Noctalia. The initial unavailability of the controls motivated preserving active Plasma and an accessible fixed main bar; it does not depend on shutting down the entire desktop environment.

## 10Integrity and transportation

The file `ricy-kit/SHA256SUMS` identify the distributed files. Check before preparing at destination:

```bash
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
```

After executing the preparer some `.desktop` change path, then your hashes stop matching the original package. For transport, copy the entire folder `ricy-kit` and this `ricy.md`; SVG, license, scripts and TOML must travel together. The full SVG Kvantum stays in the kit to avoid partial playback only by description.

## Contribution — Integration Noctalia/KDE and compact menus — 2026-10-08  17:19 (America/Sao_Paulo)

Chat/work: Noctalia's reversible test on KDE Plasma, visual continuity and settings of Qt/Kvantum menus. Unconfirmed chat title. This contribution complements the previous script with the conference of active archives, the correction of the update of memory style and separate portable materials. There was no reapplication of changes during this documentation step.

### Objective, applied changes and status conferred

KDE initially used its menu, taskbar and search, with Catppuccin Mocha Mauve palette, JetBrainsMono Nerd Font source 10 Breeze decoration and pt. The request was to try Noctalia with accessible controls, preserved wallpaper and possibility to return, then approximate the format and compaction of the KDE menus of Noctalia.

1. **Noctalia and reversal:** package `noctalia 5.2.1-1.1`, isolated profile under `work/noctalia-profile`, scripts in `outputs/noctalia-test`, transitional unit `noctalia-teste.service`. Plasma panels have been removed from the test layout after Noctalia is ready; plasmashell remains active. Initial backup, manifest and return to Plasma have been prepared. The installed autostart is **recovery**, not autostart of Noctalia. There was no recompilation or change of Noctalia code.
2. **Useful area:** lower bar of 44 px, top layer, `reserve_space=true`; previous attempts with overlay and intelligent concealment have been replaced. Final state always visible, without auto-hide or smart-auto-hide. Scale 1,5, font_scale 0,85; taskbar scale 0,666667, icon_scale 1,725, item_spacing 6. These values compensate for the expansion of menus while keeping the icons readable.
3. **Tray, panels and colors:** network/volume without text (`show_label=false`); tray drawer 3 columns/24 px; central attached/auto near anchor. Custom palette `KDE-Current.json` with mandatory terminal in the format of the version used. 0,70 with compositor_blur; solid cards/boards. KWin: blurEnabled true, BlurStrength 5, NoiseStrength 2. Wallpaper remains under Plasma, with wallpaper/backdrop/dock/lockscreen/osd/Noctalia templates turned off in this integration.
4. **Search:** implemented Python/Gio adapter for `org.kde.krunner` on  `/App` and `/org/kde/krunner`. Answer `ActivateAction("Query", …)` it was necessary after the user reported that typing did not open the search. **This has been replaced in the current checked state** by launcher attached/auto and top support `search_edge` of 10 px without space reserve, in addition to Super/Super+space wrappers and Super+V clipboard. This evolution is already described in the anterior body of ricy.md; the copies of this contribution reflect the current archives, do not attribute a new execution during this documentation.
5. **KDE/Kvantum:** installed `kvantum 1.1.8-1.1` via `pkexec pacman -S --needed --noconfirm kvantum`. Created local variant Catppuccin MIT, installed in `$HOME/.config/Kvantum/KDE-Noctalia`, selected in `kvantum.kvconfig`; `kdeglobals/KDE/widgetStyle=kvantum`. Before, the direct key did not exist and Breeze was inherited from kdedefaults. The previous Kvantum configuration selected `Catppuccin-Mocha-Mauve-Glass`We didn't change Breeze's external decoration, nor KDE's general sources.
6. **Geometry and final source of menus:** Full SVG with external corner 12 px, background #313244, outline #46485c and selection #977dba; SVG selection with radius 6 px. Vertical frame of items 4 px/lateral 6 px, vertical text margin 0/lateral 2 px, min_right 24, separator 5. `spread_menuitems=false`, `shadowless_popup=true`, `menu_shadow_depth=0`, `popup_blurring=false`, `reduce_window_opacity=0`, `reduce_menu_opacity=0`. Restored menu font to 10 pt. The native test produced lines of 26 px; min_height is not a real height guarantee of 24 px.
7. **Effective update in applications:** the user reported that the compaction seemed to return and the corners still had a rectangle. We confirmed that the Dolphin was open since before the last adjustments. `setStyle` if the name changes; simply emit StyleChanged with Kvantum already active does not force reread the theme. We perform temporary alternation Breeze → Kvantum with signal `/KGlobalSettings`, `org.kde.KGlobalSettings.notifyChange(2,0)`. For sources, the correct signal is `/KDEPlatformTheme`, `org.kde.KDEPlatformTheme.refreshFonts()`. Previous notifyChange(0,0) was palette, not font. The portable script `reload-style.py` records the corrected sequence, with D-Bus flush and interval of 0,5 s.

Conference when documenting: `noctalia-teste.service`, `noctalia-busca-desktop.service` and `plasma-plasmashell.service` assets; `plasma-krunner.service` inactive; name `org.kde.krunner` belongs to the Python process of the adapter; `panels().length=0`. The active TOML profile coincides byte to byte with the copy in outputs; active SVG/kvconfig coincide with the output variant. `menuFont` It's JetBrainsMono Nerd Font, 10 pt; widgetStyle Kvantum; KDE-Noctalia theme. Desktop entries menu/clipboard/back present in `.local/share/applications`; recovery present in `.config/autostart`.

Checked Packages: Plasma Desktop 6.7.5-1.1, KWin 6.7.5-3.1, python-gobject 3.58.0-1, qt6-tools 6.12.0-1.1, python-pyqt6 6.11.0-4, noto-fonts 1:2026.10.01-1. `pacman -Q papirus-icon-theme` did not find this package name; Papirus-Dark is a previously existing visual preference, not a proven installation of this chat or script dependency. 5 and application interfaces are not covered by Qt style 6 installed.

### Materials and reproduction in other CachyOS

Independent folder: `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/`- Yours. `README.md` contains the full sequence. Do not execute this copy and copy of the kit root at the same time: share shortcut drives and IDs.

Files included: `prepare-destination.py`, `apply-style.sh`, `reload-style.py`, `restore-style-and-blur.py`, `verify-native-menu.py`, README; `outputs/kde-outlines/`, public color scheme, full SVG/kvconfig and MIT license; `outputs/noctalia-test/`, TOML/palette and start/back/recovery scripts, search activation, D-Bus adapter, open wrappers, shortcut configuration and four models `.desktop`.

The `.desktop` distributed use placeholders and are recalculated in the destination. The preparer captures layout, wallpaper, font, style, blur and Kvantum **of destination**, generates backup 0600 and refuses to overwrite it. Desktop IDs are obtained locally. Original shortcut files are created when enabled and protected on 0600. We do not include personal backups, active sentry, Noctalia status/clipboard, photos, conversations, SSID, Python caches or actual desktop captures.

Brief sequence after copying document and kit and checking `sha256sum -c SHA256SUMS` at the root:

```bash
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python prepare-destination.py
./apply-style.sh
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/start-test.sh
```

`python-pyqt6` is optional for the native test; `wl-clipboard` is optional for the query method that uses text already copied. The kit preserves the target user font family and adjusts the Font menu 10 pt; does not impose an absent family. Apply `KDE-Noctalia.colors` via plasma-apply-colorscheme is a migration option explained in README, **no** change applied to KDE in this chat: the palette already existed. The current full TOML is in the copy, avoiding rebuilding only from the summarized values.

### Verification actually performed and limits

- During the configuration: palette/TOML and IPC validation, conference of reserved zones; preservation/return of Plasma tested in the initial cycle; verified D-Bus Query calls; visual user monitoring confirmed icon size, palette and rounded format. The user also reported failures, so we did not treat all intermediate adjustment as approved.
- Menus: Qt offscreen previews showed selection/outcome and allowed correcting SVG gaps. The first preview forced WA_TranslucentBackground; she **no** it proved the automatic behavior of the applications.
- Later test in Wayland session: new QMenu **without forcing** this attribute, kvantum style, transparency activated by style, font 10 pt, five lines of 26 px, corner alpha 0.Alpha has also been checked 0 in the four corners/255 in the center of the preview. This proves transparent pixels of the test widget, not the final composition in all programs.
- After the last account of filled corners/old scale: correct update of fonts and real alternation Breeze/Kvantum executed in open applications. Later capture showed desktop/apps, but the context menu was not open. **There was no final visual confirmation of the user of the Dolphin menu after this recharge.** Thus, the previous passage associating popup_blurring=false to avoid the rectangle should be read as applied technical configuration/hypothesis, not as final proof of universal resolution.
- In this documentation: comparison of active files and services without changing configuration; static validation of all Python/Bash, TOML and JSON scripts. Preacher executed only in disposable copy with fictional HOME: verified backup 0600, local wallpaper/IDs, `.desktop` portable and refusal of second preparation. We did not execute the new application/reversion scripts in the actual session. Migration to another CachyOS has not been tested.

### Existing undo and backups

On this machine, personal backups remain in `/home/delta/Documents/Codex/2026-10-08/no-x20/outputs/noctalia-test/plasma-antes.tar.gz` and `outputs/kde-outlines/kde-antes-contornos.tar.gz` from the same folder; they were not transported to the contribution. `menuFont-antes.txt` and `kvantum-config-antes` The original local scripts are specific to this state of origin.

at the destination prepared with this contribution:

```bash
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
./outputs/noctalia-test/return-to-plasma.sh
python restore-style-and-blur.py
```

The first operation restores captured panels/plasmashellrc and local shortcuts, restarts KRunner and removes restored launchers/autostart from the test. The second restores only source keys, widgetStyle and blur and the previous Kvantum configuration/theme. If you have already used Kvantum, reloads the restored style. Do not remove packages. The optional color scheme requires selecting the previous scheme or restoring kdeglobals from the local backup (ReadME procedure, with the exception of replacing later preferences). The history produced during the test in the destination is not deleted automatically.

### Attempts discarded and pending

- Early Smart-hide/overlay committed bar access/position; replaced by top fixed main bar with reserve. Do not terminate the entire Plasma session to perform integration.
- Giant taskbar menus were compensated with local scale; tray menus, placed in the drawer. Do not modify Noctalia code to blur in context, as explicit user request.
- Increase of the Font menu 10 → 11 pt was incorrect interpretation of the request and was reversed. Compaction involves source **and** theme padding.
- First SVGs with stroke edge left cut-off faults in the corners; replaced by fills with exact limits. Kit actives contain the corrected variant.
- Deactivating blue popup alone did not demonstrate solving the report; it was necessary to investigate the style cache and font signal. We keep the final confirmation on actual menus and validation on the target computer pending.
- Initial central search is not the current state: current copy attached/top with search_edge already documented above. No additional profile change has been applied only to document.

Origin and license: Catppuccin Kvantum MIT, checkout consulted `71105d224fef95dd023691303477ce3eea487457`. Code of investigation: Kvantum `110aff8b97a221531ef55acc4faeacfd719cdfea`; Plasma Integration `46eddde9d38cf907786e567dd4a942140bb1f797`They are reviewed, unproven identification of the exact code of the installed packages. Ready actives allow you to play without compilation.

## Contribution — DEB/RPM Installer in Dolphin — 2026-10-08  17:31 (America/Sao_Paulo)

Chat/work: DeB/RPM support in CachyOS, double-click integration with Dolphin and Parsec conversion fixes. Unconfirmed chat title. This step only documented, checked the state and prepared materials; did not reinstall packages, changed active associations or corrected pending system.

### Objective, previous status and applied changes

The request was to open packages `.deb` and `.rpm` in Dolphin and install in CachyOS itself. Initially there was pacman and bsdtar; dpkg/rpm/debtap were not available, and both types of files opened with `org.kde.ark.desktop`. The first response installed only terminal tools, which did not meet the expected graphical flow. After correction of the scope, the user chose installation in CachyOS itself when compatible, without Ubuntu/Fedora environment.

1. **Packages installed by this work, confirmed in pacman.log:**  `dpkg 1.23.11-1.1`, `rpm-tools 6.0.1-2.2`; dependencies `nettle3 3.10.2-2.1`, `rpm-sequoia 1.10.3-1.1`; `namcap 3.6.0-3` with `python-boolean.py 5.0-2`, `python-license-expression 30.4.4-2`, `python-pyelftools 0.33-1`; `debtap 3.6.3-1` constructed from the AUR; `python-pyqt6 6.11.0-4`, `python-pyqt6-sip 13.13.0-1.1` for the interface. `binutils 2.47-2`, `fakeroot 1:1.37.2-3.1`, `pkgfile 26-1.1`, Git and base-devel already existed; do not assign your installation to this chat. The preserved AUR checkout has revision `d7c54a59fa0e3ac99a13f5db594de172aca0b1f4`; sources and debtap.install passed the SHA-check512 Makepkg.
2. **Converter bases:** startup with privileges in `/var/cache/pkgfile` and `/var/cache/debtap`. The first attempt took time on Ubuntu server, was closed and repeated with IPv4 wrapper curl, connection timeout 15 s and total 180 s. Debian/Ubuntu indexes, AUR list, virtual packages and extended-base-packages-list have been created; synchronization has reported success. This has not made dpkg/rpm native installers of CachyOS. Upstream still uses HTTP/`curl -k`, registered as a limitation.
3. **Local application:**  `/home/delta/.local/share/cachyos-package-installer/backend.py`, `installer.py`, `normalize_control.py` and executable copy `debtap`; Local README. PyQt6 opens a window, automatically converts if receiving file, confers metadata and transaction via `pacman -Qip`/`pacman -Up`; only then does it offer **Install**. This button runs `pkexec /usr/bin/pacman -U --noconfirm`, displaying Polkit authentication. Conversion does not use root, dpkg -i, rpm -i, --nodeps or --overwrite. `conversion.lock` serializes the conversions of this application; intermediate/output files remain in `/home/delta/.cache/cachyos-package-installer/conversion-*`, log in `last-conversion.log`. Test caches remain at source; they have not been transported.
4. **Dolphin and MIME:** created application entry `/home/delta/.local/share/applications/cachyos-local-package-installer.desktop` (ID) `cachyos-local-package-installer.desktop`) and executable service `/home/delta/.local/share/kio/servicemenus/cachyos-install-package.desktop` with action **Install in CachyOS...**. The `Exec` active is `/usr/bin/python /home/delta/.local/share/cachyos-package-installer/installer.py %f`. Defaults in `.config/mimeapps.list`: `application/vnd.debian.binary-package`, your alias `application/x-debian-package` and `application/x-rpm` point to the new application. Other defaults have been preserved. Up-to-date desktop/KDE caches. No autostart, services, daemons, Polkit rules or login/Fish shell changes were created.
5. **Corrections effectively applied to the local copy of Debtap without changing `/usr/bin/debtap`:** recognizes pkgfile bases completed in `.files`; payload size without taking over directories with 4096 bytes in Btrfs; fakeroot with explicit Bash, heredoc without premature expansion, `bash -e` and error if tar/zstd fail; `.INSTALL` It's only packaged if it exists. `backend.py` sets `LC_ALL=C`, `SHELL=/usr/bin/bash`, `TERM=dumb`. `normalize_control.py` normalizes CRLF and deploys dependencies fields. Numeric Loop avoids `cut: invalid decreasing range`. The normalizer solves common libraries by the exact ABI on `/usr/lib` and its providers pacman/pkgfile, including alternatives and version limits >=/>> with vercmp; other names remain subject to Debtap heuristics. This corrected the wrong choice of looparch64 cross compiler/Proton observed in Parsec conversion. It is not a universal dependency solver.
6. **RPM:** query header with temporary user rpmdb, binary payload capture of rpm2archive, tarfile extraction with data filter, generates intermediate DEB and converts by Debtap. RPMs with installation / trigger scripts, incompatible architecture or dependencies without viable mapping are rejected with explanation. temporary rpmdb avoids trying to create lock in `/var/lib/rpm`; binary capture avoids interpreting gzip as text. RPM scripts are neither ignored nor executed directly.
7. **Parsec, later status confirmed:**  `parsec 150-1` installed in 12:36:53, together with `ffmpeg4.4 4.4.8-5.1` and `libmfx 23.2.2-6`, as pacman.log and current bank. Chat has prepared and reopened the window for completion by the user; documentation confirms that the installation happened later, does not claim that we run a new installation now. Files include `/usr/bin/parsecd`, `/usr/share/applications/parsecd.desktop`, icon and library `/usr/share/parsec/skel/parsecd-150-104a.so`. Depends On current: alsa-lib, curl, ffmpeg4.4, glibc>=2.17, libgcc>=3.0, libglvnd, libjpeg-turbo, libpng, libsm, libstdc++>=5.2, libx11, libxcursor, libxi, opensl and systemd-libs. Optional: libxrandr. The original DEB corresponds to SHA-256  `c8a4407713d72dcb1c59f082977e81e1b9e8ffd679d0666882cde4c8a0821dd2`We didn't copy that binary to the kit.

### Materials and reproduction in other CachyOS

Independent folder: `$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer/`. README contains complete procedure, dependencies/AUR commands, index update, final configuration, diagnosis and reversal. We copy only the necessary scripts, two models `.desktop.in`, GPL-license2.0 Debtap patch against Debtap 3.6.3 and observed versions. There are no personal backups, mimeapps.list of origin, logs, credentials, binary Parsec or caches in the kit.

The portable copy keeps backend/GUI/normalizer byte a byte with the assets. The only Debtap adaptation to the kit changes the absolute normalizer path by script path. Desktop templates use `@INSTALLER@`, calculated and escaped by the preparer in the destination; do not depend on `/home/delta`. The script `install-integration.py` backups DESTINO before replacing integration/MIME in directory 0700 and manifest 0600 under `$HOME/.local/state/cachyos-package-installer-backups/<data-hora>/`. Captures the existence/absence of targets, MIME archives, defaults and local list of packages without reusing the original backup of this computer. Each execution generates new folder.

Sequence summarized, **to run on another computer**in Bash:

```bash
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
umask 077
backup_pacotes=$(mktemp -d "$HOME/ricy-pacotes-antes-XXXXXXXX")
pacman -Q > "$backup_pacotes/pacotes.txt"
pacman -Qqe > "$backup_pacotes/explicitos.txt"
sudo pacman -Syu
sudo pacman -S --needed dpkg rpm-tools binutils fakeroot pkgfile namcap python-pyqt6 desktop-file-utils git base-devel
build_debtap=$(mktemp -d "$HOME/debtap-build-XXXXXXXX")
git clone https://aur.archlinux.org/debtap.git "$build_debtap/debtap"
cd "$build_debtap/debtap"
cat PKGBUILD debtap.install
makepkg --verifysource
makepkg -si
sudo bash -c 'curl() { /usr/bin/curl -4 --connect-timeout 15 --max-time 180 "$@"; }; export -f curl; /usr/bin/debtap -u'
cd "$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer"
python install-integration.py
```

Execution prerequisites include KDE/Dolphin/Polkit, Python/PyQt6, pacman, Bash, binutils, libarchive/bsdtar, fakeroot, pkgfile, namcap, zstd, curl, gawk/grep/sed/coreutils/tar/gzip, and desktop-file-utils. Reference state: Python 3.14.7-2, libarchive 3.8.9-1.1, Polkit 127-3.1, zstd 1.5.7-2, Dolphin 26.08.1-1.1, desktop-file-utils 0.28-1.1. The complete observed list is in the kit. Decompressed indexes occupied about 1.1 GiB on this machine; this is not a fixed limit. AUR and databases may change; migration to another CachyOS was not performed.

### Verification performed and limits

- Previous tests: Python/Bash syntax; desktop-file-validate; Qt window offscreen with captures; minimal DEB/RPM reached Arch packages without installing fixtures; RPM with scriptlet was rejected with explanatory message. The first fixtures did not cover Fish/CRLF/Parsec.
- After user reported failure: Repeat conversion with the same Parsec DEB; hash comparison with the original file; GUI offscreen under `SHELL=/usr/bin/fish` and TERM removed reached **Install**, no tput/cut notices and no loongarch/Proton dependencies. Pacman -Up solved only libmfx/ffmpeg4.4/parsec missing. There was no proof of login/streaming or full Parsec operation in this chat.
- By documenting: pacman -Q/Qi/Ql and log confirmed versions and installation; gio mime confirmed defaults; checked scripts and active entries. Syntax AST Python and bash -n of portable materials passed; compared copies and absence of user paths from verified source. We do not perform application/restoration, GUI, conversion or installation again during this documentation.
- **New presidency of the conference:**  `pacman -Qkk parsec` reported differences in UID/GID in all 15 entries, no other notices in that execution. `stat` of `/usr/bin/parsecd` and the installed library showed root:root with modes 755/644, respectively; this does not prove the consistency of the manifesto `.MTREE`. The current flow does not explicitly normalize ownership in tar/mtree. We do not correct by prohibition of reapplying changes in this step. Kit preserves the current implementation and highlights the need to audit UID/GID metadata before expanding use.

### Restore and backups

Local MIME historical backup of this machine: `/home/delta/.local/share/cachyos-package-installer/mimeapps.list.before`. It has not been copied to the kit because it contains personal defaults. Restore this complete file can overwrite changed associations later; prefer to review the three entries. Research files and fonts remain in `/home/delta/.cache/package-support`; Indexes remain in `/var/cache/debtap` and `/var/cache/pkgfile`Transactions created snapshots Snapper (17–26 during tools/interface, 27–28 when installing Parsec, according to outputs; we do not confirm its current availability or include snapshots in the kit.

In the prepared destination, close the installer after completing the operation and run:

```bash
cd "$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer"
python restore-integration.py "$HOME/.local/state/cachyos-package-installer-backups/<data-hora>"
```

Restores complete files/absences of targets and updates KDE caches. Requires confirmation because it can replace later changes in those archives; for selective restoration, review backup. Do not remove packages, installed apps, cache or backup. No backup, if Ark exists, `xdg-mime default org.kde.ark.desktop <tipo-MIME>` for the three types returns the opening in Ark, but does not automatically recreate different previous preferences.

Parsec is removable by `sudo pacman -R parsec`. To remove tools, compare previous/current list, check dependents and review the transaction; do not automatically remove Python/Qt or tools that already existed. `sudo pacman -Rns dpkg rpm-tools debtap namcap` only if these packages have been added and are not required for other jobs. PyQt6 is already quoted by another theme of this document: your removal can affect it. User cache can be deleted after closing the window, losing output/log; removal of Debtap package does not delete `/var/cache/debtap`. Pkgfile indices are shared, do not delete indiscriminately. Converted Apps and installed dependencies require separate reversal by pacman.

### Discarded attempts and remaining to-dos

Discover/PackageKit, Alien and rpmtoarch were consulted, not installed or used as final solution. The attempt to update without IPv4/timeout was replaced by successful synchronization. RPM without temporary rpmdb produced lock error; rpm2archive interpreted as text produced bytes gzip: both corrected. First Parsec conversion under Fish failed compression and issued misleading permission message; explicit Bash corrected. CRLF/folded fields generated invalid architecture and incomplete dependencies; fixed. The next conversion suggested cross compiler/Proton, never installed by this attempt; replaced by native providers before the final installation.

Do not promise universal compatibility or installation of any RPM. RPMs with scripts need to be adapted; some DEBs also require specific adjustments. The pacman -Up check does not test the operation of the app, libraries dynamically loaded or replaces final verification of conflicts. Converted programs do not receive automatic updates of the source distribution. The UID/GID divergence of metadata, testing on another computer, and complete functional validation of applications remain pending.

Third Origin: Debtap https://github.com/helixarch/debtap, copyright George Savvidis, GPL-2.0 (or later in the header), preserved license. https://aur.archlinux.org/packages/debtap. Patch and ready fonts allow you to audit local changes without depending on a partial description.

## Contribution — Implementation of destination and validation — 2026-10-08  19:10 (America/Sao_Paulo)

Work: execution of migration authorized by the user from `/home/delta/ricy/ricy.md`. This step implemented the configuration; the historical restriction of the steps prior to only documentation does not match the current request. Previous reports have been preserved. The active copy of this installation is in `/home/delta/ricy-kit/contributions/`, and the transportable kit remains in `/home/delta/ricy/ricy-kit/`. The old paths under Documents/Codex refer to the origin of the document, not to the active profile of this implementation.

### Previous state and result

The destination already executed CachyOS/KDE Plasma Wayland, with two Plasma and KRunner panels active. Noctalia, Debtap, dpkg, rpm-tools, namcap and PyQt6 were missing; Kvantum was installed. The original copy of the kit passed on all SHA256SUMS hashes before any preparation. The kit was copied for `$HOME/ricy-kit`, preserving the original. We use the contribution `noctalia-kde-integration-and-menus`, which adds style/blur key backups; the old variant at the kit root has not been activated.

Result: Noctalia and active D-Bus adapter, active plasmashell for desktop/wallpaper, inactive KRunner and collected Plasma panels. Lower bars on both monitors, 44 px, exclusive_zone=44, top layer, always visible. Profile and palette of kit validated with Noctalia 5.2.1. Launcher by wrappers and Query D-Bus; central clipboard; Kvantum KDE-Noctalia, Font menu 10 pt preserving the existing JetBrainsMono Nerd Font family; KDE-Noctalia scheme applied; hard activated KWin blur 5 and noise 2. The local wallpaper already pointed to limine-splash.png and was preserved. The icon theme observed in the destination is Breeze-Dark; Origin papirus was not imposed as dependency on integration.

Dolphin: association of the three MIMEs with the installer and context action applied with destination backup. Conversion as common user, installation via button/pkexec/pacman; pkgfile/Debtap databases initialized. Implementation maintains the script's reversible test character: autostart is recovery, and Noctalia does not start automatically after re login. `/home/delta/ricy/start.sh`, `/home/delta/ricy/return.sh` and `/home/delta/ricy/IMPLEMENTADO.md` for local use.

### Packages and sequence executed

The complete script update ended with 190 updated packages and 15 added. Previous list and final list are in the private directory `/home/delta/ricy/execucao-2026-10-08/`They were added debtap, dpkg, ministream, namcap, nettle3, noctalia, pyalpm, python-boolean.py, python-license-expression, python-pyelftools, python-pyqt6, python-pyqt6-sip, rpm-sequoia, rpm-tools and sdbus-cpp. Some are update dependencies/additions, not components chosen separately. The system recommended restarting due to updating of base/kernel components; the session was maintained.

Final versions: noctalia 5.2.1-1.1; Plasma Desktop 6.7.5-1.1; Plasma Workspace 6.7.5-3.1; KWin 6.7.5-3.1; Kvantum 1.1.8-1.1; python-gobject 3.58.0-1; qt6-tools 6.12.0-1.1; glib2 2.90.1-1.1; noto-fonts 1:2026.10.01-1; dpkg 1.23.11-1.1; rpm-tools 6.0.1-2.2; debtap 3.6.3-1; namcap 3.6.0-3; python-pyqt6 6.11.0-4.

Applied sequence, summarized with portable paths (local execution was in Bash, using the scripts present in the kit):

```bash
# Register packages and check hashes before installing/preparing.
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
sudo pacman -Syu --needed --noconfirm noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts python-pyqt6 wl-clipboard dpkg rpm-tools binutils fakeroot pkgfile namcap desktop-file-utils git base-devel
cd contributions/noctalia-kde-integration-and-menus
python prepare-destination.py
./apply-style.sh
mkdir -p "$HOME/.local/share/color-schemes"
cp outputs/kde-outlines/KDE-Noctalia.colors "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/start-test.sh
```

AUR Debtap checkout has been read, sources verified by SHA-512, built with `makepkg` and installed by `pacman -U`. Checkout, package and logs have been preserved in `execucao-2026-10-08/debtap-aur/` (local materials, not added to the portable kit). The indexes were synchronized with IPv4 curl wrapper, retractions, connection time 15 s/total 180 s, HTTPS and TLS check; all required indexes were checked as non-empty. `python install-integration.py` Dolphin contribution installed integration as the desktop user.

### Corrections required during deployment

1. The first start recorded the shell/adapter and removed the panels, but failed to register Super. `setForeignShortcut` alone did not create the record in this destination. `doRegister` and `setShortcut` before `setForeignShortcut` ed `configure-super.py`. Super/Super+Space came to appear on KGlobalAccel; the new complete start cycle ended without error. The original local JSON was conserved.
2. We fixed the UID/GID to-do of the converter: `.MTREE` uses zero UID/GID, the final tar uses zero owner/number group, `.INSTALL` only enter when there is and error in the generation of mtree interrupts the conversion. This change was made in the local copy and active copy of contribution, keeping `/usr/bin/debtap` original for the indexes.
3. Fixtures without dependencies exposed `namcap-checks`, `namcap-dependencies` and `namcap-libraries` included in the final package. `namcap-*` and `pkgbuildinstallations*` both tar and mtree and size calculation. The new conversion does not contain these intermediaries.
4. Update wrapper deletes `-k`, convert HTTP URLs from Debian/Ubuntu indexes to HTTPS and validate index files after command. The completed update does not depend on the password to stay in file; no secret has been added to the kit.

The distributed historical archives of other chats have been preserved. `ricy-kit/contributions/target-implementation-fixes/` contains the two corrected archives, its diffs, hashe manifest, idempotent applicator, index wrapper, README and Debtap license. For another migration, run `apply-fixes.py`  **after the SHA256SUMS conference and before preparation/installation**. The applicator accepts only the known original file or corrected version; unknown modifications require patch revision. The corrections were reproduced in disposable copy and compared byte to byte with the asset.

### Verification carried out

- `noctalia config validate` approved TOML/palette. Logs registered lower reservation of 44 px on both monitors and top support without reservation. KWin confirmed blur effect loaded.
- Active Noctalia, Adapter and Plasmashell Services; KRunner inactive; `panels().length=0`. KGlobalAccel records checked for Meta, Meta+Space and Meta+V. Wrappers opened launcher/clipboard; call `org.freedesktop.Application.ActivateAction("Query", …)` opened launcher by the adapter.
- Real restoration with `return-to-plasma.sh`: the two Plasma panels returned. Restart by fixed script: collected panels, configured shortcuts and active test. The IDs/wallpaper checked before/after remained the destination ones.
- Native Qt Menu again tested without forcing translucency: Kvantum, source 10 pt, five lines 26 px, active translucency attribute and alpha zero in the corner. There was session capture inspection, then removed; no visual confirmation of the user of the Dolphin menus was recorded. Do not state universal resolution of the app menus themselves.
- DEB and minimal RPM generated locally, converted and validated by pacman, file/mtree with UID/GID zero and absence of intermediaries. `pacman -Qkk` reported, for each of them, 4 Archives and 0 changed. Both removed when finished; no test packages remain installed.
- RPM containing scriptlet was refused with explanation. GUI offscreen executed with SHELL=fish/TERM missing reached the Install button without clicking this button. The test transaction was made directly by the pacman with privileges; no interactive Polkit authentication was tested.
- Defaults of the three MIMEs checked. `.desktop` application passed on desktop-file-validate with category tooltip. This validator does not accept Type=Service from KDE menus; its output in servicemenu is not error proof because the structure follows KDE documentation (https://develop.kde.org/docs/apps/dolphin/service-menus/).
- Syntax of Python/Bash scripts of the approved corrected kit. Corrections app tested twice on the same disposable copy. Hashes of the transport kit checked after adding the new files.

### Backups and undo

Local private backups of this implementation: `plasma-antes.tar.gz`, `backup-manifest.json` and JSON of the shortcuts in `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/`; `kde-antes-contornos.tar.gz` and `estado-antes.json` ed `outputs/kde-outlines/`. Backup/shortcut files checked have mode 0600Don't transport those files to another computer.

```bash
# Layout and original shortcuts; keeps colors/style:
"$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/return-to-plasma.sh"
# Previous style/source/blur and Kvantum keys:
python "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/restore-style-and-blur.py"
```

For colors, select the previous scheme in KDE or selectively restore kdeglobals from the local backup as README, considering later preferences.

Backup of Dolphin integration in this implementation: `$HOME/.local/state/cachyos-package-installer-backups/20261008-190438-261237/`. Close the window and use the contribution restorer with this folder. The date/time is appropriate for this destination: in another installation use the path emitted by the installer. Do not remove packages/tools, bases or external installed programs.

### Limitations and pending status

The installation and migration were effectively executed in this destination, unlike the historical documental phase only. Fixtures validate the flow and correction of metadata; they do not prove compatibility of any DEB/RPM. Parsec does not follow the kit and has not been installed/reinstalled at this stage, nor have its historical metadata changed. Log-in/streaming tests remain out of the verified result. Noctalia Bluetooth notice indicates absence of BlueZ active in the destination; Bluetooth service has not been changed for integration. The reset recommended by the updater and the user's visual conference remain pending. After a new login, run `start.sh` resumes the Noctalia test.

## Contribution — Automatic start of Noctalia in KDE 2026-10-08  19:40 (America/Sao_Paulo)

Objective: After restarting, the user reported that he entered Plasma again and requested that Noctalia come by default. The previous implementation followed the test mode of the document and had only recovery in the login. **The final manual start state described above was replaced by the automatic start described in this contribution.** Plasma/KWin remain responsible for the session, desktop and wallpaper.

### Applied changes

- Installed and enabled `$HOME/.config/systemd/user/ricy-noctalia-integracao.service`, WantedBy=plasma-workspace.target, after plasmashell. A oneshot unit awaits real readiness of Plasma/KGlobalAccel, initiates integration and remains active. In error during its execution, wrapper restores Plasma. Uses Wants for plasmashell, allowing rollback to restart plasmashell without canceling its own recovery.
- `$HOME/.config/systemd/user/noctalia-teste.service` from transient to permanent. `/usr/bin/noctalia`, the same NOCTALIA_CONFIG_HOME/NOCTALIA_STATE_HOME of the isolated profile under `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/`, Restart=on-failure/RestartSec=2, PartOf=graphical-session.target and Wants=noctalia-busca-desktop.service.
- `$HOME/.config/systemd/user/noctalia-busca-desktop.service` is permanent, with Requirements/BindsTo/After shell and PartOf shell/session. Use Type=exec, no BusName in systemd; Python assumes `org.kde.krunner` As before. Permanently declaring the same BusName of the KRunner native unit caused conflict between units; this attempt was corrected. The activation compares the D-Bus owner's PID with the MainPID of the adapter before declaring success.
- Active search start and activation Scripts detect permanent units and use `systemctl start` instead of creating transitory units. KRunner is stopped before the shell starts its adapter.
- `recover-at-login.sh` does not restore the panels while automatic integration is enabled. Autostart makes its own recovery. `return-to-plasma.sh` disables/for automatic integration before restoring panels and shortcuts; an internal recovery prevents interrupting the drive itself.
- `configure-super.py` waits up to two seconds for the effective creation of the action in KGlobalAccel. The first creation after new login failed at the immediate conference; the wait/repetition of the record was applied. Original shortcut backups remain intact.
- `$HOME/ricy/start.sh` enables and restarts automatic integration. `$HOME/ricy/return.sh` keeps the return to Plasma, now also for the next logins. IMPLEMENTADO.md It's been updated. `noctalia-plasma.service`, pre-existing and disabled, was not enabled; thus does not open another profile.

### Reproduction and materials

New, independent directory: `ricy-kit/contributions/noctalia-autostart/`. Includes Python installer, three systemd unit models, automatic wrapper, five updated scripts and README. The historical archives of the other chats in the transport kit have been preserved; the installer applies these updates to the contribution prepared at the destination.

After checking SHA256SUMS, apply `target-implementation-fixes` and prepare the contribution `noctalia-kde-integration-and-menus`:

```bash
cd "$HOME/ricy-kit"
python contributions/noctalia-autostart/install-autostart.py
```

The installer must be run by the desktop user, without sudo, in Plasma Wayland. Captures the previous files in `$HOME/.local/state/ricy-inicio-automatico-backups/<data-hora>/`, generates local paths in the units, updates scripts, validates units and enables/starts integration. `20261008-193935-356538`; the first execution generated another previous backup, preserved in that same root. Each destination must use its own emitted path. No layout/style backups were remade or additional packages installed at this stage.

### Tests and final result

- Python/Bash Syntax and `systemd-analyze --user verify` of the three approved units.
- Enabled integration, with real symlink in `plasma-workspace.target.wants`. ExecStart final finished with 0/SUCCESS. Shell, active adapter and plasmashell; Plasma panels collected; isolated profile preserved.
- Explicit return to Plasma disabled the automatic start and restored the two panels. New start reactivated preference and shortcuts without manual pre-recording.
- Restart shell restarted adapter; PID owner of `org.kde.krunner` coincided with MainPID of the adapter. ActivateAction Query opened the launcher.
- The old login recovery was executed with auto-start enabled and preserved integration.
- Invalid TOML configuration was temporarily entered: the drive failed and restored the two panels/KRunner. The original content was restored finally and the integration started again successfully. `execucao-2026-10-08/inicio-automatico-recuperacao.log`.
- An intermediate copy lost the wrapper execution permission when synchronized; script modes were fixed to 0755. The final installer and the full cycle were executed after correction.

No other full reboot was executed by the agent after these changes. The same starting services and their KDE target enablement were tested. The final state is already active in the current session and configured for the next logins.

### Undo

Use the entry **Back to Plasma**, `$HOME/ricy/return.sh`or the `return-to-plasma.sh` This disables the automatic start and restores the local panels/tails, keeping the colors and style. Permanent units can remain installed and inactive; `start.sh` Reactivate preference. To also return to scripts/units prior to persistent deployment, review files in the private backup issued by the installer, considering later changes. Style/blur restorers and Dolphin integration remain separate and valid.


## Contribution — Locking the login screen look (08/10/2026, 19:51)

After implementation, the user asked the lock screen to have the view of the screen to sign in and clarified that the change was restricted to the lock. It was added `contributions/login-matched-lock-screen/` to the kit without changing SDDM. The local login theme is `mocha-limine`, with Limine background and JetBrainsMono font. The lock uses the same wallpaper and the native Breeze visual components: watch, user and form. The form appears already in the opening and waits a minute of inactivity, such as login; media and password reveal button are hidden. Session buttons remain suitable for an already open session.

In Plasma 6.7 the lock comes from the shell package `org.kde.plasma.desktop`. The applicator generates a local package of the same ID, adapting only presentation and display time in the native QML; the other components point to KDE installed. Authentication/PAM, password synchronization, biometrics and errors continue in KDE implementation. The applicator validates the snippets before writing and refuses a pre-existing local shell without its marker. After updating Plasma, reapplying it regenerates the files from the new KDE.

Verification: prior `kscreenlocker_greet --testing`, local loading confirmed on the journal on both monitors and visual conference of the capture. The form remained visible after 15 seconds, without the media controls. Restoration of the previous state was executed, followed by new application. No real lock or password test was done at this stage. Backups and captures are private in the destination, outside the kit. Noctalia services remain active and the auto login start is enabled.


## Correction — Unlock initialisation (08/10/2026)

After the visual test of the block contribution, the user reported that the unlocking did not process the password, although the SDDM authenticated. The adaptation had changed the initial state of `uiVisible` of `false` for `true`, preventing the transition whose handler starts native authentication. The applicator has been fixed to keep KDE's initial state and make the interface visible after mounting via `Qt.callLater`. The appearance and initial presentation of the form continue as in the login.

Functional verification: the copy of the previous version reproduced the problem, without login and with timeout. The corrected version was exercised in temporary copy using the original form (`passwordBox` and `startLogin`) up to the real authenticator `kde`, with WFP result code 0 / Success and closing of the greeter. They passed the modes immediately and with tolerance of 1200 ms in `--testing` and rendering offscreen, without blocking the actual session. The password passed by descriptor in memory and was not saved in the kit or logs. Active copy, portable contribution, README and hashes have been updated.


## Contribution — Login, blocking, cursor and resettlement kit — 2026-10-09  23:39 (America/Sao_Paulo)

Work: capture of effective settings requested by the user to reuse appearance at the next installation. Assets and preferences have been exported; new installers have not been applied to the source system. `REINSTALL.md`, next to this record.

### Visual status captured

- **SDDM Login:**  `/etc/sddm.conf.d/95-mocha-limine.conf` select
`mocha-limine`, CursorTheme Bibata-Modern-Classic, Cursor 16 and Font JetBrainsMono Nerd Font. `theme.conf` sets showlogo hidden, showClock true, type image, color #1e1e2e, fontSize 10 and Limine background. The local QML uses immediate form, timeout 60000 ms and proportional clipping of the image.
- **Login colors:** privileged reading, visual only, of
`/var/lib/sddm/.config/kdeglobals`; ColorScheme CatppuccinMochaMauve, widgetStyle Breeze, Icons breeze-dark and JetBrains fontMono Nerd Font 10 en. Colors/ColorEffects groups were exported in `greeter-preferences.json`. The login selection is #cba6f7, distinct from the KDE-Noctalia #977dba selection.
- **Block:** kscreenlockerrc confirms Limine, FillMode 2, watch always
visible, without media. The active QML preserves uiVisible false and the Qt.callLater transition corrected; the form has 60 s. We reused the contribution `login-matched-lock-screen`, generated from KDE of the destination, without copying the local shell of this machine. There was no new password lock/test in this capture.
- **Cursor:** kcminputrc Mouse cursorTheme Bibata-Modern-Classic/cursorSize 16;
GTK 3/4 and environment.d/20-cursor.conf The local copies and the Bibata system confirm the same. 2.0.6 file to file were compared and are identical.
- **Other preferences:** JetBrainsMono Nerd Font 10 en in KDE, WM and
GTK; icons Breeze Dark inherited from kdedefaults; theme Plasma mocha-blur; splash Catppuccin-Mocha-Mauve; effective decor Breeze without edge, BorderSizeAuto false, NoPlugin false; Qt/Kvantum KDE-Noctalia; GTK adw-gtk3-dark, Ocean sound; fontconfig with antialiasing and hintslight; blur 5/2. The old global theme defaults that cite another cursor/Aurorae were not treated as effective values. The application uses selective overrides.
- **Optional extensions:** adaptivepanelwidth, smoothwindowgeometry fonts
and included windowsarrows; captured selected flags and shortcuts. The native windowsarrow module is recompiled in the destination before applying. .so from this machine not even test/backups files from the sources.

### Materials included and reproduction

New portable folder: `ricy-kit/contributions/login-lock-cursor-appearance/`, containing README, preferences.json, greeter-preferences.json, kwin-preferences.json, system.py, user.py, common.py, apply-wallpaper.sh. Assets: QML/metadata/logo SDDM, Bibata complete, Limine wallpaper, four Regular/Bold/Italic/BoldItalic JetBrainsMono Nerd Font with OFL, local themes Plasma/splash, fontconfig and sources of KWin extensions. Kvantum and KDE colors reuse the existing files of the Noctalia contribution. GTK/icons/sounds come from the packages of the new destination.

Go on. `REINSTALL.md`: Hashes from the original kit; dependencies; apply fixes; install assets/visual preferences; choose wallpaper; prepare integration Noctalia; install auto start; generate lock; optional Dolphin extensions/installer; new session and conference. All accounts, IDs and local installer/backups paths are resolved at destination. The transported wallpaper is the Limine audience of the local package, not a personal photo.

### Backups and undo in destination

Installers create new private backups on `/var/lib/ricy-appearance-backups/DATA-HORA/` (system) and `$HOME/.local/state/ricy-appearance-backups/DATA-HORA/` (user), with manifesto, previous existences and affected files/themes. System backup records previous UID/GID; the application resolves the destination sddm account. To undo:

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python user.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python system.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

The lock keeps your own restorer/backup. Revert multiple plays in reverse order. Restores replace integral files and can replace later edits; do not remove packages. The optional wallpaper script changes the image of local desktops without saving layout; choose the previous image by Plasma if you want to undo this choice.

### Verification and limits

Python/Bash Scripts and JSON data have been validated. Application/restoration have been exercised in disposable root/home, with previous values, absence of assets and other preserved keys, including GTK with duplicate key. Generation/restoration of the block in disposable HOME confirmed uiVisible false, Qt.callLater and timeout 60000 ms. The native arrow module has been recompiled in temporary folder against the installed KWin. The transport kit/file has updated SHA256 verification.

The active KDE/SDDM/Noctalia settings have not been modified at this stage, nor has SDDM restarted or a complete new installation been performed. Privileged reading has only exported visual preferences without login data, password/PAM, user list or avatar. No personal backups, monitor IDs, historical or Noctalia status have been copied. Drivers/devices and future KDE/Noctalia versions require setting/checking in the destination.


## Scope correction — Konsole animated cursor — 2026-10-09  23:45 (America/Sao_Paulo)

The user clarified that the requested cursor was Konsole's animated text cursor. Bibata's previous capture corresponds to the mouse pointer, which remains as an additional preference; it did not meet the request alone.

The current default profile in `~/.config/konsolerc` Yeah. `PlasmaBlur.profile`. The file `~/.local/share/konsole/PlasmaBlur.profile` contains:

```ini
[Terminal Features]
AnimatingCursorEnabled=true
```

The Konsole 26.08.2-1.1 installed recognizes this property natively, according to `/usr/bin/konsole --list-profile-properties`. The definition was also checked in the official version code: https://github.com/KDE/konsole/blob/v26.08.2/src/profile/Profile.cpp . It is neither a pointer theme nor requires modifying the Konsole executable.

The new contribution `ricy-kit/contributions/konsole-animated-cursor/` contains complete profile/palette, Qt/Kvantum wrapper, application input, backup/restoration applicator and README. JetBrainsMono Nerd Font have been captured 10 en, palette Catppuccin Mocha, Opacity 0.85, Blur true, MenuBar Disabled and DefaultProfile PlasmaBlur.profile. BlinkingCursorEnabled, CursorShape and cursor-specific colors are not defined in the local profile: the inherited values of FALLBACK remain, without inventing new options.

The applicator confers animation support on the destination before writing, merges DefaultProfile/MenuBar only into konsolerc and saves previous files/absences under `$HOME/.local/state/ricy-konsole-backups/DATA-HORA/`. It does not carry backups, terminal history, SSH, commands, home directory or source user names. The shell is that of the destination user.

```bash
sudo pacman -S --needed konsole kvantum ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit/contributions/konsole-animated-cursor"
python apply.py
# To undo, use the printed backup in the destination:
python apply.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
```

The Guide REINSTALL.md was corrected to apply this contribution as well. Application/restoration were tested in disposable HOME, preserving other keys and restoring previous/removing files missing. Python Syntax, Wrapper Bash and desktop input were validated. Distributed profile/palette coincide with active files; native support was checked without opening a new terminal window. There was no change in active configuration or new animation visual test. Hashes and portable package were updated.

## Contribution — Permanent status, complete appearance and SDDM at destination — 2026-10-10  18:04 (America/Sao_Paulo)

Work: validation of the updated package from 09/10 and completion of the requested implementation. The user replaced the previous package and explicitly chose SDDM. This state replaces the test/manual mode of historical sections. The reference script is now `REINSTALL.md`; the reports of other destinations have been preserved.

### Validation and recovery of kit

- The kit freshly extracted in `/home/delta/Documents/ricy/ricy-kit` passed in full SHA256SUMS before changes. Syntax of Python/Bash and contents of the checked JSONs. The current version includes automatic start, complete appearance, fixed lock and animated Konsole cursor, missing from the previous package.
- The directory change had taken the active kit, its backups and its profile to the trash. They were recovered from the local folder `$HOME/.local/share/Trash/files/ricy/`, without moving or deleting the copy from the trash. The original backup of recovered layout was compared by SHA256 and is identical to the previous, mode 0600.
- The active installation is now in **`$HOME/ricy-kit`**. Document and transport kit remain in `$HOME/Documents/ricy`. Private profile/state, backups and `.desktop` calculated belong only to the active kit. Do not transport the entire active folder as a clean kit. The record of the first deployment was preserved in `$HOME/.local/state/ricy-implementacao/ricy-registro-primeira-implantacao.md`.
- The final corrections of `target-implementation-fixes` to the active kit before installers. Updated local copy of the Dolphin installer: metadata with UID/GID zero and deletion of `namcap-*`/`pkgbuildinstallations*`. Indexes synchronized by the updated version of the HTTPS/TLS wrapper.

### State applied

| Component | State in this destination |
|---|---|
| Noctalia | Permanent KDE Wayland login; plasma-workspace.target enabled integration |
| Shell/adapter | Units in `.config/systemd/user`, restart in failure and session link; Type=exec without Bus disputeName |
| Desktop | Plasma/KWin maintained; panels replaced by Noctalia lower bars, 44 px and space reserve |
| Search and Clipboard | Meta/Meta+Space and Meta+V, top search with hidden support outside the opening |
| Palette/menus | KDE-Noctalia, Kvantum KDE-Noctalia, blur KWin 5/2  |
| Sources | JetBrainsMono Nerd Font 10 en KDE/GTK/WM; four sides of the kit installed on the system |
| Icons | Breeze Dark (`breeze-dark`), according to the final capture; replaces Papirus-Dark used in the first deployment |
| Plasma Appearance | mocha-blur; global package and splash Catppuccin-Mocha-Mauve, with selective overrides |
| Windows | Breeze without borders; WindowsArrows compiled against local KWin; Super registered arrows; smoothwindowgeometry loaded |
| Wallpaper | Limine on both local desktops, `/usr/local/share/ricy/limine-splash.png`, FillMode 2; Noctalia wallpaper disabled |
| Pointer | Modern Classic Bibat, size 16, KDE/GTK, SDDM, environment.d and user systemd environment |
| Konsole | PlasmaBlur.profile default, animated text cursor, JetBrainsMono font 10 Catppuccin palette, opacity 0,85 and blur |
| Login | SDDM installed/selected, mocha-limine, color/source/cursor kit; starts to control login after restarting the computer |
| Lock | Native KDE adapted: Limine, clock, immediate form/60 s, hidden password media/revelation; uiVisible false + Qt.callLater preserved |

Historical Names `noctalia-teste.service`, `start-test.sh` and `outputs/noctalia-test/` were kept for compatibility between scripts; **do not indicate test mode**. The drive is now permanent. Names of menu entries and start messages no longer display “test”. Old recovery does not return the panels while autostart is enabled. Explicit return to Plasma remains available and disables the preference for the next logins.

### Accomplished sequence and destination adjustments

1. Kit copied to `$HOME/ricy-kit`; profile, status and original backups recovered; paths of the four `.desktop` recalculated. Not executed again `prepare-destination.py`, preserving the original backup.
2. Applied `contributions/target-implementation-fixes/apply-fixes.py`.
3. Installed via pacman `sddm 0.21.0-8` and `adw-gtk-theme 6.5-1`, with Xorg dependencies. The other components were already installed. Snapshots Snapper 15/16 were created by the transaction.
4. Executed `system.py` as root and `user.py --extensoes-kwin` as user. The WindowsArrows module was compiled with the headers/Qt/KWin of this destination; no old binary was imported. Applied wallpaper, `konsole-animated-cursor/apply.py` and `login-matched-lock-screen/apply.py`.
5. Updated only the local wallpaper preservation script with local IDs and the chosen Limine image; the original layout backup has not been modified.
6. Executed `noctalia-autostart/install-autostart.py`. Migration stopped the transit units, installed the permanent units, validated them and enabled/initiated integration. Effective profile: `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/config/noctalia/config.toml`.
7. Before selecting SDDM, captured the previous preference of the login manager. Executed `systemctl disable plasmalogin.service` and `systemctl enable sddm.service`, **without --now**. The link display-manager.service points to SDDM. The Plasma Login Manager process of the current session has been preserved; the precise computer reset.
8. Reinstalled Dolphin integration from the fixed kit and running the updated index wrapper. New fixture passed without installing test packages.
9. `adaptivepanelwidth` was installed by the extension option, but disabled in this destination: looking for missing Plasma panels and issued “panel update failed: missing”. WindowsArrows and smoothwindowgeometry were maintained; the concurrent maximum effect was downloaded. Flags/tails were also applied to the active instance via KWin/KGlobalAccel.
10. Prior SDDM revealed reference `config.logo` Undefined even with hidden logo. Added `logo=default-logo.svg` ed theme.conf installed and to the two copies of the asset in the kit. The logo remains hidden. Labels/messages of the permanent integration have been corrected in active templates and scripts.

To play in another destination, use the sequence of `REINSTALL.md`, preparing new backups on that computer. Recovery from the trash was specific to this installation and should not be copied as migration step.

### Verification carried out and limits

- `systemd-analyze --user verify` integration enabled, symlink in KDE target, `Result=success`, `ExecMainStatus=0`; shell/adapter/Plasma active. FragmentPath from shell points to the permanent home file. Restart of integration ended successfully.
- PID owner of `org.kde.krunner` coincides with the Adapter's MainPID; Query query opens search after migration. Meta/Meta+Space/Meta+V shortcuts maintained; Super+arrows registered in the KWin script. Plasma panels: zero. Both desktop images point to Limine installed.
- Bibat 16 applied by KDE tool; updated systemd environment. Fontconfig solves JetBrainsMono Nerd Font installed. Qt Menu: Kvantum, JetBrainsMono 10 pt, five lines 26 px and alpha zero in the corner.
- `konsole --list-profile-properties` recognizes AnimatingCursorEnabled; checked default profile and true property. Konsole has not already been opened, to preserve the work in progress; new windows carry the profile. There was no animation specific visual test.
- Prior to locking with `kscreenlocker_greet --testing --shell org.kde.plasma.desktop` carried the local QML: journal confirmed the Ricy message on both exits. The preview was closed by timeout; GetActive of the session remained false. 60000 no password was provided, no real unlocking was tested; the origin MAP functional test remains historical evidence, no new test in this destination.
- Previa SDDM offscreen/software executed as the sddm account: theme/QML have been loaded and a view has been created. Socket/backend warnings graphics are from the previous without real daemon/screen; the indefinite logo reference has been corrected. SDdm account has ownership of your private kdeglobals. There was no real login/authentication by SDDM or restart of the computer at this stage.
- Fixture DEB with the final converter passed in pacman, UID/GID zero and absence of namcap intermediates in tar/mtree; was not installed. Previous RPM/refusal scriptlets tests were not repeated.

### Backups and reversals

New backups of this destination:

- System/SDDM/assets: `/var/lib/ricy-appearance-backups/20261010-175757-266724/`.
- Appearance and User Extensions: `$HOME/.local/state/ricy-appearance-backups/20261010-175814-614754/`.
- Konsole: `$HOME/.local/state/ricy-konsole-backups/20261010-175817-074216/`.
- Block: `$HOME/.local/state/ricy-lockscreen-backups/20261010-175817-144082/`.
- Autostart/scripts: `$HOME/.local/state/ricy-inicio-automatico-backups/20261010-175834-898747/`.
- login manager selection: `/var/lib/ricy-display-manager-backups/20261010-xxc6JxxS/`.
- updated Dolphin integration: `$HOME/.local/state/cachyos-package-installer-backups/20261010-175846-254383/`; Previous initial backup also preserved.

To return to panels/tails and disable Noctalia at the next login:

```bash
"$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/return-to-plasma.sh"
```

To reactivate Noctalia:

```bash
systemctl --user enable ricy-noctalia-integracao.service
systemctl --user restart ricy-noctalia-integracao.service
```

Blocking, Konsole, appearance and system assets have the restorers and backups above as per `REINSTALL.md`. Full restoration of a file can replace later changes. To return Plasma Login Manager at the next restart, use `sudo systemctl disable sddm.service` followed by `sudo systemctl enable plasmalogin.service`, without --now within the current session. Packages are still installed. The previous wallpaper was the north pattern; it can be selected again by Plasma.


## Contribution — Cedilla on the international US keyboard — 2026-10-10  18:09 (America/Sao_Paulo)

After the user validated the visual implementation, he reported that the cedilla was missing in Konsole and Brave. The session confirmed a single active layout: English (US, alt. intl.), `us(alt-intl)`, inherited from the system configuration. `$HOME/.XCompose` nor layout configuration in kxkbrc. The Plasma/Konsole session uses LANG=en_US.UTF-8. The English composition table was reproduced locally: dead_acte+c/C produced ć/Ć.

Applied `$HOME/.XCompose`, including the locale table (`include "%L"`) and overwriting only dead_acute+c/C for ç/Ç. Physical layout and language have not been changed. Absence backup: `$HOME/.local/state/ricy-teclado-backups/20261010-180848-912053/`. User applications have not been closed; open processes can keep the previous table and need to be closed completely/reopened.

Added `contributions/keyboard-cedilla/` active and transport kits, with idempotent applicator, preservation of existing rules and reversal instructions. REINSTALL.md now includes step 3a. Original compressed files have not been regenerated; this correction is in the updated directories.

Validation: libxkbcommon confirmed in en_US.UTF-8, C.UTF-8 and pt_BR.UTF-8; á, ã, ê, apostrophe and dead_cedilla+c remained correct. Gtk.IMContextSimple confirmed ç/Ç, a and a window offscreen, without sending keys to user windows. Applicator syntax and second execution without changes checked. Physical typing in existing Konsole/Brave windows depends on user reloading and was not presented as a test performed. The separate SDDM account and the virtual console were not changed by this user setting.

## Contribution — Cedilla no Brave by XWayland — 2026-10-10  18:14 (America/Sao_Paulo)

The user confirmed ç in Konsole after the previous contribution, but Brave continued producing ć. The first correction did not cover the native Wayland route of Chromium. Local Brave: 155.1.97.56. The upstream code WaylandInputMethodContext uses CharacterComposer for events not consumed by the IME, with its own table.

Configured `$HOME/.config/brave-flags.conf` with `--ozone-platform=x11`. The Launcher `/usr/bin/brave` the package reads this file. Only the browser uses XWayland; the KDE session remains Wayland. .XCompose, layout, language, sandbox flags or personal profile. Absence backup: `$HOME/.local/state/ricy-teclado-backups/20261010-181356-714082/`. Brave must be completely reopened to load the option. On HiDPI screens, changing backend can change scale/rendering.

Added idempotent applicator `contributions/keyboard-cedilla/apply-brave.py` to both kits. README, resettlement script and SHA256SUMS updated. Historical compressed archives continue without this update.

Functional test: Brave instance with temporary profile on separate nested XWayland server, local HTML field and XTest input only on this display. The X11 option alone (without forcing GTK without IM variables) produced `ççÇ`. The first round with explicit GTK also passed; these extra options were not included in the definitive setting. Isolated instances were closed; test logs/files remain in /tmp/ricy-brave-validation-*. Second execution of the applicator did not change the file. No input was sent to the user's windows or used its profile in the test.

## Contribution — USB AIC8800 Driver for Wi-Fi and Bluetooth — 2026-10-10  18:25 (America/Sao_Paulo)

User request: Install the Wi-Fi/Bluetooth AIC8800 adapter driver. Local identification before installation: USB `a69c:8800` (AIC Wlan), door 1-14, no network driver/interface. Kernel active 7.2.9-2-cachyos with Clang; LTS 6.18.55-2-cachyos-lts also installed, compiled with GCC. Both had matching headers. Secure Boot was disabled. Existing Ethernet was preserved; no network/password was configured.

Installed `dkms 3.4.3-1` and local package `aic8800-usb-dkms-ricy 5.0.20260123.9-3`. Radxa primary source: https://github.com/radxa-pkg/aic8800, commit `d13d07963cd15d731e2895e8288a04cca6152ac9`, source file verified by SHA256. The preparation normalizes CRLF and applies the series of upstream patches, including compatibility of new kernels and use of BlueZ. Only USB drivers/firmware were packaged; no Android library was installed.

Modules: `aic_load_fw`, `aic8800_fdrv`, `aic_btusb`. Firmware: `/usr/lib/firmware/aic8800_fw/USB`. DKMS chooses Clang/GCC by reading the configuration of each kernel and recompiles the updates with available headers. The first DKMS compilation of the LTS used fixed Clang and failed; corrected the kernel selection. Both passed after correction. The final version records the Bluetooth driver before loading the firmware and gives priority to aic_btusb when btusb is requested. The circular reference between aic_load_fw and aic8800_fdrv was removed: the latter already has native dependence of the first. btusb was not globally blocked.

After charging the firmware, the device went to `a69c:8801`, with two Wireless interfaces linked to aic_btusb and a Specific Vendor linked to aic8800_fdrv. NetworkManager recognized wlan0 and p2p-dev-wlan0. RFKill without locks. Searches found 9–13 Wi-Fi networks. BlueZ created hci0, Powered=yes; Bluetooth discovery started without error and was closed after the test. No devices have appeared in this search window. Bluetooth service was already enabled before; it has been started and is active.

Final verification: DKMS installed for 7.2.9-2-cachyos and 6.18.55-2-cachyos-lts; correct vermagic on both. Functional test performed only on active kernel 7.2; there was no boot in the LTS, Wi-Fi connection or matching. The upstream driver emits build/debug warnings, preserved in the logs; builds ended successfully. The pacman transactions generated snapshots Snapper by the already existing hook and rebuilt the initramfs by Limine/mkinitcpio. There was no computer restart or Ethernet interruption.

Reproduction: `contributions/driver-aic8800/README.md` in the active and transport kit, with PKGBUILD, dkms.conf, build.sh and modprobe configuration. REINSTALL.md gained optional step 6a. SHA256SUMS updated/verified in both copies. Historical compressed files have not been regenerated. Downloaded fonts and compilations stay in local cache without credentials. Logs and previous inventory: `$HOME/.local/state/ricy-aic8800/`.

Revert: `sudo pacman -R aic8800-usb-dkms-ricy`; DKMS removes modules on disk. Reconnect the adapter or restart to close modules still loaded. DKMS/BlueZ can be maintained for other devices; the previous status of the Bluetooth service was enabled and inactive.

## Contribution — Search by the bar magnifying glass — 2026-10-10  18:34 (America/Sao_Paulo)

The user asked Search Applications opened by the magnifying glass to appear in the corner, following the behavior of the Noctalia control on the right. Activated `shell.panel.open_near_click_launcher = true`. The launcher remains attached/auto: the click on the magnifying glass positions the search next to the widget on the left side of the bar. The equivalent control-center option was already true. The keyboard wrappers and the top search_edge bar have been preserved.

Updated the active profile and the config.toml of noctalia-kde-integration-and-menus contribution outputs in active and transport kits. Backup: `$HOME/.local/state/ricy-busca-backups/20261010-183355-074732/`Executed `noctalia config validate` (valid) and `noctalia msg config-reload` (ok). Effective export confirmed true, attached and auto. The shell remained active with the same PID 1218, without restarting or closing child applications. The already open panel may require closing/reopening by magnifying glass to reposition; there was no automated click or visual capture of the new geometry. REINSTALL.md and hashes of config.toml They've been updated.

Reference: [official configuration of Noctalia panels](https://github.com/noctalia-dev/noctalia/blob/main/docs/user/configuration/shell.mdx).

## Contribution — Compact and rounded search upper bar — 2026-10-10  18:37 (America/Sao_Paulo)

After validating the opening next to the magnifying glass, the user asked for a narrower and rounded top bar for the open search for Super/digitation. `[bar.search_edge]`:Thickness 16, margin_ends 640, margin_edge 8, radius and the four radii 8. Remain opacity 0,70, blur, no shade, no space reserve and no auto-hide. The revelation and concealment continue under the existing adapter/wrapper. The bottom magnifying glass continues with open_near_click_launcher=true.

The two current monitors have logical width 1920; the resulting bar measures 640 px, centralized, about 40 px beyond the launcher of 560 px per side. The top is the 8 px edge. In other resolutions, recalcule margin_ends like `(largura lógica - largura desejada) / 2`; for different scales/resolutions, use overrides per monitor. REINSTALL.md.

Updated active profile and two templates of config.toml. Backup: `$HOME/.local/state/ricy-busca-backups/20261010-183630-034925/`Noctalia validation passed and config-reload returned ok; shell remained in PID 1218. Search reopened by the D-Bus interface used by shortcuts. Visual capture checked reduced width, union with panel and rounded corners. The check panel was closed upon completion. Temporary local captures were not included in the kit. Updated SHA256 Manifestos.

## Contribution — Search bar only on active monitor — 2026-10-10  18:40 (America/Sao_Paulo)

The user validated the compact look, but the bar appeared on both screens while the launcher opened in one. The adapter now query `org.kde.KWin.activeOutputName`, the same reference used by Noctalia/KDE to resolve the opening monitor. Before revealing the launcher, collect the search_edge bar on all screens and run `bar-show search_edge NOME` for only the active connector. When closing the search, collect the bar as before.

`open-menu.sh` now calls toggleDisplay of the same D-Bus adapter; this unifies Super/Super+Space and typing without duplicating the choice of monitor. No DP/HDMI name has been fixed in scripts. 640 px, rounding, lower magnifying glass behavior and opening next to click. Query/command failures return D-Bus error and try to collect the bar.

Backups from the two previous scripts: `$HOME/.local/state/ricy-busca-backups/20261010-183834-044045/`. Updated active/transport copies, REINSTALL.md and SHA256SUMS. Restarted only noctalia-busca-desktop.service, preserving the shell and its children applications; MainPID of shell continued 1218.

Check: Python/Bash valid. D-Bus display opening in DP-1 visually confirmed with the bar only on this screen. Open by Super wrapper on HDMI-A-1 also checked: bar and launcher only on the correct screen. The focus was alternated by the actions KWin Switch to Screen for the test, waiting for its application; on completion, closed panel and focus returned to DP-1. There was no automated click on the magnifying glass or change in window geometry.

## Contribution — Continuous notifications with the taskbar — 2026-10-10  18:55 (America/Sao_Paulo)

Work: notifications in the lower right corner with time bar and visual union with the taskbar. After the previous, the user explicitly asked to remove the rounded cut from the lower right edge. The result applied keeps the other three corners rounded and makes this edge reach the taskbar.

In the active profile in `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/config/noctalia/config.toml` and in the templates `outputs/noctalia-test/config.toml` of the two kits, `[notification]` passed position="bottom_right", follow_focused_output=true, background_opacity=0.70, border=false, offset_x=0 and offset_y=0. The notification follows the active monitor and the same transparency of the taskbar. Mauve progress bar and expiration are already native to Noctalia; no other daemon has been created. Persistent notifications maintain native behavior.

The Noctalia 5.2.1 does not offer individual radius preference for this card. `src/shell/notification/notification_toast.cpp` to use zero radius only in the bottom right corner when bottom_right and offset_y=0. Background and blur region use the same four radii. This state replaces the historical premise of using only settings without recompiling Noctalia: now there is a small local adaptation on the v5 commit.2.1  `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`.

Installed in this meson destination 1.12.1-2, ninja 1.13.2-3.1, wayland-protocols 1.49-1, nlohmann-json 3.12.0-2 and stb (20260415), in addition to python-tqdm dependence 4.70.1-1. Installing by repositories was completed with local authentication; hooks created snapshots Snapper 41/42. Compilation release Meson/C++23 and Ninja completed without errors. Sources/build in `$HOME/.cache/ricy-noctalia-src-5.2.1/`, out of portable materials.

The binary selected by the shell is `$HOME/.local/lib/ricy-noctalia/noctalia`, by `~/.config/systemd/user/noctalia-teste.service.d/50-notificacoes-ricy.conf`. `/usr/bin/noctalia` and the original package remain installed. The prefix /usr from the compilation serves to locate the existing assets; it was not executed meson install. The shell and adapter were restarted with KillMode=temporary process to preserve the applications released by the menu, including the Codex used in this work; the temporary override was removed and the drive returned to KillMode=control-group. Shell and adapter are active.

Materials included in active and transport kits: `contributions/notification-continuity/README.md`, `build.sh`, `enable.py`, `notification-right-corner.patch` and MIT upstream license. `REINSTALL.md` won step 4a. To play, follow README: prepare first the permanent integration, install the dependencies, run `bash build.sh` and `python enable.py`. The compiler requires compatible version/commit and refuses unknown font changes. The local executable does not follow package updates alone: review/rebase and recompile the patch when changing version, or restore the original selection before using other Noctalia asset.

Executed check: Python/Bash syntax, git diff --check, native compilation and new compiler execution on the existing build passed. Notification captures in HDMI-A-1 confirmed the union of the lower right corner and the lower time bar between the beginning and the middle. 8000 ms received NotificationClosed with reaction=1 lon 8,0 seconds; later capture confirmed its disappearance. The visual and expiration test was in this installation, not in another computer. The pause when passing the pointer was checked in the native code, without separate interaction test.

Local backups, not included in the kit: `$HOME/.local/state/ricy-notificacoes-backups/20261010-184413-289100/config.toml` contains the previous configuration; activation kept its state in `20261010-185312-672533/manifest.json` in the same base directory. To undo binary selection use `python enable.py --restaurar CAMINHO_DO_BACKUP` to undo the preferences, restore the config.toml previous or only adjust `[notification]`; binary restoration does not remove packages or those preferences.

SHA256SUMS updated and verified in both copies preserving their entries. Historical ZIP/tar files have not been regenerated. No clipboard history, private status or screenshot has been included in the materials.

## Contribution — Curved joining of the lower left corner of the notification — 2026-10-10  18:59 (America/Sao_Paulo)

The user corrected the previous result: removing only the right lower radius did not solve the visual connection, because the lower left corner was still rounded into the card. The local variant was adjusted again: now this corner opens out with a concave curve, following the native geometry of the embedded panels, and finds the upper edge of the taskbar. The lower right corner continues straight; the top two are rounded. This contribution replaces the previous description of keeping three rounded corners. Position preferences, monitor, opacity and deadline continue those documented in the previous contribution.

The patch in `src/shell/notification/notification_toast.cpp` now reserve a left extension on the surface and in the animation clipping area, preserving the content width and alignment to the right. Background and blur use CornerShape::Concave in the lower left corner and the same side insert. Special geometry applies only in bottom_right with offset_x=0 and offset_y=0; other positions/leaves maintain the native format. The daemon function or time count has not been changed.

Incremental compilation Ninja completed without errors and git diff --check passed. Run again `python enable.py`; the shell uses the corrected local binary. Backup of this exchange in `$HOME/.local/state/ricy-notificacoes-backups/20261010-185903-989917/`. This backup restores the previous variant with just the right corner; the backup of the first activation restores the selection of the original package. The exchange used the temporary application preservation override; at the end, shell and active adapter and KillMode=control-group restored.

Visual capture in PD-1 confirmed the curve extension to the left until the taskbar, with the card aligned to the right edge. Repeated the D-Bus test of 8000 ms: NotificationClosed reaction=1 lon 8,0 seconds, with less progress in intermediate capture and absence of card in later capture. There was no new hover test, other positions or installation on another machine.

Patch and README Updated at `contributions/notification-continuity/` in active and transport copies, step 4a of REINSTALL.md and the two SHA256SUMS (423 verified entries). To play/revert, the script commands and version update precautions described in README remain. Captures and backups remain local; historical compressed files have not been changed.

## Contribution — Continuity of the blur between bars and panels — 2026-10-10  19:20 (America/Sao_Paulo)

Corrected the continuity of the background blurred between taskbar, notifications, search by the magnifying glass, Noctalia menu and top support of the search for Super or typing. Equalizing opacity and corners did not eliminate the amendment: the native blur sampled a different rectangle for each surface.

Separate effect compiled `ricyblur`, based on the official KWin code 6.7.5, commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`. While a panel or Noctalia warning is visible, its surfaces use the same filtered background by monitor, cut by the shapes of each window. The background copy is made before drawing Noctalia, without including the bar itself. The OpenGL clipping is preserved in the final composition and does not limit the copy or shared filter. Other applications follow the native algorithm. Also applied `panel_overlap = 0` ed `[bar.default]` and `[bar.search_edge]`, in the active profile and in the two public templates, removing the range of a pixel with duplicated transparency at the junction. 0,70, the compact bar and the choice of monitor remain preserved.

The new plugin has been installed in `/usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so`, keeping the original KWin files. Helper `$HOME/.local/lib/ricy-blur/start.py` and the unit `ricy-blur-continuidade.service`, enabled in the graphical session, select the effect only in KWin 6.7.5 when supported. The native blur remains enabled in the configuration and is maintained/reloaded if the variant cannot be used. The compositor and the main shell were not restarted in this exchange.

Public material in Mexico - AmarillasLatinas.net `contributions/blur-continuity/`: README, GPL-license2.0-or-later, patch and scripts `build.py`, `integrate.py`, `start.py`. The compiler fixed version and commit, refuses unknown changes in source and recompiles in destination; we did not distribute the binary of this machine. Official Vulkan headers were used 1.4.363 cache, commit `6802bb4733b63ed5efd3adb308a6c885ef180ea1`, without installing new packages in this work. The reinstallation script uses the target vulkan-headers package. Please refer to README and 4b step of REINSTALL.md to play or return to native blur; future versions of KWin require patch revision/recompilation.

Executed verification: final compilation reproduced by the kit script, patch without whitespace errors and Python syntax checked. Visual test in KWin/Noctalia isolated with color track background checked the continuity between embedded menu and bar; the test session was closed upon completion. In the main session, loaded ricyblur effect, active/habilitated unit and validated/reloaded Noctalia configuration; opened the upper search and verified its support on the corresponding monitor. The user confirmed: “Visually passed”. There was no new hover test or notification expiration in this contribution; the term tests are in the previous record. The main compositor journal did not record framebuffer errors since the application of the final variant.

Limits: different scales, reinstallation on another machine and consumption with video/animations were not measured. With open panel/warning, changed frames repaint the monitor to avoid reusing pixels containing the bar; this can increase the cost of composition. There is no continuous repainting loop when the scene is stopped, nor recording the disk background by effect.

Private backups in `$HOME/.local/state/ricy-blur-backups/`: integrator `20261010-191516/` and previous profile in `20261010-191527/config.toml`. Restore native blur does not reverse panel_overlap; use backup or only adjust this preference. Active and portable copies have been synchronized, with all checked hashes and previous preserved entries (429 archives in each SHA256SUMS). Captures, caches, profiles/clipboard and backups have not been included. Historical ZIP/tars continue as previous portraits; to transport this correction, copy the updated public folder with this record and script.

## Contribution — Wallpaper on the home card of the actual session — 2026-10-10  19:24 (America/Sao_Paulo)

The user pointed out that the actual session did not show wallpaper in the menu. The isolated test had active Noctalia wallpaper service; in the main session it is disabled because Plasma manages the desktop. No surface/texture of Noctalia wallpaper, HomeTab received currentPath empty and showed solid color.

The local variant Noctalia 5.2.1 now query getDefaultWallpaperPath on Home card when currentPath is empty and the Noctalia wallpaper is disabled. The image is loaded by native thumbnail, keeping Plasma responsible for the desktop. The change is in src/shell/control_center/tabs/home_tab.cpp, included in the patch composed of contributions/notification-continuity; the geometry of notifications and the ricyblur effect remain applied. The card displays the image; the rest of the menu remains translucent with blur content behind it, without applying artificial wallpaper to the entire panel.

Added sync-wallpaper.py: reads the static image by Plasma API, validates existence and equality between desktops and records the path via IPC wallpaper-set. On this machine, both use /usr/local/share/ricy/limine-splash.png. We do not enable [wallpaper] in Noctalia. Synchronizer does not follow future changes automatically: run it again after changing the background in Plasma. Different/animate backgrounds require another integration and are refused without changing preferences for the script.

Verification: Ninja compiled binary; build.sh accepted compound patch; git diff --check and syntax Python/Bash passed. Engagement with preservation of completed applications, KillMode=reestablished control-group and ricyblur still loaded. Open home control-center in the main session; capture confirmed the Limine image on the card compared to desktop file. Closed menu at the end. No new notification test or migration to another machine was done.

Backup of previous binary in $HOME/.local/state/ricy-notificacoes-backups/20261010-192258-920118/; restores the previous executable with corrected notifications and solid card. The first syncer pointed the backup to config/settings.toml instead of state/settings.toml: 20261010-192254-917307 DOES NOT contain backup of the original state and its manifest was marked as invalid for restoration. Fixed the path in the distributed script. $HOME/.local/state/ricy-menu-wallpaper-backups/20261010-192326-080532/ saves the already synchronized state before the second idempotent execution; should not be presented as copy prior to the first change. The standard path Noctalia observed before was /usr/share/noctalia/assets/noctalia-wallpaper.png.

Patch, README and synchroniser updated on the two copies of the kit; step 4 of REINSTALL.md updated and 430 hashes checked on each manifest, preserving the previous entries. No capture, personal image, state or backup was included; historical compacted remain unchanged.

## Contribution — English dates, weather and events in Cosmópolis/SP — 2026-10-10  19:28 (America/Sao_Paulo)

Attended the request for dates in English keeping Cosmópolis/SP-BR as location. The Noctalia process inherited LC_TIME=pt_BR.UTF-8, despite the interface in English. Applied shell.lang="en" and drop-in 60-ricy-idioma-localizacao.conf with LC_TIME=en_US.UTF-8, TZ=America/Sao_Paulo and UnsetEnvironment=LC_ALL. Global locale, regional units and keyboard composition have not been changed.

Fixed location: auto_locate=false and address="Cosmopolis, Sao Paulo, Brazil". The full address was validated in the API used by Noctalia: latitude -22.64583, longitude -47.19611, name Cosmópolis, Brazil. Consult only Cosmópolis returned a homonymous city in the USA; this result was not applied. Weather enabled in metric units and calendar/events enabled. The user chose only to enable events for the time being: no account or source of events/seasons has been added. The calendar uses the session time zone; the location itself does not provide personal events or holidays.

New contribution contributions/noctalia-language-and-localization with apply.py and README. The applicator adjusts the same keys in the profile and in settings.toml, because there was a private override auto_locate=true; preserves other preferences and accounts. Install the drop-in and use the existing application preservation helper to restart shell/adapter. The local executable was not changed at this stage. Public templates of the two copies also updated; apply.py is required to install LC_TIME/TZ in the drive and fix destination overrides.

Verification performed: Noctalia config validation passed; process environment confirmed LC_TIME=en_US.UTF-8 and TZ=America/Sao_Paulo without LC_ALL. Calendar in the real session exhibited Saturday and October; event card enabled without connected accounts. Native Cache confirmed Brazilian location and forecast with timezone America/Sao_Paulo, offset -10800 and seven days available. ToML comparison with backup confirmed that unrelated preferences were preserved. ricyblur remained loaded; KillMode pattern restored. No account synchronization or installation on another machine were tested.

Previous private backup in $HOME/.local/state/ricy-idioma-localizacao-backups/20261010-192713-914138/. The manifest indicates previous presence of config/settings/drop-in. Please refer to README for reversal and preservation of subsequent changes; private data and captures were not included in the kit. REINSTALL.md and both synchronized copies, with 432 Hashes conferred on each manifesto. Historical compacted remain unchanged.

## Contribution — Visual identity Noctalia as a system reference — 2026-10-10  19:35 (America/Sao_Paulo)

The user asked to register the visual identity of Noctalia and incorporate it to the Ricy to guide the adequacy of other parts of the system. VISUAL-IDENTITY.md as current guide, with link at the beginning of this record and the resettlement script.The next visual adjustments should consult this reference and document adaptations and results in the actual component.This contribution records the approved basis; it does not apply new themes to the system.

The reference captures KDE-Actual palette/Catppuccin Mocha with Mauve accent, background #181825, cards #313244, text #cdd6f4/#a6adc8, contours #46485c, hover #977dba and semantic colors. Defines materials with fill alpha 0,70 for bars, notifications and panels that inherit the bar, preserving readable text and solid cards. 1, and opaque Kvantum menus: not widespread transparency for the whole system.

Registered current corners and junctions: taskbar 44 px with superiors 6 px and lower rectum; upper support 640 × 16 px, radius 8 px and upper margin 8 px; notification with lower left concave corner out and right; bar.panel_overlap=0 and shared background ricyblur by monitor. Noto Sans shell font; KDE/GTK JetBrainsMono Nerd Font 10, with distinction between points and logical pixels. Rays, spacings, paddings and native durations were extracted from the code constants 5.2.1 and marked as reference, not measuring all components. 1,3 is distinct from the explicit radii of the bar.

Public materials in contributions/noctalia-visual-identity: README.md (guide) tokens.json (structured, non-executable values/papers) and reference.svg (vectorial drawing without personal data). README was also published in Documents/ricy/VISUAL-IDENTITY.md for direct access. The board illustrates colors, cards, source and junction with alpha in a common form; it is not a real capture nor simulates the OpenGL filter. Archives allow other agents to use the same parameters in the next works.

Executed validation: active palette and public template compared byte to byte; verified pertinent visual overrides without copying private settings; Style reads, transparency/radius rules in KDE code and preferences, Kvantum, GTK and Plasma current. JSON and SVG analyzed; JSON colors checked against palette; SVG rendered and inspected visually. Ricyblur effect confirmed loaded. No application, service or preference was changed/restarted.

The guide differentiates current reference and future work: Qt/KDE is part of active integration; GTK and third party applications are not declared fully harmonized; login/blocking have its own record and have not been revalidated here. English dates, São Paulo time zone and Cosmópolis region remain preserved. Applying language to new areas will require changes and validation of their own; this contribution does not present these adaptations as completed. Reversal here is only documentary, preserving the history; future adjustments should save their backups and record reversion by component.

Synchronized the three materials in active and portable copies. SHA256SUMS of both preserves the 432 previous entries and adds three (435 The documents outside the kit are not part of this manifest, as existing structure. Not included captures, clipboard, profiles, backups or source/build complete; historical compressed have not been modified. To transport, copy also VISUAL-IDENTITY.md next to ricy.md, REINSTALL.md and current kit.

## Contribution — Application menu as Noctalia composition — 2026-10-10  19:44 (America/Sao_Paulo)

The user asked for the right button options in a taskbar application to appear in the Noctalia composition, such as tray. The independent XDG popup was replaced by an embedded native Panel, id ricy:taskbar-menu, managed by the same PanelManager from the tray drawer. The opening uses the anchor bar callback at the center of the icon, keeping source bar/monitor. Herda opacity, blur, junction and native animation. Internal apps menus have not been changed.

The list and its original handlers have been preserved: Pin/Unpin, desktop actions entry, Close and Close All, as per the application/windows available. Callbacks use widget life guard weak; activation/opening postponed until the end of the event. Included arrows and Enter/Space to navigate/activate; Escape and external click are in charge of PanelManager. Removed your own popup and your event intercept in the taskbar.

The user saw the first composition and pointed out that the height generated scrolling. Identified duplicate padding: PanelManager already discounted the native margin. Fixed layout and removed ScrollView; height calculated by all inputs, separators and padding, without limit of 12 lines. Width calculated by broader text, minimum content 240 px at scale 1This replaces the fixed minimum width popup and the first rollable composition.

New contribution contributions/taskbar-menu-composition with README, build.sh, patch compound noctalia-ricy.patch and MIT license. Patch applies on commit Noctalia 5.2.1 Known and maintains previous notification and wallpaper corrections of Home. The compiler of this directory is the reference to reconstruct the current full state; the previous refuses this cache with different changes. README guides to preserve the previous source and use clean cache when migrating variant, without overwriting unknown changes. Updated step 4a, identity/tokens guide and note of the previous contribution to point to the composite compiler.

Verification performed: final compilation Ninja by contribution script, git diff --check, bash -n and Noctalia config validate passed. SHA of the active executable corresponds to the final build: 8fa83842d58d1d1ceedd791defb9a82169f7cfa96ac1065f94ed14a861d24a26. Active Shell/adapter, KillMode=reestablished control-group and loaded ricyblur. The user's capture proved the initial composition, still with scroll. No visual confirmation of the final adjustment without scroll was recorded, test of the actions in disposable application, very extensive lists, side/superior bars or migration to another machine. The attempt to automate a click did not open the target menu; no result of this attempt was used as validation. The temporary input and script device was closed.

Private backups in $HOME/.local/state/ricy-notificacoes-backups/: 20261010-193948-522126 restores the previous variant with popup and previous fixes; 20261010-194151-517805 restores the first composition with scroll. Use enable.py  --restaurar according to README, preserving applications. The exchange does not modify language, wallpaper or climate preferences.

Synchronized four public archives on active and portable copies; both manifestos preserve previous entries and have 439 Hashes checked. Captures, test devices/scripts, binaries and private state have not been included. Historical compacted remain unchanged.

## Contribution — Tray options in composition Noctalia and return to drawer — 2026-10-10  19:56 (America/Sao_Paulo)

The user requested the same composition of the application menu for the tray items options. Replaced the independent popup by native embedded panel ricy:tray-menu, preserving DBusMenu as the source of options and actions. Keep Pin/Unpin, separators, disabled entries, checkmarks, radio and submenus. Inherit bar opacity, shared blur, merge drawing, animation, monitor/bar and external closing of PanelManager. Items that do not expose DBusMenu continue to present the application's own menu.

Width follows the largest text (minimum content) 240 px at scale 1). The height considers all native inputs and margins, without duplicate padding or artificial line limit. ScrollView only shows scrolling if the list exceeds the available area. Submenus navigate within the same composition, with return line and left/Escape to rise a level. At the root Escape closes. Opened/closed events, updates and loading on demand remain connected to the provider; retry limited to 300/900/2000 ms. Delayed actions check the current line and the generation/life of the menu before acting. Remove the item closes the menu. A public rectangle query in PanelManager translates the click in the drawer to monitor coordinates before opening the replacement menu.

The user confirmed: “Passed and got good”, asking for a arrow between menu and tray to return to the drawer. Added native Ghost button at the base of the menu, chevron-down in the bottom bar; 32 px and interval 4 px at scale 1. Allows you to return directly to the drawer in the same monitor/bar/anchore, including from submenus. The button participates in the native Tab/Enter. The user confirmed “Passed” after activation of the arrow: both steps passed visually.

New contribution contributions/tray-menu-composition with README, compiler, full patch and MIT license. Patch matches commit Noctalia 5.2.1 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 and includes previous notifications changes, Home wallpaper and Taskbar menu. This is the reference compiler to play the current variant. Previous compilers/patches remain historical and refuse cache with different changes; preserve the previous font and use clean cache while migrating as the README. Updated resettlement, visual identity and tokens, previous contributions notes, active kit and portable copy. Language/climate preferences and accounts have not been changed.

Checks: final compilation Ninja by contribution script, git diff --check, bash -n and profile validation passed. Active and build executable coincide, SHA256 cf9ee62d8a0cb359a9a2775eb4ccc5d90d08c3d45833967cc0fd1c8c56b95ada. Active Shell/adapter, KillModel=reestablished control-group and loaded ricyblur effect. Visual confirmation of registered user to menu and set. No full test of actions, submenus, extensive lists, sidebars/superiors or other machine was recorded and removed; attempt to click on it automatically did not open its menu and was not used as validation. Input devices, KWin script and temporary device preferences were removed. No actual update/closure action was triggered as test.

Private backups in $HOME/.local/state/ricy-notificacoes-backups/: 20261010-195150-527306 restores the previous variant with taskbar menu; 20261010-195539-054921 restores the trace composition without the arrow. The previous activator/restaurator remains responsible for the safe binary/drop-in exchange, preserving applications and the package /usr/bin/noctalia.

Both manifestos preserve previous entries and have 443 hashes checked. No binaries, accounts, private status, catches or clipboard material in the kit. Historical compacts remain unchanged.

## Adjustment — Alignment of the menu and return to the tray drawer — 2026-10-10  20:01 (America/Sao_Paulo)

The user pointed out that the drawer changed position when returning by the bottom button of the menu; he wanted the arrows in the same horizontal position. The previous reference was the position of the click on the item (with conversion of coordinates of the surface). Altered TrayMenu::toggleForItem: when opening through the drawer, the reference is the real center of the rectangle of the drawer in coordinates of the monitor, regardless of the item clicked. Menu, its submenus/resizings and return use this reference.

In the arrow layout, the horizontal coordinate is designed from this fixed axis to the panel content, discounting the actual position and native padding. This also preserves alignment when a wider menu needs to be limited by the monitor edge: the arrow accompanies the drawer axis, not the center of the dislocated menu. The button remains inside the panel body. Actions, appearance, duration, monitor or source of options have not been changed.

Final compilation Ninja/play script, git diff --check, bash-n and config validate passed. 45 geometric scenarios of drawers/menus with different widths and central/close positions of the edges: center of return and arrow maintain the axis, tolerance of half pixels by rounding. These calculations do not replace an automated graphical test. The user confirmed “passed” after activation: alignment visually validated in the real session. Active binar corresponds to build, SHA256 ad70b2ffdb54dcedef8a23bb9b27cf5a0b9230cc29fed26bfbcf577e2a0ee0c0. Shell/adapter active, KillMode=control-group and loaded ricyblur. No tests of actions, extensive lists, sidebars or other machines were expanded.

Private backup prior to exchange: $HOME/.local/state/ricy-notificacoes-backups/20261010-200022-501476. It can be restored by the existing activator; it returns to the composition with set before alignment correction, preserving applications. Updated the patch composed of tray-menu-composition, README, tokens/identity and reinstallation. Active and portable kit synchronized, 443 hashes conferred on each manifest; previous entries preserved. No capture, binary or private state was included; historical compacted remain unchanged.

## Contribution — Smaller icons and hover for apps and search — 2026-10-10  20:07 (America/Sao_Paulo)

User request: reduce the application icons a bit and animate them in the hover, including search, without reaching tray/options, volume, time, network or Noctalia button. Implemented only in TaskbarWidget and LauncherWidget: the drawing is scaled 0,88 at rest and grows to 1,0 in the hover, returning to 0,88 on exit. Input/output 140 ms, EaseOutCubic, with native AnimationManager and respect for motion/speed preferences. The hover inversion cancels the previous animation and continues from the current progress.

Transformed only image/glyph nodes from the icon without changing layout measure or click area. Maintained spacing, titles, indicators, badges and original interaction (activate, switch, close, menu and drag). Includes images, apps fallback and glyph/image of the magnifying glass. The existing background highlight of the apps tiles follows the transition from 140 ms; other taskbar elements keep their previous hover. Volume, watch, network, tray, track menus and control-center have not been changed. No color, font or private preferences have been modified. Code application ensures variant reproduction, without depending on a manual adjustment of the active profile.

New contribution contributions/app-icon-interactions: README, build.sh, patch complete noctalia-ricy.patch and MIT license. Noctalia patch 5.2.1 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 maintains previous notifications corrections, Home wallpaper, Taskbar menu, and Tray menu/return/alignment. This compiler is the current reference; the previous ones remain historical and refuse cache with different diff. Preserve the previous font and use clean cache while migrating as README. Updated resettlement, visual guide and tokens, with explicit deletions of effect. No binary has been placed in the kit.

Checks: final compilation Ninja/play script, git diff --check, bash -n and config validate passed. Comparing the blocks of the complete patch with the previous variant: additional changes restricted to the two widgets; all other previous blocks remain the same. Active and build binar coincide, SHA256 b30d5efc4461d0eea3e82c2001d05bbc32fe79fc3e5770ee152ce1af4b694fb. Active Shell/adapter, KillModel=reestablished control-group and loaded ricyblur. No visual confirmation of the user recorded in this setting, nor click/screw tests, fast hover, disabled movement, varied scales or other machine. Scope/compilation verification does not replace these visual and interaction tests.

Private backup before exchange: $HOME/.local/state/ricy-notificacoes-backups/20261010-200612-039983. Restoreable by the previous activator, returns to the variant with tray alignment without reduction/boom of icons, preserving applications. Active and portable kit synchronized: 447 hashes checked on each manifest, previous entries preserved. No clipboard, captures, accounts, private status or backups in the kit; historical compressed remain unchanged.

## Contribution — Icon actions: restore, minimize and close — 2026-10-10  20:18 (America/Sao_Paulo)

The user clarified that “opening minimized” means restoring the window by the icon and confirmed the previous implementation with “Passou”. This variant explicitly restored in KDE/KWin, preserved the existing middle-click to request closing and selected the exact identity by UUID to not activate/close another window of the same title. Confirmation is from that previous state, whose binary was SHA256 1b32307c4bfd041a0eb62f329ff4cab57a70f511798380d8d94ec5e9ecaa79.

New request: Windows behavior, restoring minimized and minimizing opened by the icon. Implemented left click: minimized window restores and gets focus; focus visible window minimizes, if minimized; inactive visible window comes forward. Fixed application without window continues to start. In groups, the active window is prioritized to minimize; without active in the group, the existing selection/cycle chooses the window to restore/focus. Do not play previews or selector of Windows groups. Middle-click asks to close an active/representative window, preserving save dialogs; no window ignores. Right-click and drag maintain previous menus/orders.

Only the left-click of the taskbar sends toggleMinimize; the script reads the current state in KWin, without relying on old tile flags. Search activation, dock, shortcuts and other callers restore/focus, without minimizing. Implementation of KDE/KWin specific alternation; other compositors maintain original activation. Exact UUID with fallback class/caption only without UUID; obsolete UUID does not trigger another window. Close callsWindow and does not use minimize as fallback.

New contribution contributions/taskbar-app-actions with README, build.sh, patch complete noctalia-ricy.patch, LICENSE and validate-actions.py. Current reference to compile Noctalia 5.2.1, commit 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4. Fixed TaskbarWidget, ComposerPlatform and KwinActiveWindow, with their headers; compared the blocks with app-icon-interactions, all other previous blocks are the same. Preserved icons/hover, notifications/wallpaper, menus, junctions and track. Updated reinstallation, guide and interaction tokens, warning in the previous variant.

Checks: 17 tests perform real JS extracted from the source in QJSEngine, including equal identity/titles, obsolete UUID, restoration, alternation, inactive/non-minimizable window, common activation and closing. In the actual session, disposable Qt window was minimized and corrected scripts restored/focused, minimized, restored again and preserved visibility in the common activation; then requested UUID closure. Minimization/focus states conferred directly on KWin, as client Qt state does not follow up reliably external minimization. Synchronous sequence checks the adapter, without simulating physical clicks or covering all applications/groups. Initial attempts with Qt/timers queries had inconsistent measurements; final KWin state verification passed. No working window was closed; temporary DBus scripts and object removed. The new alternation has not yet received user confirmation. --check, reverse patch application and config validate passed.

Active binary/build match, SHA256 fcfc99017bc29cdf3c93742dfc5463ea62c01e07666666baebbeb610da7a08a6. Active Shell/adapter, KillMode=reestablished control-group, ricyblur loaded. Private backup before this exchange: $HOME/.local/state/ricy-notificacoes-backups/20261010-201748-372725; returns to the approved restore/close variant, preserving applications. Private backup of the previous deployment: $HOME/.local/state/ricy-notificacoes-backups/20261010-201242-075546; returns to the icon/hover variant without action corrections.

Synchronized active and portable kit: 452 hashes conferred on each manifest, 447 Preserved entries and five new ones added. No binaries, clipboard, captures, accounts, private status, Python bytecode or backups in the kit. Historical compacts remain unchanged.

## Contribution — Purple ball by state and animation of shares — 2026-10-10  20:28 (America/Sao_Paulo)

User confirmed “It’s working” for the variant restore/minimize by icon and close with middle-click. He asked the purple ball to react and add animations. Implemented four states in the indicator: activate opacity/scale 1/1; open inactive 0,55/0,82; minimized 0,28/0,65; fixed without window 0/0,55. Transition 160 ms EaseOutCubic, Native AnimationManager, respecting shell preferences. Part of the current visual value and preserves snapshots by identity between reconstructions; this allows erasing the indicator of a closed fix. Unfixed icon disappears when closing the last window. Same rule in line when titles are visible. Layout, click area and hover preserved; summary of workspace points maintains its composition. No changes in track, volume, clock, network or control-center.

KDE adapter connects minimalizedChanged, serializes sixth minimization field by UUID and includes state changes in callback. Status reaches model; minimized window cannot remain active by retained focus of shell. Active selection prioritizes UUID, without lighting title duplicates. Fixed grouped are only minimized if all windows are; workspace group representative prioritizes active/visible. WaylandToplevels preserves minimalized in wlr.

Local effect ricywindowactions derives from the KDE Squash GPL-2.0-or-later. Minimizes with compression, displacement and fade; restores in reverse; base 240 ms, InCubic/OutCubic, with fast reversal and blur cleanup. Native squash did not animate when Noctalia did not publish iconGeometry. New fallback uses destination 18×18 on the same monitor, horizontal axis of the center of the window and 22 px above the bottom edge (taskbar 44 px). It is approximate destination, not the exact icon; if iconGeometry exists, it is preferred. Only normal taskbar windows, respecting full screen effects. If the bar changes position/height, review fallback. No Plasma protocol of icon geometry has been added.

Native Scale to Open/Close: Base 180 ms, scale 0,92 and fade; dialogues can also receive the Scale as KDE implementation. Squash, Magic Lamp and Fade disabled to avoid overlap; Smooth Window Geometry and ricyblur maintained.0,25 preserved: real reference times approximately 60/45 ms to minimize/close. Noctalia and KWin move preferences are independent; AnimationManager and animationTime respect their preferences. No rebooting compositor or finishing apps.

New compilation reference contributions/app-indicator-animations includes full patch Noctalia 5.2.1 no commit 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 and effect tested in KWin 6.7.5. Ten public archives: README, compiler, patch, MIT license, two validators, applicator, GPL license and two asset effects. Comparison of the blocks confirms additional changes only in TaskbarWidget, KwinActiveWindow and WaylandToplevels with respective headers. Other blocks, menus, notifications, wallpaper and corrections of previous preserved actions. Updated resettlement, visual guide and tokens; warning in the previous contribution points to this variant.

Checks: 17 JS tests of shares and 15 signal/serialization/animations passed; final compilation/reproduction, bash-n, config validate, git diff --check and reverse application of patch passed. Wide compilation presented warnings -Wmaybe-uninitialized pre-existing in config_service.cppNo changes in this file. Real disposable Qt window confirmed restore/minimize/restaurate, common activation without minimizing and closing; ricywindowations and Scale appeared active during transitions. Speed 0,25 did an initial consultation after 65 ms miss animations; observation within 60 ms passed. Private captures confirmed the active indicator→minimized. There was no physical simulation of click, validation of all groups/apps, scales or real quick reversals; this adjustment has not yet received visual confirmation from the user. Test Scripts and DBus removed. No working window has been closed.

Active Shell/adapter, KillMode=reestablished control-group; ricyblur, ricywindowations and Scale loaded. Active/build binary match, SHA256 ac14659d1461da4cb5c86b2b38dfb1757c25b875a729d939cd670bfbb28a2. Shell backup: $HOME/.local/state/ricy-notificacoes-backups/20261010-202443-366945, returns to the behavior of the approved actions before this indicator. Backup effect/keys: $HOME/.local/state/ricy-indicador-animacoes-backups/20261010-202354-251513. Full reversal requires restoring both as README. Backup of keys limited to modified ones, without distributing private state in the kit.

Synchronized active/portable kit: 462 hashes checked by manifesto, 452 preserved previous entries and ten new ones added. Preserved KDE credits and licenses. No binary, screenshot, clipboard, account, bytecode, private state or backup in the kit. Unchanged historical compacts.

## Contribution — Animations of icons, correction of background and reorganization — 2026-10-10  20:46 (America/Sao_Paulo)

User requested pulse/bounce by state and reported black background in the first implementation. Slot Box was replaced by Node without painting, keeping click area and independent hover. Private captures before/after confirmed removal. Icons receive finite actions: open 420 ms (bounce/pulse), restore 360 ms (bounce), focus 260 ms (pulse), minimize 220 ms (compression to bar), background 200 ms (decrease/decrease), closed 240 unfixed removed dissolves in 220 ms, scale 1→0,72, no hit-test/layout, with window exit check and lifeguards. Respected native movement/speed, no loops at rest, no initial animation of all apps, resuming progress in reconstructions and interruptions. Captures check boom/compression; no conclusive capture of the ghost upon closing. Real disposable Qt window confirmed states/effects; no closed user work.

Next request: click/scramble to reorganize applications. Extended upstream mechanism restricted to fixed for all strips of the plane, without changing fixing. Icon accompanies cursor, transparent spacer target mark, neighbors yield space. Native threshold avoids confusing click with drag; hold without moving preserves click. Release of gesture consumed suppresses window action. Medium-click/context preserved. Search/tray/controls stay out of the range; grouping by workspace maintains original layout. Horizontal/vertical axis as orientation, real pitch considers title/scale/spagging.

ConfigService saves widget.taskbar.app_order in settings.toml private, after dispatching the event. App+occurrence keys do not contain titles/UUIDs. Instances retain key during updates, new ones can reuse free slot; between restarts there is no specific document identity in windows of the same app. List preserves closed/filtered apps and adds new ones without preference at the end. Shared Widget applies order on your monitors. Generation guards invalidate commit in changed model; cancellation restores flow; release waits to recharge in final position. Private preference not copied to kit.

User confirmed “Passed” after activation of reordering. Real order with two different slots found and config validate passed after drag. Private capture shows the altered order and absence of black background. There was no automated physical simulation; visual validation came from the user. Vertical bars, other scales and model changes during real drag were not visually validated. Tests: 22 Order No (including 24 permutations), 11 against native TaskbarWidget/ConfigService objects in temporary profile, 20 of motion, 17 JS of shares and 15 the indicator/effect passed. Native test confirmed unfixed apps, movement, cancellation, invalid generation, click suppression, writing without pin and schema/definition decoding order in new instance; did not connect to the compositor. Patch on clean font, 17 identical files, compilation/reproduction, bash-n and git diff --check passed. New stage changes only TaskbarWidget, definition and taskbar_order.h; patch fully includes the previous adjustments, including motion header.

Public contributions: app-icon-states (12 archives) records the previous step; app-icon-reordering (16 Archives) is the current cumulative reference. Reinstallation, identity and updated tokens. Active/build binary match, SHA256 of 29814a36e2091d3889c1abce94ea046bb89aa27c4df66efb36d3cc18e87d4f. Active Shell/adapter, KillModel=reestablished control-group; ricyblur, ricywindowations and Scale loaded. No change in KWin effects at this stage. Backup to undo only drag: $HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447, returns to the animations with corrected background. For before the animations of icons, use 20261010-203450-476691; 203558-299413 He's a middleman with a black box.

Active and portable kit synchronized, 490 hashes per manifesto: 462 previous preserved entries, 12 of the state stage and 16 added reordering. No binaries, captures, clipboard, accounts, local preferences, bytecode or public backups. Preserved historical compacted. MIT and GPL licenses and upstream credits maintained.

## Contribution — Fade and window expansion — 2026-10-10  21:00 (America/Sao_Paulo)

User provided reference Slick Window Arrangement: https://windhawk.net/mods/slick-window-arrangement Asked for the scope, it confirmed “Open/restorate and close/minimize”. Checked primary sources Windhawk and KDE Scale/Squash. The provided mod implements scrolling/snapping drive; no Windows code was copied. Fade + expansion applied requested using native KWin API.

Open/restor: scale 0,85→1 and opacity 0→1, OutCubic. Close/minimize: 1→0,85 and opacity 1→0, InCubic. Center of the window itself, without translation to icon or monitor, without modifying real geometry. 320 ms; global KDE AnimationDurationFactor=0,25 preserved, approximate reference 80 ms. Ricywindowactions passes from compression/displacement to Scale+Opacity; Native Scale opens/closes with the same values and preserves its filters/dialogues.

Reversions use redirect and, if necessary, cancel before the new direction. Track IDs accompanied to release blur only when both end; old/strange IDs ignored. Close during action cancels local transition; Closure Scale blur is already active is not cleaned prematurely. Filters kept for normal taskbar windows/full screen effects. Fade, squash and Magic Lamp disabled to prevent duplication. Smooth Window Geometry, ricyblur, Noctalia binary, drag/order/hover/pulse/bounce/indicator and preserved panels. There was no change in maximization or window drive.

New contribution window-fade-expand, seven files: README, applicator, validator, GPL license and three asset(metadata, JS, schema XML). Applicator saves package and ten changed keys, preserves too many kwinrc keys, reconfigures/reloads effects without restarting KWin/Noctalia or closing apps; automatically restores backup if activation fails. Backup of this session: $HOME/.local/state/ricy-fade-expand-backups/20261010-205749-431612. REversion to README; undistributed local status/backup. Previous app-icon-reordering installer remains historical for effects; current reinstallation combines your Noctalia compiler with apply-animations.py of the new contribution.

28 JS/config/package scenarios passed. Real disposable Qt window confirmed open, restore/minimize/restaurate, minimize/restaurate in quick sequence, common activation without minimizing and closing; active scale in input/output and local effect on actions. checked package/keys; loaded ricywindowations, Scale and ricyblur, shell/active adapter. Refer to the journal did not bring script errors. Removed DBus test/object, no closed working window. There is no frame measurement to scale/opacity frame or validation of all apps/dialogues/monitors/scales; still no visual user confirmation.

Reinstallation, identity, tokens and previous updated contribution notices. Synchronized active/portable kit: 497 Hashes per manifesto, 490 previous preserved and seven new added. Preserved GPL credits/license. No binaries, screenshots, clipboard, accounts, private preferences, bytecode or public backups; preserved historical compressed.


## Contribution — Dolphin with Noctalia identity — 2026-10-10  21:07 (America/Sao_Paulo)

Request: Bring Dolphin's appearance closer to the Noctalia reference. Created exclusive variant Kvantum Ricy-Dolphin, derived from KDE-Noctalia/Catppuccin MIT: surface #181825, text #cdd6f4/#a6adc8, contour #46485c and Mauve accent. Sheet Qt with Noto Sans 10 pt, toolbuttons/fields/beds with lightning 8 px, hover in #313244 and selection #977dba. Sources of archives in the three modes configured in dolphinrc (UseSystemFont=false/ViewFont=Noto Sans). Icons and file behavior preserved. KDE Global Source, Noctalia, MIME and intact decoration.

Theme assigned only to dolphin executable via Kvantum/Applications. Wrapper $HOME/.local/bin/ricy-dolphin Inject -stylesheet. Local app input, D-Bus FileManager1 service and drop-in plasma-dolphin.service use wrapper. No system file replaced; daemon not restarted. QSS applied by D-Bus to existing processes without closing windows. Old windows may require reopening to load variant and file sources. /usr/bin/dolphin do not inject the sheet; the normal launcher and wrapper carry it.

Inspected captures before/after new window, with proportional source and rounded controls. Syntax Python, XML SVG, assignment, fonts, active QSS path, desktop-file-validate and systemd-analyze --user Verify checked. Dolphin 26.08.2-1.1, Kvantum 1.1.8-1.1. Only agent conference windows were closed; preserved existing Home window. An initial assertion expected literal QSS in D-Bus, but Qt returns file:////CAMINHO when you load -stylesheet; check the path and equality of the installed file. Not proven all dialogues/actions, new sessions, all monitors or migration. Still no visual confirmation of the user. Opaque surfaces for reading; not extended shared shell blur. Decoration conserves KDE font.

Portable material: contributions/dolphin-noctalia-identity/apply.py, dolphin.qss, README.md and MIT license. Applicator generates private backup and offers --restaurar BACKUP. In this work were two applications: undo in reverse order 20261010-210632-242640 and 20261010-210604-287127, under $HOME/.local/state/ricy-dolphin-backups. Restorer restores entire files and absences; reopens Dolphin. Later changes in these files can be replaced. Synchronized active/portable kits and new hashes checked, preserving previous entries. Backups/captures/unpublished state. Preserved historical compacts.


## Contribution — Dolphin: blur, corners and chips — 2026-10-10  21:33 (America/Sao_Paulo)

Harmonization Chat Dolphin/Noctalia. The user rejected the first opaque/squared version; this contribution replaces this final state, preserving its historical record. Background Now #181825 alpha 178/255 (~0,70), translucent card of archives #313244 alpha 40/255, radius 12, contour #46485c. A private generic Qt plugin, activated by -plugin ricydolphinui no launcher, brand DolphinMainWindow WA_TranslucentBackground before surface creation. Kvantum Ricy-Dolphin activates translucent_windows/blurring, reduce_window_opacity=30 for the surface, Base/AlternateBase transparent and transparent_dolphin_view. Texts/icons are clear; ricyblur provides native blur to external apps, without extension of the shared background Noctalia. No restart of the compositor.

Ricydolphinrounding own effect, installed with Polkit in /usr/lib/qt6/plugins/kwin/effects/plugins/ricydolphinrounding.so, assigns native radius Window::setBorderRadius(16) only normal/dialogues dolphin/org.kde.dolphin. Partial/complete maximization, fullscreen and tinting use zero. Original radii save/restaure and follow changes by signals. It does not add shader or own passes; it uses KWin native clipping and blur 6.7.5Breeze maintains solid title and KDE source. Ricydolphincorners/ricydolphinshape prototypes downloaded, deleted keys and removed libraries. Only final effect installed.

At later request, side hover became chip by content and all detail lines received rounded backgrounds. User approved, then asked to include icons and adjust header. Final status: side involves icon + name; lines #313244 alpha 90, radius 10, inserts 3/2; hover/selection #977dba with alpha 95/170/195 and solid focus #cba6f7 covering icon and line.313244 alpha 155, contour #46485c alpha 150, Noto Sans 10 native pt and arrow. QProxyStyle over Kvantum primitive exchange; wrapper preserves delete KIO for sections, devices, capability and tooltips. QGraphicsEffect draws backgrounds before native drawSource. No intercept mouse/keyboard or change files. Line Chips used in items >140 Px of a width and <=64 px height; large thumbnails maintain their content. QSS alone does not correct zebra fillRect; transparent palette and item backing solve this design itself.

Compilation Qt and installation of checked helper; new captures showed chips, selection with icon, rounded solid focus and arrowheader. Desktop capture showed composite blur. Previous RGBA capture measured alpha 178 at the bottom (before) 255). Native status confirmed lightning16; disposable Qt client confirmed normal16, maximized0 and restored16. No crashes observed in test logs. ricyblur/ricydolphinrounding loaded and active Noctalia/adapter. User approved chips before icons/header inclusion; this final revision still without visual confirmation of it. Not tested all dialogues, transfers, drag/drop, reordering/resizing columns, monitors/scales, giant folders or performance; reset to another PC has not been tested.

Sources/compilers/README/MIT license in the new contribution contributions/dolphin-blur-corners. Updated apply.py, QSS and dolphin-noctalia-identity README; added launch.py. Qt6 Widgets/headers, g++ and pkg-config suffice for helper. Effect requires headers/KWin dependencies 6.7.5; build.py Reused Vulkan heads of official Ricy cache. None .so, screenshot, cache, backup or private data included in the kit. External sources of consulted corners without reuse code. Credits from Catppuccin/MIT theme preserved. Services/desktop keep wrapper; daemon not restarted or automatically closed windows by the applicator. Old instances need to reopen for plugin/theme, QSS applied live by D-Bus; script treats running when user closes an instance during application.

Play/restor by READMEs and updated step 8 of REINSTALL.md. Corner backup: ~/.local/state/ricy-dolphin-corners-backups/20261010-211849-253315. Backup before chips: ~/.local/state/ricy-dolphin-backups/20261010-212842-374549; reverse in reverse order 213035-906999, 212959-440141, 212842-374549 (prefix 20261010-) returns to the previous blur revision. For state prior to blur, continue 211713-181764, 211458-875287 and 211018-558522. Corner restorer preserves keys/radii without replacing whole kwinrc; does not remove library. Backups are private, use new names issued in destination.

Register added under shared flock. Updated identity and tokens, synchronised active and portable kits; manifests preserve existing inputs, recalculate only edited materials, and include new files. Preserved old compacted. This section supersides the previous affirmation of opaque surfaces.


## Contribution — Plasma/Noctalia Alternance without restoring old settings — 2026-10-10  22:49 (America/Sao_Paulo)

Work: Concise alternation between the two shells, preserving the Ricy. The user reported no simple return to Noctalia and unexpected change of the wallpaper when using the return to Plasma. This state replaces the exchange flow of previous noctalia-autostart and integration/KDE contributions; historical records and original backup were preserved.

### Cause conferred and result applied

The old return overwrites plasma-org.kde.plasma.desktop-appletsrc and plasmashellrc whole from plasma-before.tar.gz. The restored layout had a group of old north wallpaper; the living desktops 43/44 The old input also ran restore-wallpaper.js, with fixed IDs and image captured before. Wrappers $HOME/ricy/start.sh and return.sh mentioned in the history no longer existed in the destination. At the beginning of this work, Plasma was active, Noctalia/adaptor/integer inactive and login preference disabled; there was a live panel (23, monitor 0).

Installed contributions/plasma-nottalia-switching with seven public files. $HOME/.local/bin: ricy noctalia, ricy plasma, ricy alter (also the action of ricy without argument), ricy status, back-to-nottalia, back-to-plasma. Persistent entries in the menu: Back to Noctalia, Back to Plasma, Toner Plasma and Noctalia. Recreated $HOME/ricy/start.sh, return.sh and switch.sh. The two explicit actions also change the preference of login.

The installer has replaced start-test.sh and return-to-plasma.sh in three sites of the active kit (historical outputs, integration/KDE and start-automatic models) by wrappers that lead to new implementation. In the public kit these historical scripts remain original; the new installer replaces them in the destination. Units, drop-ins and profile names remained existing.

Before collecting panels, plasmashell is briefly stopped/started to sync KConfig and capture all groups of panels and their geometry. Return restores only these groups; conserves desktops, wallpaper, widgets and current general groups. Includes external trace and remaps IDs when they conflict with later desktops/widgets; on this machine the nested applet 43 was remapped to 47 in the first return. Return with already existing panels is innocuous. Snapshot without panels does not replace a valid snapshot.

Super, Super+Space and Super+V are captured every cycle, transferred to Noctalia and restored to their previous actions. Shell/adapter must be ready before the panels are removed. Error in this step tries to recover Plasma; the command also disables Noctalia preference if the drive fails. Command and integration locks serialize calls; login continues using ricy-noctalia-integracao.serviceEach command fires a worker in a separate transitory unit to survive the caller shell closure. Thus the return can also conclude when initiated by the Noctalia menu.

Retrieved once the previously chosen Limine, /usr/local/share/ricy/limine-splash.png, FillMode 2, on live desktops by locally obtained IDs. The private state of Noctalia and the previous record confirmed this image. The following exchanges do not impose any wallpaper. Desktop and general appearance are shared; Noctalia is integrated with KDE/KWin. It is neither songwriter/session nor restoration of the old themes.

### Play and undo

After preparing integration/KDE and installing noctalia-autostart:

```bash
python "$HOME/ricy-kit/contributions/plasma-noctalia-switching/install.py"
"$HOME/.local/bin/ricy" noctalia
# To return or switch:
"$HOME/.local/bin/ricy" plasma
"$HOME/.local/bin/ricy" alternar
```

Require Python/PyGObject, qdbus6, flock, systemctl and kbuildsycoca6 in the already prepared Plasma Wayland session. Do not use sudo or reinstall packages. Profile continues in contributions/noctalia-kde-integration-and-menus/work/nottalia-profile; service keeps executable custom $HOME/.local/lib/ricy-noctalia/noctalia. No torque change, patches, colors, Dolphin, effects, login or lock. REINSTALL.md updated with the installer and commands in both directions. Reinstall the installer if you reinstall the old scripts later.

Private backup emitted on this machine: $HOME/.local/state/ricy-alternancia/backups/20261010-224512-267960. Guard previous wrappers, absences and Plasma files prior to wallpaper recovery. Panel/shortcut snapshots and markers stay on $HOME/.local/state/ricy-alternancia. They are not migration materials. README contains restore-installation.py: Run first plasma ricy, then pass the backup to restore wrappers/inputs and previous status; the restorer preserves the current desktop. Do not undo the wallpaper or appearance. The original full backup remains available, but restores it fully reintroduces the loss of later preferences.

### Verification and limits

Two actual cycles Plasma→Noctalia→Plasma completed, plus a third return initiated by a disposable caller linked to shell and final entry into Noctalia. The caller was closed with the shell; the separate worker continued and restored panel/KRunner successfully. This simulates the dependence of the shell-opened command life cycle; there was no visual click on the menu in this test. Ricy tests alternate, aliases, status and repeated calls in both environments. The second return had complete groups of panels/geometry identical to the last snapshot; a Plasma panel was conserved. Wallpaper Limine present on both monitors in both directions. Shell/adaptator and active integration at the end, zero Plasma panels, enabled Noctalia preference; KRunner active when Selected Plasma. Original shortcuts conferred on D-Bus in return. Eight torque hashes, TOML, kdeglobals, kwinrc, dolphinrc and Kvantum selection remained identical; P-Bus added.

verify.py passed: preservation of wallpaper/desktops/widgets/views, IDs and references in conflict, external tragedy, comments, idempotence and refusal of empty backup. Syntax Python/Bash, desktop-file-validate and systemd-analyze --user verify passed. An initial error in fixture used expectation of inconsistent ID with its own applets; fixed the fixture, final suite passed. There was no complete restart/new login, visual measurement of all geometries or actual injection of failure during removal/recovery. Not tested on another PC.

Public material copied explicitly, without profile/clipboard, backups, binaries, screenshots or bytecode. Both manifests now have 518 entries granted; 511 Existing preserved, seven new materials, hashes of the six wrappers updated only in active kit. Historical compacted preserved. Register added under shared documentation lock.


## Contribution — Header Dolphin hover position — 2026-10-11 (America/Sao_Paulo)

At user request, correct the hover chip position in header columns: Starts 8 px before the native column rectangle, vertical insert 3 px and intersection with the entire header retreated 5/3 px. Avoid touching the text on the edge and extrapolate the capsule into the wide/rolled columns. HeaderChip provides temporary bundles to QProxyStyle during drawSource, without changing events, labels, arrows or geometry of the columns. ui.cpp recompiled/installed by apply.py; backup 20261011-083312-062208 ed ~/.local/state/ricy-dolphin-backups. Restore with apply.py  --restaurar BACKUP, then reopen Dolphin. Qt offscreen drawing test passed: padding before label, top/ bottom insect and overflow clipping. New Dolphin window open for conference; old instances need to reopen to new code. Not tested all monitors, scales, RTL or real horizontal scroll. README and ui.cpp synchronized in active/portable kit; updated hashes preserving too many inputs.


## Contribution — Hover Size/Modified Dolphin — 2026-10-11 (America/Sao_Paulo)

Hover includes the native rectangle of the margin sorting arrow 6 px. Last column identified by padding End painting (section-1), or End position of the column itself; its hover reaches the right internal border of the header. Name keeps the previous inserts. Without using translated strings of the columns. Qt test offscreen passed to identify the last column, fill to the right margin, external/vertical limits and arrow inclusion. Backup ~/.local/state/ricy-dolphin-backups/20261011-084408-791214. Revert with apply.py  --restaurar BACKUP and reopen Dolphin.

Recompiled/installed Helper; sources/ README synchronized in the two checked kits and hashes. Existing instances need to reopen for new code. No visual confirmation of the user in this review.


## Contribution — Size text only on hover — 2026-10-11 (America/Sao_Paulo)

Enlightened request: Size should have a short chip only around the text, without including arrow. Replaces the arrow inclusion rule of the previous revision. Intermediate columns use SE_HeaderLabel, native alignment/direction and width of the deleted text + 8 px padding on each side. Name and extension of last Modified column preserved. Arrow continues natively drawn. Helper recompiled/installed; Offscreen test checked chip smaller than column, text inside and no fillout next to arrow. Last column continues filling up to the right margin. No final visual confirmation of user. Backup ~/.local/state/ricy-dolphin-backups/20261011-084526-161433. Restore with apply.py  --restaurar BACKUP and reopen Dolphin.


## Contribution — Size: width of column without arrow — 2026-10-11 (America/Sao_Paulo)

Order correction: chip occupies the width of the Size column, not only the text. Intermediate columns use native rect with insert 3 px on each side, without the negative displacement that swallowed the arrow of the anterior column. When the column itself has sorting arrow, this space is excluded with margin 4 px. Name and Modified preserved. Replaces the rule of width by text. Compilation/installation and offscreen test passed: start inside the column, fill in beyond the label, previous area without hover and arrow reserve. Backup ~/.local/state/ricy-dolphin-backups/20261011-084620-426269. Revert with apply.py  --restaurar BACKUP and reopen Dolphin. No final visual confirmation; old processes need to reopen.


## Contribution — Internal Padding of Size — 2026-10-11 (America/Sao_Paulo)

Chip keeps the column width and the limit that deletes the previous arrow. Now the intermediate column label is backed down to ensure 8 px internal at the beginning/end, without moving the chip over the arrow. Name and Modified preserved. Helper recompiled/installed. Qt painting test offscreen passed to fill in the width, reserve the arrow and first pixel of the text at least 8 px after chip edge. New window by open launcher. Backup ~/.local/state/ricy-dolphin-backups/20261011-084751-069063; restore with apply.py  --restaurar Backup and reopen.


## Contribution — Name: arrow-right space — 2026-10-11 (America/Sao_Paulo)

User approved Size padding. Hover of the first column Name now extends the right border on 6 px, keeping clipping on the common header. Size and Modified preserved. Helper recompiled/installed. Offscreen test checked finite extension to the right and maintained Size checks, padding and last column. Backup ~/.local/state/ricy-dolphin-backups/20261011-084856-807309; restore with apply.py  --restaurar Backup and reopen, no final approval from Name.


## Contribution — Uniform spacing of the Dolphin header — 2026-10-11 (America/Sao_Paulo)

User approved Size and requested symmetry of spacing. HeaderChipRect centralized geometry: chips end at column limit +3 px; the following starts at this limit +9 px, keeping 6 px between them. Name conserves margin of the arrow, last column reaches the right internal margin. All use vertical insert 3 px and content with minimal padding 8 px; intermediate/final backed labels, without shifting chip over the previous arrow. The arrow of the column itself, when necessary, has area reserved to the part. It does not change width/hit-test of the columns. Compilation/installation and Qt offscreen test confirmed 6 px in both ranges, height/y equal, Modified to the end, text with padding and Size occupying width. ~/.local/state/ricy-dolphin-backups/20261011-085034-172903; restore with apply.py  --restaurar BACKUP and reopen Dolphin. Still no visual confirmation of this spacing; does not measure all sorting/RTL/scroll scenarios.


## Contribution — Sidebar Padding Dolphin — 2026-10-11 (America/Sao_Paulo)

KFilePlacesView receives padding-left/right 8 px on the Qt sheet. Viewport backend moves together titles, icons, chips and capacity bars without shifting only the design of the delegate. Applicator created private backup ~/.local/state/ricy-dolphin-backups/20261011-085235-777886. New window capture confirmed backwards titles/icons/chip; sidebar does not touch the left. QSS also applied to existing instances without closing them. Source/helpers and header spacing preserved. Revert: apply.py  --restaurar BACKUP and reopen Dolphin. Not tested scrollbars/drag-drop in all widths.


## Contribution — Stable sidebar, expansion and nested chips — 2026-10-11 (America/Sao_Paulo)

User confirmed that the crash of the sidebar stopped; approved chips accompanying the visible width and the final indentation to approximately the parent folder icon. Removed PlacesDelegate/setItemDelegate: no longer swap native KFilePlacesView. ChipStyle query index/text/icon via public view/model during painting. Preserves connections and events KIO. Core coredumpctl/gdb indicated treatment of KIO events; there are not enough debug symbols for the exact line. Native test KIO QtTest passed 21 clicks/21 UrlChanged signals.

Another cause of crash in updates: copy2 overwrites library inode .so mapped by open processes. Installer now copies to tempfile in the same directory and trades for os.replace. Reapplication preserved previous process 315482 live, without corrupting the loaded library. This replaces in-place installation; previous visual checks did not cover that risk.

Final configuration dolphinrc: DetailsMode/ExpandableFolders=true and LeftPadding=20; General/ShowSelectionToggle=false/BrowseThroughArchives=true. .md it was hover selection, not expansion, and it was shut down. 6 px, dash1,5 #a6adc8 only for PE_IndicatorBranch State_Children; right/low closed/open. Common files have no arrow. QStyleSheetStyle Qt discarded branch with simple QStyleOption; graphics items now use ChipStyle directly, widgets keep QSS. Real Dolphin test in private fixture expanded folder via click, 2→3 lines, indented child and chevron. Compacted navigation enabled; native model expands tree directories, not compressed files. These can be opened via KIO when supported; no arrow without functional action. Not tested all formats.

RowChip intersects items with viewport visible in local coordinates. Rounded background/clip/focus accompany visible width; over cut content. sourcePixmap NoPad with context measures depth by native branch slots. Crop reaches hover/cache selection, redesigned focus on chip to maintain contour after indentation. End state approved: root insert3px; son adds 20px gutter + depth × line height. At height22px, first level begins ~45px, in the parent folder icon; next advance22px. Replaces attempt8px for rejected level as small. Inset3px right, vertical2px/ray up to10px; content/columns not moved. Real viewport captures checked expansion, chevron and indentation. User approved width and indentation.

Probe temporary Qt explicitly loaded and fixture in cache do not enter the kit. Probe library and copy extracted from core removed at the end; preserved user-managed windows. Not tested RTL, hundreds of levels, file scales/formats, transfers, drag/drop or performance.

Backups in ~/.local/state/ricy-dolphin-backups, restore in reverse order to return before the sequence: 20261011-090752-444876, 20261011-090705-662420, 20261011-090614-400487, 20261011-090454-088355, 20261011-090310-602007, 20261011-090132-953293, 20261011-085727-916570- Use it. apply.py  --restaurar BACKUP and reopen. Restorer replaces entire files, and can replace later edits. Do not reapply old installer that overwrites .so. Probe in backups remains private/inactive; launcher only uses ricydolphinui. It can delete libricyprobe.so while restoring snapshot with probe.

Sources/applicant/Readmes synchronized in active/portable kits; hashes checked preserving other inputs. Not included .so, screenshots, core or backups.


## Contribution — Panel and tabs as Noctalia buttons; nested arrows — 2026-10-11 (America/Sao_Paulo)

Request: topbar/sidebar with blur, delimited panel content and tabs with color/Noctalia button format. Also preserve adjustment of nested arrows made before the request amplification. Tabs: neutral #313244/#cdd6f4, outline #46485; active #cba6f7 with text #11111b; hover #977dba/text #000000. Radius12 px, padding6/14 px and margin3 px (range6 px). Swap the tabs pill radius14/translucent Mauve from the previous attempt by buttons as reference. QTabBar::close-button reserve right8/12px; compact tabbar buttons; QTabWidget::pane without edge; helper setDrawBase(false) eliminates baseline. Icons and closing/reordering maintain native behavior.

Root QMainWindow keeps #181825 alpha178/255 (~0,70), sidebar/topbar remain transparent on this background, with alpha channel before creating the surface.181825 alpha96/255 over root, contour #46485c, radius12 and margin/padding8. Replace panel #313244 alpha40; alpha composite measured in window capture ~207/255. Topbar/sidebar measured178/255. Texts and icons do not receive global opacity. Real Dolphin capture new with several tabs showed Mauve/neutral buttons and delimited panel. At the time of this native KWin blur revision is loaded (blueEnabled=true/force5), ricyblur is not loaded or enabled. This state was found in the session and preserved: not reactivated ricyblur, not restarted compositor or Noctalia. Do not confuse this current observation with the previous states documented in this contribution.

Arrows of dislocated subfolders4px inside (RTL opposite direction), when the branch is beyond the root slot; preserved root arrow. Geometry/hit-test native expansion does not change; shift fits in the expansion slot. Cut of daughter chips and content accompanies viewport as approved.

Compilation/helper installed checked and preserved atomic installation. Qt tabs test confirmed preserved defined icons, back down button and deactivated base. Fixture uses synthetic icon, does not validate all Breeze icons. Real Dolphin capture confirmed palette/layout; not tested all tabs, monitors, RTL or all folder levels. A later active window capture caught Codex because the user switched focus; not used as Dolphin evidence. Visual approval of this still pending review.

Private backups in ~/.local/state/ricy-dolphin-backups: end 20261011-091610-462637; to return to the state before this sequence, restore in reverse order also 20261011-091325-096396 and 20261011-091239-713431- Use it. apply.py  --restaurar BACKUP and reopen. Restorer replaces entire files and can replace later edits. Active/portable kits and synchronized local tokens; hashes preserve too many entries. Captures/tests stay in the private cache, without binaries/state/screenshots in the kit.


### Review — opaque panel and tab closure — 2026-10-11

Main area uses #313244 solid (alpha) 255), as Noctalia panel referenced by the user. Sidebar/topbar remain on #181825 alfa178, with preserved native KWin blur. Helper repositions the native tab buttons before painting, with 12px of external indentation (includes 3px margin); preserves closing signals and actions. Previous QSS subcontrol did not move the button in the actual Dolphin. Capture/probe in the application confirmed RGBA panel(49,50,68,255), shell alfa178 and retreat12 in the three tabs. Final backup: ~/.local/state/ricy-dolphin-backups/20261011-092428-218159; previous in this sequence: 20261011-092338-169456. Helper uses atomic installation; new code requires new window.


### Revision — sidebar/topbar on an L panel; side buttons — 2026-10-11

At user request, sidebar and topbar now share a single opaque panel #313244, equal to the main panel. ShellPanel is a child QWidget behind the controls: draws the entire L with radius12, margin8 and gutter8 for the archival area, without receiving input or changing the layout. Geometry accompanies the visible containers (including more than one area), resizing and concealing the dock; without sidebar drawing only the topbar panel. The outer margin continues on the alpha178, translucent shell with preserved KWin bluff. This review replaces the internal transparency of the previously registered sidebar/topbar.

Side items are buttons of uniform width: neutral #242435, hover #977dba, selected #cba6f7, contour #46485c, radius8.Native icons24, list spacing1 and vertical indentation2 leave 6px between buttons. Side padding 12; HighlightedText #11111b palette, preserving native drawing of active/inactive text and icons. KFilePlacesView keeps its original delegate, clicks, shortcuts, drop, capability indicators and device actions. Icon size is recorded by KIO in dolphinrc, included in backups.

Checks: helper compiled/installed atomically; capture in the real Dolphin confirms continuous L and buttons; lateral test passed21 clicks/21 navigations without switching delegate. Fixture Qt confirms connected arms, free clipping for content, no mouse capture, resize and hidden sidebar. Not validated all RTL layouts or floating docks. Final backup: ~/.local/state/ricy-dolphin-backups/20261011-093607-825801. Before this sequence: 20261011-093205-549123followed by 093320-666039 and 093439-242103 (even date prefix). To reverse the entire sequence, restore in reverse order. New code requires new window.
