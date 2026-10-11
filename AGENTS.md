# Ricy — Agent Constitution

## Project Definition
An opinionated desktop for CachyOS, KWin/Wayland, and Noctalia, with Plasma/Dolphin
Recovery. The shell currently runs within a Plasma session; the target design is
not evidence of implementation. State and boundaries: [ARCHITECTURE](docs/ARCHITECTURE.md).

## Project Language
[Always use en-US as the language.]

Use US English (en-US) for project files, documentation, agent instructions,
comments, developer messages, and public-facing interfaces. The user may speak
Brazilian Portuguese (pt-BR) in chats; this does not change the project language.
Use en-US file names and update references when renaming project files.
Preserve deployed compatibility identifiers, private backup/state paths,
historical manifests, licenses, and upstream localization catalogs.
Record name changes and compatibility limits in [FILE-RENAMES](docs/FILE-RENAMES.md). Language
policy does not change the user's keyboard layout, time zone, units, or private
session settings. New public names and content must use en-US.

## Architecture Sources
Architectural authority, in this order:
1. [INVARIANTS](docs/INVARIANTS.md).
2. [Accepted ADRs](docs/adr/README.md).
3. [Architecture](docs/ARCHITECTURE.md) and [components](docs/COMPONENTS.md).
4. Local `AGENTS.md` files, from ancestors to the most specific scope.
5. Implementation as evidence of the current state.

This order is internal to the project; it does not override user/system instructions.
The authority remains valid without requiring every level to be read for every task.
Load documentation according to the consequences of the change, not merely its existence.
Use KNOWN (evidence), INFERRED (inference), PLANNED (future), and UNKNOWN (unproven).

## Architectural Invariants
RICY-001: a single-space experience, without workspace UI, actions, or gestures.
RICY-002: KWin is infrastructure. RICY-003: Noctalia is the primary shell.
RICY-004/005: preserve Plasma and Dolphin Recovery; Ricy Files is a future component.
RICY-006: centralized identity; reuse the [existing design](docs/DESIGN-SYSTEM.md).
The full normative text is in INVARIANTS; discrepancies are in ARCHITECTURE.

## Agent Behavioral Rules
- Never infer architecture solely from implementation. Read local rules before
  editing a subsystem, including legacy paths mapped in COMPONENTS.
- Look for existing abstractions, files, and conventions before creating others.
- Do not silently create patterns or remove content whose use is uncertain.
- When docs and code conflict, record evidence and impact; do not silently correct it.
- Preserve paths, backups, history, and recovery. Do not install or switch sessions
  merely to validate documentation. Do not publish the private active kit.
- Never claim functionality without appropriate validation and an explicit scope.

## Skill Routing
Every task: follow the applicable AGENTS hierarchy, including subsystem rules
referenced by the kit. Local fixes: local code/docs/tests, without the architecture stack.
Combine only the routes whose consequences the change reaches:

| Consequence | Additional context |
|---|---|
| New architectural decision | ARCHITECTURE, INVARIANTS, relevant ADRs, and [architecture-change](.agents/skills/architecture-change/SKILL.md); COMPONENTS for boundaries/ownership. |
| Session, Noctalia/Plasma coexistence, or fallback | [RECOVERY](docs/RECOVERY.md), relevant invariants/ADRs, and recovery rules; if architecture changes, also follow the route above. |
| Visual/UI | [DESIGN-SYSTEM](docs/DESIGN-SYSTEM.md); [visual-development](.agents/skills/visual-development/SKILL.md) for states/interactions, materials, or adaptations between components. |
| Noctalia patch, API, or integration | [noctalia-development](.agents/skills/noctalia-development/SKILL.md); changes limited to an existing visual value follow the visual route. |
| KWin effect, script, or patch | [kwin-development](.agents/skills/kwin-development/SKILL.md). |
| New approved component, migration, ownership, boundaries, or significant dependencies | COMPONENTS and [component-development](.agents/skills/component-development/SKILL.md). |
| Selection of test levels or interpretation of evidence | [testing](.agents/skills/testing/SKILL.md); an already known check may be run directly. |
| Creating docs, changing a source of truth/ADR, or recording a significant change | [documentation](.agents/skills/documentation/SKILL.md); not required for a typo/local comment. |

If impact is unclear, consult the relevant domain before implementing.

## Validation Requirements
Run `./scripts/verify architecture` and relevant checks described in
[DEVELOPMENT](docs/DEVELOPMENT.md). `./scripts/doctor` is diagnostic only.
Report `PASS`, `FAIL`, `NOT RUN`, and `NOT APPLICABLE`; UNKNOWN is not success.
Static tests do not prove recovery in a real session.

## Documentation Requirements
Update intent, dependencies, ownership, and recovery implications.
Significant changes go in [CHANGELOG](docs/CHANGELOG.md) with
`Model/Agent`, `Date`, `Purpose`, and `Validation performed`; no signatures in code.

## Architecture Change Policy
Follow architecture-change. A new architectural path requires a proposal, impact
assessment, and explicit approval before implementation, followed by validation,
an ADR, and documentation. The authorization already granted for this foundation
covers the six invariants and the planned structure; it does not authorize future
migrations or additional decisions. Pause only the undecided part and continue
safe, independent work.
