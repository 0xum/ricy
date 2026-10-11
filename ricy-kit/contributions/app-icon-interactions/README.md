# Smaller icons and hover animation for apps and search

In the bar, the application icons and the search magnifying glass stay 12Smaller % at rest. When passing the mouse, they grow smoothly to the previous visual size; when leaving, they return to the reduced size. Input and output last. 140 ms, with EaseOutCubic, respecting the movement/speed configuration of Noctalia. Reenter during animation continues from the current progress.

The effect transforms only the icon design: click area, spacing, layout of the bar, titles and indicators remain fixed. It applies to images, application fallback icons, and the search launcher image/glyph. It does not modify track or its menus, volume, clock, network, control-center/ Noctalia button, nor does the effect of workspace labels/badges. The existing background highlight of the apps accompanies the hover of 140 Ms.

Implementation in TaskbarWidget and LauncherWidget. Scale constants on both archives should be kept consistent: kAppIconRestScale=0.88 and kAppIconHoverDurationMs=140. Use Native AnimationManager and cancel the previous animation by changing the destination; scene owners cancel animations by destroying the nodes. Transformations mark only repainting, without recalculating the layout.

## Reproduce

Noctalia 5.2.1, commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. The complete patch also preserves notifications, Home wallpaper, Taskbar menu, Tray menu/return and its horizontal alignment. This is the reference compiler of the current variant.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/app-icon-interactions"
bash build.sh
python ../notification-continuity/enable.py
```

The compiler accepts clean font or exactly this patch. To migrate from a previous variant, preserve your cache in a still non-existent path and compile it into a clean font as per taskbar-menu-composition/README.md. Adjust the path if XDG_CACHE_HOME is set. Dependencies: BUILDING.md upstream and contribution notifications-continuity. The activator preserves applications, creates binary/drop-in backup and does not replace `/usr/bin/noctalia`. Review and reward when updating Noctalia; the shared blur remains linked to the blur-continuity contribution to the installed KWin.

## Validation and restoration

Compilation, script playback, profile validation and git diff --check The patch was compared to the previous one: only the files of the taskbar and launcher widgets changed; previous fixes and other widgets were preserved. Visual confirmation and tests of click/scramming applications, fast hover, different scales and disabled movement have not yet been recorded in this review.

Pass the mouse over apps and magnifying glass to check for smooth zoom and reduction without moving the bar. Also check to click, switch windows and drag a fixed app. Compare trace, volume, clock, network and control-center with the previous state. To restore, use the backup printed by the activator:

```bash
python ../notification-continuity/enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Upstream MIT code, license included. No binaries, captures, clipboard, accounts, backups or private state in the kit.

## Current variable: icon actions

The later variant keeps these icons/hover and adds restore/minimize by left click in KDE/KWin, with exact middle button closure. To rebuild the current full state, use ../taskbar-app-actions/build.sh. This previous compiler remains historical and refuses cache with different diff.
