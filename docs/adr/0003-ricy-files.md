# ADR-0003 — Ricy Files

Status: Accepted


> Historical record only. The separate application was explored and a prototype
> was produced, then retired before taking on file operations, Trash, devices
> and FileManager1. The user chose Dolphin to reduce infrastructure scope.
> Earlier approvals/proposals below no longer authorize implementation.

## Context

The future desktop needs a file manager aligned with Ricy identity and interactions. Dolphin is already used and customized; removing it before a replacement exists would leave a functional gap.

## Decision

Adopt RICY-005: reserve apps/file-manager/ for Ricy Files; it will be the default for the future Ricy session. Dolphin remains available for Plasma Recovery.

## Consequences

Separate the future application from existing Dolphin adaptations.
[ADR-0008](0008-ricy-files-technical-architecture.md) now selects the toolkit and
application-local boundaries for sequential isolated development. The executable
MVP contracts are specified/reviewed in milestone 08; default migration remains
unapproved.

## Constraints

The foundation-era prohibition on Files implementation is superseded only for
the isolated scope and gates accepted in ADR-0008. Settings, MIME/FileManager1
association changes and Dolphin removal remain unapproved. Do not reuse global
wrappers that affect recovery without analysis.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
