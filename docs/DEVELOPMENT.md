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
- `shell`: Bash/Python/JSON/TOML syntax in maintained active-kit sources (excluding
  work, outputs, backups, upstream assets, and explicitly HISTORICAL recipes);
  syntax of the seven historical build guards; offline Noctalia action tests when
  a local source matches the expected commit/patch and PyQt6 is available;
  single-space policy and native drag regressions when that source has a build.
- `recovery`: existing in-memory panel capture/merge test; QJSEngine window-effect
  tests when PyQt6 is available. Does not switch shell/compositor.
- `all`: combines the above; does not certify the desktop.
- `doctor`: read-only diagnostics of tools, packages through pacman, reported
  environment, units, and the Plasma Wayland entry. Never performs repairs.

`python3 scripts/test-foundation.py` exercises validator scenarios in a
temporary fixture, including missing files/links, component failure, and an
unavailable dependency, plus historical source selection and build isolation.
verify does not run it recursively.

Exit codes: verify 0 = executed checks passed without dependency skips;
1 = a check failed; 2 = an offline check could not run, without FAIL;
invalid usage also returns 2. Live trials always remain `NOT RUN`, outside
automatic scope. Doctor: 0 = queries completed; 2 = some information is UNKNOWN;
this never means the desktop is healthy. No command uses sudo.

Set `RICY_NOCTALIA_SOURCE` to an isolated checkout to validate or build the current
cumulative patch without replacing the private active source cache. Both
`verify shell` and `app-icon-reordering/build.sh` accept it and still check the
pinned commit and exact diff. Build commands do not activate the shell. See
[WORKSPACE-AUDIT](WORKSPACE-AUDIT.md) for the scope and preserved recovery surfaces.

## Historical reproduction

The [grounding audit](CONTRIBUTION-AUDIT.md#first-safe-cleanup) records the first
cleanup and its dependency review. No item is approved as REMOVE, so no file is
deleted. Normal source selection excludes the six superseded cumulative folders,
the notification-only builder, the reordering folder's old effect installer, and
the two historical root generators. This is an explicit list, not a rule based
on age or directory names. Notification activation/restoration and wallpaper
preparation, switching, autostart, Dolphin, and all UNKNOWN sources stay selected.
Historical build guards still receive Bash syntax checks.

For current shell source development, use
[app-icon-reordering](../ricy-kit/contributions/app-icon-reordering/README.md).
Its RICY-001 patch is MIGRATE pending activation; it differs from the deployed
binary/cache. The deployed binary and cache remain rollback/provenance material.
The selected window effect belongs to
[window-fade-expand](../ricy-kit/contributions/window-fade-expand/README.md).
Never apply an earlier cumulative patch or effect as the current default.

The seven historical shell builders refuse default execution before probing
Noctalia, cloning, patching, or building. Deliberate reproduction requires both
`RICY_BUILD_HISTORICAL=1` and an absolute `RICY_NOCTALIA_SOURCE` in a separate
checkout outside this repository and the preserved source cache. For example,
from the project root, using a new destination outside the kit:

```bash
RICY_BUILD_HISTORICAL=1 \
RICY_NOCTALIA_SOURCE="$HOME/.cache/ricy-history/taskbar-menu-composition" \
bash ricy-kit/contributions/taskbar-menu-composition/build.sh
```

This opt-in may download/build the pinned source; it never activates the result.
Repository/cache paths and symlink aliases are rejected. Keep the resulting
binary separate from normal activation. Restore historical bytes into an isolated
destination through Git when needed; the pre-cleanup builders are in commit
`1fb1918`. Do not add duplicate snapshots or regenerate SHA256SUMS.
The transport tree, manifests, archive, licenses, old applicators/restorers, and
compatibility outputs retain their historical paths. Transport recipes are
preserved evidence and have not received the active-tree guards; do not execute
them as normal development, installation, or recovery instructions.

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
