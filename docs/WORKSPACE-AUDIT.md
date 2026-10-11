# RICY-001 workspace exposure audit

Date: 2026-10-11. The inventory below was completed before implementation changes.
Scope: active kit sources, public templates, cumulative and historical Noctalia
patches, KWin scripts/effects, switching/shortcuts, visual references, and the
transport kit. Read-only inspection also covered the active profile's workspace
options and shared KDE desktop shortcuts; private preferences are not reproduced.

The compatible source is Noctalia 5.2.1, commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. Before editing, its local cache diff
matched [the cumulative patch](../ricy-kit/contributions/app-icon-reordering/noctalia-ricy.patch)
byte for byte. Paths under `src/` below refer to that source, not files checked
into Ricy. KNOWN describes source evidence; live reachability remains UNKNOWN
unless separately validated. The accepted decision is [ADR-0001](adr/0001-single-workspace.md).

## Inventory before changes

| ID | Evidence / surface | Classification | Finding and disposition |
|---|---|---|---|
| W-01 | `src/shell/bar/widget_factory.cpp`, `widgets/workspaces_widget*`, settings `widget_settings_registry.cpp` | user-facing/remove | KNOWN: upstream workspace widget can be instantiated, including by a custom widget name/type, and selected in settings. Disable creation and picker exposure in the Ricy binary. Keep compatibility parsing. |
| W-02 | `widgets/taskbar_widget.cpp`, `taskbar_widget_definition.cpp` | user-facing/remove | KNOWN: configurable grouping, labels, badges, counts/dots, capsule clicks and adjacent-workspace scroll navigation. Force flat application presentation regardless of legacy settings; hide grouping/label options. |
| W-03 | Same taskbar source, `activateTaskModel()` fallback | user-facing/remove | KNOWN: fallback explicitly activates a task's workspace. Remove this navigation fallback while preserving UUID/window activation. |
| W-04 | `src/app/application_ipc.cpp`, `src/cli/schema_msg.h` | user-facing/remove | KNOWN: `workspace-switch` is a registered IPC/CLI command usable by shortcuts and widget gestures. Remove registration and CLI discovery; reject the legacy verb before opening a client socket. |
| W-05 | Same IPC/schema files | user-facing/remove | KNOWN: five `workspace-alert-*` commands expose workspace identifiers and attention markers. Remove registrations/discovery and reject legacy client verbs; retain internal services/data. |
| W-06 | `src/shell/bar/widget_gesture_defaults.cpp` | user-facing/remove | KNOWN: workspace-widget scroll defaults invoke `workspace-switch prev/next`. Remove those bindings; preserve app reordering and task cycling. |
| W-07 | `src/shell/settings/settings_registry.cpp`, `src/shell/bar/bar.cpp` | user-facing/remove | KNOWN: bar/monitor settings offer reveal on workspace change; bar reacts to desktop changes. Remove settings and workspace-triggered reveal; retain window-sensitive smart auto-hide. |
| W-08 | Settings registry, `src/shell/switcher/window_switcher.cpp` | user-facing/remove | KNOWN: window switcher settings name the current workspace and offer cross-workspace filtering changes. Hide this option and keep visible-desktop membership as fixed internal behavior. Window switching itself is permitted. |
| W-09 | Both active-kit `outputs/noctalia-test/config.toml` templates and private profile | internal/harmless | KNOWN: `only_active_workspace=true` filters window membership; it does not create an indicator/switcher. Keep it as internal compatibility data, explicitly disable grouping/labels in public templates. Workspace-change reveal is already false. Do not publish or rewrite the private profile. |
| W-10 | Cumulative patch `src/compositors/kde/kwin_active_window.cpp`; action/indicator validators | internal/harmless | KNOWN: KWin's `workspace.windowList`, `activeWindow`, signals, UUIDs and desktop metadata support exact window focus/minimize/close. Preserve APIs, identifiers and tests. |
| W-11 | `src/compositors/compositor_platform.*`, workspace backends/protocols, assignment models | internal/harmless | KNOWN: compositor metadata and membership are needed by window tracking. Retain KWin virtual-desktop support and Noctalia backend data; disabling product UI does not require deleting infrastructure. |
| W-12 | [Wallpaper synchronization](../ricy-kit/contributions/notification-continuity/sync-wallpaper.py), kit preparers and wallpaper applicator | internal/harmless | KNOWN: Plasma `desktops()` / `desktopById()` enumerate containments to read/write wallpaper. No desktop-navigation UI is introduced. Preserve. |
| W-13 | `login-lock-cursor-appearance/assets/kwin/scripts/windowsarrows/` | internal/harmless | KNOWN: `KWin.Workspace` operates on active windows for quick tiling, maximize/restore/minimize. Super+Arrow window arrangement is not desktop navigation. Preserve. |
| W-14 | Same contribution, `adaptivepanelwidth/contents/code/main.js` | recovery/preserve | KNOWN: desktop/activity membership and change signals adjust a Plasma panel's width. No desktop switch/move is performed. Preserve shared Plasma behavior. |
| W-15 | [Switching integration](../ricy-kit/contributions/plasma-noctalia-switching/integration.py), `panels.py`, installers/restorers, original archives | recovery/preserve | KNOWN: saves/restores Plasma panel groups and displaced menu/clipboard shortcuts. Desktop containments/widgets and backup paths are protected. No Ricy workspace shortcut is registered here. Preserve all return paths. |
| W-16 | Shared `kglobalshortcutsrc` desktop/Overview/Grid actions; KWin window menus and KDE System Settings | recovery/preserve | KNOWN: desktop-switch/move and Overview/Grid shortcuts remain assigned in shared KDE settings. INFERRED: native KWin menus and desktop settings remain reachable through KDE. They belong to the shared recovery environment. Do not clear shortcuts, remove KCMs, reduce desktop count or change compositor support. Runtime reachability during Ricy is UNKNOWN. |
| W-17 | `login-lock-cursor-appearance/assets/plasma/desktoptheme/` (including `pager.svgz`, `switch.svgz`), SDDM/theme packages | recovery/preserve | KNOWN: upstream Plasma assets and package names such as `plasma-workspace` are not Ricy workspace features. Preserve assets, catalogs and licenses. |
| W-18 | KWin gestures/screen edges/Overview, native effect implementations | uncertain | No Ricy-owned desktop gesture/edge binding was found in public scripts/preferences. Shared/default gestures may remain live even without explicit settings. Disabling shared effects/edges would change Plasma Recovery; leave unchanged and require a prepared live audit. |
| W-19 | Taskbar desktop-entry actions, tray DBusMenu, launcher KDE applications, private materialized plugins | uncertain | KNOWN: app/tray actions are supplied externally; Ricy taskbar's own menu exposes pin/close/app actions, with no built-in move-to-desktop entry. Private plugin catalogs are not evidence that a plugin is active. Preserve external actions; live plugin/application coverage is UNKNOWN. |
| W-20 | Earlier cumulative Noctalia patches; `docs/ricy-kit/`; historical archive/manifests | internal/harmless | KNOWN: historical variants retain grouping references and executable reproduction scripts. They are not the current source and are not compliant replacements. Preserve history; do not synchronize the transport kit or manifests. Document the current variant as required for Ricy. |
| W-21 | [Identity tokens](../ricy-kit/contributions/noctalia-visual-identity/tokens.json), current identity README and [guide](VISUAL-IDENTITY.md) | user-facing/remove | KNOWN: current reference lists workspace badges/groups as unaffected surfaces. Supersede this implication with explicit exclusion from the Ricy product; preserve numeric design values and historical descriptions. |
| W-22 | `core/`, `shell/noctalia/`, `compositor/kwin/`, `apps/`, `services/`, `integrations/`, `recovery/` | internal/harmless | KNOWN: reserved structure/documents, not additional executable workspace UI. Preserve architectural reservations. |
| W-23 | Upstream Noctalia dock membership/smart-auto-hide, Niri/Umbriel overview integrations and non-KDE backends | internal/harmless | KNOWN: dock metadata does not add desktop navigation; the Ricy templates disable the dock. Non-KDE overview settings are gated to their compositor and not enabled by the KWin integration. Preserve upstream internals rather than refactor unrelated compositors. |

## Implementation boundary and recovery

Ricy owns the Noctalia patch and its public templates. The safe implementation
changes that shell only. No new session architecture, KWin replacement, global
shortcut rewrite, installation or live session switch is authorized by this
audit. Plasma/Dolphin tools, installed units, panels, effects, virtual-desktop
count and private snapshots remain unchanged.

Legacy workspace configuration keys remain parseable so an existing profile does
not fail readiness validation. They cannot re-enable Ricy grouping/navigation.
Window membership remains internal: retaining only currently visible windows
avoids offering focus targets on other desktops. KWin may still switch desktops
through its own shared shortcuts/menus. Complete session compliance is therefore
UNKNOWN; the current coexistence limitation in [RECOVERY](RECOVERY.md) remains.

Implementation changes ten source files relative to the previous cumulative
variant. The complete patch still carries its earlier window, notification, menu,
motion and ordering changes. The public templates explicitly set grouping and
workspace labels to false; numeric design tokens are unchanged. The shell and
integration contribution retain their existing ownership and dependencies. The
harness accepts `RICY_NOCTALIA_SOURCE` for an isolated pinned checkout and runs the
extended native policy/drag validator when its compiled objects are available.

## Validation and delivery

Validation results and build/activation limits are recorded after implementation
in [CHANGELOG](CHANGELOG.md). The patch must be built separately before activation;
the running binary and private source cache are not replaced by this task.
Live visual, gesture and recovery trials require a prepared session and remain
NOT RUN in this offline audit.

Subsequent task: the window-identity correction activated the maintained
cumulative RICY-001/UUID build on 2026-10-11, with the previous binary/cache
preserved. See [CHANGELOG](CHANGELOG.md). This does not retroactively change the
offline audit's validation scope or prove live gestures/Recovery.

PASS: isolated release build, complete harness with the selected source, native
legacy-profile/widget/alias/picker/settings/CLI regressions, public template
validation, clean cumulative patch replay and original-cache preservation. The
native CLI checks use an isolated runtime/socket namespace. One preliminary
argument-free `workspace-switch` probe reached the old shell and returned its
required-arguments error; no desktop transition was requested or performed.
The final client now rejects workspace verbs before attempting a connection.
