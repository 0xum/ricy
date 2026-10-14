# compositor

KWin is infrastructure shared with Plasma. Preserve ABI, licenses, and the
patch/upstream distinction. [ADR-0012](../docs/adr/0012-independent-ricy-session.md)
defines separate Ricy/KDE sessions; existing shared effects and return routes
must remain usable during migration. Do not assume session isolation or remove
installed dependencies based on the new target alone.

Effects/scripts/patches: [kwin-development](../.agents/skills/kwin-development/SKILL.md)
and [RECOVERY](../docs/RECOVERY.md). Location/ownership:
[COMPONENTS](../docs/COMPONENTS.md).
