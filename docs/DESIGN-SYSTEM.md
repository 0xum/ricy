# Design System

## CURRENT — KNOWN
Identity already exists. The canonical consumable values are now in
[themes/tokens/tokens.json](../themes/tokens/tokens.json), contract 1.0.0/schema 1.
The [token contract](../themes/tokens/README.md) defines paths, semantics, units,
consumer status and application consumption. The [source audit](../themes/tokens/AUDIT.md)
records existing hardcodes and conflicts. This document remains the normative
entry point; it does not create a second palette.

The [semantic role dictionary](../themes/tokens/SEMANTICS.md) formalizes existing
color, surface/material, border/radius, elevation, motion, typography and state
roles. These are documentary bindings to the current contract, not new JSON
keys or runtime aliases. The [Noctalia Visual Language Grounding](NOCTALIA-VISUAL-GROUNDING.md)
records official-source concepts, KNOWN/INFERRED/MISSING findings, app-theming
feasibility and the Dolphin CURRENT → role → existing target mapping.

The detailed [VISUAL IDENTITY](VISUAL-IDENTITY.md) and retained
[legacy JSON](../ricy-kit/contributions/noctalia-visual-identity/tokens.json) provide
provenance, including older implementation stages. The legacy JSON is unchanged
and no longer a second editable authority. The transport copy has its own
historical tokens: do not assume synchronization.

| Role | Existing token reference |
|---|---|
| Surface/card | `#181825` / `#313244` |
| Text / secondary | `#cdd6f4` / `#a6adc8` |
| Accent / selection / outline | `#cba6f7` / `#977dba` / `#46485c` |
| Fitted glass / cards | Background opacity 0.70 / 1.00, opaque text |
| Shell font | Noto Sans; 11 / 13 / 14 / 16 / 20 logical px before scaling |
| Spacing / padding | 4 / 8 / 12 / 16 px; native padding 14 px |
| Radius | Native 3 / 6 / 9 / 12 px × scale 1.3; the bar has its own radii |
| Motion | Native 100 / 200 / 400 ms; app hover 140 ms; indicator 160 ms |

Dolphin, KDE, and terminal variants have specific adaptations in the tokens and
guide; do not universalize a component's radius, font, or opacity. Blur depends
on compositor implementation and window class, not just color/opacity.
Application icons retain their own identity.

KNOWN: TOML configs, JSON palettes, QSS, and installers still repeat values.
Central tokens can be parsed directly or packaged by approved applications;
they are not executable desktop configuration. The existing identity SVG is the
only migrated consumer, generated offline with byte-for-byte equality. No live
shell, Dolphin or global-theme consumer was migrated.
Workspace badge/group references are legacy records. The current cumulative
Ricy source patch disables these surfaces. The cumulative RICY-001/UUID build
was activated on 2026-10-11, superseding the earlier-binary observation in
[contribution grounding G-02](CONTRIBUTION-AUDIT.md); visual values are unchanged.
See [the inventory](WORKSPACE-AUDIT.md).
They do not authorize workspace interfaces. Later guide updates may supersede
older visual details; record discrepancies.
The grounding audit records current native blur and selected Dolphin source/QSS;
older ricyblur and translucent internal-panel descriptions in identity records
are historical stages, not instructions to restore that appearance. Exact
deployed compiled-helper provenance and full private palette equivalence remain
UNKNOWN; the grounding audit did not change tokens or visual settings. This
later token promotion preserves existing values and live settings.

## APPLICATION CONSUMPTION — KNOWN contract / PLANNED runtime
[ADR-0005](adr/0005-consumable-visual-tokens.md) records the authorized promotion
of existing values to plain versioned JSON. Future explicitly approved Ricy applications consume that source through a local toolkit adapter or bundled resource.
Use shared color/type/spacing/motion roles; keep shell, KDE, Dolphin and terminal
adaptations scoped. Font px/pt, scale, fill alpha and compositor blur must not
be conflated. Blur support for a new application remains UNKNOWN.

Migrate runtime consumers one at a time with before/after comparison, contract
versioning and rollback. Dolphin is the file manager under
[ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md); no own file-manager toolkit
or application is planned. Its [baseline](DOLPHIN-BASELINE.md) maps canonical
roles versus local Qt/QSS/Kvantum hardcodes without changing token values or
migrating consumers. The own prototype's token use is historical.
No desktop generator, SDK or live token loader was introduced. Do not create
arbitrary colors, radii, spacing, animations or a parallel design system.

Ownership: Ricy maintains visual roles; upstream retains toolkit primitives.
Dependencies: Noctalia Style, KWin/blur, Qt/Kvantum, and existing KDE/GTK themes.
Recovery: global adaptations may affect Plasma/Dolphin; visual changes there must
preserve usable tools and documented restoration.

For states/interactions, materials, or adaptations between components, use
[visual-development](../.agents/skills/visual-development/SKILL.md).
Validate normal, hover, focus, selected, disabled, scale, monitors, reduced motion,
and blur/junctions when applicable. Without real captures/interactions, report
Visual NOT RUN; parsing tokens does not prove appearance.

## Semantic selection — existing identity, values preserved

1. Classify purpose: base chrome, content, floating presentation, control, or
   inherited backing. Floating placement does not choose a color or shadow.
2. Choose the existing scoped material: solid, glass intent, state overlay or
   inherited fill. Ricy has no soft preset. Text/icons remain opaque.
3. Resolve color pairs and border/radius through the
   [dictionary](../themes/tokens/SEMANTICS.md). Native radii derive from the
   existing scale; Dolphin/bar adaptations retain their own values and owners.
4. Preserve consumer state, type units and motion preferences. Enter/exit/easing
   are contextual; no new app animation, font or universal disabled recipe.
5. Identify shadow/corner/blur ownership before painting: Noctalia shell,
   Qt/QSS/Kvantum popup or KWin window integration. Missing recipes remain
   MISSING; unknown live behavior remains UNKNOWN.

Noctalia is a reference/consumer and possible future generator. Ricy tokens
remain the authority. Shipped KColorScheme templates can modify global KDE
configuration and derive colors beyond Ricy's current palette; they are not
an approved propagation pipeline. The grounding evaluates options without
adopting one. A new integration/ownership/runtime contract requires
architecture-change and explicit approval before implementation.

The [READY FOR DOLPHIN POLISH list](NOCTALIA-VISUAL-GROUNDING.md#ready-for-dolphin-polish)
contains existing references for a subsequent approved task. No polish starts
in this grounding. No canonical token, active theme/profile, compositor or
Recovery runtime setting changes; no new Recovery dependency is introduced.

## Active system typography — Identity & Motion Pass

For the authorized Dolphin/Noctalia typography synchronization, use the active
KDE/Qt application font as the family authority. Dolphin inherits its point size;
Noctalia uses that family through official shell.font_family while preserving
contextual logical-pixel sizes and font_scale. Captured Noto Sans references in
canonical JSON/identity boards remain historical reference values, not commands
to override the user's system choice. Terminal/code/monospace roles remain
separate. See [the current evidence](DOLPHIN-BASELINE.md#identity--motion-pass--phase-1-typography--2026-10-11).
