> HISTORICAL — Closed on 2026-10-11 by [ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md). This preserves the explored proposal/prototype, not an active roadmap, implementation contract, or command to execute. Dolphin is the current Ricy file manager.

# Ricy Files MVP specification — milestone 08

Status: **Milestone 08 COMPLETE: requirements independently reviewed and
ADR-0009 option A explicitly Accepted on 2026-10-11.**
Architecture: [ADR-0008](../../adr/0008-ricy-files-technical-architecture.md), Accepted
by explicit user approval on 2026-10-11 (America/Sao_Paulo). This document defines
testable implementation requirements, not evidence of implemented functionality.
No application is implemented in milestone 08.

The user explicitly requires conflicts, partial results, cancellation, applicable
rollback, destructive protection, symlinks, mount boundaries, permissions and
KIO failures. The contracts below make those requirements concrete. The bounded trash
exception is separately approved by ADR-0009; it does not expand KIO replacement
or authorize a new filesystem framework.
[ADR-0007](../../adr/0007-session-file-manager-boundary.md) remains Proposed and is not
normative authority for this MVP. Its possible future defaults/activation/restore
requirements are tracked separately in [FILES-INTEGRATION](FILES-INTEGRATION.md).

## Scope and delivery slices

| Category | Features |
|---|---|
| MVP — milestone 09 | Standalone launch to Home; Home/Documents/Downloads/Pictures/Videos Places; local directory listing; Back/Forward/Up/Refresh and editable location; Grid/List; selection and basic keyboard navigation; ordinary files opened with their selected handler; loading/empty/error states; exact central tokens |
| MVP — milestone 10 | Mounted local drives and removal handling; read-only Trash listing; create directory; single-item rename; regular-file and symlink copy; same-mount file/symlink/directory move; confirmed Move to Trash after its backend gate; operation progress/decisions/cancellation/partial outcomes |
| LATER | Recursive directory copy; cross-mount move; overwriting/merging; persistent bookmarks/tabs/search; thumbnails; Open With picker; trash restore UI; mount/unmount/eject/power-off UI; drag/drop and clipboard transfer; configurable hidden-file display |
| OUT OF SCOPE for 08–10 | Permanent delete/Empty Trash; privileged/admin operations; remote protocol URLs; package conversion/installation; Dolphin service menus/plugins; global FileManager1 ownership/activation; MIME/directory defaults; session isolation; new Ricy daemon/IPC/shared SDK; global token/theme/compositor changes |

Copy is deliberately bounded to leaf regular files and links; directory copy is
visibly unsupported rather than recursively crossing unknown mounts. Move of
directories is a nonrecursive atomic rename within one mount. Trash accepts
directories only when the approved backend can move the directory entry without
recursively copying/deleting or traversing child mounts. Features marked LATER
are not part of the acceptance claim. The overall roadmap remains 07 → 08 → 09
→ 10; no milestone may pass using a required feature's UNKNOWN result.

## App identity, launch and isolation

Executable `ricy-files`; display name `Ricy Files`; desktop/app/icon identity
`io.github.0xum.RicyFiles`. Use QGuiApplication and Qt Quick Controls Basic; no
stock KIOWidgets dialogs. Zero arguments opens QStandardPaths HomeLocation.
One optional positional argument is an absolute local directory path, a local
`file:` directory URL or `trash:/`. More arguments and invalid targets produce
a clear usage/error result. Support `--help` and `--version`; CLI parsing treats
`--` as end of options. Do not interpret paths as commands, expand shell syntax,
or make Files a generic file-opening handler.

No single-instance bus service is required. Multiple independent process windows
may run; each owns its own navigation/jobs. No desktop registration is installed
on startup, no D-Bus activation entry is shipped and `DBusActivatable` is absent
or false. Packaging may stage a normal desktop entry/icon and exact token resource
for verification without installing defaults or copying private kit state.

## Modules and frozen data boundaries

All modules are private to `apps/file-manager/`; no Core/Services API is created.
The contracts specify observable properties/commands, not a desktop-wide ABI.
C++ owns policy and I/O; QML invokes commands and renders immutable snapshots.
Implementation may split files while preserving these responsibilities.

| Module | Public-to-UI contract and ownership |
|---|---|
| NavigationController | `navigate(url)`, `back()`, `forward()`, `up()`, `refresh()`; committed/pending URL, generation, `canBack/canForward`, state/error; only successful listing commits history |
| DirectoryModel | Flat QAbstractListModel; cached item roles below; KCoreDirLister lifetime, watcher updates and listing generation; no mutation or application-launch methods |
| SelectionController | selected/current/anchor item IDs; replace/toggle/range/all/clear; IDs survive sort/view switches and are removed when entries disappear |
| PlacesModel | configured user locations, mounted Solid storage and Trash; role `placeId/label/url/available/reason`; no mount or default-policy action |
| LaunchService | `openFile(url)`; validates ordinary file, resolves current MIME/preferred service, emits one `DispatchRequested` or `DispatchFailed`; no association writes |
| OperationsService | `submit(request) -> jobId`, `cancel(jobId)`, `answerDecision(decisionId, choice, newName)`; root-owned queue, policy/guards/KIO jobs, JobModel/result records |
| TokenBridge | immutable schema/contract/version and shared role properties from the exact resource; startup validation; no environment/theme writer |

Item IDs are encoded QUrls, not display names or row numbers. An ItemSnapshot
contains `itemId`, `url`, `displayName`, `kind` (directory/regular/link/other),
`isDirectory`, `isSymlink`, `linkTarget` when known, size and modified-time values
with availability flags, `mimeName`, `iconName`, and availability/error flags.
Keep filesystem names verbatim; display them as plain text. Require a lossless
native-byte → QString/QUrl → native-byte round trip for supported names/link text;
otherwise show an unsupported-encoding indicator and refuse launch/mutation.
Do not operate on a replacement-character spelling. Unsupported special
files remain visible but not eligible for copy, move, launch or trash.
Broken links are distinguishable and remain links. UI selection roles are derived
from SelectionController, not stored in filesystem entries. Watcher rename
updates explicitly remap old URL → new URL in selected/current/anchor IDs;
stability across sorting/view changes applies to entries whose URLs are unchanged.

An OperationRequest has `kind` (CreateDirectory/Rename/Copy/Move/Trash), captured
source URLs, destination directory/new single-component name where applicable,
and a user-confirmation token for Trash. Requests are immutable after submission.
Opaque string job/decision IDs cross into QML; raw QObject/job pointers do not.
The service snapshots errors/results before KIO auto-deletion. Application-root
ownership survives changing location, view and delegate destruction.

## Navigation, directory model and filesystem view

Accept only absolute local paths or `file:` with empty/localhost authority, no
credentials, port, query or fragment; convert paths with QUrl APIs and do not
decode URL escapes twice. Reject remote authorities and unsupported schemes.
`trash:/` is the one special read-only location, not an OS path. A local path on
a mounted network filesystem is allowed for browsing; it is potentially slow
and does not imply network-protocol or write support.

Keep logical locations for history and symlink-directory navigation. Resolve
actual metadata separately for operation checks. Configure/connect a fresh
KCoreDirLister before `openUrl()` for each navigation generation: cached results
can be immediate. Stage candidate entries/state separately from the committed
model/listing. Stop/disconnect only superseded candidates; retain the committed
snapshot/lister until candidate success, then atomically replace and retire it.
Failed candidates leave committed state usable with a separate target error.
Callbacks never merge candidate entries into the committed model. Reject stale
callbacks. Do not double-insert by consuming
both equivalent addition signals. Handle clear/add/delete/refresh/redirection,
completion/cancellation and jobError; redirection is revalidated before use.

Model signals/notifications run on the GUI thread. `data()` performs no blocking
filesystem or MIME work: return cached metadata/generic icons until asynchronous
enrichment is available. Do not call delayed `KFileItem::mimetype()` in delegates.
Directory-only discovery does not recursively inspect user contents.

States: Loading, Ready, Empty, Error and PartialListing. An accepted open request
is not completion. A partial/inaccessible-child result cannot become Ready merely
because a top-level job completed. Only complete successful navigation commits
the location/history cursor. Preserve the last usable location/list when a new
target fails; show the failed target and reason. Supersession cancellation does
not produce a user error. Refresh does not add history; new successful navigation
truncates Forward; same-location requests do not duplicate entries.

Sort directories first, then locale-aware names, with URL tie-breaker; the MVP has
no user-sort persistence. Hide dot entries in ordinary views for this MVP, with
an explicit scope note; hidden-file UI is LATER. Listing invalidation removes
missing selected IDs; it never selects a different item because a row was reused.

## UX contract and design-token consumption

Sidebar labels: Home, Documents, Downloads, Pictures, Videos, backend-labeled
mounted drives, Trash. Resolve configured XDG user paths through QStandardPaths;
labels are en-US, on-disk paths may be localized/custom. Missing locations remain
identifiable with an unavailable reason; clicking gives an error and never creates
a directory automatically. A removed active mount shows a persistent unavailable
state; no silent navigation to Home, mount, force-unmount or eject occurs.

Grid and List share the same model/current/selection. List columns are Name,
Type, Size, Modified; unknown values display an em dash, directory size is not
computed recursively. Single click selects; double click or Enter activates the
current item. Ctrl-click toggles; Shift-click selects a visible range from the
stable anchor. Switching views preserves selected/current IDs and reveals the
current item. New successful navigation clears selection.

| Keyboard/action | Behavior |
|---|---|
| Tab/Shift+Tab | Traverse enabled controls in visual order, with visible native focus |
| Arrows, Home/End | Move current item in view geometry; without modifiers select it; Ctrl changes current only; Shift extends from anchor |
| Ctrl+A / Escape | Select all visible items / clear selection when the view owns focus |
| Enter | Activate current item; do not open every selected file |
| Alt+Left/Right, Alt+Up | Back/Forward/parent; disabled actions do nothing |
| Ctrl+L | Focus/select location text; Enter validates; Escape restores committed location |
| F5 | Refresh committed location |
| F2, Ctrl+Shift+N | Rename one eligible selected item / New Folder in a writable ordinary location |
| Delete | Request confirmed Move to Trash for eligible captured selection; never permanent deletion |
| Shift+Delete | No action; no destructive accelerator is registered |
| Copy To… / Move To… | Explicit destination prompt with source names/count; no clipboard ambiguity |

View shortcuts are inactive while a text input/dialog owns the keystroke.
While navigation is pending or the committed location is unavailable, disable
launch/mutation controls; also disable mutations when capability/eligibility is
unknown. The engine revalidates every request; it never pairs old selection with
a pending destination. Invalid filename/destination input retains focus and entered text. A successful
prompt returns focus to its initiating control/view. Confirmation lists captured
names/count and operation; escaping/dismissing never grants permission.

Trash is a read-only root listing in this MVP: no opening/navigating trashed
content, create, rename, copy, move, trash-again, restore, delete or empty action.
Show original location/deletion time when supplied by the backend; malformed or
missing metadata displays an unavailable marker without reconstructing paths.

Bundle exact [tokens.json](../../../themes/tokens/tokens.json) bytes via Qt resources;
require schema 1, compatible contract major and required roles. Bad tokens produce
a readable startup failure before a usable window; do not silently substitute a
second palette. Map shared surface/card/text/secondary/accent/feedback, native
spacing/padding/radii/type/motion roles. Standard control implicit sizes govern
hit targets; no new hardcoded style tokens. Use the shared base radius without
the shell-specific multiplier, Noto Sans logical-pixel UI roles, toolkit scaling
once, opaque surface/cards/text/icons and standard decoration. Font/icon fallback
uses toolkit defaults with visible diagnostic evidence when unavailable.

Normal/hover/focus/selected/disabled states retain native Quick Controls behavior;
use existing color pairs and visible accent focus. Provide accessible names for
controls/delegates and current/selected/loading state announcements; native
controls alone do not name custom file delegates. Initially use no nonessential
custom animations, so reduced-motion behavior needs no new preference service.
No blur/corners, Dolphin QSS/helper, global theme/font writes or workspace UI.
[DESIGN-SYSTEM](../../DESIGN-SYSTEM.md) remains authoritative.

## Associated-file launch contract

Validate a current ordinary file or resolved file-link target asynchronously;
broken links and special files fail visibly. Directory links navigate instead.
Do not directly execute native binaries, scripts or `.desktop` entries, follow
embedded desktop-link URLs, or infer trust from execute bits. In this initial
MVP, executable files and `.desktop` entries are refused with a clear explanation;
a later safe document-opening policy can expand this scope. Opening packages
as documents through their selected external handler is allowed; Files owns no
package installer or authorization behavior.

Resolve MIME/handler on every activation with KApplicationTrader. A null handler
or handler matching Files' own identity is an explicit error. Pass an actual
non-null KService and URL list to ApplicationLauncherJob, connect result before
starting, and propagate a valid current activation token when available. Never
build shell command strings, enable DeleteTemporaryFiles, or fall back to
OpenUrlJob/QDesktopServices/Open With when resolution fails. Report launch failure
with context. A successful dispatch is not proof the recipient read the file;
canceling a launch cannot terminate an application already started.

## Operation engine, progress and errors

One mutating request runs at a time per process; queued requests retain immutable
sources and are revalidated on start. No background daemon, restart persistence,
global lock or cancellation of another process's jobs. Concurrency with external
applications is possible; detected changes cause failure/reconciliation rather
than overwriting. The MVP is not a sandbox against malicious same-user namespace
mutation; preflight is not an atomic source-identity guarantee.

Job states: Queued → Validating → Running or AwaitingDecision → terminal.
CancelRequested is pending, not terminal. Exactly one terminal record is emitted.
Each item has Pending/Committed/Skipped/Failed/Canceled/Residual/Indeterminate
outcome, source/destination, backend error domain/code/text, mutation evidence and
known residual URL. Separate valid warnings from fatal errors. A job is:

- Succeeded only when every requested item is committed (or an explicit identical
  rename no-op) with no failures/skips/unknown result.
- Failed when no item committed, no residual remains and failure is known.
- Canceled when cancellation prevented all changes, no failure/residual remains
  and all noncommitted items are canceled, unstarted or deliberately skipped;
  expose both skip and cancel outcomes in that effect-free batch.
- Partial when any committed effect or residual coexists with a noncommitted item,
  failure, skip or cancellation; known residuals alone also produce Partial.
- Indeterminate when backend loss/reconciliation cannot establish an outcome;
  present "Result could not be confirmed" and never turn it into success.
- Skipped when every item was deliberately skipped without mutation; not success.

Evaluate Indeterminate first, then all-committed Succeeded, effects/residuals
Partial, all-skipped Skipped, effect-free Canceled, otherwise Failed. Known
warnings remain visible on successful data completion; they are not hidden errors.

Cancellation that arrives after complete commit leaves Succeeded, accompanied by
"Finished before cancellation". Job records remain until dismissed or process
exit, with no persistent history of private paths in this MVP.

Show processed bytes/items and totals only when available. Unknown/revised totals
produce indeterminate progress, not fabricated percent/ETA. Transfer progress is
not a per-item commit ledger. Capture committed events and reconcile on terminal
error; do not infer success from a throttle/progress signal or total percentage.
All UI errors identify operation/source/destination where relevant and preserve
native details as plain text. No implicit widget error/authentication dialogs.

## Conflicts and operation-specific semantics

Validate filename components: reject empty, `.`, `..`, NUL and `/`; preserve
spaces, Unicode and leading hyphens. A destination symlink counts as an existing
conflict, including a dangling link. No Overwrite flag, merge, global apply-to-all,
automatic rename or automatic skip is authorized.

For existing-name collisions offer **Choose Another Name**, **Skip** for a
multi-item Copy/Move, and **Cancel Operation**. A new name is revalidated and
attempted without replacement; another collision prompts again. A new name never
means overwrite. A single create/rename collision offers name correction/cancel.
A decision is bound to one live job/item, contains offered choices and one unique
ID, and consumes at most one answer. Stale/duplicate/unoffered answers change
nothing; closing/Escape cancels. Unsupported KIO prompts cancel/fail explicitly.
The QML-facing AskUserActionInterface is attached beneath its KJobUiDelegate;
pause/resume does not substitute for decisions.

| Operation | Required bounded behavior |
|---|---|
| Create directory | One child in validated writable parent; KIO mkdir, umask respected, no overwrite metadata; EEXIST prompts without modifying existing entry |
| Rename | One captured file/link/directory, same parent; atomic destination no-replace; identical name is explicit no-op; no copy/delete fallback |
| Copy | Regular files or literal symlink entries only; KIO leaf copy/link jobs without Overwrite; no recursive CopyJob or dereference-as-copy; source remains present |
| Move | Nonrecursive same-mount no-replace rename of each captured entry; no cross-mount copy/delete fallback; committed source removal occurs only with successful atomic rename |
| Move to Trash | Confirmation required; safe nonpurging backend and tested per-volume semantics; no failed-trash deletion; bounded native adapter accepted in ADR-0009 |
| Permanent delete | No request kind, API, action, shortcut, empty-trash or fallback in the MVP |

## Symlinks, mount boundaries and permissions

Link operations affect the link entry, not its target. Copy preserves literal
relative/absolute link text and broken links; do not convert relative links into
canonical target paths. Copying a directory link copies the link. Navigation may
follow a directory link; operations use separately validated entry identity.
If link creation is unsupported, fail rather than copy target contents.

For regular-file copies, hold an opened no-follow source and verify its type and
identity. The direct KIO worker normally reopens a path; preflight alone does not
protect against a later regular-file-to-link swap. The private operations adapter
must prove an identity-held source bridge to KIO leaf jobs in disposable tests
before enabling copy; unproven bridging is NOT RUN, not a claim of confinement.
Do not substitute a new recursive copy engine or patched worker silently.

Rename/move require a private Linux `renameat2(RENAME_NOREPLACE)` guard with held
parent descriptors, source revalidation and detected mount-change rejection.
This is local no-replace policy enforcement within OperationsService, not a new
daemon/API/general backend. KIO's check-then-rename is not used for this guarantee.
Atomic no-replace protects the destination; there is no claimed atomic
compare-and-rename of a source inode. Unsupported capability/EXDEV fails without
fallback or side effects.

Compare mount IDs, not just device IDs; bind mounts may share a device. If mount
identity is unavailable, mutation capability is unavailable. Protected operands
are deterministic, not an implementation-time arbitrary path/glob list:

- For Rename/Move/Trash, reject a source equal to `/`, configured Home or a mount
  root, or a directory ancestor containing one of those roots. Descendants of
  Home/an ordinary mount are not prohibited merely by that relation.
- Protect the configured QStandardPaths GenericConfigLocation and
  GenericStateLocation, plus the running executable's directory, from any write
  destination and from destructive sources equal to, inside or containing them.
  This deliberately restricts the initial MVP from managing configuration/state
  or its own deployment tree; no private contents are scanned.
- Protect every resolved standard trash root from ordinary write/destructive
  operations; only the separately approved trash adapter may create its owned
  metadata/payload there. A source containing such a root is rejected.
- Reject same-entry targets, a source ancestor of destination, or destination
  inside a moved directory. Resolve parent identity/containment for guards;
  a source symlink leaf to a protected root is still the link, not that root.
  Unknown containment/identity fails closed. Destination prompts identify the
  actual writable parent; unknown permissions are not authorization.

Writes target ordinary mounted local storage only; mounted remote/network
filesystems are browse-only initially. Cross-volume leaf copy is allowed only
when source/destination checks are known and neither is a protected/unsupported
mount. Cross-mount move is LATER. No recursive operation traverses nested mounts.
Directory moves/trash reject nested mount points detected within the tree and
do not recurse to process their contents. Device disappearance/read-only remount
produces a failure/partial result, not a force-mount, force-unmount or retry as
another operation. Btrfs subvolumes, unusual filesystems and unknown identities
fail visibly if their required primitive is unsupported.

Required reference cases use a verified disposable ordinary local filesystem
(ext4 or equivalent declared/tested Linux target): create, same-mount rename/move,
regular/link copy and, after ADR-0009 acceptance, same-mount standard trash must
succeed for eligible writable fixtures. Cross-volume regular/link copy to a
second prepared local volume must succeed; cross-mount move must reject. Bind
mount endpoints with different IDs reject move even with equal device IDs.
Directory move/trash with nested mounts rejects; mounted network writes and
unknown IDs reject. Btrfs same-subvolume supported primitives require positive
tests when claimed; unsupported cross-subvolume rename/EXDEV rejects. A test
suite that rejects every request cannot pass the required positive cases.

Operate as the current user, respecting umask, ACL/sticky-bit/read-only errors.
Do not chmod/chown, request root, use admin URLs, rewrite Polkit rules or promise
complete ownership/ACL/xattr preservation. KIO `NoPrivilegeExecution` is marked
not implemented in the inspected version; it is not a security guarantee.
Copy reports relevant metadata preservation warnings without losing file data;
test data completion and metadata outcomes separately.

## Cancellation, rollback and KIO failures

Queued/Validating cancellation stops before scheduling mutations. Running KIO
leaf jobs use actual Killable capability and deliberate terminal signaling; a
quiet kill cannot be expected to emit `result`. Unsupported cancellation is
shown disabled. Native rename is not interruptible once executing; honor
cancel before starting and between items. KIO mkdir uses actual job capabilities;
a cancellation after its worker created the directory requires reconciliation,
not a claim that mkdir was undone. Accepted native trash has metadata
preparation cancellation points and one noninterruptible no-replace commit per
item: honor cancellation before commit and between items, without interrupting
the commit primitive. No false "canceled" before quiescence.

After cancel/error, collect backend terminal state, reconcile known item paths
without recursively traversing user data, refresh affected views, and display
committed/residual/uncertain effects. Do not start the next item after cancellation.
Keep the application/service alive until owned work quiesces; never terminate a
thread executing a filesystem call.

**Rollback contract:** no batch transaction, undo or automatic rollback of
committed mkdir/copy/rename/move/trash. An atomic rejected rename/mkdir needs no
rollback because it has not committed. Backend cleanup of its own uncommitted
output/metadata can be recorded as rollback only when its identity and success
are established. Otherwise retain and report residuals. Never delete an arbitrary
destination, recursively clean a user directory, overwrite a newer file to undo
a move, or restore trash content automatically. Manual restore is LATER and
requires a separate no-replace contract. Cancellation is not an undo request.

Permission denied, EEXIST, EXDEV, disk full/quota, read-only, unplug/unavailable,
unsupported capability, identity changed, missing worker, worker crash and KIO
errors are distinct outcomes. Stop a failed item; later batch items do not run
automatically after an error. Offer explicit retry of selected failed/unstarted
items only after a fresh request/preflight; never replay committed items.

KIO jobs may auto-delete after result; snapshot first. File workers can be
threaded in the inspected build, so process death may prevent any trustworthy
terminal callback. No crash rollback or durability journal is promised. On
restart show no invented recovery result; persistent operation journaling would
need a later scoped decision. Missing worker/helper/backend is a visible error.

When closing the final window with active/queued jobs, keep it open and offer
Keep Working or Cancel Supported Operations and Wait. Uninterruptible work must
finish before normal exit; no hidden work without usable progress/decision UI.
Do not kill external applications or another manager to exit Files.

## Acceptance criteria and validation plan

Tests use verified fixture Home resolution/injection (XDG paths alone do not
isolate HomeLocation), user-dir/config/data/cache/state/runtime paths, handler
outputs and a private D-Bus context for real worker/launch integration. Before
mutation, assert every resolved path/worker context is contained in the disposable
environment. Trash/per-volume tests require a disposable VM/private prepared
mount namespace or equivalently proven isolation: changing XDG_DATA_HOME alone
does not exclude discovery of real mount trash. They must not write real MIME defaults, mount devices,
purge personal trash or alter recovery. Never use another user's/private kit
contents as fixtures. Real permission tests run unprivileged; running as root is
not proof of denied-user behavior. Mounted/bind/Btrfs tests require an isolated
prepared environment; absence is NOT RUN, never simulated PASS for the real
filesystem behavior. Deterministic barriers/fault points reproduce races;
assert source/destination/old-trash bytes, inode/type/link text and owned residual
identities. Record injected policy tests and actual backend tests separately.

| ID / gate | Given → action → required result |
|---|---|
| AC09-01 | Fixture Home with child/files → launch with no args → Ready listing of that Home and correct app identity; no default writes |
| AC09-02 | Empty/missing/inaccessible/slow directories → navigate → distinct Empty/Error/Loading; prior usable location/history retained on failure |
| AC09-03 | Home → child → Back → Forward → correct location and enabled states; failed Back/Forward and refresh do not mutate history |
| AC09-04 | Cached immediate signals and A → B → A supersession → only current-generation entries/state; QAbstractItemModelTester sees no model violation |
| AC09-05 | Selected/current items → reorder, watcher rename/delete, Grid/List switch → unchanged IDs retained, rename IDs remapped, current visible, no row-retargeted selection |
| AC09-06 | Unicode/custom user dirs and invalid location/URI → Places/location actions → literal paths preserved, errors without creating dirs; unsupported authorities rejected |
| AC09-07 | Selected ordinary file + fixture handler → Enter → correct URL argument and dispatch result; null/self/changed/missing/failing handlers produce visible errors |
| AC09-08 | Script/executable/desktop link/broken link/special file → activate → documented refusal or directory-link navigation, no program execution/embedded-URL dispatch |
| AC09-09 | Missing role/unsupported schema or major/corrupt token resource → start → clear failure; exact resource matches canonical bytes on valid start |
| AC09-10 | Live Wayland window → keyboard/focus/Grid/List at representative scales → usable controls, identity grouping, readable states; no doubled scaling/workspace UI |
| AC10-01 | Writable parent and invalid/existing/new name → create/rename → valid creation/no-op or error; preserve bytes/inode of collided destination |
| AC10-02 | Destination appears after preflight or becomes a link; source/path changes → create/rename/move and real KIO leaf copy → no overwrite, existing bytes/inode/link preserved, detected changes abort/reconcile; missing no-replace capability fails closed |
| AC10-03 | File and relative/absolute/broken/directory links → leaf copy/move → exact bytes or literal link target, source-copy preserved, move identity maintained; recursive copy unavailable |
| AC10-04 | Source regular→link swap while copy is pending → identity-held copy → original opened source or clear rejection; never read the substituted target |
| AC10-05 | Reference filesystem and mount cases above → required positive actions succeed, enumerated unsupported cases reject; no recursive boundary crossing/copy-delete fallback; unavailable real environment is NOT RUN |
| AC10-06 | Unprivileged denied/sticky/read-only parent → operation → permission error, no chmod/root prompt/source loss; umask respected |
| AC10-07 | Destination conflict → new name/skip/cancel/dismiss/stale or duplicate reply → only offered single-use decision; no overwrite/merge/auto-rename |
| AC10-08 | Fault after one batch commit → Partial with ledger; zero-commit disk full/quota/metadata failure → Failed if effect-free, Partial if known residual, Indeterminate if unconfirmed; no blanket success/automatic undo |
| AC10-09 | Cancel queued/running/prompt/native commit/trash item → no new item after cancel; wait for actual quiescence, report completed effects, no false rollback |
| AC10-10 | Missing KIO worker/worker error/disappearing device → visible failure/partial/indeterminate outcome; no app-default change or deletion fallback |
| AC10-11 | Disposable old trash entries + aggressive ktrashrc cleanup settings → approved safe trash → old contents remain; original-path/time metadata valid; backend gate must first be accepted |
| AC10-12 | Trash metadata/payload/orphan/late collision, relative/broken link, directory, denied volume → nonreplacement or explicit unsupported error, valid home/per-volume Path; source/payload/info reconciled before success |
| AC10-15 | Metadata short write/flush/close failure, denied cleanup, replaced/removed reservation, uncertain commit error → original data preserved or committed/residual/indeterminate disclosed; no deletion of ambiguous records |
| AC10-16 | Symlinked/insecure trash directories, unsafe ownership/sticky bits, pre/post-commit cancellation, fixture cross-manager reading → safe rejection/standard storage/no-purge outcomes, no personal trash or recovery mutation |
| AC10-13 | Trash view + Delete/F2/open/copy/restore/empty attempts → read-only state; remove media/metadata errors remain visible |
| AC10-14 | Operation + navigation/view switch/window-close attempt → root-owned job survives; close waits or stays open; no stale decision targets a different job |
| AC10-17 | All-skipped/committed-plus-skipped/skip-then-cancel-without-effects/precommit-canceled/postcommit-canceled, unsupported kill, KIO auto-delete and stale decisions → ordered result rules, exactly one terminal after quiescence; no next item after cancel, no cleanup of a replaced reservation/output |
| AC-PRESERVE | Before/after protected sources/settings fingerprint and association/bus observations in fixture → milestone finish → no task default/FileManager1/Dolphin/Plasma/private-state mutation |

Static gate: architecture/local links, source syntax/configuration, qmllint and
exact token-resource checks. Component gate: Qt Test, QAbstractItemModelTester,
QuickTest for focus/action/model contracts, injected backend lifecycle/faults and
actual disposable filesystem tests for the claimed primitives. Injected faults
test UI/policy; they do not prove actual KIO/volume behavior. Integration/Visual
gate records commands, backend/package revisions, fixture scope, environment and
captures. Existing token tests and architecture checks do not exercise Files.

Planned build invocation after the spec gate: `cmake -S apps/file-manager -B
<isolated-build-dir> -DBUILD_TESTING=ON`, `cmake --build <isolated-build-dir>`,
`ctest --test-dir <isolated-build-dir> --output-on-failure`, plus the generated
QML lint target and a recorded live slice trial. These commands are NOT RUN in
08; the application/CMake project does not yet exist and CMake/ECM are absent.
Build tooling provision must stay separate from app/default installation.

Milestone 09 must pass AC09-01–10 and preservation before 10 starts. Milestone 10
must pass AC10-01–17 and preservation for the claimed supported capabilities;
unsupported cases must produce their specified rejection. Any required live
check that is NOT RUN keeps that gate incomplete; report the blocker rather than
certifying the app. Real Plasma/Dolphin login/failure recovery remains UNKNOWN
and NOT RUN; unchanged source/defaults do not prove independent recovery.

## Milestone 08 completed checkpoint

Architecture, UX, filesystem and testing written-contract reviews are reconciled.
ADR-0008 and the bounded native trash exception in ADR-0009 are explicitly
Accepted. Milestone 08 is COMPLETE; milestone 09 may now implement and validate
the vertical slice before 10 starts. Review/approval PASS is not application or
filesystem acceptance. ADR-0007 remains Proposed and supplies no accepted
session/default integration contract.

Current implementation evidence: **KNOWN documentation only; NOT RUN application
build/runtime/operations; UNKNOWN live compatibility/recovery.** Validation of
this specification is recorded in [CHANGELOG](../../CHANGELOG.md). Source rollback
reverts this task's specification/reference/rule changes while preserving the
user's recorded acceptance of ADR-0008 unless the user explicitly revokes it.
