# ADR-0006 — Explicit service template source lookup

Status: Accepted, authorized by the user's “Siga” approval of option A on
2026-10-11 (America/Sao_Paulo).

## Context

The approved structure assigns unit definitions to services, but the existing
autostart installer reads three templates beside its runtime scripts. The
incremental migration proposal mapped these callers and offered explicit local
resource paths, temporary compatibility links, or a shared Core resolver.

## Decision

Move only `noctalia-test.service.in`, `noctalia-desktop-search.service.in`, and
`ricy-noctalia-integration.service.in` from the active autostart contribution to
`services/`. The existing installer resolves the repository root from its own
file location and reads those templates directly. Preserve template bytes/modes,
replacements and installed legacy unit IDs. This implements option A for M-02.

## Consequences

Services owns the three RICY-OWNED source definitions. The installer now needs
the repository's services directory when preparing a destination; copying only
the active kit/contribution is insufficient. No shared resolver, compatibility
link, alternate template fallback or new runtime service is introduced.
Offline comparison must prove identical rendering for all three installed IDs,
including quoted paths, ordering, environment and application-preserving KillMode.
Architecture validation detects missing maintained templates.

## Constraints

Runtime scripts, adapters, profile/state paths, installed units/drop-ins,
readiness, return behavior and backup manifests retain their existing contracts.
This approval does not authorize installation, daemon-reload, service/session
restart, later runtime relocation, other unit extraction, public packaging or
an independent session. Transport templates/manifests remain historical and
unchanged. Source rollback restores template placement and installer reads
together; offline equality does not prove live login or failure recovery.

References: [migration](../MIGRATION-PLAN.md), [components](../COMPONENTS.md),
[recovery](../RECOVERY.md), [services rules](../../services/AGENTS.md).
