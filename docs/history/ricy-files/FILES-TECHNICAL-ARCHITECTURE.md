> HISTORICAL — Closed on 2026-10-11 by [ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md). This preserves the explored proposal/prototype, not an active roadmap, implementation contract, or command to execute. Dolphin is the current Ricy file manager.

# Ricy Files technical architecture — milestone 07

Status: **Option A Accepted by explicit user approval on 2026-10-11**
(America/Sao_Paulo). Comparisons retain milestone 07's investigation and reasoning;
[ADR-0008](../../adr/0008-ricy-files-technical-architecture.md) owns the accepted
decision. [Milestone 08](FILES-MVP.md) specifies contracts, with a separate
[trash exception](../../adr/0009-ricy-files-nonpurging-trash.md) now Accepted separately under ADR-0009.
No application has been implemented.

## Objective and existing authority

Select a maintainable foundation for isolated Ricy Files development, in
`apps/file-manager/`, before specifying or implementing the MVP. Preserve
[INVARIANTS](../../INVARIANTS.md), [ADR-0002](../../adr/0002-plasma-recovery.md),
[ADR-0003](../../adr/0003-ricy-files.md) and
[ADR-0005](../../adr/0005-consumable-visual-tokens.md).

**KNOWN:** the [Files reservation](PROTOTYPE-README.md) contains only
documentation. Toolkit and application-local boundaries are now approved;
implementation remains pending. The existing
[integration assessment](FILES-INTEGRATION.md) inventories current Dolphin
consumers; [ADR-0007](../../adr/0007-session-file-manager-boundary.md) remains Proposed.
Current switching still shares a Plasma session and customized Dolphin paths.
C-002/C-003 in [ARCHITECTURE](../../ARCHITECTURE.md) are unresolved.

Explicit approval of option A permits milestone 08 and, after its specification
gate, isolated milestones 09–10. It supersedes the foundation-era prohibition on
Files implementation only within that scope. It does not accept ADR-0007 or the
separately approved ADR-0009; neither authorizes default/session migration.

## Evidence and investigation limits

Three independent subagents investigated toolkit/models, filesystem operations,
and desktop/design integration. The coordinator reconciled their findings against
the repository and upstream sources. Research and package/header inspection were
read-only; no application, installer, service activation or session switch ran.

**KNOWN, inspected host only:** Qt base/declarative/tools are 6.12.0; KIO and
Solid are 6.30.0; GCC and Ninja are available. Qt model-test headers, `qmllint`
and `qmltestrunner` exist. CMake and Extra CMake Modules are absent. PySide6 is
absent. These observations are not compilation or runtime validation.

The installed `libqwayland.so` belongs to `qt6-base`. Absence of a separate
`qt6-wayland` package is not evidence that client Wayland support is missing;
the current [Arch file list](https://archlinux.org/packages/extra/x86_64/qt6-base/files/)
also places the plugin in base. CachyOS package revisions must be recorded during
the actual build. Installed KF6 6.30 CMake metadata requires Qt 6.9 or newer;
an arbitrary Qt 6.8 floor would not match that package set.

**UNKNOWN:** supported minimum Qt/KF6 versions, application build compatibility,
large-directory responsiveness, packaged execution, live Wayland identity,
device/trash behavior, visual scaling and new-app blur. No research finding is
a milestone 09 or 10 acceptance result.

## Concrete options

| Option | Concrete benefit | Cost and limitation | Assessment |
|---|---|---|---|
| A — C++ + Qt Quick/QML, selected KF6 KIO/Solid adapters | Declarative shared-token UI; established asynchronous file/device facilities; same native dependency ecosystem as the target desktop | C++/QML boundary and custom conflict presentation; KF6 package/worker dependencies; integration still needs tests | Recommended |
| B — C++ + Qt Quick/QML, pure Qt backend | Smaller direct framework API surface; sufficient primitives for local browsing | Ricy must implement more copy/move/conflict policy, interoperable trash and device integration, or accept a narrower product | Viable, greater ownership of filesystem semantics |
| C — C++ + Qt Widgets/KIO | Mature desktop views, selection and stock KIO dialogs | Additional adaptation to Ricy visuals; QSS/Kvantum does not automatically consume canonical tokens | Credible if mature widget interactions take priority |
| D — PySide6 + QML | Python iteration with Qt Quick presentation | Adds binding/runtime packaging; KF6 reuse may require another bridge; no demonstrated benefit sufficient to offset that maintenance | Not preferred |
| E — QML-only/labs folder model | Small local-folder demonstration | No complete operation/device architecture; labs compatibility limitations | Not a suitable application foundation |

**INFERRED recommendation:** A reduces the amount of new filesystem machinery
owned by Ricy while retaining application identity and UI control. It does not
make Files a Dolphin front end. GTK/GIO and web/Electron alternatives have no
demonstrated advantage here sufficient to justify another visual/runtime stack;
they are not rejected as technically incapable.

Qt recommends separating presentation from business logic, and supports local
[Quick Controls customization](https://doc.qt.io/qt-6/qtquickcontrols-customize.html).
Its [C++/QML guidance](https://doc.qt.io/qt-6.8/qtquick-bestpractices.html) supports
this division. [PySide deployment](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html)
is a distinct packaging path rather than removal of native build maintenance.

Pure Qt is a real alternative: [QFileSystemModel](https://doc.qt.io/qt-6.8/qfilesystemmodel.html)
is in QtGui, populates in a background thread and maintains watched state. It is
not inherently Widgets-only or synchronous. It does not supply the proposed
operation/trash/device architecture. The
[labs folder model](https://doc.qt.io/qt-6.8/qml-qt-labs-folderlistmodel-folderlistmodel.html)
is not a substitute for those responsibilities.

## Accepted foundation and ownership

One Ricy-owned application process, C++17 with Qt Quick/QML and Quick Controls
Basic, built with CMake/ECM. Qt's supported C++ baseline is
[C++17](https://doc.qt.io/qt-6/cmake-get-started.html); no C++20 feature currently
justifies a higher application requirement. Propose CMake 3.25 or newer for the
inspected [Qt 6.12 toolchain](https://doc.qt.io/qt-6/cmake-supported-cmake-versions.html).
Use [qt_add_qml_module](https://doc.qt.io/qt-6/qt-add-qml-module.html) for resources,
type registration and tooling. Actual supported version floors follow builds,
not the versions merely found installed today.

| Application-local responsibility | Proposed boundary |
|---|---|
| QML presentation | Places, location/history controls, Grid/List, selection/focus, feedback and prompts; no direct filesystem mutation or shell commands |
| Navigation and selection | Typed URL identities, history and current location; view indices are not durable item identities |
| Directory model | Flat QAbstractListModel over KCoreDirLister/KFileItem; sorting/filtering in C++; loading/error/update state; reject stale navigation results |
| Operations | C++ policy/job adapter over KIO; independent from view lifetime, with explicit progress, decisions, cancellation and terminal results |
| Launch adapter | Shared MIME/selected application resolution through KService/KIOGui; validated arguments and explicit missing-handler/error behavior |
| Places/devices | QStandardPaths user directories and Solid device state; device policy stays separate from directory views |
| Token adapter | Validate and expose the exact packaged canonical JSON locally; no shared SDK, daemon or live token service |

These are accepted responsibility boundaries; executable module contracts live
in milestone 08. Milestone 08 must freeze interfaces before parallel
implementation. No Core/Services extraction or new Ricy daemon/IPC protocol is
proposed. No ownership is transferred from the active kit, Noctalia or Dolphin.

## Filesystem, asynchronous execution and operations

[KCoreDirLister](https://api.kde.org/kcoredirlister.html) provides asynchronous
listing/update/error/cancellation signals independently of graphical views.
Disable implicit error dialogs and present explicit application state. Publish
model changes on the model's owning GUI thread, as required by
[QAbstractItemModel](https://doc.qt.io/qt-6/qabstractitemmodel.html). In-flight
listing must not replace a newer location. A slow mount can still delay backend
work; asynchronous APIs alone do not prove responsiveness.

[KIO CopyJob](https://api.kde.org/kio-copyjob.html) and
[KJob](https://api.kde.org/kjob.html) supply operation/progress/capability primitives.
Ricy still owns the policies for conflicts, permissions, symbolic links,
mount boundaries, job lifetime and partial results. Proposed initial scheme
allowlist is `file:` plus the explicitly supported `trash:` view/operations.
KIO's other installed protocols do not become advertised Files features.
Validate URL authorities as well as schemes; remote `file:` authorities are not
implicitly local paths. Exact validation rules belong in the MVP contract.

KIOCore/KIOGui do not provide stock conflict dialogs. The
[default delegate factory](https://api.kde.org/kio-jobuidelegatefactory.html)
is registered by KIOWidgets. Option A therefore includes a local KJobUiDelegate
with a QML-facing
[AskUserActionInterface](https://api.kde.org/kio-askuseractioninterface.html)
implementation, not stock widget dialogs. Associate each decision with its live
job, respect offered choices, respond once, and cancel safely if its presentation
disappears. Pause/resume alone does not implement conflict decisions. If this
adapter proves inadequate, changing to widget dialogs needs an explicit scope
assessment; do not silently enable them.

Proposed safety floor: no automatic overwrite, no trash-to-delete fallback, no
privilege escalation and no promise of transactional rollback. Cancellation may
leave completed items or partial destinations; report those outcomes rather than
claiming that cancellation undid the operation. Initially leave permanent delete
disabled; milestone 08 may define an explicit separately reviewed contract if
needed. Exact symlink traversal, rename atomicity, cross-mount moves, disk-full,
collision and partial-failure rules must be executable criteria in milestone 08.

KIO is not exclusively an in-process library nor invariably a file-worker
subprocess. Inspected [KF6 6.30 worker source](https://github.com/KDE/kio/blob/v6.30.0/src/core/worker.cpp)
uses a file worker thread by default and workers for other schemes can use
processes. Existing KIO helper/activation services and trash workers are runtime
dependencies to audit during packaging. This is approved-framework reuse if A is
selected, not a new Ricy service, and does not require a running Dolphin UI.

Milestone 08 found limits requiring specific policies: KIO local rename is
check-then-rename, recursive listing has no mount-confinement hook and trash
mutation can apply configured permanent cleanup. See the MVP's guarded rename,
bounded leaf-copy scope and Accepted ADR-0009. Framework reuse does not prove
that every KIO default satisfies the application safety contract.

## MIME, opening, drag and drop, and future thumbnails

Use the shared MIME database and the user's selected handlers, with a launch
adapter independent of navigation. Associated opening does not execute a command
assembled from file names. Distinguish launch dispatch from the receiving
application successfully reading the document.

[OpenUrlJob](https://api.kde.org/kio-openurljob.html) alone is insufficient policy:
the inspected [6.30 implementation](https://github.com/KDE/kio/blob/v6.30.0/src/gui/openurljob.cpp)
can fall back to QDesktopServices when an association/UI handler is absent.
Its execution flag does not settle every script or desktop-link case. Recommend
explicit preferred-handler resolution via
[KApplicationTrader](https://api.kde.org/kapplicationtrader.html) and a controlled
[ApplicationLauncherJob](https://api.kde.org/kio-applicationlauncherjob.html),
with a clear error for no handler. Specify `.desktop`/embedded-link and executable
behavior in milestone 08; initially do not directly execute these as programs
or follow embedded links. Require a non-null resolved service, reject recursive
dispatch to Files, and never enable temporary-file deletion for ordinary user
files. No package-installation logic belongs in Files.

Qt Quick [Drag](https://doc.qt.io/qt-6/qml-qtquick-drag.html) and
[DropArea](https://doc.qt.io/qt-6/qml-qtquick-droparea.html) are presentation
primitives. Later external URI drops must pass through the same validated
operation engine and explicit action policy, not mutate files in a QML handler.
Drag/drop support requires real Wayland/source-target trials before a claim.

Future thumbnails can use [KIO PreviewJob](https://api.kde.org/kio-previewjob.html)
behind an asynchronous provider with bounded work, cache invalidation and decoder
risk review. That capability adds no MVP thumbnail requirement or indexing daemon.

## Places, devices, trash and public integration

[QStandardPaths](https://doc.qt.io/qt-6/qstandardpaths.html) supplies configured
Home/Documents/Downloads/Pictures/Videos locations; do not assume English path
names on disk or create missing user directories on launch. A Files-owned Places
model combines these with mounted local drives and Trash. Avoid importing
[KFilePlacesModel](https://api.kde.org/kfileplacesmodel.html) wholesale: it belongs
to KIOFileWidgets and introduces bookmark/action/UI coupling.

[Solid StorageAccess](https://api.kde.org/solid-storageaccess.html) exposes device
state and completion/error signals for explicit setup/teardown. The MVP must
define mounted-drive browsing and removal during I/O; any mount/unmount UI needs
an explicit contract. No Ricy automounter, fstab writer, Polkit policy or device
service is proposed. Existing UDisks/authorization infrastructure remains upstream.
Phone/remote protocols are not implicitly supported.

Use the existing KIO trash worker and
[Freedesktop Trash storage convention](https://specifications.freedesktop.org/trash/1.0/)
rather than inventing a private trash format. A Trash view belongs in the MVP
specification. Storage compatibility, listing, per-volume behavior and restore
are separate claims; cross-manager restore remains a pre-default integration
gate from FILES-INTEGRATION, even if restore UI is deferred from the first MVP.

Propose executable `ricy-files`, display name `Ricy Files`, and local desktop/app
identity `io.github.0xum.RicyFiles`, based on the inspected Git origin owner.
This is an application identifier proposal, not a new domain ownership claim.
Set Qt application/desktop identity consistently and validate KWin/Noctalia
grouping later. Build/package artifacts may contain an ordinary application
entry/icon; installed registration requires review in the prepared environment.
Keep `DBusActivatable` absent/false until an activation contract is approved and
implemented; carrying a desktop entry is not a D-Bus activation implementation.

There is **no FileManager1 name acquisition, activation file, directory-default
or MIME-default change in milestones 09–10**. FileManager1's public methods stay
future compatibility targets in the existing integration assessment. Do not
accept ADR-0007 automatically or use a second competing global bus owner to test
the isolated executable. No Dolphin launch wrapper, desktop override, plugin,
theme, systemd drop-in or session setting is changed by this proposal.

## Central identity and Wayland

Bundle exact bytes from [themes/tokens/tokens.json](../../../themes/tokens/tokens.json)
as a Qt resource. Validate schema 1 and supported contract major; required-role
errors must be visible. Reuse shared color, spacing, UI typography, radius and
motion roles through the local adapter. Preserve logical px versus pt, toolkit
device scaling, fill alpha versus text opacity and scoped shell/Dolphin values.
No new palette or edits to canonical values are proposed.

Start with an opaque application surface and standard window decoration;
compositor blur/window-corner adaptation remains deferred. Do not load Dolphin's
QSS/helper or generalize its KWin class-specific effect. This avoids choosing a
new compositor integration merely to implement navigation. Actual focus,
selection, hover, disabled states, accessibility, reduced motion and scale
adaptation belong to milestone 08's UX contract and subsequent visual validation.
The [DESIGN-SYSTEM](../../DESIGN-SYSTEM.md) remains authoritative.

## Packaging, maintenance and testing proposal

Direct application APIs: Qt Core/Gui/Qml/Quick/QuickControls2, KF6 KIOCore/KIOGui,
CoreAddons/Service as directly used, and Solid. Qt Test/QuickTest are test
dependencies. Extra CMake Modules and CMake are build dependencies. No Qt private
API, KWin plugin/header dependency, Python runtime, Kirigami, QtWebEngine or
DolphinPart is proposed.

**KNOWN:** installed KIO targets link CoreAddons, Qt Network/DBus, ConfigCore,
Service and QtGui; runtime dependencies include additional KF6 facilities.
The Arch/CachyOS `kio` package also ships widget libraries and helpers. Narrow
application target use does not mean a narrow package closure or absence of KDE
services. Audit the actual dependency closure/QML imports/platform plugins and
ship tokens/icon/entry with the app; do not copy private kit/profile material.
Native Arch/CachyOS packaging is proposed; no package installation is authorized
by this document. Build reproducibility, licenses and redistribution need review
before publication, as in [GIT-BASELINE](../../GIT-BASELINE.md).

Milestone 08 must select concrete acceptance tests before implementation:

- Static: CMake/configuration, `qmllint`, resources and token-version handling.
- Component: Qt Test and QAbstractItemModelTester; temporary-directory navigation,
  stale results, selection/history, launch resolution and job lifecycle tests.
- Operations: disposable sources/destinations, conflicts, links, permissions,
  disk-full/failure simulation, partial results, cancellation and trash metadata.
- Integration: isolated association fixtures, KIO worker availability, trash and
  device backend tests; separate prepared tests for mounted/removable media.
- Visual: live Wayland identity, keyboard/focus/selection, Grid/List, scaling,
  reduced motion and accessibility. Headless tests do not certify these.
- Recovery: repository preservation checks now; actual independent login/failure
  recovery remains a later session/default gate and cannot be proved here.

## Roadmap checkpoints

| Milestone | Current checkpoint | Exit before the next milestone |
|---|---|---|
| 07 — Technical architecture | COMPLETE; option A explicitly Accepted | Acceptance recorded in ADR-0008; ADR-0007 not accepted by implication |
| 08 — MVP specification | COMPLETE; specification reviewed and ADR-0009 Accepted | Proceed sequentially to the isolated vertical slice |
| 09 — First vertical slice | NOT STARTED | Launch → Home → listing → Grid/List → directories → Back/Forward → associated opening; tests and scoped live acceptance evidence |
| 10 — File operations | NOT STARTED | Contract-defined create/rename/copy/move/trash, safe partial/conflict/error/cancel behavior and disposable-fixture validation |

Milestones are sequential. No speculative application code is included here;
milestone 08 has its own specification. Independent research/review may run in parallel;
implementation needs frozen interfaces and isolated branches/worktrees when
delegated concurrently. The coordinator owns integration and revalidation.

## Validation and preservation

Results for this documentation-only checkpoint are recorded in
[CHANGELOG](../../CHANGELOG.md). Static architecture/link/token/preservation checks do
not certify Files functionality or a healthy desktop. Live application, file
operations, devices, login/switching and recovery trials are NOT RUN. Application
Component/Visual builds are NOT APPLICABLE before implementation.

Rollback of this checkpoint removes its proposal/navigation/changelog changes
only. Runtime sources, defaults, services, tokens, Dolphin/Plasma and recovery
paths have no task-created dependency to roll back.
