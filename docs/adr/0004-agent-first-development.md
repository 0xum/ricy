# ADR-0004 — Agent-first development

Status: Accepted

## Context

The project has accumulated kits, cumulative variants, and session records. Inferring intent solely from code tends to perpetuate historical paths and present plans as completed capabilities.

## Decision

Use AGENTS.md as a concise map and single constitution; CLAUDE.md only references it. Authority: invariants, ADRs, architecture/components, local rules, implementation. Skills provide progressive procedures; validate and record evidence.

## Consequences

Agents load context by component, look for existing abstractions, document conflicts, and report test limits. Significant changes record Model/Agent, Date, Purpose, and Validation performed in the changelog.

## Constraints

No automatic permission to create architecture. A new path requires a proposal, impact assessment, and explicit approval before implementation; respect authorization already granted in the request. Do not create bureaucracy for compatible edits or clutter code with signatures.

References: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
