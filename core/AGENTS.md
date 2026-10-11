# core

PLANNED: boundary for common logic, without a new runtime at this stage. Do not
create IPC, a daemon, or a session manager. Before abstracting, locate the actual
wrappers and helpers in the map.

Consult [COMPONENTS](../docs/COMPONENTS.md) for abstractions/boundaries;
[RECOVERY](../docs/RECOVERY.md) if session/fallback is affected.
Use [component-development](../.agents/skills/component-development/SKILL.md) for components/contracts.
