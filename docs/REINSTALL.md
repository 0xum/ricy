# Ricy — road map for the next installation

Ready in 09/10/2026 to play the captured configuration of CachyOS, KDE Plasma Wayland and Noctalia. This is the reinstallation entry point; `ricy.md` preserves the history and `ricy-kit/` contains scripts and assertions.

The reference to maintain and enlarge appearance is in `VISUAL-IDENTITY.md`, with tokens and board in `ricy-kit/contributions/noctalia-visual-identity/`. See it before adjusting other components and transport the guide with the kit.

The package `ricy-reinstalacao-2026-10-09.tar.gz` gathers this guide, the log and the entire portable kit. `ricy.zip` offers the same content in ZIP format. Save one of these files on another disk, flash drive or remote storage before formatting. The file does not contain the source's private logs/backups.

The compacted of 09/10 To carry the later contributions, copy the public folder. `ricy-kit/`, the `ricy.md` And this script is up to date.

## 1. Extract and check

In the new CachyOS installation, enter KDE Plasma Wayland as your new user. Extract the file in a workbook. Example in Bash:

```bash
mkdir -p "$HOME/ricy-importacao"
unzip /caminho/ricy.zip -d "$HOME/ricy-importacao"
# If you are using tar.gz, replace the unzip command with:
# tar-xzf /caminho/ricy-reinstalacao-2026-10-09.tar.gz -C."$HOME/ricy-importacao"
# Make this copy once, with $HOME/ricy-kit still nonexistent:
cp -a "$HOME/ricy-importacao/ricy-kit" "$HOME/ricy-kit"
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
```

Use the newly removed copy of the portable kit. Do not reuse the active folder of the previous installation with its backups, bookmarks, profiles/clipboard and IDs. All the commands below that write user preferences are sudo-free; package installation, `system.py` and installation of the blur plugin use sudo.

## 2. Dependencies and Kit Corrections

```bash
sudo pacman -Syu
sudo pacman -S --needed noctalia kvantum konsole python python-gobject qt6-tools glib2 noto-fonts sddm plasma-workspace breeze breeze-icons qt6-5compat qt6-svg fontconfig adw-gtk-theme ocean-sound-theme
# To reproduce also all the faces of the source:
sudo pacman -S --needed ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit"
python contributions/target-implementation-fixes/apply-fixes.py
```

Optional: `wl-clipboard` for the search using copied text; `python-pyqt6` for the DEB/RPM installer and the Qt test. If Noctalia is not available in the destination repositories, resolve the availability of compatible implementation before starting integration. The kit has been validated with Noctalia 5.2.1 and Plasma/KWin 6.7.5; check out new versions before applying.

Check out the hashes before running the patch applicator. After it, the two corrected files no longer have the historical hashes; after the preparation `.desktop` They also change their way. That is expected.

## 3. Login, animated Konsole cursor, fonts and appearance

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
sudo python system.py
python user.py
python ../konsole-animated-cursor/apply.py
```

This installs the login `mocha-limine`, the real colors of the SDDM account, Limine background, Bibata Modern Classic cursor 16, JetBrainsMono fonts 10 En, Breeze Dark icons, Plasma/splash themes, KDE-Noctalia Kvantum menus and GTK appearance. The script preserves other destination preferences and prints your backup.

The requested cursor is the Konsole text cursor: the default profile PlasmaBlue included active `AnimatingCursorEnabled=true`, JetBrainsMono font 10 pt, Catppuccin palette, transparency 0,85 and blur. Close and open Konsole to load this profile. The applicator checks the animation support in the destination. Bibata 16 is an additional mouse pointer preference.

If the installation uses Plasma Login Manager and you want to play the SDDM login of this kit, select the service after applying `system.py`:

```bash
# First confirm the existing manager:
readlink -f /etc/systemd/system/display-manager.service
# In this fate, the previous was plasmalogin.service:
sudo systemctl disable plasmalogin.service
sudo systemctl enable sddm.service
```

In another destination, replace the previous service with what is installed. These commands do not use `--now` and preserve the current session. Restart the computer for the exchange to take effect; exit/enter the session just does not change the process of the manager that is already running.

To also adopt the Limine wallpaper on Plasma desktops:

```bash
bash apply-wallpaper.sh
```

This last step is optional. Choose the wallpaper before the next step, as the Noctalia preparer generates its preservation with the destination IDs/images.

## 3rd. Cedilla on the international US keyboard

For the international US keyboard (`us`, variant `alt-intl`) used in this destination, apply also the cedilla composition:

```bash
cd "$HOME/ricy-kit"
python contributions/keyboard-cedilla/apply.py
python contributions/keyboard-cedilla/apply-brave.py
```

Acute accent followed by c/C produces ç/Ç; the other accents and the language of the interface are preserved. Brave uses XWayland to respect this composition; KDE continues in Wayland. Previous files are backed up. Completely reopen Konsole and Brave to load the rule. See the README contribution for reversal. If the physical keyboard is ABNT2, configure the appropriate Brazilian layout instead of applying this adjustment to the US layout.

## 4. Prepare and initiate Noctalia integration

```bash
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python prepare-destination.py
cd "$HOME/ricy-kit"
python contributions/noctalia-autostart/install-autostart.py
python contributions/plasma-noctalia-switching/install.py
```

The preparer stores layout/style/local shortcuts, creates the isolated profile and launchers. The following installer enables Noctalia on login, with Plasma recovery in error. Plasma/KWin remain responsible for desktop and wallpaper. The bottom bar is fixed on 44 px; Super/Super+Space open search and Super+V opens clipboard. The magnifying glass of the bar opens the search next to the left click, as the Noctalia control opens next to the icon on the right. Use only this contribution; the historical variant on `ricy-kit/outputs/` should not be initiated simultaneously.

The latest installer adds **Back to Noctalia**, **Back to Plasma** and **Toggle Plasma and Noctalia** on the menu and commands `ricy noctalia`, `ricy plasma`, `ricy alternar` and `ricy status` ed `$HOME/.local/bin`. The preference is also valid in the next login. Save the current Plasma panels before collecting them and restore only the panels groups, preserving wallpaper, desktops, customizations and Noctalia profile. Replace the old scripts that restored entire appletsrc/plasmashellrc from the original backup. Reapply this installer if reinstall later `noctalia-autostart`.

After editing the Noctalia profile, keep the copies synced to `outputs/noctalia-test/config.toml` and `work/noctalia-profile/config/noctalia/config.toml` of this contribution.


The search for Super or typing uses a centralized top bar of 640 px, height 16 px, corners of 8 px and distance of 8 px from the top, only while open, only on the monitor where the search appears. The adapter consults the active KWin monitor before showing the bar; Super and typing use the same opening. 1920 logical px, `bar.search_edge.margin_ends` Yeah. 640. In another resolution, adjust this margin for `(largura lógica - 640) / 2` (rounded and limited to zero), using overrides per monitor if necessary. Search measures 560 px with `accessibility.ui_scale = 1`; if you change the scale, also adjust the desired width of the bar.

## 4th Noctalia Composition: notifications, wallpaper and menus

The profile includes notifications in the lower right corner of the active monitor, without contour, with opacity 0,70 and native bar of remaining time. To also join the card to the taskbar with an open turn out in the lower left corner and the lower right right corner, compile the local adaptation of the Noctalia 5.2.1:

```bash
sudo pacman -S --needed meson ninja wayland-protocols nlohmann-json stb
cd "$HOME/ricy-kit/contributions/app-icon-reordering"
bash build.sh
python ../notification-continuity/enable.py
python ../window-fade-expand/apply-animations.py
# Plasma Image on Home Card, keeping the desktop on Plasma:
python ../notification-continuity/sync-wallpaper.py
```

The latest composite variant includes taskbar menus and tray items as embedded panels, with width/height per content. The tray menu has set at the base to return directly to the drawer on the same monitor, preserving the horizontal axis between menu, arrow and drawer. The variant also includes app icons and search 12% lower at rest, with hover of 140 ms and stable click area; the other controls are the same. In KDE/KWin, click the restore icon minimizes, minimizes the window visible in focus and brings forward an inactive visible window. The middle button asks to close a window; groups prioritize the active one, preserving selection/cycle when there is no active one. Search and other callers continue only to restore/focus. The purple indicator now distinguishes active, open inactive and minimized, with transition from 160 ms. Windows now receive fade and expansion when opening/restoring (scale 0,85→1) and contraction on closing/minimising (1→0,85), centered on the window. 320 ms follows global KDE speed (0,25 in the session, about 80 ms). The new window-fade-expand applicator preserves global preference, reloads effects without restarting the compositor and provides backup reversal. It does not require icon geometry or reference to the position/height of the bar. Icons receive bounce when opening/restoring, pulse when gaining focus and brief response when minimizing/closing, no black background. On the flat track, click/scrap rearranges all apps without fixing them; the order is saved in the profile. Search and other controls maintain position. Release drag does not activate/minimize the window. See app-icon-reordering/README.md to preserve the cache of a previous variant and recompile from a clean source when necessary.

The script maintains the original package and selects the local executable only on the shell drive. Check out README for additional dependencies, reversal and updates: the local variant needs to be reviewed/recompiled when updating the Noctalia version. The activator preserves applications during shell exchange.


The same variant includes the image on the Home card even with the Noctalia wallpaper service disabled. The Synchronizer requires Plasma desktops with the same local static image and records that path; run it again when changing the background. Read README if monitors use different images.

## 4b. Continuity of the blur between panels

To visually join the notification, search, menu and bar background after the steps 4/4a compile the separate effect for KWin 6.7.5:

```bash
sudo pacman -S --needed base-devel git vulkan-headers kwin kconfig kcoreaddons kdecoration qt6-base qt6-declarative kwindowsystem libepoxy libdrm wayland
cd "$HOME/ricy-kit/contributions/blur-continuity"
python build.py
sudo install -D -m 0755 "$HOME/.cache/ricy-blur-build-6.7.5/ricyblur.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so
python integrate.py
noctalia msg config-reload
```

If XDG_CACHE_HOME is set, adjust the plugin path in install. The script selects the compatible variant in each session; saves the native blur when you cannot use it. Do not restart KWin or applications. ABI requires reviewing/recompile the patch when updating KWin; the compiler refuses another version. Templates include `panel_overlap = 0` in default and search_edge bars; in an existing profile, also adjust these two preferences and reload. `contributions/blur-continuity/README.md` for details and reversal. The cost of composition can increase while panels/warnings are open.

## 4c. English dates, weather and events in Cosmópolis/SP

```bash
cd "$HOME/ricy-kit"
python contributions/noctalia-language-and-localization/apply.py
```

Requires locale en_US.UTF-8 generated in the destination. Sets English dates only in Noctalia and America/Sao_Paulo zone; fixed location Cosmópolis, São Paulo, Brazil, with weather in °C. Enables calendar/events without connecting accounts. For personal events, connect the source later in settings. The full address avoids the homonymous city in the USA. See the README contribution for backup/reversion; the applicator preserves applications while restarting shell/adapter and fixes destination preferences overrides.

## 5. Lock screen

```bash
cd "$HOME/ricy-kit/contributions/login-matched-lock-screen"
python apply.py
```

The lock screen uses the login background, clock and immediate form by 60 s, no media/reveal password. The script maintains native KDE authentication flow and correction `Qt.callLater`. If the target Plasma QML has changed, the script refuses to adapt; review it before insisting. After updates Plasma, reapply from the new system files.

## 6. Window effects and arrows (optional)

```bash
sudo pacman -S --needed gcc pkgconf qt6-base qt6-declarative kwin kconfig
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python user.py --extensoes-kwin
# The Noctalia bar replaces the Plasma panels:
kwriteconfig6 --file kwinrc --group Plugins --key adaptivepanelwidthEnabled false
```

Includes local effects and Super+arrows that keep the same window as target until Super is released. The native module is recompiled for destination KWin; no old library is reused. This step requires compatible API/headers. Recompilation has been checked with KWin from the capture.

## 6a. AIC8800 USB Adapter (optional)

For the adapter of this destination (`a69c:8800` before firmware, `a69c:8801` in operation), follow `ricy-kit/contributions/driver-aic8800/README.md`The DKMS source package provides Wi-Fi, Bluetooth and firmware, with compiler selection for each kernel. Use kernel-compatible headers. It is not a necessary step on machines with another adapter.

## 7. DEB/RPM Installer in Dolphin (optional)

Follow the contribution `dolphin-deb-rpm-installer/README.md`, including registration of destination packages and revised debtap construction of the AUR. Contribution `target-implementation-fixes` must have been applied in the step 2.

After installing the dependencies and Debtap, use index-corrected wrapper instead of HTTP/curl-k history wrapper:

```bash
cd "$HOME/ricy-kit"
sudo bash contributions/target-implementation-fixes/update-indexes.sh
cd contributions/dolphin-deb-rpm-installer
python install-integration.py
```

The window converts as user, displays metadata and offers Install via Polkit/pacman. RPM with scriptlets is refused. Compatibility of each external app must be checked separately; do not use --nodeps/--overwrite.

## 8. Check and load all

If you have selected another login manager, restart the computer. Otherwise, close the session normally and re-enter Plasma Wayland. This also allows you to check login and noctalia autostart. Do not restart SDDM from within a session you want to preserve.

```bash
systemctl --user is-enabled ricy-noctalia-integracao.service
systemctl --user is-active noctalia-teste.service noctalia-busca-desktop.service
kreadconfig6 --file kcminputrc --group Mouse --key cursorTheme
kreadconfig6 --file kcminputrc --group Mouse --key cursorSize
kreadconfig6 --file kdeglobals --group General --key font
kreadconfig6 --file kwinrc --group org.kde.kdecoration2 --key library
fc-match 'JetBrainsMono Nerd Font'
```

Visually check login/block, cursor 16, menus/sources, wallpaper, monitors, search and clipboard. For a preview of the lock without blocking the session: `/usr/lib/kscreenlocker_greet --testing` Previous tests and their limitations are in the READMEs and registration.

## 8th Dolphin with Noctalia identity (optional)

After configuring KDE-Noctalia/Kvantum:

```bash
cd "$HOME/ricy-kit/contributions/dolphin-noctalia-identity"
python apply.py
```

Requires Qt6 Widgets/headers, g++, pkg-config and Noto Sans. Build private Qt helper, apply exclusive variant, Noto Sans font, alpha background 0,70 with blur, chips on the side (icon + name), rounded lines and header. Reabra Dolphin by launcher to load the helper; old processes do not receive it by QSS.

For native outside corners 16 px, follow the contribution ricy-kit/contributions/dolphin-blur-corners/README.md: build.py requires KWin headers 6.7.5 and indicated dependencies, installation of the library in system directory with sudo and enable-corners.py. Do not restart KWin; when updating your version, review the API and recompile before reusing the effect. Qt transparency does not apply opacity to texts/icons. Existing ricyblur Blur provides the background. Reproduction, limits and reversal in the READMEs of the two contributions; global KDE source and preserved archives operations. Updated atomic exchange library. Native sidebar delegate, folder expansion/navigation on enabled compacted and '+' selection turned off. Chips accompany viewport by reducing window; children back down as hierarchy. Read evidence/limits at the end of dolphin-blur-corners/README.md.


## Restore to destination

The DATA-HORA paths below are examples; use printed paths in the new installation. Do not copy source backups. To return to Plasma:

```bash
"$HOME/.local/bin/ricy" plasma
```

To reactivate Noctalia:

```bash
"$HOME/.local/bin/ricy" noctalia
```

To undo the new appearance contribution:

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python ../login-matched-lock-screen/restore.py "$HOME/.local/state/ricy-lockscreen-backups/DATA-HORA"
python ../konsole-animated-cursor/apply.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
python user.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python system.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

If you applied appearance twice (e.g. to include extensions), use backups in the reverse order of applications. Reversion restores the saved files and can replace later changes in those same files. Again choose your previous wallpaper by Plasma has changed the image. Dolphin restorer is independent and uses backup issued by your installer.

This package is a portable backup of configurations and appearance assets; it is not a disk image. Drivers, resolution/scale of monitors, network connections, devices, accounts, passwords and application data should be configured on the new host. History contains replaced old settings; use the order of this guide and the final contributions to the reset.
