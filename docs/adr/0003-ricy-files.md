# ADR-0003 — Ricy Files

Status: Accepted

## Context

The future desktop needs a file manager aligned with Ricy identity and interactions. Dolphin is already used and customized; removing it before a replacement exists would leave a functional gap.

## Decision

Adopt RICY-005: reserve apps/file-manager/ for Ricy Files; it will be the default for the future Ricy session. Dolphin remains available for Plasma Recovery.

## Consequences

Separate the future application from existing Dolphin adaptations. The toolkit, contracts, and Files timeline remain UNKNOWN until a proposal is approved.

## Constraints

Do not implement Files or Settings now, change MIME/FileManager1 associations, or remove Dolphin. Do not reuse global wrappers that affect recovery without analysis.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
