# ADR-0008 — Ricy Files technical architecture

Status: **Superseded** — closed2026-10-11 by [ADR-0011](0011-dolphin-as-ricy-file-manager.md).

Approval evidence: the user stated, "Aprovo a opção A do ADR-0008," and directed
the coordinator to record acceptance and proceed to milestone 08. The user
explicitly required conflict, partial-result, cancellation, applicable rollback,
destructive-operation, symlink, mount-boundary, permission and KIO-failure
contracts. Defaults, FileManager1, Dolphin and Plasma Recovery remain protected.
ADR-0007 remains Proposed; its contracts were not accepted by this approval.


> Historical record only. The separate application was explored and a prototype
> was produced, then retired before taking on file operations, Trash, devices
> and FileManager1. The user chose Dolphin to reduce infrastructure scope.
> Earlier approvals/proposals below no longer authorize implementation.

## Context

[ADR-0003](0003-ricy-files.md) reserves Ricy Files but leaves its toolkit and
contracts undecided. The user requested sequential milestones 07–10 with an
explicit architecture approval gate before milestone 08. The
[technical assessment](../history/ricy-files/FILES-TECHNICAL-ARCHITECTURE.md) compares toolkit,
filesystem, integration, visual, dependency and testing options using independent
investigations and primary-source evidence. No application exists yet.

## Decision

Choose option A: a standalone Ricy-owned C++17 application with Qt 6 Quick/QML,
Quick Controls Basic and application-local KF6 KIOCore/KIOGui/Solid adapters.
Use CMake/ECM and a native Arch/CachyOS packaging path; support versions are
bounded by actual build/test evidence rather than package presence.

Keep QML presentation separate from C++ navigation, a flat KCoreDirLister-backed
model, operation policy/jobs, handler launch and Places/devices. Include an
application-local QML job-decision adapter; stock KIOWidgets dialogs are not the
selected UI. Resolve selected file handlers explicitly and specify executable,
desktop-link, no-handler and failure behavior before implementing launch.

Consume exact canonical token JSON through a local packaged adapter, preserving
the versioned contract/units. Start with an opaque surface and normal decoration;
defer compositor blur/corner integration. Use `ricy-files` and
`io.github.0xum.RicyFiles` as distinct executable and local application identity.

Bound initial filesystem capability to local `file:` and explicitly tested
`trash:` behavior. Reuse upstream KIO workers/helpers and Solid's existing device
infrastructure; create no Ricy daemon, IPC service, automounter or shared SDK.
No automatic overwrite, trash-to-delete fallback or privilege escalation.
Cancellation does not promise rollback. Permanent delete starts disabled unless
a later explicit contract is approved.

Approval permits milestone 08 specification/review and, once validated,
isolated milestones 09 and 10 under those contracts. It supersedes only the
foundation prohibition on implementing Files in that bounded development scope.
It does not accept [ADR-0007](0007-session-file-manager-boundary.md).

## Consequences

Ricy owns application UI and safety policy; KDE/Qt retain their framework/worker
implementations and licenses. Reusing KIO avoids inventing a second complete
filesystem stack, but adds KDE package/service dependencies and a tested
QML conflict bridge. Narrow target use does not shrink the monolithic KIO package
closure. Models/jobs and decisions need lifecycle, stale-result and partial-error
tests. Recovery has no new dependency on Files.

Pure Qt/QML (option B) is feasible but owns more operation/trash/device work;
Qt Widgets/KIO (C) trades declarative visual control for mature native views and
dialogs; PySide/QML (D) adds a binding/package path without a demonstrated
advantage. The full comparisons and evidence stay in the assessment.

## Constraints

The approval above permits milestone 08. Final module APIs, operation/UX contracts
and acceptance tests are specified and independently reviewed in milestone 08.
Additional backend paths or safety decisions outside this accepted scope still
require their own approval; accepting this ADR does not approve later proposals.

Do not change `inode/directory`, MIME defaults, global FileManager1 ownership or
activation, Dolphin, Plasma Recovery, session isolation, existing launch wrappers,
backups or private state. No default migration, installation, publication or new
compositor integration is included. Runtime and real recovery evidence remain
required before their corresponding claims.

## Original approval gate — resolved for option A

ARCHITECTURE DECISION REQUIRED

**Problem:** select the Files toolkit/backend and owned boundaries before MVP
specification and isolated implementation.

**Evidence:** reserved component only; central tokens already accepted;
independent investigations identify Qt Quick/C++ and KIO/Solid as applicable,
with explicit worker, package, conflict-UI and partial-operation constraints.
Host build tools are incomplete and runtime behavior is unproven.

**Options:** A — Qt Quick/C++ with bounded KIO/Solid; B — pure Qt/Quick;
C — Qt Widgets/KIO; D — PySide/QML.

**Recommended:** A with local UI/model/job/token adapters and the constraints above.

**Impact:** new implementation only within `apps/file-manager/` after the gates;
Qt/KF6/CMake dependencies and component tests; no default/session/Dolphin change
and no new dependency for Plasma/Dolphin Recovery.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md),
[COMPONENTS](../COMPONENTS.md), [RECOVERY](../RECOVERY.md),
[DESIGN-SYSTEM](../DESIGN-SYSTEM.md), [DEVELOPMENT](../DEVELOPMENT.md).
