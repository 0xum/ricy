# Application indicator and window animations

The user confirmed restoring/minimizing the icon and closing with the middle button. This variant adds visual response to the states of the windows.

## Taskbar purple ball

The indicator keeps the color set in Noctalia:

| Status | Opacity | Visual scale |
|---|---:|---:|
| Active Window |  1,00  |  1,00  |
| Opened in the background |  0,55  |  0,82  |
| minimized |  0,28  |  0,65  |
| Icon fixed without window |  0,00  |  0,55  |

Transition from 160 ms, EaseOutCubic, in the Native AnimationManager, respecting the motion/speed of the shell. The animation starts from the current visual value when interrupted. The values are preserved when tiles are reconstructed, allowing also to gently delete the indicator of a fixed closed app. Unfixed icon is removed when your last window closes. Do not change the area of click, layout, hover icons or trace options. The show_active_indicator option continues to be respected. When there are visible titles, the indicator line uses the same states. Workspaces summary points maintain its composition.

The KDE script now sends the minimization status of each UUID and connects minimalizedChanged. A minimized window does not remain active by ancient focus retained on a shell surface. Active selection prioritizes UUID, avoiding lighting another window of the same title. In grouped fixed, the minimized state means that all windows are minimized; in the workspace groups, the representation prioritizes an active or visible window. The ToplevelInfo structure also preserves the state announced by wlr when available.

## Animations in KWin

ricywindowactions derives from KDE's squash effect: compresses/displaces/smears to minimize and reverses to restore, with base duration 240 ms, InCubic/OutCubic. Fast reversals reuse the animation; if not possible, it is cancelled before the new one. Keeps blur forced during the transition and releases it when finished.

The native effect Squash does not animates without iconGeometry. Noctalia does not publish this Plasma icon geometry. This variant uses geometry when provided; in the absence of it, it uses a Plasma destination 18×18 on the same monitor, centered on the horizontal of the window and 22 bottom edge px, Taskbar reference 44 px. This destination is approximate: it is not the exact position of the icon. It does not move the window from one monitor to another. For bar in another position/height, review the fallback destination. It only animates normal windows that appear in the taskbar; panels, search, track and full screen effects do not receive this animation.

Opening/closing use the native effect Scale, base duration 180 ms, scale 0,92↔1 and fade. Closure occurs after the application accepts the request, respecting save dialogues. Scale can also animate dialogues according to its native implementation. Disabled squash/magic lamp and fade to avoid overlapping with the chosen effects. Smooth Window Geometry remains.

animationTime respects the global speed of KDE. In the validated session, AnimationDurationFactor=0,25 reduce 240 ms for about 60 ms and 180 ms for about 45 ms. Global preference has been preserved. Noctalia and KWin have independent movement preferences; the mentioned times are of reference, not real latency measures. Previous compositions and ricyblur remain.

## Reproduce

Font Noctalia 5.2.1, commit 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4; validated effect on KWin 6.7.5. Build Dependencies: BUILDING.md upstream and notifications-continuity. Applicator requires Python, kwriteconfig6 and qdbus6 in session without sudo.

```bash
cd "$HOME/ricy-kit/contributions/app-indicator-animations"
bash build.sh
python ../notification-continuity/enable.py
python apply-animations.py
```

The full patch preserves previous contributions. The compiler accepts clean font or exactly this diff; when migrating, preserve the previous cache and use clean font as per taskbar-menu-composition/README.md. Adjust paths when XDG_CACHE_HOME is set. Do not replace /usr/bin/noctalia. The shell activator preserves applications during the exchange. The effect applicator records backup of the changing keys and the previous local package, installs in XDG_DATA_HOME/kwin/effects/ricywindowactions and loads without restarting KWin. Review/recompile when updating the Noctalia/KWin versions.

## Validation and reversal

Compilation, playback, bash-n, profile validation, git diff --check and reverse patch application passed. Compared to taskbar-app-actions: additional changes limited to TaskbarWidget, KwinActiveWindow and WaylandToplevels, each with source/header. Other preserved blocks.

```bash
# Require Python/PyQt6; performs actual JS extracted from source without actual windows.
python validate-actions.py
python validate-indicator.py
# Alternative source:
python validate-indicator.py --fonte /caminho/para/noctalia
```

17 scenarios preserve restoration/minimization/closement and exact identity; 15 check signal of minimization, serialization, focus, monitor fallback, reversal and blur cleanup. A disposable Qt window in the real session confirmed states of restoring/minimizing/restoring and closing, with the effects effectively active during transitions. Local captures verified the change of the active indicator→minimized; captures are not distributed. 0,25 it requires to observe the effect before 60 ms: an initial consultation after 65 ms lost the animation; check within the transition passed. Test Scripts/object DBus removed. No working window has been closed. User confirmation is from the previous variant; this setting still awaits visual evaluation of it. Do not validate all groups, applications, scales or real fast movements.

To undo, restore both parts using printed backups:

```bash
python apply-animations.py --restaurar "$HOME/.local/state/ricy-indicador-animacoes-backups/DATA-HORA"
python ../notification-continuity/enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Nottalia/patch under MIT (LICENSE).2.0-or-later, with credits preserved in main.js and separate licence in LICENSE-KWIN-GPL-2.0-or-later.txt. Kit without binaries, captures, clipboard, accounts, private status, bytecode or backups.

## Later variable: icons and drag

The current cumulative reference is ../icones-apps-reordenacao. Includes pulse/bounce by status, black background correction and persistent reordering of apps. To rebuild the current session use the compiler of this contribution.
