# Technical Changelog

Record significant changes in short entries. Minimum fields:
Model/Agent, Date, Purpose, Validation performed. Do not sign source files.

## 2026-10-11 — Current contribution grounding

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** distinguish actual consumers, recovery dependencies, migration
  inputs and historical variants across all existing Ricy contributions without
  moving/removing files or changing runtime behavior.
- **Changes:** added [CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md) with individual
  classifications for all 24 contribution directories, corresponding transport
  snapshots, three materialized community plugins and shared/generated material.
  Records consumers, dependencies, relationships, cumulative lineage, recovery
  impact, previously mapped future destinations and explicit UNKNOWNs. COMPONENTS
  now carries class labels; architecture, recovery, migration, design and agent
  entry points link to the maintained evidence. No REMOVE verdict was justified.
- **Findings:** running Noctalia matches the earlier reordering variant preserved
  in the transport diff, not the current single-space source patch; native blur
  is loaded and the registered ricyblur selector is failed. Window-fade-expand
  matches the installed effect. Source/installed translations, version-specific
  destination corrections, disabled adaptivepanelwidth, and unproven community
  plugin functionality are recorded without replaying installers or repairs.
- **Validation performed:** PASS `./scripts/verify architecture`, inventory
  coverage, `git diff --check`, and SHA-256 preservation comparison. PASS shell
  syntax subcheck (83 candidates); `./scripts/verify shell` returned exit 2 with
  source-based Noctalia tests NOT RUN because the cache differs from the current
  patch. PASS `./scripts/verify recovery` (exit 0), including panel preservation
  and 28 isolated window-effect scenarios. `./scripts/doctor` returned exit 2
  with two UNKNOWN diagnostic categories. FAIL preexisting blur-selector state
  was observed separately through systemd/KWin/current-boot journal reads.
  NOT RUN live login, unlock, switching/failure recovery, interactive Dolphin,
  plugin use, package installation, input/connectivity and visual validation.
  New implementation/validator regressions and ADRs are NOT APPLICABLE.
- **Preservation:** only Markdown documentation and agent routing changed; one
  documentation file added. No implementation, token, manifest, installed unit,
  profile, private state, backup, asset or historical record was rewritten. No
  existing file was moved or removed; no service/compositor was restarted.

## 2026-10-11 — RICY-001 workspace exposure audit

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** remove safe Ricy-owned workspace exposure while preserving KWin
  infrastructure and Plasma/Dolphin Recovery. The
  [pre-change inventory](WORKSPACE-AUDIT.md) classifies product UI, internal APIs,
  shared recovery surfaces and uncertain external/runtime behavior.
- **Changes:** updated the current cumulative Noctalia 5.2.1 patch to block the
  workspace widget and aliases, force a flat taskbar, remove explicit desktop
  activation fallback, workspace commands/scroll bindings, workspace settings and
  desktop-triggered bar reveal. Legacy keys still parse; taskbar/window-switcher
  visible-desktop membership remains internal. The compiled CLI rejects legacy
  workspace verbs locally, including when an earlier shell is running. Public
  templates disable grouping/labels; current identity references exclude these
  surfaces without changing numeric design values. Historical patches, transport
  kit, manifests, private profile/state and installed recovery settings are preserved.
- **Harness:** added isolated source selection through `RICY_NOCTALIA_SOURCE` and
  extended the native drag validator with single-space policy regressions.
  Foundation fixtures retain linked patch files and isolate source-override tests.
- **Validation performed:** PASS isolated Meson/Ninja release build; PASS
  `RICY_NOCTALIA_SOURCE=<isolated-source> ./scripts/verify all` (zero failures and
  zero unavailable offline checks), including native widget/alias/picker/settings,
  legacy-profile/drag, CLI rejection, 17 window-action scenarios, panel preservation
  and 28 window-effect scenarios. PASS `python3 scripts/test-foundation.py`
  (17 scenarios), order (22), motion (20), indicator/effect (15), and compiled
  validation of both public TOML templates. PASS clean pinned patch replay: all
  26 cumulative source files match the validated checkout; ten differ from the
  previous cumulative variant. PASS exact patch/source diff comparison and original
  cache preservation. PASS source `git diff --check` and repository
  `git -c core.whitespace=-blank-at-eol diff --check` (unified-diff blank context
  markers are intentional patch syntax).
- **Limits:** NOT RUN live visual, gestures, session switching, persistent failure,
  login and Dolphin recovery trials. The new binary was compiled separately and
  was not activated. Shared KWin shortcuts, native desktop menus/settings and
  possible gestures remain preserved; complete live RICY-001 compliance is UNKNOWN.
  NOT APPLICABLE compositor ABI/replacement and new architecture: neither changed.

## 2026-10-11 — Refresh menu launcher after file rename

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** repair menu activation after the English file rename.
- **Evidence:** the installed desktop entry already referenced `open-menu.sh`,
  but KWin's embedded KGlobalAccel retained the previous service object and
  attempted the removed filename. Application database rebuilding and action-only
  re-registration were insufficient.
- **Changes:** recreated only the menu launcher component, restoring its active
  and default shortcuts from a private snapshot; documented the required refresh
  in [FILE-RENAMES](FILE-RENAMES.md). No compositor, shell, or session restart.
- **Validation performed:** PASS desktop-entry validation, executable target,
  active/default shortcut comparison, registered `_launch` invocation, and
  Noctalia's live `activePanelId=launcher` response. No new missing-program error
  appeared in the journal after the successful invocation. PASS architecture
  verification and `git diff --check`.
- **Limits:** NOT RUN full login/crash recovery; live validation covers menu activation.

## 2026-10-11 — English file names

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** extend the en-US policy to existing project file names at the
  user's explicit request, superseding the previous path-preservation exception.
- **Changes:** renamed 227 files across the repository root and both kits using
  74 English basename mappings. Updated callers, imports, installers, launcher
  references, palette names, patches, validators, and documentation. Added
  [FILE-RENAMES](FILE-RENAMES.md) with the complete mapping and compatibility limits.
  Existing directory names were already in English. Historical SHA256SUMS and
  private backup/state paths remain unchanged; operational manifest paths and
  replacement digests use current sources. Existing systemd IDs remain compatible
  through an explicit mapping to English template names.
- **Recovery implications:** five installed unit/launcher files referenced old
  repository paths. Their references were corrected after creating private backups
  outside the repository; systemd configuration was reloaded without stopping or
  restarting services. No session switch or installation was performed.
- **Validation performed:** PASS `./scripts/verify all` and
  `python3 scripts/test-foundation.py` (17 scenarios); PASS `git diff --check`.
  PASS all 227 rename destinations, old-path absence, and executable permissions;
  PASS parsing 123 Python files, Bash syntax for 69 scripts, and 36 JSON files in
  the public source selection. PASS installed systemd unit verification and
  absence of obsolete filename references in current sources (historical manifests
  and the rename map are intentional exceptions).
- **Limits:** NOT RUN live session/login/crash recovery. Other installed copies
  require their own reference updates or deliberate reinstallation.

## 2026-10-11 — en-US project language

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** use US English for project content and public-facing interfaces,
  while allowing pt-BR in chats according to the user's preference.
- **Changes:** translated project documentation, ADRs, local agent rules/skills,
  comments, script diagnostics, interface labels, metadata, and visual-reference
  text in the active and transport kit trees. Added `[Always use en-US as the language.]`
  to AGENTS, README, and DEVELOPMENT, with routing through the ricy/documentation skills.
  Existing paths, identifiers, private state, licenses, upstream localization catalogs,
  and historical SHA256SUMS remain preserved. The restore confirmation now displays
  and accepts `y/N`. Operational correction-manifest hashes were updated for translated
  sources; the active kit's preexisting modified target remains protected from replacement.
- **Validation performed:** PASS `./scripts/verify architecture` and
  `./scripts/verify all` (required files/links, syntax, 17 Noctalia scenarios,
  panel capture/merge, and 28 isolated KWin scenarios); PASS
  `python3 scripts/test-foundation.py` (17 scenarios); PASS `git diff --check`.
  Both kits' changed sources passed checks: 121 Python files, 43 Bash files,
  16 JSON files, and 2 SVG/XML files. Python AST comparison confirmed no
  changes beyond string constants/comments. PASS transport correction patch
  applicability and replacement-file hash checks. The active correction target's
  preexisting hash mismatch remains rejected. Installer labels/layout were
  inspected in an offscreen Qt window without selecting a package; the translated
  SVG reference was rendered and visually inspected.
- **Recovery implications:** shell/session selection, backups, and recovery paths
  remain in place. No installation, service restart, or session switching was performed.
- **Limits:** NOT RUN live session/login/crash recovery or full desktop visual review.
  The installer UI was inspected offscreen without selecting or installing a package.
  No publication or migration was performed.

## 2026-10-11 — Local Git baseline

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** establish an auditable Git baseline on `main`, with explicit source
  and asset selection, without a remote, publication, reorganization, or runtime change.
- **Changes:** conservative `.gitignore`, record in [GIT-BASELINE](GIT-BASELINE.md),
  and Git state update in DEVELOPMENT. Selected 1,098 files; excluded 1,939 local files
  from the index while preserving them on disk. Backups, clipboard, notification
  history, profile/work, bytecode, and ZIP containing private state are outside the
  baseline. Templates, patches, evidence, and assets remain.
- **Validation performed:** PASS `./scripts/verify architecture` (52 required files
  and local links); PASS `./scripts/verify all` (83 syntax candidates, 17 Noctalia
  scenarios, panel capture/merge, and 28 KWin scenarios); PASS
  `python3 scripts/test-foundation.py` (17 scenarios). All exited 0. Heuristic search
  of 1,098 staged files, including 244 decompressed SVGZ files, found no evident
  credentials. No gitlinks in the index; executable permissions preserved.
- **Preservation:** initial SHA-256 inventory; no preexisting file removed or with
  changed permissions. Only DEVELOPMENT and this CHANGELOG were edited by the task.
  Private notification history changed during the session through external activity;
  it was not written, reverted, or versioned by the task.
- **Limits:** NOT RUN live session/recovery; NOT APPLICABLE visual validation and
  installation because behavior did not change. Licenses, personal/machine references,
  and portability still require review before publication; the local baseline does
  not certify that all content is safe to publish.

## 2026-10-11 — Agent-first foundation

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** formalize the requested architecture around existing kits, with
  invariants/ADRs, a map of 24 contributions, progressive rules/skills, diagnostics,
  and offline checks, without migrating runtime or changing the session.
- **Changes:** AGENTS/CLAUDE, architectural docs, documentary reservations, seven
  skills, local rules, scripts/verify, and scripts/doctor. README gains an architectural
  entry point; preexisting text is preserved. No legacy file removed.
- **Validation performed:** `./scripts/verify architecture` and `./scripts/verify all`
  passed (exit 0): structure/links, syntax of 83 kit files, 17 Noctalia scenarios,
  panel capture/merge regressions, and 28 isolated KWin scenarios.
  `python3 scripts/test-foundation.py`: 17 behavioral checks passed.
  The seven skills passed `skill-creator/scripts/quick_validate.py` using a temporary
  virtual environment with PyYAML 6.0.3, without a new runtime dependency.
  `./scripts/doctor`: expected exit 2, two UNKNOWN items (live recovery and complete
  RICY-001 compliance); package/unit queries completed. The first quick_validate
  did not run in system Python because PyYAML was missing; it was repeated successfully
  in the isolated environment.
- **Limits:** login, switching, and crash recovery were not tested in this documentary
  change. C-001 through C-005 are recorded discrepancies, not runtime fixes.
- **Preservation check:** 51 new files; README was the only preexisting file edited by
  the task, retaining its entire previous text. SHA-256 comparison of 2,978 initial
  files also found a change in the active profile's `notification_history.json`
  during the session. The task did not write or revert that state. The other 2,976
  files retained their hashes; no preexisting file was removed or had permissions changed.

## 2026-10-11 — Context by consequence

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** reduce universal reading without changing architectural authority or
  approval. CLAUDE imports AGENTS; root/DEVELOPMENT/index and local routers load
  sources by impact. The component-development, testing, documentation,
  noctalia-development, and visual-development skills have more specific triggers;
  KWin retains invariants/recovery and consults the map by domain. DESIGN-SYSTEM
  only conditions invocation of the visual skill; visual values and guarantees remain.
- **Context before → after:** a local visual change previously chained architecture,
  invariants, the map, and general skills; it now uses the AGENTS hierarchy,
  DESIGN-SYSTEM, and local code/docs/tests. New architecture still requires
  ARCHITECTURE, INVARIANTS, relevant ADRs, a boundary map, and explicit approval.
- **Validation performed:** `./scripts/verify architecture` and `./scripts/verify all`
  passed (exit 0); `python3 scripts/test-foundation.py` passed all 17 scenarios;
  the seven skills passed quick_validate.py in the existing virtual environment.
  The `@AGENTS.md` import was checked statically; loading through Claude Code was
  not executed. Live session/recovery tests remain NOT RUN.
- **Runtime Changes:** None. Invariants, ADRs, architecture/recovery sources,
  validators, and implementation preserved; no new or removed file.
