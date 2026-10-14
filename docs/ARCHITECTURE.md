# Ricy Architecture

## Evidence and authority
Investigation snapshot: 2026-10-11. **KNOWN**: confirmed in a cited file/script,
not necessarily revalidated at runtime. **INFERRED**: a reasonable conclusion
from evidence. **PLANNED**: an accepted decision not yet implemented.
**UNKNOWN**: insufficient evidence; do not fill gaps with plausible assumptions.

Target updated on 2026-10-14 under [ADR-0012](adr/0012-independent-ricy-session.md):
Ricy is its own session; KDE Plasma is a separate desktop, not a backup.
Read-only environment observations on that date confirm only the Plasma login
entry exists and the current session remains KDE/Wayland. Installed login uses
plasmalogin; historical SDDM references do not establish the current manager.

[Invariants](INVARIANTS.md) → [ADRs](adr/README.md) → architecture/components →
local rules → implementation. Record conflicts and their scope.

## CURRENT — KNOWN
The [previous README and historical record](ricy.md) and the `start.sh`, `return.sh`,
and `switch.sh` wrappers point to `ricy-kit/contributions/plasma-noctalia-switching/ricy`.
`ricy-kit/` is the active kit; `docs/ricy-kit/` is the preserved transport copy,
not an automatically synchronized mirror. `archives/ricy.zip` is historical.
The original foundation investigation found no root Git repository; the later
[local baseline](GIT-BASELINE.md) established Git. The contribution-grounding
audit confirmed that baseline without changing versioning or publishing files.
See [CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md) for current consumers and classes;
directory presence alone does not establish ACTIVE implementation.

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
├── Ricy session (dedicated login and configuration)
│   ├── KWin / Wayland
│   ├── Noctalia Shell
│   ├── Selected upstream services + Ricy integration
│   └── Dolphin with Ricy visual adaptations
└── KDE Plasma session (independent desktop when installed)
    └── Its own shell, appearance and session settings
```

Ricy startup must not depend on launching the Plasma desktop and hiding panels.
Shared KWin, KDE libraries and selected upstream services are allowed. Ricy owns
its failure handling; it does not automatically fall back to the Plasma session.
ADR-0012's same-account configuration isolation, explicit application sharing
and sequential login model are approved; lifecycle/configuration implementation
and runtime validation remain pending.

The division into `core/`, `shell/noctalia/`, `compositor/kwin/`, `apps/`,
`services/`, `themes/`, `integrations/`, `recovery/plasma/`, `installer/`, and `tools/`
is primarily a documentary reservation; session executables remain in the kit.
The opt-in keyboard applicators now reside in `integrations/keyboard-cedilla/`
without changing installed preferences or introducing a runtime contract.
The three autostart templates now reside in `services/`, consumed through explicit
repository-relative lookup by the existing kit installer under
[ADR-0006](adr/0006-service-template-source-lookup.md). Installed units, runtime
scripts, profile/state and recovery paths remain unchanged.
`themes/tokens/` now holds the canonical consumable JSON and an offline identity
board renderer under [ADR-0005](adr/0005-consumable-visual-tokens.md); this does not
migrate shell/session runtime or implement an application.
New Core/Services and IPC contracts are UNKNOWN, not implicitly approved APIs.
The dedicated session and configuration-sharing boundary are approved under
ADR-0012; exact paths, startup dependencies and failure behavior require
implementation and validation within that contract. See
[migration](MIGRATION-PLAN.md).

[ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md) explicitly chooses
Dolphin for Ricy; ADR-0012 retires the Plasma Recovery context. The own prototype
and 07–10 implementation roadmap are closed; no own filesystem, Trash adapter,
FileManager1, toolkit or Dolphin fork is planned. Historical assessments/ADRs remain in
[the closed exploration](history/ricy-files/README.md), without active authority.

The [Dolphin baseline](DOLPHIN-BASELINE.md) records the read-only installed
configuration, registered integrations, helper/theme provenance and remaining
visual backlog. The user's90% visual assessment is recorded separately from
functional/recovery evidence. Current shared integration is preserved; the
policy of usable native file access when visual customizations fail is not a
claim that independent failure handling has already been demonstrated.

## Ownership and boundaries
- **UPSTREAM**: Noctalia, KWin, Plasma, Dolphin, Qt, Kvantum, and third-party themes.
- **PATCHES**: cumulative Noctalia diffs and KWin blur; preserve version, commit,
  licenses, build, and reversal alongside the patch. Old variants are historical.
- **RICY-OWNED**: integration/switching scripts, adapters, and local policies.
  Maintenance ownership does not erase the licenses of KDE-derived code.
- **RETIRED**: the own Ricy Files prototype; source history is preserved, but
  code/build/tests/packaging are removed from the active checkout.

Build scripts fetch upstream sources into caches outside the project.
[app-icon-reordering/build.sh](../ricy-kit/contributions/app-icon-reordering/build.sh)
pins Noctalia 5.2.1/commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`;
[blur-continuity/build.py](../ricy-kit/contributions/blur-continuity/build.py)
pins KWin 6.7.5/commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.
These are the kit's baseline, not claims about the latest upstream versions.

## Recorded discrepancies — unresolved at this stage
| ID | Current evidence | Consequence/treatment |
|---|---|---|
| C-001 | [Workspace audit](WORKSPACE-AUDIT.md) identifies Ricy Noctalia UI/commands and shared Plasma surfaces; [activation record](CHANGELOG.md) supersedes grounding G-02's earlier-binary observation | The cumulative RICY-001/UUID correction is deployed from an isolated build: it disables Ricy groups/badges, workspace widget, navigation/alert commands and settings. Visible-window membership remains internal. The earlier audits did not activate; the subsequent window-identity fix did. Shared KWin/Plasma shortcuts, menus and gestures remain preserved; full live compliance is UNKNOWN. |
| C-002 | `integration.py` uses plasmashell/wallpaper and restores through Ricy scripts | ADR-0012 accepts an independent Ricy session and retires KDE's backup role. Session/configuration isolation and Ricy-owned failure handling remain PLANNED; preserve current routes during migration. |
| C-003 | Launcher and FileManager1 integration use customized Dolphin | Dolphin is the chosen base. Preserve existing integration; optional visual failure recovery remains unproven, with no MIME/default changes in this task. |
| C-004 | Canonical consumable JSON now exists in themes/tokens; configs/QSS/scripts still contain values | Offline identity board consumes central tokens with exact byte equality. Runtime migrations remain PLANNED; see ADR-0005 and the token audit. |
| C-005 | Two kit trees and absolute paths in wrappers | INFERRED: moving directories can break units and shortcuts. Preserve and map references before migration. |
| C-006 | [Grounding G-03](CONTRIBUTION-AUDIT.md): native blur loaded, ricyblur absent, enabled selector unit failed at a D-Bus method lookup | `blur-continuity` disposition is UNKNOWN; old README claims that ricyblur remains loaded are historical. Preserve existing native blur and recovery; repair/retirement was not performed. |
| C-007 | [Grounding G-05/G-06/G-08/G-10](CONTRIBUTION-AUDIT.md): installed/source translation differences, mixed optional extensions, version-specific correction manifest | Source recipes and installed artifacts have independent lifecycles. Do not replay old installers, optional extension defaults, or correction bundles as if they reproduce the selected installation exactly. |

UNKNOWN: recovery after complete login/compositor failure, workspace compliance
across the entire session, full portability, and publication readiness.
Historical tests in READMEs are historical evidence, not tests performed in this task.

## Required navigation
[Components](COMPONENTS.md), [design](DESIGN-SYSTEM.md),
[contribution grounding](CONTRIBUTION-AUDIT.md),
[development](DEVELOPMENT.md), [recovery](RECOVERY.md),
[evidence index](../.agents/references/README.md).
