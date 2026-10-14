# recovery

Ricy owns failure handling under [ADR-0012](../docs/adr/0012-independent-ricy-session.md);
KDE Plasma is a separate desktop, not a required backup. Native Dolphin file
access must remain usable if optional visual helpers fail. Preserve transitional
switching routes, private snapshots and rollback until replacements are validated.
Reserved documentation does not prove session isolation.

Changes to return/fallback require [RECOVERY](../docs/RECOVERY.md).
Consult [COMPONENTS](../docs/COMPONENTS.md) for ownership/dependencies and
[testing](../.agents/skills/testing/SKILL.md) when planning trials or interpreting evidence.
