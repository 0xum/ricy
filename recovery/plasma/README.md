# Transitional Plasma switching

This retained directory was reserved for the former Plasma Recovery target;
no runtime migration occurred. [ADR-0012](../../docs/adr/0012-independent-ricy-session.md)
defines Ricy as its own session and removes KDE's backup role. Preserve the
current switching scripts and snapshots during migration; this path does not
establish the bootstrap location or failure policy of the independent session.

Current consumers: [COMPONENTS](../../docs/COMPONENTS.md). Follow the
[local rules](../AGENTS.md) and [migration plan](../../docs/MIGRATION-PLAN.md).
