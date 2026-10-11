# Ricy Architecture

## Evidence and authority
Investigation snapshot: 2026-10-11. **KNOWN**: confirmed in a cited file/script,
not necessarily revalidated at runtime. **INFERRED**: a reasonable conclusion
from evidence. **PLANNED**: an accepted decision not yet implemented.
**UNKNOWN**: insufficient evidence; do not fill gaps with plausible assumptions.

[Invariants](INVARIANTS.md) → [ADRs](adr/README.md) → architecture/components →
local rules → implementation. Record conflicts and their scope.

## CURRENT — KNOWN
The [previous README and historical record](ricy.md) and the `start.sh`, `return.sh`,
and `switch.sh` wrappers point to `ricy-kit/contributions/plasma-noctalia-switching/ricy`.
`ricy-kit/` is the active kit; `docs/ricy-kit/` is the preserved transport copy,
not an automatically synchronized mirror. `archives/ricy.zip` is historical.
No `.git` was found at the root during the investigation; no local versioned
history was confirmed. This stage does not initialize Git or publish files.

```text
CachyOS / Plasma Wayland session
└── KWin (compositing and windows)
    ├── plasmashell (shared desktop/wallpaper)
    ├── Noctalia + search adapter + Ricy integration
    │   └── Plasma panels hidden after the shell becomes ready
    └── Plasma return: panels/shortcuts/KRunner restored
```

Evidence: [integration](../ricy-kit/contributions/plasma-noctalia-switching/integration.py),
[autostart](../ricy-kit/contributions/noctalia-autostart/README.md), and
[switching command](../ricy-kit/contributions/plasma-noctalia-switching/ricy).
Switching changes the shell within the existing session; it does not replace the compositor.
The status helper observes a systemd unit; it does not prove session health.

## TARGET — PLANNED
```text
CachyOS
└── KWin / Wayland
    ├── Ricy Desktop
    │   ├── Noctalia Shell
    │   ├── Ricy Core / Services (responsibilities still to be defined)
    │   └── Ricy Files and future applications
    └── Plasma Recovery
        └── plasmashell, Dolphin, System Settings, and KDE tools
```

The division into `core/`, `shell/noctalia/`, `compositor/kwin/`, `apps/file-manager/`,
`services/`, `themes/`, `integrations/`, `recovery/plasma/`, `installer/`, and `tools/`
is a documentary reservation; executables remain in their current locations.
New Core/Services, IPC, and dedicated-session contracts are UNKNOWN, not implicitly
approved APIs. See [migration](MIGRATION-PLAN.md).

## Ownership and boundaries
- **UPSTREAM**: Noctalia, KWin, Plasma, Dolphin, Qt, Kvantum, and third-party themes.
- **PATCHES**: cumulative Noctalia diffs and KWin blur; preserve version, commit,
  licenses, build, and reversal alongside the patch. Old variants are historical.
- **RICY-OWNED**: integration/switching scripts, adapters, and local policies.
  Maintenance ownership does not erase the licenses of KDE-derived code.
- **PLANNED RICY-OWNED**: Ricy Files. No application is implemented in this foundation.

Build scripts fetch upstream sources into caches outside the project.
[app-icon-reordering/build.sh](../ricy-kit/contributions/app-icon-reordering/build.sh)
pins Noctalia 5.2.1/commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`;
[blur-continuity/build.py](../ricy-kit/contributions/blur-continuity/build.py)
pins KWin 6.7.5/commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.
These are the kit's baseline, not claims about the latest upstream versions.

## Recorded discrepancies — unresolved at this stage
| ID | Current evidence | Consequence/treatment |
|---|---|---|
| C-001 | [Workspace audit](WORKSPACE-AUDIT.md) identifies Ricy Noctalia UI/commands and shared Plasma surfaces | Current cumulative patch disables Ricy groups/badges, workspace widget, navigation/alert commands and settings. Visible-window membership remains internal. Changes are not activated by the audit. Shared KWin/Plasma shortcuts, menus and gestures remain preserved; full live compliance is UNKNOWN. |
| C-002 | `integration.py` uses plasmashell/wallpaper and restores through Ricy scripts | Separate, independent recovery is PLANNED. Do not claim isolation has already been achieved. |
| C-003 | Launcher and FileManager1 integration use customized Dolphin | Preserve until Ricy Files is validated; do not change MIME/defaults at this stage. |
| C-004 | Tokens exist, but configs/QSS/scripts also contain values | Reference existing tokens; automatic centralized consumption is PLANNED. |
| C-005 | Two kit trees and absolute paths in wrappers | INFERRED: moving directories can break units and shortcuts. Preserve and map references before migration. |

UNKNOWN: recovery after complete login/compositor failure, workspace compliance
across the entire session, full portability, and publication readiness.
Historical tests in READMEs are historical evidence, not tests performed in this task.

## Required navigation
[Components](COMPONENTS.md), [design](DESIGN-SYSTEM.md),
[development](DEVELOPMENT.md), [recovery](RECOVERY.md),
[evidence index](../.agents/references/README.md).
