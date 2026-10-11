---
name: documentation
description: Create Ricy documentation, update architecture/ADRs or sources of truth, and record significant changes; not required for a typo, comment, or local wording change that does not affect decisions.
---

# documentation

1. Read [AGENTS](../../../AGENTS.md) and look for an equivalent before creating a file.
   Prefer consolidation or a link to the maintained source, preserving history.
2. Describe why, what, constraints, ownership, dependencies, and recovery implications.
   Use KNOWN with a path/evidence; INFERRED with a reason; PLANNED for an approved
   destination; UNKNOWN when proof is missing. Do not narrate every line of code.
3. Separate normative intent from observed behavior; record conflicts without silently
   correcting them. ADRs explain why, without duplicating technical manuals.
4. Use valid relative links and progressive sources; do not copy private records into
   public documentation. Preserve historical paths and licenses. Use en-US as required
   by the root AGENTS.md; chats may use the user's preferred language.
5. Update [CHANGELOG](../../../docs/CHANGELOG.md) for significant changes with
   Model/Agent, Date, Purpose, and Validation performed. Do not sign source files.
6. Run `./scripts/verify architecture`, review links, and report limitations.
   Significant architectural changes follow
   [architecture-change](../architecture-change/SKILL.md).
