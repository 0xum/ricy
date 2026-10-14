# ADR-0011 — Dolphin is the Ricy file manager

Status: **Accepted** — explicitly approved by the user on 2026-10-11
(America/Sao_Paulo).

Amended by [ADR-0012](0012-independent-ricy-session.md) on 2026-10-14: Dolphin
remains selected, while Plasma's backup role is retired. File access when optional
visual customization fails remains required within Ricy. References below to
Plasma Recovery describe the original decision and preserved current runtime.

Approval: the user supplied the instruction to retire the own Ricy Files,
choose Dolphin, preserve runtime/tokens, and record a read-only baseline.
This selects an architecture; it does not authorize runtime/default changes.

Supersedes [0003](0003-ricy-files.md), [0008](0008-ricy-files-technical-architecture.md)
and [0009](0009-ricy-files-nonpurging-trash.md). Rejects the unaccepted
[0007](0007-session-file-manager-boundary.md) and
[0010](0010-ricy-file-manager-build-vs-adapt.md) replacement/fork proposals.

## Context

A separate Qt Quick/C++ file manager was explored and a browser prototype was
produced. Before assuming file operations, Trash, devices, FileManager1 and other
critical infrastructure responsibilities, the project chose Dolphin to reduce
scope and infrastructure maintenance at this stage. The visual adaptation of
Dolphin is assessed by the user as about 90% complete; this is a visual progress
assessment, not measured functional coverage or a Recovery certification.

## Decision

RICY-005 now states: **Dolphin is the file manager of Ricy**, and remains available
in Plasma Recovery. Ricy may customize appearance, configuration/layout,
QSS/Kvantum, design-token integration, and minimal helpers/patches when necessary.
It does not implement or maintain an own file manager, filesystem backend,
Trash adapter, FileManager1 service or replacement toolkit. No Dolphin fork is
planned. Upstream remains responsible for file-manager infrastructure.

Recovery file access must remain functional if Ricy visual customizations fail,
and must not require an own Ricy application. This policy is not proof that the
current shared wrapper/theme/helper integration is already failure-independent.

## Consequences

Remove active own source, QML, packaging, CMake, tests and exclusive runner.
Retire the07–10 replacement-application roadmap and archive its specifications.
Do not merge an unintegrated prototype into main just to remove it afterward.
Preserve Git history and historical ADR bodies; old approvals no longer authorize
continuation. Unmerged prototype branches/worktrees are historical, not active
product directions. No other chat's checkout is destroyed.

The [Dolphin baseline](../DOLPHIN-BASELINE.md) becomes the current visual/technical
reference. [Closed exploration](../history/ricy-files/README.md) preserves provenance.
Canonical design-token values and consumers remain unchanged; documentation
only retires the Files consumer. Visual gaps are backlog, with no implementation
or automatic next stage in this task.

## Constraints and recovery

No runtime launch, install/rebuild, defaults/MIME/FileManager1 changes,
Dolphin redesign, new patches, theme/QSS/helper changes, blur/corner changes,
Plasma switching, service restart or failure trial is authorized by this task.
Existing Dolphin/Plasma Recovery and private rollback state remain intact.
Future polish or recovery isolation needs its own explicitly scoped task.
Source retirement is reviewable in Git; no history is rewritten.
