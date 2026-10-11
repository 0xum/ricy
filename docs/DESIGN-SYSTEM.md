# Design System

## CURRENT — KNOWN
Identity already exists. The canonical consumable values are now in
[themes/tokens/tokens.json](../themes/tokens/tokens.json), contract 1.0.0/schema 1.
The [token contract](../themes/tokens/README.md) defines paths, semantics, units,
consumer status and application consumption. The [source audit](../themes/tokens/AUDIT.md)
records existing hardcodes and conflicts. This document remains the normative
entry point; it does not create a second palette.

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
Ricy source patch disables these surfaces; it is not yet the deployed binary,
as established by [contribution grounding G-02](CONTRIBUTION-AUDIT.md).
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
of existing values to plain versioned JSON. Future Ricy applications, especially
Files, consume that source through a local toolkit adapter or bundled resource.
Use shared color/type/spacing/motion roles; keep shell, KDE, Dolphin and terminal
adaptations scoped. Font px/pt, scale, fill alpha and compositor blur must not
be conflated. Blur support for a new application remains UNKNOWN.

Migrate runtime consumers one at a time with before/after comparison, contract
versioning and rollback. Files' toolkit and implementation remain undecided.
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
