# Click to restore/minimize and middle button to close

Current behavior of application icons in the KDE/KWin taskbar:

- Left click restores and focuses the minimized window.
- If the window is visible and focused, the left click minimizes it.
- If the window is visible behind another window, the click brings it forward.
- Fixed icon without running window starts the application.
- Middle button asks to close a window; preserves save dialogues.
- Right button keeps the Noctalia menu; drag keeps sorting fixed.

In grouped icons, the click prioritizes the active application window to minimize. No active window in the group, preserves the existing selection/cycle to restore or focus a window. It does not add previews or selection of groups identical to Windows. The middle button closes the active/representative window without closing all windows. Icon without open window ignores this button.

The user clarified that “opening minimized” meant restoring by the icon and confirmed this implementation with “Passed”. Then he also requested to minimize the window opened by the icon. Middle-click binding already existed. Previous restoration was validated by the user; the new alternation has the tests below and awaits confirmation of physical interaction in the session.

## Implementation

KDE adapter uses `window.minimized = false` before activating/restoring. Only left clicks on the taskbar pass `toggleMinimize = true`. The script consults the current state in KWin: minimizes only the focus window, not minimized and minimized. Search, dock, navigation shortcuts and other activation calls continue to only restore/focus. In other compositors, this method preserves the original activation; the alternation implemented in this variant is KDE/KWin specific.

With UUID available, the selection exclusively uses the exact identity. Class/caption is fallback only without UUID; obsolete UUID does not trigger another window with equal title. Closing calls `closeWindow()` and removes the previous fallback that just minimized. This also benefits the Close menu.

Smaller icons/hover, menus, junctions, tray, volume, network, clock and control-center preserve their previous implementations.

## Reproduce

Noctalia 5.2.1, commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. Full patch includes all previous patches. This is the reference compiler of the current variant.

```bash
cd "$HOME/ricy-kit/contributions/taskbar-app-actions"
bash build.sh
python ../notification-continuity/enable.py
```

Dependencies: BUILDING.md upstream and contribution notifications-continuity. The script accepts font clean or exactly this patch. To migrate from a previous variant, preserve the cache in a still non-existent path and compile in clean font as per taskbar-menu-composition/README.md. Adjust the paths if XDG_CACHE_HOME is configured. The activator preserves applications and creates binary/drop-in backup; `/usr/bin/noctalia` remains intact. Review and recompile when updating Noctalia; the blur keeps its own KWin version.

## Verification and return

Compilation, script playback, profile validation and git diff --check passed. The additional diff to the app-icon-interactions variant affects the TaskbarWidget, ComposerPlatform and KwinActiveWindow widgets, each with its header; the other blocks of the previous patch are preserved.

Seventeen tests run the actual JS scripts extracted from the source in QJSEngine: restoration and closing by UUID/class-caption, duplicate titles, obsolete UUID, exclusion of non-normal windows, absence of fallback from minimizing closing, alternation of the active/minimized window, focus of the inactive visible window, non-minimizable window, common activation without minimizing and pointer.

After preparing the source, repeat the isolated tests with Python/PyQt6:

```bash
python validate-actions.py
# Or source at another location:
python validate-actions.py --fonte /caminho/para/noctalia
```

Also used was a disposable Qt window in the actual session: minimized, restored/focused, minimized again, restored again, kept visible by a common activation and closed by UUID. The sequence checks the states directly in KWin, without depending on the client's Qt state for minimization. Test DBus Scripts/object were removed. No user working window was closed. This check exercises the adapter; it does not physically simulate the click on the icon, nor covers all applications/groups. Check the alternation by the icon and the middle button in a workless window.

To return to the previous variant, use the backup printed in the activation:

```bash
python ../notification-continuity/enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Upstream MIT code, license included. Kit without binaries, catches, clipboard, accounts, private status or session backups.

## Current variant: indicator and animations

The user confirmed the alternation of this variant. The later app-indicator-animations contribution preserves the actions and adds ball by state, transition and KWin effect. To rebuild the current full state, use ../app-indicator-animations/build.sh and apply-animations.py. This previous compiler remains historical and refuses cache with different diff.
