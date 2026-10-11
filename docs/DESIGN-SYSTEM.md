# Design System

## CURRENT — KNOWN
Identity already exists. The detailed guide is [VISUAL IDENTITY](VISUAL-IDENTITY.md);
structured values are in
[tokens.json](../ricy-kit/contributions/noctalia-visual-identity/tokens.json).
This document is the normative entry point; it does not create a second palette.
The transport copy has its own historical tokens: do not assume synchronization.

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
Tokens are a documentary reference, not an executable configuration or generator.
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
UNKNOWN; this documentation audit does not change tokens or visual settings.

## TARGET — PLANNED
[themes/tokens](../themes/tokens/README.md) reserves the central location,
pointing to current tokens without copying values. Migrate consumers one at a time
with before/after comparison, contract versioning, and rollback. No new generator
or format has been selected. Do not create arbitrary colors, radii, spacing,
or animations, or a parallel design system.

Ownership: Ricy maintains visual roles; upstream retains toolkit primitives.
Dependencies: Noctalia Style, KWin/blur, Qt/Kvantum, and existing KDE/GTK themes.
Recovery: global adaptations may affect Plasma/Dolphin; visual changes there must
preserve usable tools and documented restoration.

For states/interactions, materials, or adaptations between components, use
[visual-development](../.agents/skills/visual-development/SKILL.md).
Validate normal, hover, focus, selected, disabled, scale, monitors, reduced motion,
and blur/junctions when applicable. Without real captures/interactions, report
Visual NOT RUN; parsing tokens does not prove appearance.
