# Architecture Decision Records

Accepted target decisions do not imply completed runtime implementation.
Preserve closed records with a reference to their replacement. Format: Status,
Context, Decision, Consequences, Constraints.

## Current accepted decisions

- [0001 — Single Workspace](0001-single-workspace.md).
- [0004 — Agent-first development](0004-agent-first-development.md).
- [0005 — Consumable visual tokens](0005-consumable-visual-tokens.md).
- [0006 — Explicit service template source lookup](0006-service-template-source-lookup.md).
- [0011 — Dolphin is the Ricy file manager](0011-dolphin-as-ricy-file-manager.md).
- [0012 — Independent Ricy session](0012-independent-ricy-session.md): approved
  architecture and same-account isolation model; runtime implementation pending.
  KDE is no longer Ricy's backup.

## Historical — closed, not implementation authority

- [0002 — Plasma Recovery](0002-plasma-recovery.md): Superseded by 0012;
  current switching mechanisms remain transitional assets.

- [0003 — Ricy Files](0003-ricy-files.md): Superseded by 0011.
- [0007 — Session file-manager integration boundary](0007-session-file-manager-boundary.md): Rejected; no replacement-manager integration.
- [0008 — Ricy Files technical architecture](0008-ricy-files-technical-architecture.md): Superseded by 0011.
- [0009 — Nonpurging Ricy Files trash mutation](0009-ricy-files-nonpurging-trash.md): Superseded by 0011.
- [0010 — Dolphin-derived Ricy Files proposal](0010-ricy-file-manager-build-vs-adapt.md): Rejected; no fork selected.

[Closed exploration](../history/ricy-files/README.md) and
[current Dolphin baseline](../DOLPHIN-BASELINE.md).
