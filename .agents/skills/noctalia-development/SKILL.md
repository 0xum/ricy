---
name: noctalia-development
description: Change Ricy Noctalia patches, APIs, profile behavior, or Noctalia/KWin integration; changes limited to existing visual values follow DESIGN-SYSTEM and local rules.
---

# noctalia-development

1. Follow local shell rules. Consult [COMPONENTS](../../../docs/COMPONENTS.md)
   to locate ownership/contracts; [ARCHITECTURE](../../../docs/ARCHITECTURE.md)
   when responsibilities/coexistence change. Noctalia is the primary shell.
2. Identify the current cumulative variant and confirm the actual version/commit/patch.
   Do not apply complete historical patches sequentially. Ricy may have its own patches,
   clearly distinguished from upstream and accompanied by a license.
3. Verify APIs in the compatible version's source; do not assume APIs from another
   implementation/release named Noctalia. The current build pins Noctalia 5.2.1.
4. Workspaces are not part of the product. Do not add UI, actions, or gestures.
   Record existing remnants without confusing internal KWin objects with the UX.
5. Respect KWin as the window manager; use existing integrations. Visual work requires
   DESIGN-SYSTEM; use [visual-development](../visual-development/SKILL.md) for
   states/interactions, materials, or adaptations between components.
6. If crashes, readiness, child applications, shortcuts, or Plasma return are affected,
   read RECOVERY and relevant invariants/ADRs. Preserve /usr/bin/noctalia, snapshots,
   and activation/reversal tools. Do not restart the shell to validate documentation.
7. Run appropriate checks from [DEVELOPMENT](../../../docs/DEVELOPMENT.md),
   and document the version, evidence, and integration/visual/recovery limitations.
