# Status icon animations

> **Grounding status:** This is a HISTORICAL cumulative variant; its commands and test results describe an earlier stage.
> Use [CONTRIBUTION-AUDIT](../../../docs/CONTRIBUTION-AUDIT.md) and
> [DEVELOPMENT](../../../docs/DEVELOPMENT.md#historical-reproduction) before using
> the recipes below. The builder requires explicit opt-in and an isolated source;
> it cannot use the deployed cache. Current source development belongs to
> [app-icon-reordering](../app-icon-reordering/README.md), whose current patch is
> MIGRATE pending activation. Historical effect installers are not current defaults;
> preserve their restoration interfaces and backups.

The user confirmed restoring/minimizing the icon and closing with the middle button. This variant adds visual response to the states of the windows.


## Icon response

Each real state change triggers a short animation without loops:

| Action | Motion | Basic duration |
|---|---|---:|
| Open | Two cushioned heels and a light pulse. |  420 ms |
| Restore | Two smaller cushioned jumps |  360 ms |
| Gain Focus | Pulse without displacement |  260 ms |
| Minimize | Vertical compression towards the bar |  220 ms |
| Lose focus | Discreet reduction/decrease |  200 ms |
| Close fixed app | Contraction/decease, returning to launcher |  240 ms |
| Close unfixed app | Dissolve removed icon, scale 1→0,72  |  220 ms |

AnimationManager/MotionService natives respect the motion and speed of the shell. Stable state remains still; first assembly does not animates all apps. Reconstructions and interruptions preserve the current visual progress. Hover remains in the child icon, separated from state transformations. Slot and click area remain stable. Displacement follows the orientation of the bar. Search keeps only your hover; trace, volume, clock, network and Noctalia button keep their previous interaction.

The slot uses Node without painting. The first implementation with Box left a black rectangle behind the icon, reported by the user. Fixed using Node; private session captures confirmed removal. The closing ghost is non-interactive, ignored by layout and removed with lifeguards. It only appears when the exact identity of the window came out of the compositor; changing monitor, filter or fixing does not produce false closing.

20 C++ scenarios check states, pulse/bounce, limits, interruption, cancellation by owner and disabled movement, using the real header and AnimationManager. `python validate-motion.py`. Previous validators of actions and indicator remain included. A real disposable Qt window confirmed restore/minimize/restaurate/close and KWin effects. Captures verified bounce and compression; there is no conclusive capture of the closing ghost or test of all scales/groups.

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
cd "$HOME/Projects/ricy/ricy-kit/contributions/app-icon-states"
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

## Subsequent variant: reorganization

The current full reference is ../app-icon-reordering: preserves these animations, fixes the black background and lets you drag all apps, saving the order. Your historical compiler requires diff of this variant; to rebuild the current session, use ../app-icon-reordering/build.sh.
