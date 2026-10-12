# Technical Changelog

Record significant changes in short entries. Minimum fields:
Model/Agent, Date, Purpose, Validation performed. Do not sign source files.

## 2026-10-11 — Rounded Dolphin path dropdown

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** widen the compact path-dropdown button so its approved rounded
  hover backing fits, matching the root breadcrumb button reference.
- **Changes:** the existing Qt helper reserves a 24px width for
  KUrlNavigatorDropDownButton, retaining the existing 28px height, radius6 and
  hover-selection alpha65 treatment. Upstream derives the natural width from
  half the natural height; the earlier helper height override left the button
  too narrow. The user's clarification supersedes the initial glyph-only edit;
  glyph geometry/stroke are restored and no oversized backing is painted outside
  the control. Native menu, keyboard handling and breadcrumb behavior remain.
  Atomic helper-only installation with private existing-restorer-compatible backups.
- **Validation performed:** PASS helper compilation, native KUrlNavigator Qt
  fixture with ten breadcrumb/editor toggles and unchanged URL/editor; controlled
  hover in a real Dolphin window using the installed wrapper and a uniquely named
  private diagnostic plugin confirms 24x28 bounds and unclipped rounded backing.
  PASS architecture/token checks and whitespace. No token or KWin change.
- **NOT RUN:** all scales/RTL, complete dropdown-menu keyboard interactions and
  live Recovery. Existing windows retain their mapped helper; new processes load
  the change. The documented shutdown SIGSEGV remains outside this visual edit.

## 2026-10-11 — Dolphin first visual polish pass

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** correct confirmed QSS spacing/state inconsistencies in the current
  installed Dolphin while retaining approved layout, native behavior and the
  separately updated tab-overflow helper.
- **Changes:** normalize residual generic padding from 5px to existing 4px; preserve
  checked/pressed toolbar interaction fill/foreground during hover; explicit
  accent focus contours in existing border slots; unfilled disabled tools.
  Atomically deploy only QSS with a private existing-restorer-compatible backup.
  The native full-width status experiment exposed clipped storage controls and
  was reverted; dolphinrc equals its initial bytes. No token, helper, theme,
  launcher, MIME, FileManager1, filesystem implementation or KWin change.
- **Validation performed:** PASS Qt QSS painting/state precedence and native
  editor/tab/menu interactions at 1x/1.5x; installed-wrapper startup, directory/tab
  navigation and live grid/compact/details captures; token checks, architecture,
  Recovery offline, Kvantum INI/SVG parsing and changed-file whitespace checks.
  PASS limited native offline fallback with missing optional visual layers and
  Fusion under isolated D-Bus/config/state/data; not automatic Recovery.
- **FAIL (preexisting):** customized Dolphin shutdown SIGSEGV in Qt application
  destruction, also present before edits and documented by the tab-overflow task.
- **UNKNOWN / NOT RUN:** independent live Recovery, every device/hover/focus state,
  complete popup composition, live scale/monitor/RTL/reduced-motion combinations.
  No complete Recovery-regression claim. No new compiled layer or backend test
  applies. Wrong/incomplete early test captures were discarded after user correction.
- **Record/backlog:** [first-pass audit](DOLPHIN-BASELINE.md#first-visual-polish-pass--2026-10-11)
  documents categories, current-source differences, unchanged ownership/dependencies,
  recovery implications and deferred status/lifetime work. No second phase.

## 2026-10-11 — Dolphin tab overflow controls

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prevent tab close controls from overlapping overflow arrows and
  provide 8px trailing spacing using existing Dolphin/Qt ownership and spacing.
- **Changes:** horizontal scroll subelement geometry reserves 64px; native 24px
  arrow buttons have an 8px gap and 8px edge inset. Close-button paint/hit masks
  exclude clipped controls and reset after scrolling/resizing. Installed only
  the Qt helper atomically with a restorer-compatible private backup; existing
  windows retain their mapped helper. No new architecture or Recovery dependency.
- **Validation performed:** PASS helper build, 18 Qt overflow layouts across
  three widths/LTR/RTL/three selections, native close/scroll clicks and restored
  masks after overflow removal; live Dolphin capture/probe confirms geometry.
  PASS `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py`
  and `git diff --check` for the changed files.
- **FAIL (preexisting):** live probe teardown SIGSEGV in Qt application
  destruction reproduced with the preserved pre-change helper as well as this
  change, including window close. Captured geometry passes; clean process exit
  does not. No unrelated teardown fix is claimed.
- **Publication validation:** PASS architecture/token checks and helper build
  against the selected Git index in an isolated export. An existing audit link
  to the intentionally excluded private ZIP was changed to a plain path; no
  archive contents were added. Unrelated visual-grounding edits remain local.
- **NOT RUN:** all monitor scales, live drag/reorder and live Recovery.
  Offline checks do not certify the session. Transport snapshots are preserved.


## 2026-10-11 — Dolphin final-tab containment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** keep the final tab border inside the shell panel when no overflow
  arrows are shown.
- **Changes:** bound the horizontal Qt tab-bar allocation with an 8px trailing
  gutter, mirrored for RTL; preserve content geometry and existing overflow
  controls. Installed the helper atomically with a restorer-compatible backup.
  No new architecture, tokens, compositor change or Recovery dependency.
- **Validation performed:** PASS helper build; eight Qt allocations across
  four widths/LTR/RTL with and without overflow; native last-tab close;
  previous 18 overflow cases and close/scroll/mask regressions; live Dolphin
  seven-tab capture/probe with hidden arrows and an 8px trailing gutter;
  `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py` and
  changed-file `git diff --check`.
- **FAIL (preexisting probe limitation):** live capture process exit 139 at
  teardown; the previous comparison reproduced failure with the prior helper.
- **NOT RUN:** all monitor scales, live drag/reorder and live Recovery.
  Existing processes retain their mapped helper; new windows load this update.


## 2026-10-11 — Dolphin rounded purple overflow indicator

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** replace the thin blue tab-overflow line with the existing purple
  accent, a 4px width and rounded ends.
- **Changes:** Qt helper paints the native tear primitive and reserves its wider
  horizontal rectangle. Qt retains visibility/placement and native tab controls.
  No token, compositor, architecture or Recovery dependency changed. Installed
  the helper atomically with a restorer-compatible private backup.
- **Validation performed:** PASS helper build; LTR/RTL pixel checks for accent,
  4px geometry, rounded tips and native visibility; 18 overflow layouts and
  native close/scroll regressions; live Dolphin capture;
  `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py` and
  changed-file `git diff --check`.
- **FAIL (preexisting probe limitation):** live capture-process teardown again
  exited 139; the previous baseline comparison reproduced the same failure.
- **NOT RUN:** all display scales, live Recovery and every tab interaction.
  Existing windows keep the mapped helper; open a new window for the update.

## 2026-10-11 — Noctalia Visual Language Grounding

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** formalize existing Ricy visual roles using official Noctalia v5+
  concepts while preserving themes/tokens as the canonical authority.
- **Changes:** updated [DESIGN-SYSTEM](DESIGN-SYSTEM.md), added the documentary
  [semantic dictionary](../themes/tokens/SEMANTICS.md) and
  [grounding assessment](NOCTALIA-VISUAL-GROUNDING.md). Recorded
  KNOWN/INFERRED/MISSING findings, color correspondences, surfaces/materials,
  border/radius/shadow ownership, contextual motion/type/states, App Theming/
  KColorScheme feasibility, Dolphin CURRENT → role → existing token mapping
  and READY FOR DOLPHIN POLISH references. The existing token validator now
  resolves documentary canonical paths; it does not implement semantic aliases.
  No new architecture/generator contract was selected or made normative.
- **Validation performed:** PASS `./scripts/verify architecture`,
  `python3 -B scripts/test-foundation.py` (39 disposable-fixture regressions),
  `python3 -B themes/tokens/validate.py` (95 documentary token references plus
  existing schema/units/provenance/equality checks),
  `python3 -B themes/tokens/render-reference.py --check` (identical SVG),
  five isolated reference-validator probes (valid scalar/group and rejection
  of missing scalar/scoped leaf, empty references and scalar traversal),
  47 local documentation links/three heading anchors and diff whitespace.
  Official URLs were accessed and the pinned upstream template/Style source
  was inspected read-only. Repository/selected runtime fingerprints confirm
  unchanged canonical JSON, existing identity assets and 49 selected installed
  configuration/asset files; unrelated preexisting work was preserved.
- **Harness scope:** `./scripts/verify all` exited2 with no failures and one
  unavailable check. PASS maintained source syntax/historical guard syntax,
  offline Recovery panel merge and 28 window-effect scenarios. This does not
  certify a live session.
- **FAIL:** none remaining. The initial foundation regression rejected new
  direct links to outputs excluded from its fixture. Grounding now cites the
  maintained provenance inventory and records those inspected paths as text;
  the unchanged foundation suite passes. An initially incorrect external
  Theme path was corrected to the official navigation target.
- **NOT RUN:** Noctalia action/native regressions through the default harness
  cache, which does not match the current cumulative patch; no cache was
  rebuilt/replaced for this documentation task. Visual/scale/RTL interactions,
  application propagation, live session and failure Recovery were not exercised.
- **UNKNOWN:** generated output equivalence/end-to-end app theming, full private
  palette equivalence, composited opacity/blur continuity, full shadow toggles,
  helper lineage and independent live Recovery. Missing semantic values remain
  unassigned rather than borrowing upstream defaults.
- **NOT APPLICABLE:** runtime deployment, visual changes, generator/consumer
  migration, KWin changes, new daemon/engine/ADR and automatic Dolphin polish.
- **Recovery:** no applicator/hook/installer, profile/theme selection, service
  restart, file-manager launch or compositor action ran. Canonical JSON remains
  schema1/contract1.0.0 byte-identical; QSS/Kvantum/KColorScheme and existing
  restoration paths remain intact. Rollback affects only this step's
  documentation and reference-validator edits; no runtime dependency was added.

## 2026-10-11 — Taskbar actions preserve the clicked KWin window

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** fix separate Brave/Dolphin icons activating another window of
  the same application, particularly across two monitor bars.
- **Changes:** the cumulative Noctalia 5.2.1 patch (pinned commit
  `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`) marks nonempty KWin UUIDs as exact
  identities. This uses the existing authoritative task identity for
  focus/minimize/close, preventing monitor/placement reconciliation from
  substituting a same-app window. No runtime dependency, ownership boundary,
  design value, window effect or session architecture changed. The native
  validator now covers the compiled KDE adapter/model/action path on a private
  D-Bus KWin fixture; `dbus-run-session` is an offline-test dependency only.
- **Validation performed:** PASS isolated release build, clean patch replay
  (26 source files), `verify architecture`, `verify shell` with the matching
  isolated source, `verify recovery` offline, 39 foundation regressions,
  32 compiled KDE identity/action scenarios, 17 JS action scenarios,
  22 ordering scenarios, 20 icon-motion scenarios, 15 indicator/historical
  effect scenarios, native single-space/drag regressions, active service
  configuration validation and diff whitespace. The new regression failed
  against the preserved earlier build with a substituted window UUID and
  passed against the corrected build. GCC emitted an unrelated warning in
  unchanged upstream `theme/fixed_palette.cpp`; compilation completed.
  PASS user-reported real-session icon focus after activation ("Passed");
  the exact application/monitor/title combinations were not independently recorded.
- **Activation:** the existing notification-continuity activator backed up the
  previous binary/drop-in and restarted the shell with its temporary
  application-preserving KillMode. This also deploys the previously accepted
  cumulative RICY-001 source revision. PASS running-executable/build byte
  equality, previous-binary backup equality, original cache/diff/binary
  preservation, active shell/search/Plasmashell units, new-shell ownership of
  the KWin tracking adapter, and valid live status IPC. Thirty-eight captured
  child PIDs remained alive; one transient PID ended between snapshots, so
  the initial blanket child-PID assertion was too broad. No real window was
  closed/minimized for validation.
- **NOT RUN:** agent-operated physical clicks/visual captures, all
  scales/orientations, persistent shell failure, login and a live
  Plasma/Dolphin Recovery round trip. Process/IPC readiness does not certify
  those interactions or independent Recovery.
- **NOT APPLICABLE:** KWin/effect installation, session migration, token
  changes and transport-tree synchronization.
- **Recovery:** restore using `notification-continuity/enable.py --restaurar`
  with the private backup printed by the activator. The original cache,
  upstream `/usr/bin/noctalia`, private settings, Plasma/Dolphin tools and
  existing return paths are preserved. Historical transport/manifests remain
  unchanged. Private profiles, binaries and backups are excluded from this commit.

## 2026-10-11 — Dolphin selected; own Ricy Files retired

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** execute the user's explicitly approved direction: Dolphin is the
  Ricy file manager; retire the own application and record its current baseline
  without visual or runtime work. User assesses Dolphin visual progress at 90%.
- **Changes:** Accepted [ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md), updated
  RICY-005/architecture/components/recovery/design/development rules. ADRs 0003,
  0008 and 0009 are Superseded; unaccepted 0007/0010 are Rejected. Removed 24 tracked
  prototype files (C++, QML, CMake, packaging, tests and exclusive runner) from
  the active checkout. No own build directory existed there. Retired 07–10 gates;
  specifications/evaluation/prototype README preserved as [history](history/ricy-files/README.md).
  The code was not in main, was not merged into it, and remains in Git history.
  Unmerged browser/UI worktrees were left intact as historical work.
- **Baseline:** [DOLPHIN-BASELINE](DOLPHIN-BASELINE.md) distinguishes installed
  registration/configuration, inferred behavior and unproved runtime behavior;
  records hashes, colors/geometry/materials/controls, token hardcodes and gaps
  only as backlog. No automatic next stage. Earlier uncommitted Dolphin work
  remains intact; no applicator ran in this task.
- **Validation performed:** PASS architecture (57 mandatory files, 420 links),
  foundation regression suite (39 checks, including rejection of the retired
  application reservation), token/provenance checks, offline Recovery panel
  merge and 28 window-effect scenarios, historical moved-document links,
  installed Dolphin before/after hashes and diff whitespace.
  Canonical JSON/validators/renderers/identity board remain byte-identical in
  this task; only token README consumer-direction documentation changed.
- **FAIL:** none in the executed checks.
- **UNKNOWN:** independent live Recovery when visual helpers/themes fail,
  process-loaded helper/source reproducibility and full functional/visual coverage.
- **NOT RUN:** live UI/cold launch/FileManager1/device/Trash/portal operations,
  failure switching/login, all scales/RTL. No Dolphin process/FileManager1 owner
  was present at the read-only snapshot; no application was launched to fill gaps.
- **NOT APPLICABLE:** own backend implementation/build tests after retirement;
  external-link/latest-upstream verification for the local installed baseline.
- **Recovery:** installed wrapper/desktop/default/service/theme/QSS/helper and
  dolphinrc unchanged by this task; no KWin/Plasma/Noctalia action. Historical
  transport/manifests and private rollback state preserved. This source/document
  change is reviewable in Git without rewriting any history.

## 2026-10-11 — Dolphin menus follow configured KDE proportions

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** match the user's configured KDE menu density and spacing.
- **Changes:** panel padding 12, item vertical padding4/margin1 and horizontal
  padding 12; native icon inset retained; transparent4px separator gaps.
- **Validation performed:** PASS Qt menu capture/fixture, architecture/token
  validation and diff whitespace. NOT RUN all live submenus, RTL or scales.
- **Recovery:** QSS applied to existing windows with private whole-file backup;
  no helper, session or compositor change in this revision.

## 2026-10-11 — Dolphin popup corner transparency and icon spacing

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** remove native popup backing from rounded corner cutouts and
  give context-menu icons more left breathing room.
- **Changes:** radius 12 native menu surface mask, transparent Window palette
  and no background autofill; icons and text shift inward8px together.
- **Validation performed:** PASS helper build/atomic application, Qt menu
  fixture (transparent corners/mask, icon capture, keyboard/native actions),
  architecture/token checks and diff whitespace. NOT RUN all live submenus,
  RTL or display scales.
- **Recovery:** existing private backup/whole-file rollback; new process
  required for helper changes. No shell/compositor or historical kit changes.

## 2026-10-11 — Dolphin menus, scrolling and panel containment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** match context menus, scrollbars, selection and draggable panel
  divisions to the existing identity; fix clipping and stale Meta+E launches.
- **Changes:** rounded opaque popup with native actions, compact rounded
  scrollbar track/thumb, rounded translucent drag selection; card backing
  around the full view container with real layout insets and contained scrolls.
  Internal gaps reduced while preserving outer 8px margins. Native divider
  paints track color normally, thumb color on hover and accent during drag.
  GUI launches use a new process; existing KDE shortcut cache refreshed.
- **Validation performed:** live menu/split captures; native Qt fixtures for
  menu actions, scrollbar keyboard input, selection and splitter interactions.
  User confirmed Meta+E, scrolls, reduced gap and neutral divider. PASS
  architecture/token validation and diff whitespace. NOT RUN all scales, RTL,
  floating docks, every popup/dialog or live Recovery.
- **Recovery:** existing atomic installer and private whole-file backups;
  no session/compositor changes. Qt helper changes require a new process.

## 2026-10-11 — Dolphin breadcrumb and path input alignment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** align native breadcrumbs and give the editable path the
  Noctalia search-input treatment with padded internal content.
- **Changes:** transparent breadcrumb container, centered28px native segments;
  36px surface path field, accent2px border, radius 8, internal horizontal
  padding and a clear action independent of toolbar sizing/padding.
- **Validation performed:** PASS helper build/atomic application, live Dolphin
  captures including centered native clear button,10 native KIO mode switches,
  architecture verification, token validation and diff whitespace.
  NOT RUN all widths, RTL, scales or live recovery.
- **Recovery:** existing private backups/whole-file rollback; historical
  transport snapshots, compositor and Noctalia remain unchanged.

## 2026-10-11 — Dolphin rounded rows and navigation header

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's request for less pill-shaped file rows
  and better header padding, breadcrumbs and editable location-bar styling.
- **Changes:** radius 6 across row backing/focus/clipping; padded toolbar
  and outlined neutral location bar. Both KIO height limits remain36px
  across mode changes, fixing lower-edge clipping. Canonical adaptations
  and provenance validation updated; Places/tabs/nesting behavior retained.
- **Validation performed:** PASS helper build, live breadcrumb hover/path
  captures, and native KIO fixture (10 mode toggles, URL/editor retained).
  PASS `./scripts/verify architecture`, `python3 themes/tokens/validate.py`
  and `git diff --check`.
  NOT RUN all widths, nested levels, RTL, monitors/scales or live recovery.
- **Recovery:** existing atomic applicator/whole-file backups retained;
  no KWin, shell, default or transport-kit change.

## 2026-10-11 — Dolphin Places match Noctalia search results

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's search-result reference and subsequent
  smaller-icon request, preserving Dolphin navigation and the unified L.
- **Changes:** transparent/borderless normal rows, accent/on-accent selection
  without focus, semibold labels, 16px icons and native6px label gap. The
  native default delegate stays installed/alive; a column paint adapter
  forwards native behavior. Canonical tokens and provenance validation
  reflect this approved adaptation; transport copies/manifests stay intact.
- **Validation performed:** PASS Qt helper build and native KIO fixture
  (default delegate identity, unfocused dark selection,21 navigations); live
  Dolphin normal-row capture and final user visual approval. PASS
  `./scripts/verify architecture`, `python3 themes/tokens/validate.py` and
  `git diff --check`.
  NOT RUN all devices, drag/drop, scales/monitors or session recovery.
- **Recovery:** existing atomic applicator and private file backups retained;
  no shell/KWin/default migration.

## 2026-10-11 — Accepted bounded native Trash and completed milestone 08

- **Model/Agent:** Codex (GPT-6), coordinator.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** record the user's explicit option A approval for ADR-0009 and
  finish the reviewed MVP specification before executable development.
- **Changes:** ADR-0009 is Accepted with approval evidence and strict send-to-trash
  scope; KIO retains the other selected responsibilities. Milestone 08 is COMPLETE,
  with reconciled architecture/UX/filesystem/testing requirements and sequential
  AC09/AC10 gates. Updated maintained references; ADR-0007 remains Proposed.
- **Validation performed:** PASS `./scripts/verify architecture` (zero failures/
  skips) and `git diff --check`; prior milestone 08 review findings remain resolved.
  NOT RUN application build/runtime/operations or live recovery at this checkpoint.
- **Preservation:** no default/FileManager1/Dolphin/Plasma/session change or native
  backend implementation in this checkpoint. Accepted Trash is not a framework,
  purge, overwrite, deletion/restore API or authority to replace other KIO roles.

## 2026-10-11 — Accepted Files architecture and reviewed milestone 08 draft

- **Model/Agent:** Codex (GPT-6), coordinator with separate architecture, UX,
  filesystem and testing review subagents.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** record the user's explicit option A approval for ADR-0008 and
  specify the MVP with conflict, partial-result, cancellation, applicable rollback,
  destructive protection, symlink, mount, permission and KIO-failure contracts.
- **Changes:** marked ADR-0008 Accepted with approval evidence; kept ADR-0007
  Proposed. Added [FILES-MVP](history/ricy-files/FILES-MVP.md), MVP/LATER/OUT OF SCOPE, private module
  boundaries, navigation/selection/UX/token/launch contracts, bounded operation
  semantics and AC09/AC10 acceptance criteria. Updated foundation-era Files
  restrictions only for the approved isolated scope and synchronized maintained
  architecture/component/design/development/recovery/migration references.
- **Safety findings:** KIO 6.30 rename uses check-then-rename; require private
  Linux no-replace policy for rename/same-mount move. Generic recursive KIO
  traversal has no mount-confinement hook; recursive copy/cross-mount move are
  LATER. KIO trash can purge old entries via configured policies. Qt 6.12 trash
  avoids that policy but has a replace-capable orphan-payload commit. Added
  Proposed ADR-0009 for a bounded native standard-trash adapter with exclusive
  metadata/no-replace payload commit, reconciliation and no-purge/no-delete
  fallback. This is extra backend ownership, awaiting explicit approval.
- **Review reconciliation:** PASS scoped written architecture, UX, filesystem and
  testing reviews after clarifying candidate/committed navigation, rename-ID
  remapping, protected operands, unsupported name encoding, byte metadata,
  ambiguous commit cleanup, fixture Home/mount/trash containment, positive volume
  cases, deterministic collision races and mixed skip/cancel result oracles.
  Review PASS is not implementation acceptance.
- **Validation performed:** PASS `./scripts/verify architecture` (zero
  failures/skips), scoped current-document links, `python3 themes/tokens/validate.py`
  and `git diff --check`. PASS before/after SHA-256/mode preservation of the
  1,113-file baseline, except intended documentation/local-rule edits; only two
  new milestone 08 documents were added. ADR-0007 bytes remain unchanged.
- **Limits/checkpoint:** 07 COMPLETE and Accepted; 08 written contract reviewed,
  final exit pending ADR-0009; 09–10 NOT STARTED. Builds/runtime/real KIO primitives,
  trash/volumes/Wayland and login/failure recovery are NOT RUN; new app
  Component/Visual execution is NOT APPLICABLE to this document-only task. Live
  recovery remains UNKNOWN. No application, native backend, package installation,
  service/default/FileManager1/Dolphin/Plasma change or private-state mutation
  occurred. Rollback of this work removes specification/proposal/reference/rule
  edits; preserve recorded ADR-0008 acceptance unless the user revokes it.

## 2026-10-11 — Ricy Files milestone 07 technical proposal

- **Model/Agent:** Codex (GPT-6), coordinator with three independent research/review
  subagents for toolkit/models, filesystem safety and desktop/design integration.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** investigate the requested initial Files roadmap and prepare the
  technical decision required before milestone 08, preserving sequential gates.
- **Changes:** added [FILES-TECHNICAL-ARCHITECTURE](history/ricy-files/FILES-TECHNICAL-ARCHITECTURE.md)
  and Proposed ADR-0008; linked them from the Files reservation, architecture,
  components and ADR index. Compared Qt Quick/C++ with selected KIO/Solid, pure Qt,
  Widgets/KIO and PySide/QML. Recommended a standalone Qt Quick/C++17 application,
  local model/job/token/device/launch adapters, own QML conflict presentation,
  bounded local/trash capability, opaque initial surface and distinct identity.
  No architecture was accepted, contract frozen or application implemented.
- **Findings:** KIOCore/KIOGui reuse does not provide stock conflict dialogs or
  eliminate worker/helper dependencies. Explicit association resolution is needed
  to avoid OpenUrlJob's missing-handler fallback. Cancellation does not imply
  rollback. KIO package closure is broader than selected link targets. Qt/KF6
  are present, but CMake/ECM are absent; package presence is not build readiness.
  ADR-0007, session/default isolation and C-002/C-003 remain pending/unresolved.
- **Validation performed:** PASS independent architectural/toolkit/testing,
  filesystem/safety and desktop/recovery/design proposal reviews; nonblocking
  executable-contract details remain milestone 08 work. PASS
  `./scripts/verify architecture` (zero failures/skips), targeted proposal/ADR/Files
  README relative-link checks, `python3 themes/tokens/validate.py` and
  `git diff --check`. PASS before/after tracked-file SHA-256/mode comparison:
  all 1,111 baseline files retain bytes/modes except the five intended navigation
  and changelog documentation edits; new files are the two proposal documents.
- **Limits and checkpoint:** runtime listing, launch, file operations, media/trash,
  Wayland visuals, login/switching and recovery trials are NOT RUN. New application
  Component/Visual builds are NOT APPLICABLE to this documentation-only stage.
  Recovery runtime functionality remains UNKNOWN; preservation is limited to
  unchanged sources and absence of task-induced runtime/settings mutations.
  No installation, service/default change, token change, private-kit copying or
  publication occurred. ADR-0008 awaits explicit approval; milestones 08–10 are
  NOT STARTED. Rollback removes proposal/navigation/changelog edits only.

## 2026-10-11 — Future Files integration assessment and proposed boundary

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prepare the future Ricy Files integration architecture without
  implementing the application or changing defaults, MIME associations or Dolphin.
- **Changes:** added FILES-INTEGRATION with source/installed-registration evidence
  for directory opens, launcher, FileManager1, MIME/defaults, desktop entries,
  removable/remote devices, trash, package handlers, themes, external actions and
  Plasma Recovery. Added ADR-0007 as Proposed with alternatives, recommended
  session-scoped selection, required Files contracts, Dolphin/KDE-exclusive
  adapters, external package ownership, migration gates and recovery implications.
  Linked the proposal from architecture, components, recovery and the ADR index.
  Accepted ADR-0003 and current ownership/defaults remain unchanged; no session,
  bus topology, toolkit, backend or new daemon implementation is selected.
- **Validation performed:** PASS `./scripts/verify architecture` (56 mandatory
  files, three script syntax checks, 384 local links, zero failures/skips); PASS
  `git diff --check`; PASS content fingerprint equality for 1,073 inspected
  runtime/source files, including installed directory/package associations,
  Dolphin desktop/D-Bus/systemd overrides, wrapper, dolphinrc and Kvantum
  assignment. Read-only MIME queries and source/registration inventory performed;
  primary FileManager1, MIME, Desktop Entry, Trash, portal and KDE service-menu
  documentation reviewed. No private configuration contents exported. Component
  builds/Visual checks are NOT APPLICABLE to this documentation-only change.
- **Limits:** source and registration observations do not prove interactive
  directory/reveal/properties, device/trash/portal behavior or independent
  Recovery. Live trials and default migration are NOT RUN. Approval is pending;
  documentation rollback removes the proposal and its navigation references only.
  Existing uncommitted changes, private backups/state and historical kits remain
  preserved.

## 2026-10-11 — Approved service template extraction (M-02)

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's approval of option A for the next small batch,
  making services the owner of three source unit templates.
- **Changes:** moved the three autostart `.service.in` files into `services/`
  with exact bytes/modes. The existing installer resolves this resource directory
  from its own repository location; only its lookup changes. Added ADR-0006,
  source dependency/copy limits, recovery/rollback documentation and mandatory
  template availability checks with three missing-file harness regressions.
  Runtime scripts/profile/state paths and installed legacy IDs remain anchored.
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (38 behavioral checks). `./scripts/verify all`
  returned exit 2 with zero failures: PASS 65 source syntax candidates, seven
  historical guards, offline panel preservation and 28 window-effect scenarios;
  NOT RUN Noctalia source tests because the preserved cache differs from the
  expected patch. PASS exact source template bytes/modes and before/after
  production read/render equality for six units across ordinary and
  special-character paths, unrelated cwd and symlink aliases; only selected AST
  statements executed in disposable fixtures, never the installation body.
  PASS `git diff --check`, installed unit states/MainPIDs/ExecStart equality,
  and static source/asset/transport/archive/installed-unit fingerprint comparison.
  FAIL broad live-state fingerprint equality: private settings/clipboard files
  changed during observation; the cause is UNKNOWN, contents were not exported
  and no restoration was attempted. That live state is outside the narrower
  passing static comparison. FAIL preexisting blur selector state remains.
- **Limits and rollback:** NOT RUN installation, daemon-reload, service restart,
  login/switching, persistent-failure recovery or interactive/visual trials.
  New daemons, Core abstractions and environment changes are NOT APPLICABLE.
  Copying only the active kit/contribution is no longer sufficient for this
  maintained installer: its checkout must include `services/`. Historical
  transport templates, manifests and archive are preserved without fallback
  links or synchronization. Source rollback restores template placement and
  installer lookup together; retain the completed M-01 keyboard migration.
  No installed-state rollback is needed for the source-only extraction.

## 2026-10-11 — Incremental migration preparation and keyboard source move

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** turn the existing grounding/component map into concrete incremental
  batches across the approved subsystems, with one independently safe source move.
- **Changes:** expanded MIGRATION-PLAN with file-level payload/installer ownership,
  script/unit/desktop/symlink edges, pinned builds, rollback state and transport
  limits. Core has no justified extraction candidate. Moved only keyboard-cedilla's
  README and two opt-in applicators into `integrations/keyboard-cedilla/`;
  script bytes/modes remain identical. Updated maintained references, relocation
  map and a scoped historical reinstallation note. Kept explicit syntax coverage
  and added two harness regressions for moved-source selection/failure propagation.
- **Findings:** session/Recovery wrappers contain absolute contribution paths;
  mixed families have sibling imports/build calls and private backup contracts.
  Installed blur ExecStart still uses `iniciar.py`, whereas the current recipe
  copies `start.py`; existing selector failure was preserved. Current Noctalia
  source/deployed provenance mismatch and Dolphin-helper UNKNOWN remain gates.
  Next template extraction has a concrete resource-lookup proposal awaiting
  approval; no common resolver, shim, new daemon or independent session was added.
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (35 behavioral checks in a disposable
  fixture); `./scripts/verify all` returned exit 2 with zero failures: PASS syntax
  (65 candidates), seven historical guard checks, offline panel preservation and
  28 window-effect scenarios; NOT RUN Noctalia source checks because the preserved
  cache does not match the current patch. PASS moved README/reinstallation-note
  relative links and `git diff --check`. PASS before/after fingerprint comparison:
  1,573 source/asset/private-kit/transport/archive/installed-entry-point/input
  files and symlinks retain bytes/targets/modes, accounting for relocated scripts;
  only the relocated README differs within that 1,574-item baseline. PASS installed
  unit states, MainPIDs and ExecStart equality. FAIL preexisting registered blur
  selector state remains unchanged; no repair was attempted.
- **Limits and rollback:** NOT RUN live typing/browser rendering, switching,
  persistent failure, login/unlock, Dolphin interaction or visual trials. Runtime
  Integration/Environment changes are NOT APPLICABLE to this source-only move.
  Both transport manifests, archive, private profile/state/backups and installed
  preferences remain intact. Revert source placement/references/harness changes
  together; no session or settings rollback is necessary. External ad hoc callers
  outside the examined entry-point scope remain UNKNOWN. Remaining coupled
  extractions, public packaging and architectural decisions are proposals only.

## 2026-10-11 — Consumable Ricy visual tokens

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prepare existing Ricy identity for future owned applications,
  especially Files, without redesign, live appearance changes or bulk migration.
- **Changes:** promoted existing visual values into `themes/tokens/tokens.json`
  with schema1/contract1.0.0, explicit units and scoped adaptations. Shared
  Dolphin colors reference canonical roles; derived shell radii are calculated.
  Added source/hardcode audit, consumption contract, offline renderer/validator
  and ADR-0005. The existing SVG board is the sole migrated consumer; generated
  output is byte-for-byte identical. Updated design, component, architecture,
  migration and Files documentation without choosing a toolkit or implementing
  an application.
- **Findings:** native Style provides the spacing/type/radius/motion cadence;
  existing runtime sources retain hardcodes. Shell fill .70, Dolphin alpha 178/255
  and Konsole .85 remain distinct. Native KWin blur is attributed to grounding
  G-03; old ricyblur records are historical and new-app blur support remains
  UNKNOWN. Root/contribution search-support radii differ and were preserved.
- **Validation performed:** PASS `python3 themes/tokens/validate.py` (contract,
  references/units, retained-snapshot SHA-256, value/adaptation equality,
  source-backed additions, SVG XML and accent propagation); PASS
  `python3 themes/tokens/render-reference.py --check` (exact retained SVG bytes);
  PASS `./scripts/verify architecture`, token-script syntax, targeted documentation
  links and `git diff --check`. NOT RUN live visuals, monitors/scaling, motion,
  session switching, login/unlock or recovery trials. Runtime Integration,
  Recovery and Environment checks are NOT APPLICABLE to this offline-only change.
- **Preservation/rollback:** original token JSON and SVG bytes, transport kit,
  historical manifests, private profiles/state/backups and live consumers remain
  intact. No applicator, installation or service/compositor activation occurred.
  Revert this task's source/template/tooling/documentation edits to roll back;
  recovery has no new token-loader dependency.

## 2026-10-11 — First safe cleanup of historical development paths

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** use the approved grounding to prevent historical variants from
  being mistaken for the current build, while preserving the active desktop and
  Plasma/Dolphin Recovery. No item meets REMOVE; no file was deleted or moved.
- **Changes:** gated seven historical Noctalia builders behind explicit opt-in
  and an absolute isolated source, rejecting repository/cache paths and symlink
  aliases before probing/downloading/building. Normal source selection omits only
  explicit HISTORICAL recipes; mixed-role activation/restore helpers and UNKNOWN
  material stay selected. Guard syntax remains checked. README/agent entry points
  distinguish current source, deployed binary, selected effect and historical
  transport recipes. Added fixture regressions for isolation/source selection;
  fixed fixture link validation with an empty archive placeholder, without
  copying the private ZIP. See the
  [dependency review](CONTRIBUTION-AUDIT.md#first-safe-cleanup) and
  [reproduction workflow](DEVELOPMENT.md#historical-reproduction).
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (33 behavioral checks). `./scripts/verify all`
  returned exit 2: PASS maintained-source syntax (65 candidates), all seven guard
  syntax checks, offline panel capture/merge preservation and 28 window-effect
  scenarios; NOT RUN Noctalia source tests because the preserved cache differs
  from the current patch. PASS `git diff --check` and before/after SHA-256/symlink
  comparison: none of the 1,606 baseline files disappeared; only the intended
  development scripts/docs changed. Installed units/wrappers, binary/cache,
  snapshots, both manifests, patches, assets, archive and private kit material
  retain their bytes. User-unit states, PIDs and ExecStart values remain identical.
  Doctor returned exit 2 with its two expected UNKNOWN categories. FAIL preexisting
  blur-selector service state remains unchanged; no repair was attempted.
- **Limits:** NOT RUN live switching, persistent-failure recovery, login/unlock,
  interactive Dolphin and visual trials; no session/service was restarted.
  Builds/downloads and historical activation were NOT RUN; guard tests used a
  sentinel build body in a disposable fixture. New architecture, migration and
  visual design are NOT APPLICABLE. Unchanged bytes/state and offline tests do
  not certify interactive recovery. No extra historical copy or regenerated
  SHA256SUMS was created; Git retains the pre-cleanup recipes at `1fb1918`.

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
