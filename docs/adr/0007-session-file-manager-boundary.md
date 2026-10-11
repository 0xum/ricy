# ADR-0007 — Session file-manager integration boundary

Status: Proposed — awaiting explicit user approval; not Accepted.


> Historical record only. The separate application was explored and a prototype
> was produced, then retired before taking on file operations, Trash, devices
> and FileManager1. The user chose Dolphin to reduce infrastructure scope.
> Earlier approvals/proposals below no longer authorize implementation.

## Context

[ADR-0003](0003-ricy-files.md) and RICY-005 already establish Ricy Files as the
future Ricy default and Dolphin for Plasma Recovery. Detailed contracts were left
UNKNOWN. The [integration assessment](../history/ricy-files/FILES-INTEGRATION.md) maps current
directory defaults, launcher discovery, FileManager1, desktop overrides, devices,
trash, package handlers, KDE actions, appearance and recovery dependencies.

Current shell switching stays inside Plasma and declares KDE. The same user
Dolphin desktop override, FileManager1 activation and `plasma-dolphin.service`
drop-in use the Ricy visual wrapper. Selecting Files for `inode/directory` alone
would not change D-Bus ownership or make Recovery independent.

## Decision proposed for approval

Adopt the responsibilities, required contracts and validation gates in the
assessment, with these boundaries:

- Ricy Session selects Ricy Files through its own identity and validated
  session-scoped directory defaults and FileManager1 activation policy.
- Plasma Recovery selects Dolphin through a native launch/activation path with
  no dependency on Files, Noctalia, Ricy visual plugins/assets or a shared Ricy
  router. KDE/system dependencies remain available.
- Files supplies directory launch, the three public FileManager1 methods,
  standard application registration and MIME delegation, removable-media
  integration, interoperable trash, central identity consumption and independent
  operation. Concrete APIs/toolkit/backends remain subject to implementation review.
- Dolphin/KDE retain their service-menu/native-plugin APIs, KIO-specific protocol
  integrations, settings, accelerator identities, Qt helper/Kvantum adaptations
  and class-specific KWin effect. Files need not implement Dolphin-specific
  `SortOrderForUrl` or impersonate Dolphin.
- The existing DEB/RPM application is an optional external handler. Its KDE
  service menu stays in the Dolphin domain; conversion, authorization and package
  installation stay outside Files. Ordinary file opening preserves user handlers.
- Session/default/activation integration belongs outside the Files process.
  No new routing daemon is selected. The concrete isolation mechanism, MIME
  precedence policy, concurrent-login support and rollback need a later proposal.

## Options

| Option | Benefit | Cost / limitation |
|---|---|---|
| A — Distinct application identities, session-scoped defaults and validated activation contexts (recommended) | Preserves public interoperability and allows native independent Recovery. | Requires session identity, MIME precedence, D-Bus lifecycle/environment and same-user concurrency evidence before migration. No concrete isolation mechanism chosen here. |
| B — A global Ricy router/wrapper selects Files or Dolphin by shell mode | Centralizes dispatch and may accommodate current in-session switching. | Adds a shared Ricy failure point to Recovery, policy/state races and a new daemon/IPC contract; not recommended for this boundary. |
| C — Change directory MIME only and keep Dolphin's FileManager1 activation | Small association change. | Splits directory opening from reveal/properties and leaves the global visual overrides/recovery coupling; does not satisfy the requested boundary. |

## Consequences

The future Files implementation can be evaluated without loading Dolphin's UI
adapters or inheriting KDE extension APIs. Shared storage/protocol conventions
remain interoperable. Optional external applications stay independently owned.
Recovery independence becomes a testable acceptance condition, not an inference
from package presence or a direct binary launch.

Implementation cost includes proving default resolution and one-owner activation
in the supported session model, plus cold-start, media/trash and real Recovery
trials. The current deployment and unresolved C-002/C-003 discrepancies remain.
No source migration, package removal or installed-state rollback is needed for
this documentation-only proposal.

## Constraints

Do not implement Files, alter defaults/MIME associations, modify Dolphin, change
service activation, install/switch sessions, or retire existing backups here.
Approval of this ADR accepts the boundary and criteria only. Toolkit, application
ID, CLI spelling, device/filesystem backend, session/bus topology, services and
activation implementation, publication, and default migration are not authorized.
Record explicit approval before changing Status to Accepted; keep Proposed if
the decision is still pending.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md),
[COMPONENTS](../COMPONENTS.md), [RECOVERY](../RECOVERY.md),
[ADR-0002](0002-plasma-recovery.md), [validation](../DEVELOPMENT.md).
