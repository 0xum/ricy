# Continuous notifications with the taskbar

Distributed Preferences in config.toml Noctalia integration:

```toml
[notification]
position = "bottom_right"
follow_focused_output = true
background_opacity = 0.70
border = false
offset_x = 0
offset_y = 0
```

Notifications appear on the active monitor, next to the lower taskbar and the right edge, with the same transparency. 5.2.1 already draws a time bar that decreases until it expires; when passing the pointer, the count pauses. Persistent warnings without a deadline do not gain an artificial deadline.

The native card leaves a rounded cut at the junction with the taskbar. `notification-right-corner.patch` keeps the lower right corner straight and opens the bottom left corner out, with a concave curve that finds the bar. The top two corners remain rounded. This applies when the position is bottom_right with offset_x=0 and offset_y=0. The surface reserves space to the left without reducing the content or moving the card from the right edge. Drawing, clipping of the animation and blur region follow this geometry, without changing the logic of the daemon or countdown.

## Reproduce

First prepare and install the permanent integration Noctalia of this kit. This contribution was made to Noctalia **5.2.1**, commit upstream `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. The script refuses other versions; review/rebase the patch before migrating to another Noctalia.

In CachyOS/Arch, check out the dependencies of BUILDING.md upstream. In this destination it was necessary to add only:

```bash
sudo pacman -S --needed meson ninja wayland-protocols nlohmann-json stb
cd "$HOME/Projects/ricy/ricy-kit/contributions/notification-continuity"
bash build.sh
python enable.py
```

Compilation uses prefix /usr only to find package assets; does not execute `meson install` and does not replace `/usr/bin/noctalia`. The local executable is in `$HOME/.local/lib/ricy-noctalia/noctalia`, selected by a drop-in of the unit noctalia-teste.service. The original CLI continues to send IPC to the same shell. The source/build code is in the user cache outside the kit.

`enable.py` saves previous binary/drop-in, recharges the drive and restarts the shell/adapter. During this exchange temporarily applies KillMode=process to preserve the applications launched by the menu; removes this override right after the switch. The permanent unit closure setting is maintained.

Updating the Noctalia package does not automatically update the local executable. Updating the version, review the patch and recompile, or restore the original package before adopting assets/configuration of the new version.

## Restore

```bash
python enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Use backup printed by activator (contains manifest.json), which restores the previous shell selection and its local binary, if any. This does not reverse visual preferences in config.toml; to do this restore the configuration backup or adjust only `[notification]`. The applicator does not remove packages.

Upstream code under MIT license, included in LICENSE. References: [notifications](https://docs.noctalia.dev/noctalia/services/notifications/) and [version compilation](https://github.com/noctalia-dev/noctalia/blob/v5.2.1/BUILDING.md).

## Home Card Wallpaper with Desktop Plasma

The local variant also allows the Home card to use the path configured when `[wallpaper] enabled = false`. Noctalia continues without drawing the desktop background; the card thumbnail is loaded independently by the native thumbnail service. The opacity and blur of the panels remain the same.

After building/activating, register the image of Plasma desktops:

```bash
python sync-wallpaper.py
```

The script uses the Plasma API and only goes on when all desktops use the same local static image. settings.toml from private backup integration and uses Noctalia's IPC wallpaper-set to register that same image (the API also syncs selection with Plasma). Different, animated or missing files are rejected before changing preferences. Do not copy personal images to the kit. Run again if you change the wallpaper in Plasma; this contribution does not install an automatic change monitor.

The image is from Home Card; the rest of the menu keeps the background translucent with blur from the scene behind it. The wallpaper is not drawn on the entire panel. Restore the binary by the activator also restores the previous behavior of the card; settings.toml and Plasma wallpaper are separate preferences. Review a backup of settings before restoring it as it contains other preferences.

## Current compound variant

To also play the Taskbar menu as a Noctalia panel fitted and without scrolling, use ../taskbar-menu-composition/build.sh and its full patch. This previous compiler remains as a reference for the notification/Home variant; it correctly refuses a cache with different changes. The activator/restaurator of this folder continues to be used by the new variant.

## Update: Tray menus

The current state also includes the options of the Tray items as Noctalia panel and set to return to the drawer. To rebuild all changes, use ../tray-menu-composition/build.sh and its patch complete. This previous compiler remains as historical reference and refuses different cache.
