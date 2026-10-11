# ADR-0005 — Consumable visual tokens

Status: Accepted, authorized by the user's token-centralization task on 2026-10-11.


Files references below describe the historical context of this token decision.
The own application is retired by [ADR-0011](0011-dolphin-as-ricy-file-manager.md);
canonical token authority remains accepted and its values are unchanged.

## Context

RICY-006 requires one identity source. Existing structured values are documented
in the visual-identity contribution, while TOML, palettes, QSS, native Style,
Kvantum and effect scripts repeat them. The reserved `themes/tokens/` location
did not yet contain consumable values. Files remains a planned application with
no selected toolkit. Source/history and observed blur behavior differ.

## Decision

Promote existing visual values to `themes/tokens/tokens.json`, plain JSON with
schema1 and versioned contract1.0.0. Preserve shared semantics, explicit units
and scoped shell/KDE/Dolphin/terminal adaptations. Reference shared color roles
instead of repeating their literals in adapters; calculate derived shell radii.
Record compositor blur settings and attributed observations without inventing a
portable kernel or guaranteeing support in applications.

Keep legacy/transport snapshots and compatibility paths intact. Use the existing
identity SVG as the only migrated consumer: a standard-library offline renderer
and template must reproduce its existing bytes. The user authorized this small
proof; no runtime consumer or global theme migration is included.

## Consequences

Future approved Ricy applications can parse or package the canonical JSON and
map it locally to toolkit primitives. This requires no daemon, IPC, SDK or
desktop runtime loader. The documented contract and source audit own token
meaning and provenance. A new contract major is required for incompatible
structure/meaning/unit changes; visual changes require their own validation.
Existing runtime hardcodes remain migration candidates, not competing editable
authorities. The retained snapshot is a migration-equivalence baseline.

## Constraints

No redesign, appearance change, toolkit choice, Files implementation, global
font/theme change, compositor activation, MIME/FileManager1 change or recovery
dependency is authorized by this decision. No bulk consumer migration or
historical manifest rewrite. Generated SVG equality does not certify live
visual behavior. Preserve upstream licenses and Plasma/Dolphin recovery.

References: [INVARIANTS](../INVARIANTS.md), [DESIGN-SYSTEM](../DESIGN-SYSTEM.md),
[contract](../../themes/tokens/README.md), [audit](../../themes/tokens/AUDIT.md),
[Files decision](0003-ricy-files.md).
