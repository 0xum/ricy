# ADR-0001 — Single Workspace

Status: Accepted

## Context

The product seeks a direct experience centered on applications and windows; the compositor's inherited organization into desktops must not dictate Ricy's mental model.

## Decision

Adopt RICY-001: a single workspace in the Ricy experience, without indicators, switchers, move-to-workspace actions, gestures, or navigation across desktops.

## Consequences

New components cannot depend on multiple desktops. Legacy exposure requires a separate audit; preserving KWin APIs needed for operation does not imply exposing them.

## Constraints

Do not indiscriminately refactor upstream, treat every occurrence of `workspace` as a violation, or break Plasma Recovery. Runtime compliance remains UNKNOWN.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
