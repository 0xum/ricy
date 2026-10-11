# Tray Item Options in Noctalia Composition

> **Grounding status:** This is a HISTORICAL cumulative variant; its commands and test results describe an earlier stage.
> Use [CONTRIBUTION-AUDIT](../../../docs/CONTRIBUTION-AUDIT.md) and
> [DEVELOPMENT](../../../docs/DEVELOPMENT.md#historical-reproduction) before using
> the recipes below. The builder requires explicit opt-in and an isolated source;
> it cannot use the deployed cache. Current source development belongs to
> [app-icon-reordering](../app-icon-reordering/README.md), whose current patch is
> MIGRATE pending activation. Historical effect installers are not current defaults;
> preserve their restoration interfaces and backups.

DBusMenu menus of tray items use the native panel embedded `ricy:tray-menu`, with bottom/opacity of the bar, continuous blur, junction, animation and external closure of PanelManager. The presentation replaces the independent popup; actions and states continue provided by the application.

In the bottom bar there is a **set down at the base of the menu**, next to the bar. It goes straight back to the tray drawer, keeping monitor, bar and anchor. The horizontal reference is the center of the drawer, regardless of the icon clicked. Menu and return use the same axis; the arrow attached this axis even when a wider menu needs to be moved by the monitor limit. The button uses the native Ghost style: transparent background and highlight when passing the mouse. It is also present inside submenus when the drawer is enabled.

Pin/Unpin, separators, disabled inputs, selection marks and radio options are preserved. Submenus navigate within the same composition, with `← Back`, left/scape to climb a level; Escape at the root and external click close. Arrows run enabled actions; Enter/Space activate, right enters submenu. The return button also participates in Tab navigation. Actions are postponed until the end of the event and check the current line before the drive. Opened/closed events continue to be sent to the provider.

The width considers the largest text and has minimum content of 240 px at scale
1. Height includes all lines, separators, native padding and button
return, without repeating the padding already discounted by PanelManager. There is no scrolling when the list fits on the monitor; ScrollView allows you to access larger lists than the available area. Loading on demand and updates DBusMenu keep the retry limited and resize the composition as the lines change. When removing the track item, the menu closes.

Items without DBusMenu continue to deliver their menu to the app itself. Actions, including updating packages or leaving, keep the original meaning.

## Reproduce

Compatible with Noctalia 5.2.1, commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. This composite patch brings together notifications, Home wallpaper, Taskbar menu and Tray items menu.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/tray-menu-composition"
bash build.sh
python ../notification-continuity/enable.py
```

Dependencies: BUILDING.md upstream and contribution notification-continuity. The compiler accepts clean font or exactly this patch; does not overwrite unknown changes. To migrate from variant, preserve the previous cache in a name that is still missing before recompiling in clean font, as per taskbar-menu-composition/README.md. Adjust the path if XDG_CACHE_HOME is configured. The activator creates backup and preserves applications during the exchange. It does not replace `/usr/bin/noctalia`. Shared blur requires Blur-Continuity contribution corresponding to the installed KWin.

## Validation and return

Compilation and validation of the profile passed. The user visually confirmed the composition of the track menu and then the set of return to the drawer. The user also confirmed the subsequent adjustment of the horizontal alignment between menu, set and drawer. 45 Geometric scenarios of widths and borders, in addition to profile compilation/validation. Complete tests of submenus, selection states, actions of each application, extensive lists and other bar positions have not yet been registered. A temporary test provider has been registered and removed; the attempt to automate the click did not open its menu, so it does not confirm the actions or submenus. Temporary devices and scripts have been closed.

To check, open the drawer and menu of an item, click the lower arrow and check the return to the drawer on the same monitor. Also check Escape, submenus and a safe action before using actions like closing or updating.

To restore the previous binary, use the backup printed by the activator:

```bash
python ../notification-continuity/enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Upstream MIT code; license included. The kit contains only public code and documentation; no binaries, captures, clipboard, accounts or private status.

## Current variant: icons and hover

The later variant maintains this menu/alignment and adds smaller app icons and search with smooth zoom when passing the mouse. To rebuild the current full state, use ../app-icon-interactions/build.sh. This previous compiler remains historical and refuses cache with different changes.
