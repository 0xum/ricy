---
name: kwin-development
description: Modify KWin effects, scripts, or patches used by Ricy, with version compatibility and protection of the Plasma session.
---

# kwin-development

1. Read [INVARIANTS](../../../docs/INVARIANTS.md),
   [RECOVERY](../../../docs/RECOVERY.md), and local AGENTS; consult COMPONENTS
   when ownership, boundaries, or dependencies are in question.
2. KWin is critical infrastructure. Prefer a conservative, local change;
   never replace the compositor or weaken mechanisms required for fallback.
3. Check the installed version, headers/ABI, upstream commit, patch, and licenses.
   The kit blur pins 6.7.5; do not assume binary compatibility with another version.
4. Separate patches from upstream and Ricy installers. Inspect application and
   restoration before changing an effect shared with Plasma/Dolphin.
5. Run the relevant isolated test first; real integration requires an appropriate
   environment and a return path. Do not manipulate windows containing work for evidence.
6. Preserve Plasma Recovery; document effect changes, dependencies, rollback,
   tests run, and NOT RUN checks. If new architecture is required, follow
   [architecture-change](../architecture-change/SKILL.md).
