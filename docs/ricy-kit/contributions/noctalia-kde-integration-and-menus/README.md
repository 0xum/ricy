# Noctalia/KDE integration and compact menus

This folder is an independent contribution to the ricy-kit. Copies record the status conferred on 08/10/2026. Do not run both integration kits simultaneously: both use `noctalia-teste.service`, `noctalia-busca-desktop.service` and IDs `codex-noctalia-*.desktop`.

## Preparing in DESTINATION

Use a KDE CachyOS Plasma Wayland session with already chosen Plasma panels and wallpaper. Copy this folder to `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus`. Check out the root SHA256SUMS first. Do not bring backups, Noctalia status, monitor IDs or original source machine shortcuts.

Observed execution dependencies: Noctalia 5.2.1-1.1, Kvantum 1.1.8-1.1, Plasma 6.7.5, KWin 6.7.5-3.1, python-gobject 3.58.0-1, qt6-tools 6.12.0-1.1, Python, glib2, coreutils, util-linux, bash. Qt 6 PyQt6 6.11.0-4 is required only for the optional menu test. Noctalia source is Noto Sans; in destination preserve your KDE source. JetBrainsMono Nerd Font, Papirus-Dark and Catppuccin were already source choices, not mandatory dependencies of these scripts.

```bash
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts
# Optional according to the test/method used:
sudo pacman -S --needed python-pyqt6 wl-clipboard
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python prepare-destination.py
```

The preparer only creates kit files: local private backup of relevant archives, manifesto, previous status of keys, wallpaper restoration with DESTINATION IDs, isolated profile and `.desktop` with recalculated paths. Do not start services or apply style. Refusal to overwrite original backup. Backups may contain personal preferences: keep them in the destination, do not redistribute them. `config.toml` and `KDE-Current.json` do not contain network identification, user, recent files or clipboard status.

## Apply style and blur, then start Noctalia

```bash
./apply-style.sh
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/start-test.sh
```

`apply-style.sh` installs full assets Kvantum KDE-Noctalia, selects style and sets menuFont 10 pt preserving the family of the destination. It does not modify the Breeze decoration or the overall font size. When editing a theme already selected, `python reload-style.py` switches temporarily to Breeze and returns to Kvantum, and emits the actual feed update signal. This is necessary because Qt/KDE integration ignores the style change if the name remains the same.

The public palette is in `outputs/kde-outlines/KDE-Noctalia.colors`. If fate does not yet use these colors and wants to adopt them, use optionally:

```bash
mkdir -p "$HOME/.local/share/color-schemes"
cp outputs/kde-outlines/KDE-Noctalia.colors "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
```

This scheme application was not done in this chat: KDE of the origin already used Catppuccin Mocha Mauve. It is a migration option, regardless of the style installation.

The start removes Plasma panels only after the IPC of Noctalia is ready. Plasshell remains desktop/wallpaper active. The adapter replaces KRunner in D-Bus and records Super/Super+Space and Super+V; the original shortcuts are captured locally. The login recovery restores the panels if the test is not active. The kit does not automatically start Noctalia after login. The script retains the current integration logic; it is not a generic installer for sessions without the expected Plasma services.

## Expected final state

- Bottom bar top, 44 px, reserved area, scale 1,5, no auto-hide/smart-auto-hide, background 0,70 with blur. Taskbar icons approximately 28 px: scale 0,666667, icon_scale 1,725, spacing 6.
- No SSID or volume percentage; tray with drawer 3 columns, icons 24 px. Central attached/auto and opaque cards.
- Dark palette #181825, cards #313244, text #cdd6f4, accent #cba6f7, hover #977dba, contours #46485c. Terminal object also included in JSON to pass the validator.
- Current search attached/auto at the top through support `search_edge`  10 px without reserve; wrapper-controlled opening/hiding and adapter controlled. Previous floating/center test has been replaced. Clipboard floating/center active in current copy.
- Qt Menus: External Corners 12 px; SVG selection with radius 6 px, vertical frame 4 px and lateral 6 px; vertical text margin 0/lateral 2; minimum height 24 px; separators 5 px; `spread_menuitems=false`, `shadowless_popup=true`, `popup_blurring=false`, reduced opacities 0. The actual height depends on the source/icons; native test of this machine produced lines of 26 px.

## Verify

```bash
export NOCTALIA_CONFIG_HOME="$PWD/work/noctalia-profile/config"
export NOCTALIA_STATE_HOME="$PWD/work/noctalia-profile/state"
noctalia config validate
systemctl --user is-active noctalia-teste.service noctalia-busca-desktop.service plasma-plasmashell.service
noctalia msg status
kreadconfig6 --file kdeglobals --group KDE --key widgetStyle
kreadconfig6 --file kdeglobals --group General --key menuFont
python verify-native-menu.py
```

The last command opens a small Qt menu without forcing WA_TranslucentBackground and closes it to 1 s. Prints style, font, line height and alpha of the corner; alpha 0 means transparent pixel. Test the actual result on a window and Dolphin, because alpha of a widget capture itself does not prove the visual composition of all applications. The final visual confirmation of the user on the problem of the corners was still pending in the closing of this record.

Check also: maximized windows respect bar; menus and icons have acceptable size; tray/gavette; Super and type on desktop; Esc collects search/support; Super+V; preserved wallpaper. These tests should be repeated at destination. No real migration to another computer was done.

## Undo in DESTINATION

```bash
./outputs/noctalia-test/return-to-plasma.sh
python restore-style-and-blur.py
```

The first restore uses the local layout/plasmashellrc backup, retrieves the local shortcuts, initiates KRunner and removes the launchers/recovery from the test. The second restores the captured font, style, and blur keys and the previous Kvantum theme/configuration. Keeps the packages installed. Reopens applications to ensure update. It does not perform blind restoration of entire KDE.

If you optionally applied the color scheme, restore the colors by choosing the previous scheme in KDE. For an exact restoration of captured kdeglobals (includes other preferences and replaces later changes), only extract this file from the local backup:

```bash
tar -xzf outputs/kde-outlines/kde-antes-contornos.tar.gz -C "$HOME" .config/kdeglobals
```

Do a new session to reflect this complete restore. Reversion does not erase the history generated later in the isolated profile; this is given to the destination's personal, to be managed by your user.

## Content and origin

Preparation/application/restoration scripts have been adapted to the destination in this contribution and checked statically; they have not been executed against this session. `outputs/noctalia-test/` are copies of the active integration conferred, including the evolution to top search/clipboard already described in the main part of ricy.md. Do not represent execution of new changes when documenting.

Catppuccin MIT theme included in `outputs/kde-outlines/KDE-Noctalia/LICENSE`. Checkout consulted: catppuccin/kvantum 71105d224fef95d023691303477ce3eea487457. Consulted code of tsujan/Kvantum 110aff8b97a221531ef55acc4faeacfd719cdfea and plasma/plasma-integration 46eddde9d38cf907786e567ddd4a942140bb1f797: are research reviews, not proof that they correspond exactly to the package installed. Theme ready files are sufficient to install; it is not necessary to compile or download these checkouts.

Origins: https://github.com/catppuccin/kvantum ; https://github.com/tsujan/Kvantum ; https://invent.kde.org/plasma/plasma-integration ; https://github.com/noctalia-dev/noctalia .
