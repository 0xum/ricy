---
name: architecture-change
description: Assess changes to Ricy boundaries, contracts, critical dependencies, or invariants; require an explicit decision for new architecture.
---

# architecture-change

1. Identify the requested change and authorization already provided by the request.
2. Read [ARCHITECTURE](../../../docs/ARCHITECTURE.md),
   [INVARIANTS](../../../docs/INVARIANTS.md), and relevant [ADRs](../../../docs/adr/README.md).
3. Map affected components in [COMPONENTS](../../../docs/COMPONENTS.md),
   read local rules, and look for existing abstractions and conventions.
4. Determine whether the change modifies architecture or implements an already
   approved contract. Agents have no automatic authorization to create architectures.
5. If a new architectural decision is needed, record the block below, explain impact,
   STOP that part, and request explicit approval before implementation. Continue safe,
   independent work. Do not request approval already granted for the same proposal;
   that approval does not extend to additional decisions.
6. After approval: implement incrementally, validate relevant levels, create/update
   the ADR, components, recovery, and changelog. Record the limits of the tests.

```text
ARCHITECTURE DECISION REQUIRED
Problem: ...
Evidence: ...
Options: A ... / B ...
Recommended: ...
Impact: components, dependencies, compatibility, and recovery
```

Do not silently resolve docs/code conflicts. The future structure alone does not
approve a new daemon, IPC protocol, or path migration.
