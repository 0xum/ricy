> HISTORICAL — Closed on 2026-10-11 by [ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md). This preserves the explored proposal/prototype, not an active roadmap, implementation contract, or command to execute. Dolphin is the current Ricy file manager.

# Ricy file manager: Build vs Adapt

Status: evaluation complete; **ARCHITECTURE DECISION REQUIRED**. Date:
2026-10-11 (America/Sao_Paulo). Recommendation: **C, a bounded Dolphin-derived
Ricy Files application**, subject to the gates below. This is a proposal, not
authorization to implement it. [ADR-0010](../../adr/0010-ricy-file-manager-build-vs-adapt.md)
records the decision awaiting approval.

## Scope and evidence

The user suspended milestones 09 and 10 and designated the existing application
a prototype/benchmark. This task changes documentation only: no new operations,
Trash implementation, defaults, FileManager1, Dolphin or session integration,
package installation, production fork, or disposable implementation spike.
The prototype remains on `codex/ricy-files-mvp` at
`0fe09c224c62a076c533ad7df464c80a04e64aef` (`0fe09c2`). The evaluation branch is
`codex/files-build-vs-adapt`, starting from that exact commit. Uncommitted fixes
in the separate browser worktree are preserved and excluded from the benchmark.

KNOWN means inspected source or recorded scoped evidence; INFERRED means an
assessment of likely cost or suitability; PROPOSED means an unapproved choice;
UNKNOWN means not established. Existing features in upstream source are not
runtime certification for a Ricy adaptation. No option was performance-benchmarked
against the others. Independent reviews covered Dolphin, PCManFM-Qt/libfm-qt,
the exact prototype, and the proposed maintenance/safety boundaries.

| Evidence baseline | Inspected version / identity | Limit |
|---|---|---|
| Ricy benchmark | Exact `0fe09c2`; [source](PROTOTYPE-README.md) | Partial milestone 09; neither 09 nor 10 is accepted as complete |
| Dolphin | `v26.08.2`, commit `f19f070e7dc140213a2c6dd5d11f26122c89e1a0` | Source inspection; no fork executed |
| KDE backends | KIO/Solid/KService `6.30.0` | Behavior differs across workers; no personal Trash inspected |
| PCManFM-Qt | `2.4.1`, commit `56312ce4a0c728155a9127372bc7b84651caad08` | Source inspection; not installed for this task |
| libfm-qt | `2.4.0`, commit `4294f29ed314388f1f6d051ae0128320354e417a` | C++ core plus bundled legacy C/GIO code, not an external libfm dependency |
| GIO local backend | GLib `2.90.1`, commit `e05063ccc6c8f222465a1080927f4c14349f3de6`; GVfs `1.62.0`, commit `046d5423ef100255f554eff84388f8ba765a2182` | Local-file findings do not certify every GVfs backend |
| Host / distribution | Installed Dolphin `26.08.2-1.1`, KIO/Solid `6.30.0-1.1`, Qt `6.12.0`, GLib `2.90.1` | Read-only package queries; Arch revisions differ from CachyOS |

Primary source baselines: [Dolphin](https://github.com/KDE/dolphin/tree/f19f070e7dc140213a2c6dd5d11f26122c89e1a0),
[PCManFM-Qt](https://github.com/lxqt/pcmanfm-qt/tree/56312ce4a0c728155a9127372bc7b84651caad08),
[libfm-qt](https://github.com/lxqt/libfm-qt/tree/4294f29ed314388f1f6d051ae0128320354e417a),
[GLib](https://github.com/GNOME/glib/tree/e05063ccc6c8f222465a1080927f4c14349f3de6).

## What the prototype actually establishes

KNOWN at the exact commit: a Qt Quick Controls Basic/C++17 browser with local
directory listing, staged navigation/history, selection, keyboard interaction,
Grid/List, editable location, static user-directory Places, associated-document
opening, app-local identity, and canonical token consumption. Its directory
contains 2,075 physical lines: 717 C++ runtime lines, 649 QML lines, 625 test/runner
lines, and 84 build/documentation/packaging lines. Line counts describe this
snapshot, not quality, completion, or estimated future effort.

KNOWN absent: operation engine, conflict UI, per-item outcome ledger, native
Trash adapter, Trash view, removable-device model, remote browsing policy,
thumbnails, drag and drop, FileManager1 service, or session/default integration.
Solid is linked but not used by an implemented device model. Directory-byte
auditing and launch preflight already introduce local filesystem policy beyond
simply forwarding public KIO APIs.

The source supplies the visual benchmark: dark surface/card separation, mauve
accent and selection, a persistent Places panel, compact navigation/location
bar, Grid/List modes, explicit focus and status/error states. These requirements
can be expressed with Widgets; reproducing every QML control or animation
pixel-for-pixel is not established as a requirement. Central tokens remain the
source of truth, including logical units, typography, scaling and opaque fallback.

Historical isolated UI evidence reports seven passing cases offscreen and on
Wayland at scales 1 and 1.5, with captures for integrated UI commit `29bd90c`.
That is useful visual evidence, not a new run or full acceptance of `0fe09c2`.
The committed backend still has recorded rapid rename/delete and changed-handler
failures. Subsequent fixes exist only in the excluded uncommitted worktree.
Some tests also accept weaker selection outcomes or increment a counter inside
a retry expression; their existence does not prove the required contract.
Large-directory performance, complete accessibility and real recovery are UNKNOWN.

Documentation discrepancy: earlier maintained pages described the milestone 08
checkpoint as documentation only even after executable code was added. Current
status is corrected explicitly to prototype; historical ADR context and prior
validation entries remain preserved.

## Comparative matrix

A = current custom Qt Quick/C++ + KIO/Solid application. B = upstream Dolphin
with supported Ricy appearance/configuration. C = a separately identified thin
Dolphin fork retaining its views/models/backend machinery. D = PCManFM-Qt and,
where necessary, libfm-qt adaptation/fork. Capability rows describe inspected
upstream features; freedom/cost rows are INFERRED. Safety qualifications apply
even when a capability already exists.

| Criterion | A — Build | B — Adapt Dolphin upstream | C — Thin Dolphin fork | D — PCManFM-Qt/libfm-qt |
|---|---|---|---|---|
| Visual / UX freedom | Highest; owns QML shell and delegates | Palette, fonts, icons, toolbar/settings; item geometry has limits | High within owned Widgets/painter/layout sites; arbitrary frontend replacement breaks the thin boundary | High with Widgets shell and libfm view patches; QML requires an additional bridge/rewrite |
| Distinct Ricy experience | Direct control, with all interactions to build | Visually recognizable adaptation; structural UX remains Dolphin | Distinct identity/chrome/navigation possible while retaining mature interactions | Distinct identity possible; must adapt app and library behaviors |
| Critical filesystem code owned by Ricy | Native Trash and local safety primitives, orchestration, outcomes, lifecycle | Very little new code; inherited policies cannot be claimed equivalent | Upstream primitives retained; bounded safety exceptions and mutation-entry routing still owned | GIO/libfm operations retained; stricter guarantees require library/backend policy changes |
| Copy / move / rename / conflicts | No implementation; all specified orchestration still to build | Existing KIO jobs and dialogs; broader merge/overwrite/fallback behavior | Retain machinery only inside an explicitly approved capability envelope; audit every action/drop/inline path | Existing GIO transfer jobs and dialogs; filesystem-ID/copy-delete fallback differs from mount-boundary contract |
| Trash | Native nonpurging send adapter accepted, unimplemented | Existing KIO Trash; configured age/size cleanup is a contract conflict | Same inherited conflict; carry bounded ADR-0009 exception forward, disable bypasses | GIO local Trash protects initial metadata reservation but uses replace-capable payload rename; unsupported-trash permanent-delete prompt conflicts with Ricy |
| Partial failure / cancellation / rollback | Explicit requirements exist; executable reconciliation absent | KIO errors/progress/cancel exist; no guarantee of Ricy per-item results or transactional rollback | Preserve useful upstream job feedback; add/test precise result evidence; safe-only rollback, never assume batch atomicity | Generic finished/progress signals do not establish a per-item ledger; inspected error/return paths require correction |
| Destructive protection | Policy specified; entry guards and tests missing | Upstream Delete/Empty Trash/service actions remain available | Must enumerate and constrain shortcuts, menus, drops, clipboard, inline rename, plugins and Trash paths | App and libfm entry points need control; cannot solve with theme or one menu change |
| Symlinks | Listing/open preflight exists; copy/move/Trash literal-link guarantees unimplemented | Worker/job-dependent; link copy and traversal policies need operation-specific tests | Same inherited semantics; retain leaf-link safety gates, reject unsupported recursion | GIO has NOFOLLOW_SYMLINKS; verify actual caller flags and recursive behavior, not just API availability |
| Mounts / permissions | Planned held-parent/mount guards; no implemented mutation proof | Local worker mount/rename behavior and privilege options differ from Ricy policy | Bind mounts/subvolumes, denied/read-only paths and worker fallback remain explicit gates | `id::filesystem` is not mount identity; recursive traversal and copy-delete fallback need stricter gating |
| Removable devices | Solid dependency only; discovery, removal and races absent | Places/Solid integration and setup/teardown already exist | Retain upstream device UI/model; prove removal during jobs and recovery-safe policy | GVolumeMonitor/GIO; GVfs and authentication stack supply relevant mounting features |
| Remote filesystems | KIO architecture supports workers; prototype local only | Broad worker support with kio-extras/protocol packages | Reusable upstream capability; remote mutation is outside the initial local contract | GIO/GVfs support depends on installed backend packages and authentication |
| MIME / opening | KService/ApplicationLauncherJob exists; changed-handler failure unresolved | Existing KDE service/launch integration | Retain upstream launch path; apply Ricy executable/desktop-file restrictions deliberately | GIO application associations/opening; external helper and preference semantics need tests |
| FileManager1 | Not implemented; ADR-0007 Proposed | Dolphin already implements/registers it | Existing implementation must remain disabled for the separate candidate pending a future approved contract | Existing service registration also needs isolation/disablement; no new owner authorized |
| Thumbnails | Absent; PreviewJob/provider/caching/lifecycle work remains | Existing previews and worker/plugin ecosystem | Retain item updater/previews; test changed layout, scaling and untrusted inputs | Existing thumbnail loader and helpers; protocol/cache/format coverage differs |
| Drag and drop | Absent; negotiation/actions/clipboard/selection rules remain | Existing mature handling and KIO drop integration | Retain mechanics but gate mutation destinations/actions; test Wayland cross-app transfers | Existing FolderView/FolderModel drop paths call operations directly; library policy must cover them |
| Wayland / KWin | Scoped previous UI/scaling evidence; full app acceptance incomplete | Qt Widgets Wayland support; current Ricy helper/effect provenance has limits | Standard Qt Wayland window; separate app identity and opaque fallback; no new KWin patch | Qt Widgets Wayland; XCB linkage is not proof of X11-only use; desktop/layer-shell management must stay inactive |
| Ricy tokens | Existing TokenBridge/QML consumption | Generate scoped palette/style/config values; custom paint coverage limited | Local Widgets token adapter plus explicit style-option/painter mapping | Local Widgets adapter and library painting changes where necessary |
| KDE dependence | Qt Quick plus KIO/Solid and transitive framework/worker dependencies | Largest existing KDE feature closure | Similar closure to Dolphin; trim only after measured compatibility review | Less KDE coupling, but Qt, GLib/GIO, GVfs, menu-cache/libexif and LayerShellQt; KDE remains for Recovery |
| Fork size / difficulty | No upstream application fork; owns new application behavior | No app fork for supported theming; private runtime injection creates version-coupled debt | Narrow app patch series initially; private rendering seams are active, safety integration can expand it | Smaller app, but safety often reaches libfm-qt: two maintained source bases and GIO assumptions |
| Upstream update strategy | Track Qt/KF public APIs and worker semantics; app regressions remain Ricy-owned | Distribution updates plus appearance regression checks | Pin stable Gear release; rebase categorized patches and run upstream + Ricy gates; submit generic fixes upstream | Pin compatible pcmanfm/libfm pair and ABI; rebase both, track GLib/GVfs changes separately |
| CachyOS / Arch packaging | New package and full dependency declaration needed | Existing repository Dolphin package; scoped Ricy assets/profile separate | New coinstallable package; preserve stock Dolphin, rename colliding artifacts/config/DBus identity | Existing repository packages; fork needs separate names/ABI handling and GVfs optional-feature declarations |
| Testability | Small modules/test harness; many critical cases still missing | Existing upstream tests; external theme tests less access to structural internals | Existing tests plus patch-local UI/policy/fault tests; job/worker boundaries still need integration fixtures | GIO/jobs can use fixtures; tests and outcome oracles must be added for inspected gaps |
| Agent maintenance | Small local code readable today; lifecycle/FS requirements make agents own broad new behavior | Lowest patch burden using supported knobs; private helper patches are brittle | Clear pinned patch categories and bounded ownership help; requires upstream-aware reviews | Smaller app is approachable, but mixed C/C++/GIO and dual-repo policies increase context |
| Prototype reuse | Highest direct source reuse, with unresolved fixes | Tokens/assets/UX requirements/fixture strategy; little QML code | Tokens/assets/behavior tests/fixture strategy; selected Qt helpers, not QML views/controllers wholesale | Tokens/assets/contracts/fixture strategy; KIO controllers and QML have little direct portability |

## Concrete limits behind the comparison

### Visual freedom is about owned rendering seams

Dolphin's item views are QGraphicsWidget-based custom painting and layout,
not interchangeable QListView delegates. Palette/QStyle changes are useful;
QSS does not expose arbitrary item geometry, hierarchy or all interaction states.
The retained Ricy Dolphin helper already traverses private class names, installs
graphics effects, changes tab hit geometry and inserts an overlay panel. That
shows an existing visual path, but also version coupling; it is not a supported
Dolphin appearance extension API. No helper was enabled or modified here.
Sources: [item view](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/kitemviews/kitemlistview.h),
[file-item painter](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/kitemviews/kfileitemlistwidget.cpp),
[retained helper](../../../ricy-kit/contributions/dolphin-blur-corners/ui.cpp).

C makes the necessary paint/layout ownership explicit. It can change the
application chrome and selected view states without replacing the established
view/controller system. Wholesale QML replacement would recreate selection,
drag/drop, accessibility and preview integration, losing the main benefit of C.
DolphinView is a QWidget coupled to private Dolphin targets, not a stable QML
backend library. [Build targets](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/CMakeLists.txt).

Qt supports [QQuickWidget](https://doc.qt.io/qt-6/qquickwidget.html), but embedding
adds rendering work and disables the threaded render loop. It does not turn
existing Widgets views into QML components. Hybrid rendering is not proposed.

### Mature operations do not imply the strict Ricy safety contract

The [Freedesktop Trash specification](https://specifications.freedesktop.org/trash/latest/)
defines interoperable storage. It does not alone guarantee no purge, atomic
no-replacement, cancellation reconciliation or a two-file transaction.
Those additional requirements remain mandatory under
[ADR-0009](../../adr/0009-ricy-files-nonpurging-trash.md).

KIO 6.30 `adaptTrashSize()` can remove unrelated existing Trash entries using
configured time/size policies. The inspected local rename path checks a target
before a replace-capable rename. GIO's GLib 2.90.1 local Trash reserves metadata
with O_EXCL, subsequently writes by pathname, then commits with `g_rename`;
an existing orphan payload is not protected by atomic no-replace. Its ordinary
rename/move paths also have check-then-rename windows. These are source findings,
not reports of data loss or claims about this user's settings. Sources:
[KIO Trash](https://github.com/KDE/kio/blob/v6.30.0/src/kioworkers/trash/trashimpl.cpp#L1160),
[KIO local worker](https://github.com/KDE/kio/blob/9e623578249516599d6f5373bb7f4daefe2d59ac/src/kioworkers/file/file_unix.cpp#L996),
[GIO local file](https://github.com/GNOME/glib/blob/e05063ccc6c8f222465a1080927f4c14349f3de6/gio/glocalfile.c#L2195).

libfm-qt transfer uses filesystem IDs, allows fallback copying/deleting and does
not establish mount-ID confinement for recursion. Generic completion is not an
explicit result for every selected item; some inspected return/error paths
need stronger accounting. Its failed-trash UI can offer permanent deletion.
Sources: [transfer job](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/core/filetransferjob.cpp),
[operation UI](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/fileoperation.cpp),
[GIO flags](https://docs.gtk.org/gio/flags.FileCopyFlags.html).

Accordingly B cannot deliver the strict operational contract through appearance
alone. C and D must account for backend behavior, including alternate action
entry points. The recommendation retains the already approved bounded native
Trash exception and existing local-operation constraints; it does not authorize
a KIO/GLib fork or a general filesystem framework. If satisfying the contract
requires broader ownership, stop that portion for another architectural decision.

Additional capability evidence: Dolphin's
[FileManager1 registration](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/dbusinterface.cpp#L18),
[Places](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/panels/places/placespanel.cpp#L73),
[PreviewJob integration](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/kitemviews/kfileitemmodelrolesupdater.cpp#L977),
[drop handling](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/views/draganddrophelper.cpp#L37),
and [operation dispatch](https://github.com/KDE/dolphin/blob/f19f070e7dc140213a2c6dd5d11f26122c89e1a0/src/views/dolphinview.cpp#L947).
D's corresponding interfaces include
[FolderView](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/folderview.h),
[launching](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/core/basicfilelauncher.cpp),
[thumbnail jobs](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/core/thumbnailjob.cpp),
[startup/registration](https://github.com/lxqt/pcmanfm-qt/blob/56312ce4a0c728155a9127372bc7b84651caad08/pcmanfm/application.cpp)
and [GVfs architecture](https://github.com/GNOME/gvfs/blob/046d5423ef100255f554eff84388f8ba765a2182/README.md).

### Distribution fit and upstream maintenance

The checked Arch repositories supply
[Dolphin 26.08.2-1](https://archlinux.org/packages/extra/x86_64/dolphin/),
[PCManFM-Qt 2.4.1-1](https://archlinux.org/packages/extra/x86_64/pcmanfm-qt/) and
[libfm-qt 2.4.0-4](https://archlinux.org/packages/extra/x86_64/libfm-qt/).
Dolphin brings KDE framework/worker integrations; PCManFM's relevant remote and
mounting features depend on optional GVfs packages. The smaller PCManFM package
size is not a measurement of the complete desktop dependency closure, memory,
startup latency, or long-term maintenance cost. Recovery retains KDE regardless.

C needs an independently named package that coexists with stock Dolphin,
including binary, desktop/app identity, configuration, data and any colliding
private libraries/services. Public Dolphin plugin compatibility after renaming
is UNKNOWN and must be explicitly tested or excluded. D needs an equivalent
coinstallation strategy; a libfm-qt fork must not replace the system library
implicitly. Preserve upstream licenses and per-file notices; verify the packaged
license manifest rather than assigning one guessed license to a mixed tree.

Observed Dolphin churn in selected item/view/main-window/Places paths was
28 files (+1,109/-356 lines) from v26.04.3 to v26.08.2, and 44 files
(+1,479/-479) from v26.08.2 to the inspected master
`e41ce849bb4b9d66f355cdfb11597aaefaf5271c`. These are selected-path source diffs,
not the total fork size, predicted conflicts, or measured rebase hours. They
show why private-painter patches need continuous upstream tracking.
[Stable source history](https://github.com/KDE/dolphin/compare/v26.04.3...v26.08.2).

## Relative cost and risks

Costs are INFERRED ordinal categories, not staffing estimates. Compare the same
Ricy identity and safety requirements, not a custom production application
against an unchanged upstream demo. None of the four has proven all strict
Ricy operation requirements in this evaluation.

| Cost dimension | A | B | C | D |
|---|---|---|---|---|
| Read-only visual/browser parity | Low incremental cost | Low for conventional styling; structural parity limited | Medium: Widgets adaptation and separate identity | Medium: Widgets adaptation plus new integration stack |
| Broad file-manager feature coverage | High new application work | Low inherited work | Low–medium integration work | Medium integration and feature differences |
| Strict local mutation safety | High | Not achievable by appearance-only scope | High policy/testing work; narrower existing exception ownership | High; library/GIO gaps expand ownership |
| Ongoing application behavior maintenance | High Ricy ownership | Low with supported styling | Medium if patch boundary holds | Medium, potentially high with library patches |
| Upstream update/rebase work | Medium API/behavior tracking | Low; higher with private helpers | Medium; active internal seams | Medium–high if both app/library forked |
| Overall fit for a distinct Ricy manager | Highest freedom, highest new behavior burden | Lowest cost, insufficient structural control | Best balance if bounded patches and safety gates hold | Smaller app, weaker reuse of current KDE ecosystem |

Principal risks and responses:

1. **Silent data loss / ambiguous outcomes:** no option earns a safety pass from
   upstream reputation. Preserve no-purge/no-overwrite, collision-safe names,
   exclusive metadata, literal symlinks, mount/permission controls, explicit
   Total/Partial/Failure outcomes, residual evidence and safe-only rollback.
   Cancellation after a commit must never imply the commit was undone.
2. **Thin fork becoming a frontend or backend rewrite:** keep the retained
   KItemList/model/selection/preview machinery. Track every patch's purpose and
   owner. A proposed replacement view, protocol worker, generalized operation
   layer or cross-mount copy/delete guarantee triggers fresh architecture review.
3. **Mutation bypasses:** shortcut, inline editor, paste, drop, context/service
   menu, plugin, Trash view, Undo/Redo, editable properties and device paths need
   an entry-point inventory. An
   unverified path stays unavailable in the candidate; hiding one toolbar action
   is insufficient. Broader upstream operations remain capabilities, not approved
   Ricy features. No elevated operation/admin integration is inherited silently.
4. **Recovery or public identity collision:** stock Dolphin remains installed,
   configured and launchable through its existing paths. The candidate must not
   queue for global FileManager1 or reuse default/config identities. Independent
   session recovery remains UNKNOWN; ADR-0007 is still Proposed.
5. **Dependency/security updates:** an application fork does not isolate KIO,
   previewers, protocol workers or Qt from security changes. Track distribution
   and upstream fixes; avoid freezing the whole stack to preserve a visual patch.
   Rebase or drop a visual patch when needed to accept a critical upstream fix.
   For D, external thumbnail helpers and QtGuiPrivate usage add process and
   compatibility review surfaces; neither protocol breadth nor helper execution
   is enabled merely by adopting a library.
   [Library configuration](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/CMakeLists.txt),
   [external thumbnailers](https://github.com/lxqt/libfm-qt/blob/4294f29ed314388f1f6d051ae0128320354e417a/src/core/thumbnailer.cpp).
6. **False reuse / sunk cost:** QML UI and tests are not portable to Widgets as
   source. Preserve the benchmark and its evidence, but reuse behavior and tokens
   where upstream already solves the corresponding mechanism better.
7. **Unmeasured runtime and staffing cost:** performance, accessibility completeness,
   real device/remote behavior and actual rebase effort remain UNKNOWN. The first
   approved candidate and first upstream update must measure these before promotion.

## Prototype reuse

| Artifact | A | B / C / D | Treatment |
|---|---|---|---|
| Canonical JSON/schema and token validation cases | Direct | Direct data/contract reuse | Preserve exact values; adapt toolkit mapping, not the design system |
| Packaged Ricy icon / identity intent | Direct | Reusable for a separate C/D app; B keeps upstream identity | Audit artifact/config/service collisions before packaging |
| QML Main/FileDelegate | Direct with fixes | Visual/behavior reference; no drop-in source reuse | Keep as benchmark; avoid hybrid UI merely to preserve code |
| TokenBridge / small Qt helpers | Direct | Conditional extraction/adaptation in C/D | Review units/errors/resource semantics; no shared SDK |
| DirectoryModel/navigation/selection | Direct with corrective work | Mostly replace with upstream equivalents | Reuse acceptance cases, not redundant controllers |
| LaunchService | Existing but flawed | KDE policy/test ideas for B/C; different GIO path in D | Do not transfer the cache bug or assume opening parity |
| Tests / isolated runner / fixture plans | Direct after correcting weak tests | Reuse fixtures, oracles and requirements; rebind UI tests | Previous PASS is not new candidate validation |
| OperationsService / native Trash code | Does not exist | Does not exist | Reuse only the specification, safety research and future acceptance cases |

## Recommendation and decision impact

Recommend **C**: a separately identified Ricy Files derived from Dolphin, with
Qt Widgets presentation changes and retained upstream file views, models,
navigation/selection, previews, KIO/Solid and launch integration. The prototype's
demonstrated visual grammar does not require rebuilding those mechanisms.
It does require more structural control than B offers through supported knobs.

A remains defensible if unrestricted QML interaction design becomes the main
product requirement and Ricy accepts owning the entire application lifecycle.
Current evidence does not establish that need. B is preferable if the user
accepts conventional Dolphin structure and upstream identity; adopting it as
the future primary manager also requires reconsidering RICY-005/ADR-0003.
D reduces KDE coupling in the candidate, but introduces GIO/GVfs and potential
dual-repository safety patches while KDE is still retained for Recovery. A smaller
source base alone does not offset those contract gaps.

This recommendation is conditional on maintaining a bounded application patch
set and proving the operation policy. It is not a claim that C already meets
the strict filesystem contract or a promise of cheap safety integration.
Keep [ADR-0009](../../adr/0009-ricy-files-nonpurging-trash.md) as the accepted, narrowly
bounded native send-to-trash exception. Its adapter and direct-operation routing
still have to be implemented and validated in a future authorized task. Its
historical Qt Quick/module references are mapped explicitly by ADR-0010, without
rewriting the original decision. KIO retains the other selected responsibilities.

On approval, ADR-0010 would supersede ADR-0008's toolkit/application choice;
the old record must remain with a supersession reference. ADR-0009's safety and
bounded mutation decision is carried forward, not discarded. ADR-0003 and
RICY-005 remain compatible with a distinct Dolphin-derived Ricy Files and stock
Dolphin Recovery. No defaults/FileManager1/session contract is accepted by this
choice. Today ADR-0010 is Proposed; ADR-0008/0009 remain historical Accepted
records with implementation suspended by the user's current instruction.

Private Qt Quick module/context-object/delegate contracts in FILES-MVP would be
replaced by the retained Widgets/Dolphin structures after approval. The UX
requirements (navigation commitment, selection, focus, location editing, error
states and opening restrictions), tokens and safety/outcome requirements survive
as acceptance criteria. Dolphin's unmodified model/history behavior is not
assumed equivalent: document each mapping and incompatibility before candidate
acceptance. Changes to behavioral requirements need explicit review; toolkit
supersession alone does not waive them.

## Proposed migration after explicit approval

1. **Record the decision and preserve the benchmark.** Accept ADR-0010 and add
   a supersession reference/status to ADR-0008, preserving its full history.
   Carry ADR-0009 forward with explicit module mapping. Keep the original branch
   and exact commit; preserve excluded uncommitted fixes separately. Agree the
   candidate task scope before restarting milestones under a revised plan.
2. **Create a separate candidate and upstream patch inventory.** Pin a stable
   Dolphin release/commit, retain licenses, and categorize patches as identity,
   token/presentation or approved policy. Retain KItemList/controller machinery.
   No Qt Quick frontend replacement, KIO worker fork or general filesystem SDK.
3. **Prove isolation before running the candidate.** Use disposable profiles;
   separate binary/desktop/app/config/data identities and colliding private
   artifacts. Disable inherited FileManager1 registration and desktop/default
   setting routes. Do not modify current wrappers, Dolphin settings or session.
4. **Reach browser/visual parity.** Map tokens to Widgets/style options; implement
   the approved chrome/layout differences; compare selection/focus/error/location
   behavior with the benchmark on Wayland at scales 1 and 1.5. Preserve upstream
   accessibility/navigation behavior and opaque fallback. Measure startup,
   memory and large-directory behavior using the same fixtures.
5. **Inventory and prove every operation entry point before enabling it.** Keep
   the accepted local-operation envelope; use KIO only where its behavior fits.
   Carry the bounded native Freedesktop send-to-trash exception and no-replace
   local policies forward. No purge, overwrite fallback, automatic permanent
   delete, recursive mount crossing or broad cross-mount move is inherited.
   If safe routing needs a wider framework/backend fork, stop for a new decision.
6. **Run the required safety and integration gates.** Deterministic metadata and
   payload collisions (including late races), orphan metadata/payload, short
   writes/flush failures, permission/readonly errors, literal and broken links,
   bind mounts and positive supported-volume cases, device loss, partial batches,
   cancellation around commit, and safe/unsafe rollback cases. Every item must
   have an evidenced outcome; no residual or data loss may be hidden. Run retained
   upstream tests and Ricy regressions; worker errors must reach the user.
7. **Prove maintenance and package coexistence.** Rebase the bounded patch series
   onto the next stable upstream update; record conflicts and effort. Build a
   separate Arch/CachyOS package in a clean environment, verify dependencies,
   optional workers/previewers, licenses and artifact collisions. Rollback removes
   only the candidate package/profile and preserves user files and stock Dolphin.
8. **Stop before session/default promotion.** Promotion needs a separately
   accepted session/default/FileManager1 contract and real Recovery validation.
   ADR-0007 remains Proposed. A working candidate alone cannot authorize that
   migration or claim independent Plasma Recovery.

Acceptance of direction must not turn UNKNOWN safety, coinstallation or recovery
into PASS. If C cannot preserve its patch boundary while meeting the mandatory
contract, return to this decision with measured evidence; do not silently grow
the fork or fall back to weaker guarantees.

## Validation for this evaluation

PASS: read-only exact-commit/upstream source inspection and independent review;
documentation/link and preservation results are recorded in [CHANGELOG](../../CHANGELOG.md).
NOT RUN: new application builds, runtime benchmarks, operation/device/remote
tests, candidate packaging, upstream-rebase trial and live Recovery; no production
candidate was implemented. NOT APPLICABLE: activation/deployment validation for
this documentation-only task. Historical prototype runs remain attributed above.
