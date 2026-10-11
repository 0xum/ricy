---
name: visual-development
description: Change visual states/interactions, materials, or adapt identity between Ricy components; an isolated change to an existing token only requires DESIGN-SYSTEM and local rules.
---

# visual-development

1. Read [DESIGN-SYSTEM](../../../docs/DESIGN-SYSTEM.md) and only the relevant
   identity guide section. Look for existing tokens and components.
2. Identify the actual consumer (Noctalia Style, Qt/QSS/Kvantum, KWin, or a theme).
   Reuse existing roles and values, respecting units, scale, and toolkit.
3. Prohibited: random colors, random radius, random spacing, random animations, and
   parallel design systems. Do not copy tokens to establish another authority.
4. Preserve geometry, readability, application icons, reduced motion,
   hit areas, and Ricy identity. Do not generalize Noctalia blur to other apps.
5. When a suitable tool is available, verify before/after in normal, hover, focus,
   selected, and disabled states, relevant scales/monitors, and blur junctions.
   Without visual access, report NOT RUN and the limitation; parsing does not prove appearance.
6. Update the reference only when the corresponding change is validated;
   record recovery implications for Plasma/Dolphin. New values require justification
   in the central system, not a parallel convention hidden in the component.
