> HISTORICAL — Closed on 2026-10-11 by [ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md). This preserves the explored proposal/prototype, not an active roadmap, implementation contract, or command to execute. Dolphin is the current Ricy file manager.

# Ricy Files

PLANNED: booked architectural address, no runtime migration. Current locations and dependencies: [COMPONENTS](../../COMPONENTS.md)Read them. [local rules](../../../apps/AGENTS.md) and [migration plan](../../MIGRATION-PLAN.md). Ricy Files has not yet been implemented. Dolphin remains available.

The future application consumes the versioned
[Ricy visual tokens](../../../themes/tokens/README.md) through its approved toolkit's
local adapter or packaged JSON resource. Reuse shared palette, spacing, UI font
and motion roles; preserve units/scaling and keep shell/Dolphin adaptations
scoped. Token centralization defines visual-data consumption only; toolkit choice
now follows ADR-0008. Implementation, packaged execution and compositor
integration remain unvalidated. No Files code,
default association or recovery dependency is changed by token centralization.

Milestone 07's [technical architecture assessment](FILES-TECHNICAL-ARCHITECTURE.md)
and [ADR-0008](../../adr/0008-ricy-files-technical-architecture.md) select
Qt Quick/C++17 with bounded KIO/Solid adapters; option A is explicitly Accepted.
[Milestone 08's specification](FILES-MVP.md) defines modules,
UX/operation policies and acceptance tests. Its
[nonpurging trash amendment](../../adr/0009-ricy-files-nonpurging-trash.md)
is Accepted separately, so milestone 08 is complete. The next checkpoint is
milestone 09 executable implementation/validation before 10 begins. Defaults, FileManager1, Dolphin and Plasma Recovery remain
protected; ADR-0007 is not accepted by the technical decision.
