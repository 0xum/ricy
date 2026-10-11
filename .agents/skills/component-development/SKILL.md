---
name: component-development
description: Add an approved Ricy component, migrate a component, or change ownership, boundaries, responsibilities, significant dependencies, or contracts between components; do not use for a local internal fix.
---

# component-development

1. Locate the component in [COMPONENTS](../../../docs/COMPONENTS.md).
2. Follow applicable AGENTS and ADRs for the affected contract. For legacy contributions,
   use `ricy-kit/AGENTS.md`; the planned destination does not transfer current ownership.
3. Map affected callers and dependencies, including the transport copy.
   Look for an equivalent contract or abstraction before creating another.
4. Make the smallest compatible change. Preserve paths used by units,
   installers, and backups. Distinguish UPSTREAM, PATCHES, and RICY-OWNED.
5. Run component validation and integration checks when applicable; consider
   [RECOVERY](../../../docs/RECOVERY.md) for changes to the session or Dolphin.
6. Document relevant changes, conflicts, and limits; use
   [DEVELOPMENT](../../../docs/DEVELOPMENT.md) for checks and changelog requirements.

If boundaries or contracts need to change, use
[architecture-change](../architecture-change/SKILL.md) before implementing.
