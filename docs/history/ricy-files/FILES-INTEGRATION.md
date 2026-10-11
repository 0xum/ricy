> HISTORICAL — Closed on 2026-10-11 by [ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md). This preserves the explored proposal/prototype, not an active roadmap, implementation contract, or command to execute. Dolphin is the current Ricy file manager.

# Ricy Files integration assessment

Status: investigation and **Proposed** contracts, 2026-10-11. This document does
not authorize implementation or default changes. [ADR-0003](../../adr/0003-ricy-files.md)
already accepts Files as the future Ricy default and Dolphin for recovery;
[ADR-0007](../../adr/0007-session-file-manager-boundary.md) proposes the integration
boundary below. Until approval, new contracts are proposals, not PLANNED policy.

The separate toolkit/application-local decision in
[ADR-0008](../../adr/0008-ricy-files-technical-architecture.md) is now Accepted. Its
[MVP draft](FILES-MVP.md) permits no default/session/FileManager1 migration;
ADR-0007's contracts here remain Proposed, and the additional trash-backend
decision in ADR-0009 is now separately Accepted for bounded native trash mutation.

## Scope and evidence

**KNOWN** means inspected source or registration, not an exercised workflow.
**INFERRED** identifies a consequence of those registrations. **PLANNED** is
reserved for accepted target intent. **UNKNOWN** means unproven behavior.
The [contribution audit](../../CONTRIBUTION-AUDIT.md) remains the broader grounding.

This assessment inspected the active kit, maintained cumulative Noctalia patch,
the preserved Noctalia 5.2.1 source cache, installed file-manager registrations,
KDE device actions, and installed KIO service menus/plugins. The cache at commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4` represents the older deployed patch
lineage recorded by G-02, not the current single-space patch. Relevant cached
paths below are relative to that source root. Nothing was built or activated.
`docs/ricy-kit/` and the archive remain historical evidence, not runtime owners.
Private settings, backups, file lists and history are not copied into this report.
Targeted scans found no embedded file-manager command references in the inspected
active-profile TOML configuration/settings. Compiled third-party applications,
arbitrary user scripts and live portal/device workflows are not exhaustively
audited; their generic directory/reveal entry points and validation gaps are
mapped below rather than asserted to work.

### Repository evidence index

| ID | Source and responsibility |
|---|---|
| E1 | [Dolphin identity applicator](../../../ricy-kit/contributions/dolphin-noctalia-identity/apply.py): desktop override, FileManager1 activation, user systemd drop-in, per-app Kvantum assignment, dolphinrc and backup/restoration. |
| E2 | [Dolphin launcher](../../../ricy-kit/contributions/dolphin-noctalia-identity/launch.py): forwards arguments to `/usr/bin/dolphin`, injecting `QT_PLUGIN_PATH`, `ricydolphinui` and QSS. |
| E3 | [Qt helper](../../../ricy-kit/contributions/dolphin-blur-corners/ui.cpp), [KWin effect](../../../ricy-kit/contributions/dolphin-blur-corners/corners.cpp), [identity history](../../../ricy-kit/contributions/dolphin-noctalia-identity/README.md): Dolphin widget-specific adaptations and class-filtered corners; distinct lifecycles. |
| E4 | [Search adapter](../../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/desktop-search.py): owns the KRunner compatibility name and opens the Noctalia launcher; it does not route directory URIs. |
| E5 | [Package integration installer](../../../ricy-kit/contributions/dolphin-deb-rpm-installer/install-integration.py), [application entry](../../../ricy-kit/contributions/dolphin-deb-rpm-installer/desktop/cachyos-local-package-installer.desktop.in), [service menu](../../../ricy-kit/contributions/dolphin-deb-rpm-installer/desktop/cachyos-install-package.desktop.in), [backend](../../../ricy-kit/contributions/dolphin-deb-rpm-installer/app/backend.py): separate package app, three MIME defaults and a KDE action. |
| E6 | [Package restorer](../../../ricy-kit/contributions/dolphin-deb-rpm-installer/restore-integration.py), [correction bundle](../../../ricy-kit/contributions/target-implementation-fixes/README.md): destination backups and version-specific Debtap preparation. |
| E7 | [Switching integration](../../../ricy-kit/contributions/plasma-noctalia-switching/integration.py), [command](../../../ricy-kit/contributions/plasma-noctalia-switching/ricy), [recovery](../../RECOVERY.md): panel/shortcut restoration inside the existing Plasma session. |
| E8 | [Shared KDE style applicator](../../../ricy-kit/contributions/noctalia-kde-integration-and-menus/apply-style.sh), [design system](../../DESIGN-SYSTEM.md), [token contract](../../../themes/tokens/README.md): shared KDE appearance versus scoped Dolphin values. |

## Current integration map

| Surface | KNOWN dependency and observed path | Proposed Ricy boundary | Dolphin/Plasma boundary and limits |
|---|---|---|---|
| Open directories | Read-only `xdg-mime query default inode/directory` returns `org.kde.dolphin.desktop`. Its user entry executes `ricy-dolphin %u` (E1/E2). Generic XDG/GIO/KDE directory openers can resolve this entry; that complete call chain is INFERRED, not a live test. | Files accepts local directory paths and `file:` URIs through its own entry and process interface. Integration selects it only in the future Ricy context. | Recovery selects Dolphin. Explicit Dolphin launches retain Dolphin semantics; no executable-name alias or replacement. |
| Launcher/search | E4 delegates search UI to Noctalia. Cached `src/launcher/app_provider.cpp` discovers desktop entries/actions and calls `src/system/desktop_entry_launch.cpp`; activation tokens and optional systemd app launches are supported. No hard-coded Dolphin route was found in the maintained patch or adapter. | A distinct Files entry, icon and application identity; zero-argument launch opens a usable initial location. Pins and directory shortcuts are migrated only after inventory/approval. | Dolphin's existing entry remains available. App discovery is not proof of a configured pin, shortcut, or file-search provider; those remain UNKNOWN. |
| FileManager1 | User `$XDG_DATA_HOME/dbus-1/services/org.freedesktop.FileManager1.service` executes `ricy-dolphin --daemon` and names `plasma-dolphin.service`. Its `70-ricy-aparencia.conf` user drop-in repeats that wrapper. Upstream `/usr/share/dbus-1/services/org.kde.dolphin.FileManager1.service` and `/usr/lib/systemd/user/plasma-dolphin.service` use `/usr/bin/dolphin --daemon`. | Files supplies the public interface in the validated Ricy activation context. MIME selection alone cannot select a D-Bus owner. | Dolphin supplies it in Recovery without Files or a Ricy router. Current registrations reach both shell modes. Bus ownership/activation and cold start were not exercised. |
| MIME/default applications | `inode/directory` selects Dolphin. Three DEB/RPM MIME queries select `cachyos-local-package-installer.desktop`. Those entries exist in user `.config/mimeapps.list`; inspected user KDE-specific/deprecated application MIME files are absent. `x-scheme-handler/trash` query returns no entry. | Change only the future directory default after validation; ordinary files continue to their selected applications. Respect explicit user choices and precedence. | Preserve Dolphin's associations and package defaults. An empty trash association does not mean KDE trash is absent. |
| Desktop entries | E1 replaces every `Exec=` line in the copied `org.kde.dolphin.desktop`, potentially including actions; inspected entry has `MimeType=inode/directory`, `X-DBUS-ServiceName=org.kde.dolphin`, `StartupWMClass=dolphin`. The system application and `/usr/share/kglobalaccel/org.kde.dolphin.desktop` retain `Exec=dolphin %u`. | New Files desktop ID, executable and window/app ID, validated together; never impersonate `org.kde.dolphin`. | User overrides, accelerator registrations and direct binary launches are separate routes. No current Dolphin shortcut binding was established. Broad Exec rewriting is a migration hazard to review, not correct here. |
| Removable storage | Installed Solid `openWithFileManager.desktop` executes `kde-open "%f"`. Device-notifier plugin is installed. E3 retains native `KFilePlacesView` behavior. Cached Noctalia `src/system/disk_mounts.cpp` enumerates mounted `/dev/` filesystems for monitoring; it is not a mounting service. | Browse mounted directories; cooperate with an approved existing device service for mount/unmount/eject, authentication, busy/error and disappearance handling. Backend selection remains UNKNOWN. | Plasma Solid/device notifier, KIO Places and their device actions remain maintained KDE integrations. No hotplug, mount, eject or authentication test performed. |
| Phone/remote devices | Installed Solid actions use `kioclient5 exec mtp:udi=%i/`, `kioclient5 exec afc://%j/`, and `kioclient exec kdeconnect://%j/`. KIO workers for these and remote schemes are present. | Do not advertise support without an approved backend. Unsupported schemes receive a clear error or an explicit launch of a suitable external application, avoiding a default-handler loop. | KDE protocol browsing remains available through Dolphin/KIO. Installed `kioclient5` action strings are recorded as compatibility questions; executable availability and device behavior remain UNKNOWN. |
| Trash | Installed KIO `kio_trash.so` and KDE `directory.trash` link (`URL=trash:/`, `OnlyShowIn=KDE`) establish the KDE route. E3 preserves Dolphin's native navigation. | Interoperable storage and restore, with a Files-owned trash UI. Handle any Ricy trash entry points explicitly; scheme support is a separate declaration. | KIO `trash:/` and Plasma links/applets remain KDE integrations. Storage compatibility does not automatically implement KIO URLs. No trash contents were inspected or modified. |
| DEB/RPM | E5 installs a standalone PyQt app under `.local/share/cachyos-package-installer`, an application entry, and `.local/share/kio/servicemenus/cachyos-install-package.desktop`. Three types: `application/vnd.debian.binary-package`, `application/x-debian-package`, `application/x-rpm`. Backend converts to an Arch package; the UI invokes `pkexec /usr/bin/pacman -U --noconfirm` after its Install action. | Delegate opening packages to the external selected handler; no package conversion, privilege escalation or pacman logic in Files. A special package action would need separate approval. | The KDE service-menu adapter remains Dolphin/KDE-specific. The underlying package app is shared/optional, not exclusive to Dolphin and not required for Recovery file access. No conversion/install performed. |
| Themes/Kvantum | E8 selects shared KDE-Noctalia; E1 assigns Ricy-Dolphin only to `dolphin`, installs QSS/helper and changes dolphinrc. E3's KWin effect filters Dolphin resource classes. | Consume central versioned design tokens via a future toolkit adapter. Files does not load the Dolphin helper or inherit its Qt class assumptions. | Kvantum/QSS/helper, Dolphin settings and class-specific corners remain Dolphin adaptations. They may be optional in the target Recovery but must not be required to open files. Exact installed helper/source equivalence remains UNKNOWN (G-05). |
| External actions | Installed KIO menus include `konsolerun` (`konsole --hold -e %f`), `installfont` (`kfontinst %U`), `filelight` (`filelight %u`) and the package action. Installed KFileItemAction plugins include extract/compress, admin, share, KDE Connect, slideshow, tags, activities, hide/forget, folder-icon and move-to-new-folder actions. | Open With and explicit external application dispatch are baseline contracts. Any future terminal/archive/share action needs an approved scope and argument/URI contract. Do not import all KDE plugin behavior implicitly. | KDE menus/native plugins stay in Dolphin/KIO. Presence does not prove every action works or is enabled. No arbitrary custom action contents or private scripts were exported. |
| Browser/app reveal; portals | No repository-specific browser/editor reveal adapter was found. FileManager1 is the public integration point. Portal OpenDirectory provides another client route; installed backend selection and caller behavior remain UNKNOWN. | Implement public reveal semantics and validate actual browser/editor/sandbox callers before changing defaults. | Preserve KDE portal/FileChooser dependencies. Files is not automatically a portal backend or replacement file picker. |
| Plasma Recovery | E7 restores panels, shortcuts and KRunner; it does not isolate file-manager configuration. Observed environment is `XDG_CURRENT_DESKTOP=KDE`, `XDG_SESSION_DESKTOP=KDE`, Wayland. | Ricy default policy is enabled only after a separate session/default/activation plan is approved and tested. | Current shell switching is not independent Recovery. Stock Dolphin file access must remain usable when Files, Noctalia and Ricy-specific adapters/assets are absent. |

## Proposed responsibilities

The accepted destination remains **PLANNED**: Ricy Session uses Ricy Files;
Plasma Recovery uses Dolphin. The following ownership detail is **Proposed**:

| Owner | Responsibility | Dependency constraint |
|---|---|---|
| `apps/file-manager/` | Files process, navigation, file operations, public file-manager interface and Files-specific UI/state. | May use approved system libraries/services; does not own shell/session policy, Dolphin configuration or package installation. |
| `integrations/` | Session-scoped directory selection, launch/reveal clients and compatibility adapters. | Uses public contracts; no mandatory shared Ricy routing daemon proposed. Exact paths/mechanism require a later implementation proposal. |
| `shell/noctalia/` | Launcher/dock presentation and Ricy entry points. | Selects Files by its identity or public contract; does not become a filesystem/device/package backend. |
| `recovery/plasma/` | Recovery default policy and proof of native Dolphin access. | No runtime dependency on Files, Noctalia, Ricy plugins or a new Ricy router. Existing paths/snapshots preserved until a validated transition. |
| `themes/` and `compositor/kwin/` | Shared identity data and existing optional Dolphin effects. | Tokens may be shared; Dolphin Qt/Kvantum implementation and KWin class filters are not Files APIs. |
| Existing package integration / future approved installer owner | External package app and its KDE service-menu adapter (E5/E6). | Independent of the file manager; optional. The current migration map remains unchanged. |
| KDE/upstream | Plasma, Dolphin, Solid, KIO workers, native plugins, accelerator and portal implementations. | Preserve packages and compatibility identities; these interfaces are not automatically Files dependencies. |

### Required Files contracts before becoming the default

These are proposed acceptance criteria, not an implemented API or toolkit choice.

1. **Launch and directory navigation:** accept zero arguments, local paths and
   encoded `file:` directory URIs; define multi-location behavior. Handle spaces,
   Unicode, symlinks, nonexistent/inaccessible targets and filenames resembling
   flags without executing them. Unsupported schemes fail visibly or offer an
   explicit external handler. Preserve normal listing, copy/move/rename/create,
   cancellation, progress and collision/error behavior before migration.
2. **Public reveal/properties:** provide bus/interface `org.freedesktop.FileManager1`
   at `/org/freedesktop/FileManager1`. Implement `ShowFolders(as, s)` for directory
   contents, `ShowItems(as, s)` for selection inside parent folders, and
   `ShowItemProperties(as, s)` for metadata UI. Accept empty StartupId and define
   multi-URI behavior. Unsupported or inaccessible URIs must not be acknowledged
   as successful navigation. The public methods come from the
   [File Manager interface](https://wiki.freedesktop.org/www/Specifications/file-manager-interface/).
   The installed Dolphin XML additionally exposes `SortOrderForUrl`; that KDE
   extension is not required by this public contract.
3. **Application registration:** provide a distinct desktop/executable/app ID,
   icon and valid directory MIME capability, with consistent launcher/dock
   matching. Choose CLI and optional `org.freedesktop.Application` activation
   together; declare `DBusActivatable` only if implemented. Preserve argument and
   activation-token handling using the
   [Desktop Entry specification](https://specifications.freedesktop.org/desktop-entry/latest-single/).
   Do not claim every KDE desktop key is a portable API.
4. **Delegation:** resolve file types through the shared MIME database and the
   user's associations; launch selected handlers or Open With. Do not make Files
   the default for ordinary documents/packages, overwrite user choices on startup,
   or route unsupported directories back recursively to itself. Directory
   capability, default policy and D-Bus ownership are separate contracts.
5. **Removable media:** support browsing mounted local storage and explicit
   device operations through the later approved backend. Handle removed media,
   denied/canceled authorization, read-only mounts and busy unmounts; preserve
   transfers and report errors. Do not create a new automounter, write fstab or
   change system Polkit rules as part of the file-manager boundary.
6. **Trash interoperability:** read/write compatible `files/` and `info/` records
   in `$XDG_DATA_HOME/Trash` and supported per-volume locations; restore original
   paths with collision handling. Preserve `.trashinfo` metadata, permissions and
   uniqueness. Failed trashing must not silently become permanent deletion.
   Validate Files-to-Dolphin and Dolphin-to-Files restore using disposable files.
   The [Trash specification](https://specifications.freedesktop.org/trash/1.0/)
   defines storage, not KIO's `trash:/` routing. Support for that URI and per-volume
   operations must be explicitly tested before advertising them.
7. **Independence and identity:** Files runs without Noctalia IPC or Dolphin
   plugins; Recovery runs without Files or Ricy-specific services/assets. Files
   uses the existing token contract; toolkit, KIO/GIO choice, executable name,
   packaging, application ID and device backend remain UNKNOWN pending proposals.

KDE service menus are their own
[Dolphin integration format](https://develop.kde.org/docs/apps/dolphin/service-menus/).
Supporting standard application entries does not require a service-menu parser,
KFileItemAction ABI, DolphinPart, Baloo/tags/activities, KIO admin/remote/archive
protocols, Dolphin settings, or Kvantum. These integrations stay with Dolphin/KDE
unless independently approved for Files. Equivalent user features may be proposed
later without importing those implementation contracts.

The [OpenURI portal API](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.OpenURI.html)
is a client/backend integration to validate, not a Files-owned backend:
OpenDirectory reveals a containing directory using FileManager1; OpenFile handles
local file/directory descriptors; OpenURI excludes `file:` URIs. FileChooser is
a separate portal. This proposal preserves existing KDE providers and requires
testing the selected backend rather than inferring it from Files registration.

## Session selection and recovery independence

Recommended: distinct Files identity plus session-scoped defaults and a validated
activation context; no shared routing daemon. A single D-Bus well-known name has
one owner on a given bus. Separate visual shells, different desktop entries or
different MIME defaults do not alone establish distinct activation contexts.
Concurrent logins can share user-manager/bus infrastructure; the proposal does
not assume a separate login automatically fixes ownership or environment races.

The [MIME Applications specification](https://specifications.freedesktop.org/mime-apps/latest-single/)
supports desktop-specific default files selected by `XDG_CURRENT_DESKTOP`.
Lookup interleaves desktop-specific and generic files at each precedence level;
user configuration can outrank distribution defaults. Desktop-specific files
specify defaults, not added/removed associations. Candidate Ricy/KDE defaults
must therefore be tested with generic user overrides, application capability
and inherited environment; a new desktop identity/file alone is insufficient.
Do not repeatedly rewrite the shared user `mimeapps.list` when switching shells.
Product defaults describe the baseline; explicit user preferences need a documented
policy, not silent replacement to force isolation.

Before any migration, a separate implementation proposal must resolve:

- The Ricy session identity and MIME precedence policy, including existing explicit
  user defaults and the supported same-user concurrent-session behavior.
- FileManager1 activation selection, one-owner enforcement, correct graphical
  environment and cold activation. A user-wide Dolphin service drop-in cannot
  become a Files service, and a second conflicting global service is insufficient.
  No new bus topology, daemon or unit is approved by this assessment.
- A native Dolphin Recovery launch and activation path that works with Ricy
  overrides/assets unavailable. Direct `/usr/bin/dolphin` avoids E2's injection,
  but alone does not prove independence: existing daemons, user overrides,
  environment, Kvantum assignments and service drop-ins still need verification.
- Reversible retirement or scoping of E1's overrides, with original backups and
  later user edits preserved. Its whole-file restorer can overwrite later changes;
  it is not an automatic migration rollback recipe.
- No forced daemon termination, transfer cancellation, session switch or global
  association write to obtain evidence. Tests belong in a prepared environment.

Current discrepancy C-003 is retained: customized Dolphin handles file-manager
integration. Current C-002 is also retained: Recovery still uses Ricy switching
scripts. The proposal adds gates; it does not silently mark either discrepancy
resolved. Migration batches in [MIGRATION-PLAN](../../MIGRATION-PLAN.md) are not executed.

## Future validation and transition gates

| Gate / level | Required evidence before defaults change |
|---|---|
| Static / Component | Valid desktop and D-Bus contracts; CLI/URI escaping and multiple-target cases; file operations/error recovery; tokens; no accidental Dolphin dependencies. |
| Integration | Actual XDG/GIO/KDE directory opens, Noctalia launcher/dock, browser/editor reveal, all three FileManager1 calls, cold start and already-running instances; selected portal backend and sandboxed caller. |
| Integration / Environment | Removable mount/browse/unmount/eject, denied authentication, busy transfers, unplug and read-only cases; selected dependency versions and explicitly supported schemes. |
| Component / Integration | Shared trash create/list/restore across both managers, name collisions and per-volume behavior; external package handoff without conversion/install. |
| Recovery | Ricy and Plasma login/return/failure paths; Files/Noctalia unavailable; Ricy plugin/theme/adapter missing; Dolphin directory/reveal/properties/device/trash access; defaults and FileManager1 owner remain correct. Resolve same-user concurrency or explicitly restrict it in an approved session design. |
| Migration / rollback | Snapshot exact affected associations, entries, service registrations and prior absences; preserve unrelated and later user edits. Restore original configuration without replacing personal data or terminating transfers; revalidate Recovery. |
| Visual | Validate Files identity through central tokens after toolkit approval; Dolphin visual migration is separate and optional. |

No implementation milestone is authorized here. Sequence after separate approval:
resolve session/default/activation mechanism; implement and validate Files in an
isolated environment; prove independent Recovery; only then request a concrete
default migration with backups and rollback. Package MIME associations stay
outside the directory-default migration.

## Validation performed for this assessment

- PASS: read-only source/registration inventory described above and primary
  protocol documentation review; no application contract was exercised.
- PASS: `./scripts/verify architecture` (documentation links/foundation scope).
- PASS: scoped whitespace/link and protected-file fingerprint checks recorded in
  the changelog; these are preservation checks, not functionality tests.
- NOT RUN: live file-manager, D-Bus activation, portal, device, trash, package,
  login/switching and failure-recovery trials; no implementation or prepared
  migration environment is available, and the active session was preserved.
- NOT APPLICABLE: new runtime Component/Visual tests or builds; documentation only.

Approval is required for ADR-0007's proposed contracts. It would not authorize
implementation, a toolkit, session topology, or default/MIME/Dolphin changes.
