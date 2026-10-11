---
name: ricy
description: Manual bootstrap for Ricy tasks using the existing agent-first harness.
---

# Ricy task bootstrap

Use this repository's existing agent-first harness.

- Follow every AGENTS.md applicable to the task area.
- Use en-US for project content and interfaces, as required by the root AGENTS.md.
  Chats may remain in the user's preferred language, including pt-BR.
- Use progressive disclosure and load only the context needed for the actual
  consequences of the change.
- Investigate the current state before modifying it.
- Do not silently create new architecture.
- If the solution requires an architectural decision that has not been made:
  - present evidence;
  - present options;
  - explain impact;
  - make a recommendation;
  - stop and wait for explicit approval before implementing that part.
- Preserve architectural invariants and Plasma/Dolphin Recovery.
- Run appropriate validation before claiming success.
- Distinguish PASS, UNKNOWN, NOT RUN, and NOT APPLICABLE when relevant.

The user's task description is the current objective.
