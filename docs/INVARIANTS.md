# Architectural Invariants

Status: Accepted, project decision on 2026-10-11. These are normative contracts;
partial current compliance is documented in [ARCHITECTURE](ARCHITECTURE.md).
RICY-005 was explicitly amended by [ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md)
on the same date to select Dolphin and retire the own file-manager direction.
On 2026-10-14, [ADR-0012](adr/0012-independent-ricy-session.md) replaced the
Plasma Recovery requirement with an independent Ricy session and amended
RICY-005's recovery context. The runtime migration remains PLANNED.

| ID | Contract | Implementation limit |
|---|---|---|
| RICY-001 — Single Workspace | A single-space experience; prohibit switchers, indicators, move-to-workspace actions, gestures, and navigation between desktops. | KWin may have internal APIs; its `workspace` object does not authorize UI. Audit legacy behavior without deleting fallback. |
| RICY-002 — KWin is infrastructure | KWin/Wayland composites and manages windows; Ricy does not replace it. | Conservative patches compatible with the installed version. |
| RICY-003 — Primary Noctalia | Noctalia is Ricy's visual shell, with identifiable custom patches. | Do not assume upstream APIs or make Plasma the primary experience of the target design. |
| RICY-004 — Independent Ricy session | Ricy owns a dedicated KWin/Wayland + Noctalia session, with session-scoped settings and failure handling. KDE Plasma, when installed, is a separate desktop, not a required backup. | Current integration still runs within Plasma; preserve transitional routes until validated replacements exist. This decision does not authorize removing installed packages or assume that startup/configuration isolation is implemented. |
| RICY-005 — Dolphin file manager | Dolphin is the file manager of Ricy. Native file access must remain usable if optional Ricy visual customization fails. | Ricy may adapt appearance, layout, QSS/Kvantum, tokens and minimal helpers/patches; no own file-manager/filesystem implementation is planned. Independent session and native file-access failure handling remain unproven. |
| RICY-006 — Centralized design | One source of truth for identity; reuse colors, radii, spacing, motion, transparency, blur, and fonts. | Preserve existing values; do not create a parallel design or migrate all consumers now. |

Contract changes require [architecture-change](../.agents/skills/architecture-change/SKILL.md)
and an explicit user decision, followed by an ADR. Knowing about a discrepancy
does not grant permission to weaken the contract. See [RECOVERY](RECOVERY.md) and
[DESIGN-SYSTEM](DESIGN-SYSTEM.md) for how these contracts apply.
