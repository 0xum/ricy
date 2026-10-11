# ADR-0010 — Dolphin-derived Ricy Files with bounded ownership

Status: **Rejected** — closed2026-10-11 by [ADR-0011](0011-dolphin-as-ricy-file-manager.md).

Date: 2026-10-11 (America/Sao_Paulo).

Supersedes on acceptance only: [ADR-0008](0008-ricy-files-technical-architecture.md).
Carries forward: [ADR-0009](0009-ricy-files-nonpurging-trash.md)'s bounded
nonpurging native send-to-trash decision and mandatory safety semantics.
Neither earlier ADR is marked Superseded or rewritten by this proposal.


> Historical record only. The separate application was explored and a prototype
> was produced, then retired before taking on file operations, Trash, devices
> and FileManager1. The user chose Dolphin to reduce infrastructure scope.
> Earlier approvals/proposals below no longer authorize implementation.

## Context

The user suspended milestones 09 and 10 and designated `codex/ricy-files-mvp`
at `0fe09c2` as a prototype/benchmark rather than the definitive architecture.
It implements a local Qt Quick browser and token/interaction shell, but no
operation engine, device model, Trash adapter, thumbnails or drag and drop.
[Build vs Adapt](../history/ricy-files/FILES-BUILD-VS-ADAPT.md) compares A (continue custom Quick),
B (upstream Dolphin appearance), C (thin Dolphin fork), and D (PCManFM-Qt/libfm-qt).

Dolphin already has the broader view/selection/preview/KIO/Solid integrations.
Supported appearance changes alone do not expose all custom-painted layout
seams. Replacing its frontend with QML would surrender much of its reuse value.
PCManFM-Qt is smaller, but strict operation semantics reach libfm-qt/GIO and
require a different remote/device stack. None of these inherited backends has
proved all mandatory Ricy safety guarantees.

## Proposed decision

Choose **C**: a separately identified Dolphin-derived Ricy Files, using Qt
Widgets and a bounded upstream application patch series. Retain upstream
KItemList views, models, selection, navigation, preview and KIO/Solid machinery.
Own the Ricy identity, token mapping and specific chrome/painter/layout changes.
Do not replace the retained view stack or extract a new public SDK/daemon/IPC.

Replace the Quick-specific private modules, context objects and delegates in
FILES-MVP with explicit Widgets/upstream mappings after acceptance. Keep its UX,
token and safety/outcome requirements as acceptance criteria. Staged navigation,
history and selection behavior must be compared and reconciled explicitly;
unmodified upstream controllers are not assumed to satisfy every Ricy contract.

Carry forward ADR-0009's native Freedesktop send-to-trash exception exactly as
a bounded operation. Its historical Quick/OperationsService references map to
the future application's private operation-policy integration; the storage,
commit, reconciliation and scope guarantees do not change. The adapter is
unimplemented today. KIO retains its other selected responsibilities; no KIO,
GLib or GVfs fork is authorized by this proposal.

Preserve the existing local-operation safety envelope. Audit every mutation
entry point; unavailable or unproved paths remain disabled in the candidate.
No-purge/no-replacement, collision-safe names, exclusive metadata, symlink/mount/
permission checks, explicit full/partial/failure results, cancellation evidence,
safe-only rollback and no silent data loss remain mandatory. A broader backend
or filesystem framework needed to meet them requires another architectural
decision, rather than weakening them.

## Consequences

The application/toolkit choice in ADR-0008 would be superseded after explicit
approval, with the original ADR retained and cross-linked. This changes future
application ownership and adds upstream application rebasing to Ricy's work.
It reduces new interaction/feature implementation compared with A, but safety
integration is still substantial and Qt Widgets token adaptation is new work.
QML files stay as the visual benchmark; tokens, assets, fixture strategy and
behavioral acceptance cases are the principal reusable artifacts.

ADR-0009 remains a historical Accepted decision carried forward, with its
original assumptions visible. ADR-0003/RICY-005 remain compatible because the
candidate is a distinct Ricy Files application and stock Dolphin remains
available for Plasma Recovery. [ADR-0007](0007-session-file-manager-boundary.md)
remains Proposed; none of its contracts become accepted implicitly.

## Constraints and approval boundary

- Preserve the exact benchmark branch/commit and excluded uncommitted fixes;
  no destructive replacement or cleanup.
- No implementation, packaging/installation or executable spike in this
  evaluation. Approval of this proposal selects a direction; it does not certify
  future operations or recovery.
- Require distinct binary, desktop/app, config/data and private artifact identity;
  disable inherited global FileManager1 registration before candidate execution.
- Stock Dolphin, current defaults, MIME associations, session integration,
  wrappers, private state and Plasma Recovery remain unchanged.
- Keep app patches categorized, pinned and testable; generic fixes go upstream
  where practical. Do not freeze vulnerable dependencies to retain visual patches.
- The first candidate, mandatory safety gates and a stable-update rebase trial
  must establish feasibility before promotion. If the patch boundary expands
  materially, return for a new decision.

Proposed migration, risks, relative costs and evidence limits are in
[the evaluation](../history/ricy-files/FILES-BUILD-VS-ADAPT.md). Implementation remains suspended
pending the user's explicit decision.
