# Reorganize application icons

> **Current status (2026-10-11):** the cumulative RICY-001/UUID correction is ACTIVE
> after isolated build and activation; the earlier cache/binary is retained for rollback. The bundled
> `apply-animations.py` and window assets are HISTORICAL; use
> [window-fade-expand](../window-fade-expand/README.md) for the selected effect.
> Keep historical restoration interfaces and consult
> [CONTRIBUTION-AUDIT](../../../docs/CONTRIBUTION-AUDIT.md) before interpreting
> the earlier commands or session results below.

## Exact window activation

The KDE inventory now marks each nonempty KWin UUID as an exact window identity.
KNOWN: previously `windowsForApp()` supplied a UUID without `exactIdentity`, so
taskbar monitor/placement reconciliation could replace that UUID with another
window of the same application when the original window was absent from the
monitor's assignment list. The icon kept its original title and ordering key
while its action targeted another window. This was reproduced against the
preserved deployed build in the compiled regression fixture.

The fix uses the existing `TaskModel.exactWindowId` path for activation,
minimization and single-window close. App grouping, pinned-app cycling, icon
geometry, design values and window effects retain their existing behavior.
Ownership remains the cumulative Noctalia patch under the existing shell/KDE
integration boundary; no new dependency or architecture is introduced at runtime.

`validate-native-drag.py` also compiles `validate-window-identity.cpp`, which
feeds synthetic KDE inventory through the actual adapter and taskbar model, then
captures focus/toggle/close scripts on a private D-Bus KWin fixture. It covers
Brave/Dolphin identities, equal/different titles, both monitor bars, reversed
discovery, title/minimization changes and monitor moves. `dbus-run-session` is
required only for this offline test; no active compositor/window is contacted.
For comparison against the preserved earlier build, use `--identity-only`.

Build this revision in an isolated checkout with `RICY_NOCTALIA_SOURCE`; retain
the original cache and binary backup. Activation uses the existing
`notification-continuity/enable.py --bin <isolated-source>/build-ricy/noctalia`
application-preserving path. Restoration uses that activator's emitted backup,
without changing KWin, Plasma/Dolphin defaults or private settings. Build/offline
results and activation are recorded in [CHANGELOG](../../../docs/CHANGELOG.md).
PASS: 32 compiled model/action scenarios; the running executable matches the
isolated build and the KWin tracking adapter is owned by the new shell process.
PASS: the user reported successful icon focus in the real session after activation.
The exact application/monitor/title combinations were not independently recorded.
NOT RUN: agent-operated physical clicks/visual captures and a live Recovery round trip.

## Current single-space policy

RICY-001 supersedes the workspace-group descriptions preserved below. The current
cumulative patch disables the workspace widget (including named aliases), desktop
grouping/badges/navigation, workspace IPC/gesture commands and related settings.
Taskbar and window-switcher membership stays limited to visible desktops as an
internal window-management detail. Legacy configuration keys remain parseable but
cannot enable these interfaces. Plasma/KWin desktop support and recovery are
unchanged. See [the pre-change inventory](../../../docs/WORKSPACE-AUDIT.md).

Use a clean isolated source for this updated patch; the existing cache may contain
the earlier cumulative diff and the build deliberately rejects it. Set
`RICY_NOCTALIA_SOURCE=/absolute/path/to/isolated/source` for `build.sh` and
`scripts/verify`. Keep the old cache/binary and activation backups. Build and
offline verification are separate from activation. The earlier single-space
audit did not activate the shell; the subsequent window-identity fix activated
the maintained cumulative revision. Existing restore paths remain available.

For activation of an isolated build, the existing
activator requires `--bin "$RICY_NOCTALIA_SOURCE/build-ricy/noctalia"`; its default
still points to the preserved original cache. Do not activate that earlier binary
as evidence of the current policy. The activator creates a private rollback
backup and restarts shell/adapter; read its recovery instructions first.

`validate-native-drag.py` now also checks legacy grouping preferences, named
workspace aliases, widget picker/settings visibility, CLI command discovery and
workspace scroll defaults using the compiled Noctalia objects in a temporary
profile without a compositor connection.

The user confirmed “Passed” in the real session. Left-click, drag to the desired position and drop. The icon accompanies the cursor; a space indicates the destination and the neighbors change position. The gesture starts when overtaking the native drag threshold; one stopped click continues to restore/minimize. The consumed drag does not trigger opening, focus or minimization when dropping. Right button and middle-click keep the previous actions.

The upstream mechanism was limited to the fixed list. It now works across the entire flat range of applications, including unfixed open and launchers. Search is another widget and saves its position. Tray, controls and workspace grouping stay out of this reordering. Horizontal/vertical tracks use the corresponding axis, bounded to existing slots. Width of titles, scale and spacing enter the actual pitch of the tiles.

The preference `widget.taskbar.app_order` is saved by ConfigService in settings.toml from the active and re-applied profile when mounting the bar. It orders apps regardless of attachment; drag never fixes an application. The list preserves closed or filtered apps slots on another monitor/workspace. New unsaved apps enter at the end. Monitors using the same widget share the preference. settings.toml private in the kit.

Keys use app identity and occurrence number, no titles or persisted UUIDs. Duplicate windows keep your keys during updates; new instances can reuse a free slot. After restarting, the order of instances of the same app matches the natural discovery order; does not identify a specific document between restarts. Generation guards prevent saving indexes from a model that changed during the gesture. Cancellation restores the layout. The recording is postponed until the event is finished, protecting InputArea while reloading; the icon waits on the destination slot.

## Play current version

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/app-icon-reordering"
bash build.sh
python ../notification-continuity/enable.py
# Required when installing KWin effects for the first time:
python ../window-fade-expand/apply-animations.py
```

Font Noctalia 5.2.1, commit 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4. The patch is cumulative and includes notifications, wallpaper, menus, hover, actions, indicator and animations. Compiler refuses cache with different diff; for another variant, preserve cache and recreate clean font before applying. Installation preserves open applications and does not restart compositor. Review/recompile when updating Noctalia/KWin; dependencies on BUILDING.md upstream and ../notification-continuity/README.md.

## Checks

```bash
python validate-order.py
# Requires built-ricy ready; uses really compiled Noctalia objects:
python validate-native-drag.py
python validate-motion.py
python validate-actions.py
python validate-indicator.py
```

22 order scenarios, including 24 permutations, they've passed. 11 native scenarios instantiate TaskbarWidget/ConfigService in temporary profile, without connecting to the compositor: allow unfixed apps, move the tile, cancel, invalidate old model, delete consumed click, record and decode the order in new instance. 20 animation scenarios, 17 the shares and 15 indicator/effect passed. Compilation, reproduction, config validation, bash-n, git diff --check and application on clean source passed; all 17 patch files match the active source. Compared to the animation variant of icons, only TaskbarWidget (.cpp/.h), its definition and the new taskbar_order.h changed.

User confirmation after activation; real preference with two different slots was found and validated. There was no physical automation of drag: native tests cover logic and visual validation was made by the user. Private capture confirmed icons without black background. Further scales, vertical bars and model changes during a real drag have not been visually validated.

## Reversion

Backup before this activation: `$HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447`, which returns to the animations of icons with black background already fixed:

```bash
python ../notification-continuity/enable.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447"
```

The saved order remains in the profile; removing it restores the default order. KWin effects have not changed in this step. To return also to previous effects, use apply-animations.py  --restaurar with the backup of the keys/effect registered in the indicator-apps-animacoes contribution. To get back before the animations of the icons, the correct backup is 20261010-203450-476691; 203558-299413 contains the intermediate implementation with Black Box and is not recommended.

Nottalia/patch under MIT (LICENSE). KDE effect under GPL-2.0-or-later, preserved credits and separate license. Kit without binaries, screenshots, clipboard, accounts, private preferences, bytecode or backups.

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

## Updating of window animations

Noctalia continues to use this source/binary. For the current fade effect and expansion in all four actions, use ../window-fade-expand/apply-animations.py after compiling/activating this contribution. The KWin applicator of this folder records the previous step; the reference below describes the effects of that step. Read ../window-fade-expand/README.md for current values and reversal.
