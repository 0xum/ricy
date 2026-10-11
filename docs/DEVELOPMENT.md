# Agent-first Development

## Entry point and workflow
Follow the applicable hierarchy and consequence-based routing in [AGENTS](../AGENTS.md).
A local fix starts with local code, documentation, and tests. Load additional docs
when impact reaches their domain; the authority order is not a universal reading
list. If an affected boundary or contract is discovered, expand context before
implementing. A known validation command does not require loading the testing
skill. Do not run installers to understand them. Active-kit profiles, backups,
and state are private.

## Project language
[Always use en-US as the language.]

Use US English for project documentation, agent instructions, comments,
developer messages, and public-facing interfaces. Chats may use pt-BR.
The full [language policy](../AGENTS.md#project-language) requires en-US file names while preserving deployed compatibility identifiers,
private state, historical manifests, licenses, upstream localization catalogs,
and private regional preferences. See [FILE-RENAMES](FILE-RENAMES.md). New public content and names use en-US.

## Executable validation
From the project root (or with an absolute path; scripts resolve their own root):

```bash
./scripts/verify architecture
./scripts/verify shell
./scripts/verify recovery
./scripts/verify all
./scripts/doctor
python3 scripts/test-foundation.py
```

`verify` uses Python 3.11+ and existing tools; it does not install dependencies.

- `architecture`: required files, skills/frontmatter, local rules, relative
  foundation Markdown links, and syntax of the new scripts.
- `shell`: Bash/Python/JSON/TOML syntax in active-kit sources (excluding work,
  outputs, backups, and upstream assets); offline Noctalia action tests when
  a local source matches the expected commit/patch and PyQt6 is available.
- `recovery`: existing in-memory panel capture/merge test; QJSEngine window-effect
  tests when PyQt6 is available. Does not switch shell/compositor.
- `all`: combines the above; does not certify the desktop.
- `doctor`: read-only diagnostics of tools, packages through pacman, reported
  environment, units, and the Plasma Wayland entry. Never performs repairs.

`python3 scripts/test-foundation.py` exercises 17 validator scenarios in a
temporary fixture, including missing files/links, component failure, and an
unavailable dependency. verify does not run it recursively.

Exit codes: verify 0 = executed checks passed without dependency skips;
1 = a check failed; 2 = an offline check could not run, without FAIL;
invalid usage also returns 2. Live trials always remain `NOT RUN`, outside
automatic scope. Doctor: 0 = queries completed; 2 = some information is UNKNOWN;
this never means the desktop is healthy. No command uses sudo.

Link checking covers foundation files, the root README, and local AGENTS,
without traversing the entire history, external links, or title anchors.
It checks inline Markdown targets and link references; text in code blocks
is not a link. Inline-code paths and runtime symlinks are outside its scope.
Preserved historical documents may contain old paths.

## Levels and evidence
| Level | When relevant | Limit |
|---|---|---|
| Static | Changed docs, rules, scripts/configs | Parsing/link checks do not guarantee behavior |
| Component | Component logic | Run appropriate local regressions |
| Integration | D-Bus contracts, units, profile, and KWin | Run in a prepared environment with a return path |
| Recovery | Login, compositor, shell, defaults/files | Offline tests do not replace real round trips and login |
| Visual | Appearance/interaction changes | Record captures/observations, monitors, and scale |
| Environment | Dependencies and versions | Package presence does not prove compatibility |

Report `PASS`, `FAIL`, `NOT RUN <reason>`, and `NOT APPLICABLE <reason>`.
Do not claim “This should work”, “Probably fixed”, or “Everything is working”
without evidence. Attribute historical results to their original session.

## Changes and future publication
Use [CHANGELOG](CHANGELOG.md) for Model/Agent, Date, Purpose, and Validation performed.
Unplanned architectural changes follow
[architecture-change](../.agents/skills/architecture-change/SKILL.md).
The local Git baseline selection is recorded in [GIT-BASELINE](GIT-BASELINE.md).
Before publication, review the privacy, portability, and license/attribution
caveats recorded there. Keep the explicit source/asset selection separate from
profiles, clipboard, backups, and state; do not run `git add .` in the active kit.
No remote, global license, or release has been selected.
Consult [MIGRATION-PLAN](MIGRATION-PLAN.md) for sequence and risks.
