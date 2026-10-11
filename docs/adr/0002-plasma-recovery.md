# ADR-0002 — Plasma Recovery

Status: Accepted

## Context

The custom shell and patches may fail. The current kit already depends on Plasma for desktop/wallpaper and uses Ricy scripts to restore panels, so recovery remains coupled.

## Decision

Adopt RICY-004: keep Plasma, Dolphin, System Settings, and KDE tools functional. Recovery should have as few Ricy dependencies as reasonably possible.

## Consequences

Changes to login, units, shortcuts, compositor, or defaults must account for the return path. Preserve the current mechanism while an independent session remains PLANNED.

## Constraints

Do not remove packages or disable mechanisms required for fallback. Offline tests do not prove real login/recovery; do not invent a watchdog or session manager at this stage.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
