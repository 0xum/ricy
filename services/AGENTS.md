# services

Three autostart source templates now live here under
[ADR-0006](../docs/adr/0006-service-template-source-lookup.md). The existing
kit installer resolves them from the repository root; runtime scripts, profiles,
installed units and overrides retain their existing paths. Other unit migrations
remain PLANNED. Preserve names, readiness, KillMode and return behavior; do not
invent a daemon/watchdog.

Units/readiness/return: [RECOVERY](../docs/RECOVERY.md).
Ownership/dependencies/contracts: [COMPONENTS](../docs/COMPONENTS.md) and
[component-development](../.agents/skills/component-development/SKILL.md).
