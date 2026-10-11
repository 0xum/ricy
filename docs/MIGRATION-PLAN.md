# Incremental migration

## Current structure — KNOWN
- Root: README and wrappers with absolute paths to the active kit.
- `ricy-kit/`: 23 remaining contribution directories, outputs/scripts, demonstrations
  and installation materials. All 24 logical contributions remain mapped.
- `integrations/keyboard-cedilla/`: first source relocation, two opt-in applicators
  and their README; installed preferences were not reapplied.
- `services/`: three relocated autostart source templates; installed units and
  runtime scripts retain their existing paths.
- `docs/ricy-kit/`: preserved transportable variant; it is not automatic mirror.
- `docs/ricy.md`, `REINSTALL.md`, `VISUAL-IDENTITY.md`: history and references.
- `archives/ricy.zip`: preserved original file; later local Git selection is
  documented in [GIT-BASELINE](GIT-BASELINE.md).

Sources and dependencies per contribution are in [COMPONENTS](COMPONENTS.md).
The file-level map and migration batches below refine those approved destinations
without approving new runtime contracts or bulk extraction.
[CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md) grounds all 24 contributions, consumers,
part-level roles and cumulative variants. It does not authorize relocation or
removal. The foundation created documentary directories and validators; it did
not relocate runtime.

The later [token-centralization decision](adr/0005-consumable-visual-tokens.md)
implements the canonical JSON source in [themes/tokens](../themes/tokens/README.md).
Only the offline identity board consumes it so far, with exact before/after
bytes. Existing runtime sources and transport snapshots remain in place;
application/toolkit and desktop consumer migrations remain PLANNED.

Grounding gates: current RICY-001 source is not deployed (G-02); blur-continuity
has a failed registered consumer and UNKNOWN disposition (G-03); exact compiled
Dolphin-helper provenance and individual private plugin consumers remain UNKNOWN.
Preserve these limits before selecting migration inputs. MIGRATE tooling and
PLANNED destinations do not imply that a move, activation, or new contract has
been approved. No contribution currently has sufficient evidence for REMOVE.

## Target structure — PLANNED
| Current | Destination expected | Condition before migration |
|---|---|---|
| Patches Noctalia and public profile | shell/noctalia/ | Identify cumulative variant and consumers; do not transport private profile |
| Blur/ricywindowactions/corners | compositor/kwin/ | Preserve version/ABI, licenses, build/install/reversion |
| Theme Tokens and Assets | themes/ and themes/tokens/ | Canonical JSON and offline board consumption implemented; runtime/assets require individual migration while maintaining values and appearance |
| Search/ Shortcuts Adapter/KDE/Dolphin | integrations/kde/ | Map D-Bus, units, desktops and paths in both kits |
| Autostart and integration units | services/ | Preserve order/readiness, names and return policy |
| Alternance and snapshots | recovery/plasma/ | Validate restoration and reduce Ricy dependency without losing panels |
| Preparation/applicators | installer/ | Separate public backup/state materials by allowlist |
| AIC8800 Driver | integrations/hardware/ | Keep optional, pin/licenses and kernel support |
| Common wrappers/helpers | core/ if justified | Find real duplication; do not create framework |
| Checks of this step | scripts/ | Keep offline; tools/ only for needed tools |

## Safe migrations
The own Files application and 07–10 implementation gates are retired under
[ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md). There is no app migration
or replacement-manager roadmap. Future Dolphin visual polish must start from
the [recorded baseline](DOLPHIN-BASELINE.md), with separate authorization.

Documenting borders, adding rules/links and read-only tests are safe at this stage. Consolidating references can precede movement of sources. Even a seemingly simple change of path requires search for callers. Before each migration: inventory → references → backup → minimum change → appropriate validation → update of affected docs/manifests → clear rollback.

## Risky migrations — not executed
Rename contributions/outputs; unify kits; move profiles/snapshots; change paths recorded in drives, symlinks, desktop entries and wrappers; reorganize cumulative patches; change activators; separate Plasma/Noctalia session; remove Dolphin; exchange login manager. Require own plan and recovery tests. Do not regenerate historical SHA256SUMS to disguise installation divergences.

## Deprecated Concepts — Preserved as History
Names `noctalia-teste.service`/`start-test.sh` do not mean temporary session today. “Transport configuration” remains useful for playback, but no longer defines the whole product. Previous cumulative compilers remain historical. Inherited workspaces do not define future experience. No files have been removed because it appears obsolete.

## Migration order
1. Audit RICY-001 in configs, UI, menus, shortcuts and gestures, distinguishing API KWin
of exposure to the user; propose minimum adjustment without altering fallback.
2. Inventory references and prepare revised public baseline: sources/licenses,
portable path, absence of private data; choose versioning before publishing.
3. Centralize consumption of tokens, one component at a time, with visual comparison.
4. Extract patches/builds and component integrations with path compatibility.
5. Design Plasma Recovery isolation and only then an independent Ricy session.
6. Maintain Dolphin as the file manager; evaluate separately authorized visual
   polish without taking over upstream filesystem responsibilities.

## Architecture Decisions Required — Only Blocked Future Parts

ARCHITECTURE DECISION REQUIRED

**Problem:** how to separate the future Ricy session without losing wallpaper/desktop and recovery that today depend on plasmashell and Ricy scripts?

**Evidence:**  `plasma-noctalia-switching/integration.py` keeps plasmashell, uses D-Bus/KGlobalAccel and reads Ricy snapshots when restoring. View
[ARCHITECTURE C-002](ARCHITECTURE.md) and [RECOVERY](RECOVERY.md).

**Options:** A. conserve the current integration while specifying and testing an independent route; B. create dedicated sessions and set wallpaper ownership, login and recovery before migrating.

**Recommended:** A in this foundation; draw up comparative proposal before B.

**Impact:** units, login, wallpaper, shortcuts, compositor and return after crash. Runtime separation is PLANNED and is not implemented without explicit approval. The already requested documentary reservation remains valid and independent of this decision.

## File-level extraction map

Assessment date: 2026-10-11 (America/Sao_Paulo), after grounding and token
centralization. Paths below are relative to `ricy-kit/contributions/` unless
explicitly prefixed otherwise. **KNOWN** source relationships were inspected;
**PLANNED** targets assign responsibilities, not a new directory/API contract.
The [grounding audit](CONTRIBUTION-AUDIT.md) retains classifications and runtime
limits. Installed entry points and symlinks were inspected read-only again;
no applicator, service reload, effect activation or session switch ran.

| Approved subsystem | Concrete source payload and ownership | Callers/dependencies and extraction gate |
|---|---|---|
| `shell/noctalia/` — PLANNED | `app-icon-reordering/noctalia-ricy.patch`, `build.sh`, `validate-{actions,indicator,order,motion,native-drag}.*`, Noctalia LICENSE; `notification-continuity/enable.py` binary activation/restore. Public `noctalia-kde-integration-and-menus/outputs/noctalia-test/config.toml` is a seed. Localization `apply.py` contains shell preference handling. PATCHES + RICY-OWNED. | Build/validators depend on a pinned checkout and local patch. All cumulative variants call the notification activator; the activator reads sibling integration settings and changes units. Carry the selected source, license and validators together; keep build and activation separate. G-02 blocks using the deployed cache as the current source. Private profile/state and plugins are not public migration inputs. Older cumulative diffs remain historical in their current paths. |
| `compositor/kwin/` — PLANNED | `window-fade-expand/assets/kwin/effects/ricywindowactions/`, its GPL license and `validate.py`; `blur-continuity/blur-continuity.patch`, `build.py`, LICENSE; `dolphin-blur-corners/corners.cpp`, `metadata.json`, `build.py`, `enable-corners.py`, LICENSE; appearance `assets/kwin/scripts/windowsarrows/` and `assets/kwin/effects/smoothwindowgeometry/` with their licenses. UPSTREAM derivatives + PATCHES + RICY-OWNED. | Effect IDs and KWin ABI survive relocation. Window activation writes shared `kwinrc` and has backup/restore; windowsarrows native build and shortcuts are inside appearance `user.py`. Qt `ui.cpp` is a different plugin, assigned to integrations below. Native blur is loaded; ricyblur is unresolved, so preserve its source and installed selector. `adaptivepanelwidth` and squash-style packages remain HISTORICAL. |
| `themes/` — tokens implemented; other payloads PLANNED | Existing `themes/tokens/` JSON/schema/template/tools; integration `outputs/kde-outlines/KDE-Noctalia/` Kvantum assets; Dolphin `dolphin.qss` and theme transformations in `apply.py`; appearance `assets/` cursor/font/SDDM/Plasma assets, preferences and licenses; Konsole `assets/PlasmaBlur.{profile,colorscheme}`; lock-screen QML adaptations in `login-matched-lock-screen/apply.py`. UPSTREAM/derivative assets + RICY-OWNED configuration. | `apply-style.sh`, appearance `user.py`/`system.py`, Dolphin `apply.py`, Konsole `apply.py` and lock adapter locate assets locally or through siblings. Do not move a theme away from its applicator without an explicit lookup plan. Runtime token consumption needs per-consumer equivalence/visual checks; this relocation task does not redesign values. Keep login/unlock and fonts/cursors usable in Recovery. |
| `integrations/` — keyboard sources implemented; other payloads PLANNED | `integrations/keyboard-cedilla/{apply.py,apply-brave.py,README.md}` now owns opt-in Compose/Brave configuration. KDE: integration `outputs/noctalia-test/{desktop-search.py,open-menu.sh,open-clipboard.sh,configure-super.py,configure-clipboard.py,codex-noctalia-*.desktop}`; Dolphin `launch.py`, FileManager1/defaults handling, `dolphin-blur-corners/{ui.cpp,ui.json,build-ui.py}`; package integration `app/`, `desktop/`, Debtap license; Konsole launcher/desktop adapter; shell language/region preference adapter; `notification-continuity/sync-wallpaper.py`; hardware `driver-aic8800/{PKGBUILD,dkms.conf,90-aic8800-usb.conf,build.sh}`. RICY-OWNED + upstream/derivative code. | KDE adapter owns KRunner D-Bus behavior, not compositor policy. Dolphin identity calls sibling `build-ui.py`, installs a Qt generic plugin and selects a wrapper shared with Recovery. Package UI/backend remains optional; privileged package conversion is separate from source installation. Hardware packaging stays optional with pins/patch series/licenses. Language/keyboard choices remain user-specific. No general integration framework is justified. |
| `services/` — three templates implemented; other extraction PLANNED | Three relocated `services/*.service.in` templates and existing unit/drop-in definitions generated by notification, localization, blur and Dolphin applicators. RICY-OWNED definitions. | Preserve installed IDs, environment, order, readiness, restart, `KillMode=process`, stop/return semantics. Unit packaging belongs here; startup/recovery logic and integration adapters retain their domain owners. Do not create a daemon/watchdog or move all unit helpers together merely because systemd calls them. |
| `recovery/plasma/` — PLANNED | `plasma-noctalia-switching/{ricy,integration.py,panels.py,verify.py,restore-installation.py}`; forwarding `start-test.sh`/`return-to-plasma.sh` in three output/autostart locations; `recover-at-login.sh` guard. Shared shortcut transfer inside `integration.py` also has an `integrations/kde/` responsibility. RICY-OWNED. | `ricy` starts a transient systemd worker and locks state; integration imports `panels` locally and reads sibling integration outputs. Keep panel merge/ID remapping, current snapshots, original seed and KRunner restoration. Splitting the shortcut portion or independent fallback needs a separate contract decision; moving the whole folder does not isolate Recovery. |
| `installer/` — PLANNED | Destination `prepare-destination.py`, `noctalia-autostart/install-autostart.py`, switching `install.py`, package `install-integration.py`/`restore-integration.py`, appearance `user.py`/`system.py`/`common.py`, lock apply/restore, Dolphin apply/restore, style applicator/restorer and version-specific `target-implementation-fixes/` tooling. Their public inputs remain owned by the relevant subsystem. RICY-OWNED + PATCHES. | Keep each installer paired with its restore interface, allowlist, local resources, original manifests and emitted backup path. Package restorer reads installer TARGETS via `runpy`; Konsole imports appearance `common.py`; fix manifest accepts only particular target hashes. No replay against active state. Root generators are HISTORICAL, not new default installers. `common.py` currently carries appearance-specific policy; sharing by two consumers does not justify promoting it to core. |
| `core/` — no justified candidate | Root `start.sh`, `return.sh`, `switch.sh` simply forward to switching; the worker/lock and panel logic belong to recovery. Appearance helper serves its existing install/restore family. | **INFERRED:** current reuse is domain-specific and does not establish common desktop logic. Keep wrappers at their entry-point locations; no core module, daemon, IPC or session manager is created. Reconsider only with concrete independent consumers and an approved contract. |

Some scripts mix payload creation, installation and runtime selection. The map
assigns their responsibilities without splitting functions into speculative new
modules. Planned extraction must first select a coherent batch and resource
lookup scheme; these classifications alone do not authorize that split.

## Paths and deployment edges that must survive

### Scripts, units and desktop entries — KNOWN

| Edge | Current path/identifier and consequence |
|---|---|
| Root and installed commands | `start.sh`, `return.sh`, `switch.sh` and `$HOME/.local/bin/{ricy,voltar-ao-noctalia,voltar-ao-plasma}` contain absolute paths to `plasma-noctalia-switching/ricy`. They are forwarding files, not symlinks. Ricy `ricy-{noctalia,plasma,alternar}.desktop` entries use that same command. A source move alone leaves these consumers behind. |
| Login integration | `ricy-noctalia-integracao.service` is active (exited)/enabled; ExecStart points at `noctalia-autostart/start-automatically.sh`. That script resolves the sibling integration output, waits for Plasma/KGlobalAccel, then calls `start-test.sh`; ERR invokes return through `RICY_RECUPERACAO_INTERNA`. Template filename is `ricy-noctalia-integration.service.in`; the installed legacy ID is intentional. |
| Shell and search | `noctalia-teste.service` runs `$HOME/.local/lib/ricy-noctalia/noctalia`; shell/search MainPIDs were 1305/1307 at inspection. `noctalia-busca-desktop.service` executes `/usr/bin/python` with the repository integration output `desktop-search.py`. Templates `noctalia-test.service.in`/`noctalia-desktop-search.service.in` use CONFIG/STATE/ADAPTER replacements; installed profile stays in contribution `work/noctalia-profile/{config,state}`. Search Requires/BindsTo/After shell; shell Wants search. |
| Shell overrides | Persistent `50-notificacoes-ricy.conf`, `60-ricy-idioma-localizacao.conf` and observed `90-preserve-launched-apps.conf` live under `noctalia-teste.service.d/`. Activator also writes runtime `99-ricy-preservar-aplicativos.conf` when needed. Preserve application-survival behavior and personal locale/time zone. |
| Menu, clipboard and login guard | `codex-noctalia-{menu,clipboard}.desktop` execute integration output `open-menu.sh`/`open-clipboard.sh`. `.config/autostart/codex-noctalia-recover.desktop` executes output `recover-at-login.sh`; retained return entry points at `return-to-plasma.sh`. KGlobalAccel may retain an old launcher object after desktop files change: see [FILE-RENAMES](FILE-RENAMES.md#refreshing-already-registered-launchers). An on-disk edit alone does not prove the registered action is refreshed. |
| Compatibility wrappers | Switching `install.py` writes start/return forwarders in integration `outputs/noctalia-test/`, `noctalia-autostart/`, and root-kit `outputs/noctalia-test/`. Current return is panel-only switching; historical transport/full-layout return scripts are different algorithms. Preserve all three anchors until their callers are separately handled. |
| Blur selector | `ricy-blur-continuidade.service` remains enabled/failed, with installed ExecStart `$HOME/.local/lib/ricy-blur/iniciar.py`. Current `blur-continuity/integrate.py` copies `start.py` and would generate an ExecStart for that name. **KNOWN divergence:** do not translate the installed old basename in documentation into a claim that the current recipe is deployed. Disposition and D-Bus repair remain UNKNOWN (G-03). |
| Dolphin | Source `apply.py` calls sibling `dolphin-blur-corners/build-ui.py`, copies `launch.py` to `$HOME/.local/bin/ricy-dolphin` and QSS/helper under `$HOME/.local/share/ricy-dolphin/`. `org.kde.dolphin.desktop`, FileManager1 D-Bus service and `plasma-dolphin.service.d/70-ricy-aparencia.conf` select the installed wrapper. Default Dolphin access is shared with Recovery. |
| Optional package workflow | `cachyos-local-package-installer.desktop` and KIO `cachyos-install-package.desktop` execute `$HOME/.local/share/cachyos-package-installer/installer.py`. `install-integration.py` copies app files/license and renders `@INSTALLER@`; `restore-integration.py` reads sibling installer TARGETS. Source translations lag/differ from installed strings (G-06); source relocation must not redeploy as an incidental side effect. |
| Konsole and appearance | Konsole `apply.py` imports sibling appearance `common.py`, copies profile/palette/launcher/desktop and updates `konsolerc`. Appearance `user.py` reads sibling KDE outlines and can build/install optional KWin extensions. Lock adaptation reads system Plasma QML and installed SDDM theme; system appearance changes SDDM/boot/global assets. Keep these dependencies explicit. |

These are inspected paths and registered consumers, not complete coverage of
external ad hoc shell commands, hidden launchers or other installations.

### Symlinks — KNOWN in the inspected scope

- `$HOME/.config/systemd/user/plasma-workspace.target.wants/ricy-noctalia-integracao.service`
  points to the existing user unit; graphical-session.target.wants links the blur
  selector. Preserve enabled-unit links and IDs even if templates move.
- Local Plasma shell `contents/{activitymanager,applet,configuration,explorer,views,...}`
  links to `/usr/share/plasma/shells/org.kde.plasma.desktop/contents/`; its metadata
  and customized lock-screen files are copies. Source: lock `apply.py`.
  These are intentional upstream dependencies, not kit relocations to rewrite.
- No asset-tree symlinks were found in the inspected active/transport baseline.
  Cursor alias basenames are materialized files in these kits; do not invent
  missing symlink edges from upstream naming conventions.
- No symlink or installed caller referencing `keyboard-cedilla` was found in the
  repository and inspected user unit/autostart/application/KIO/D-Bus/bin/lib
  entry-point scope. Unexamined external callers remain UNKNOWN.

### Patches and builds — KNOWN source contracts

| Build family | Source/build boundary and preservation requirement |
|---|---|
| Current Noctalia | Reordering pins 5.2.1/`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`, takes a complete cumulative patch and supports `RICY_NOCTALIA_SOURCE`; default cache `ricy-noctalia-src-5.2.1`, Meson/Ninja output `build-ricy/noctalia`. Keep exact diff guards, C++/QJSEngine validators, license and activator call path. Never stack historical cumulative patches. Current source is not deployed; retain old binary/cache provenance. |
| KWin native plugins | Blur pins 6.7.5/`ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`, uses `ricy-kwin-src-6.7.5` and `ricy-blur-build-6.7.5/ricyblur.so`. Dolphin corners checks installed KWin headers and uses `ricy-dolphin-corners-build-6.7.5/ricydolphinrounding.so`. Keep header/API gates, metadata, licenses, compiler inputs and native-blur fallback. No rebuild/reload in this task. |
| Dolphin Qt helper | `build-ui.py` copies `ui.cpp`/`ui.json`, uses Qt 6 moc/C++, outputs `ricy-dolphin-ui-build/libricydolphinui.so`; identity installer replaces it atomically under `plugins/generic/`. Keep separate from KWin corners. Exact installed helper provenance remains UNKNOWN. |
| Scripted/optional effects | Window-fade-expand copies a JS effect, no native build. Appearance optionally runs the windowsarrows native build; its three extensions have different current classes. Keep packaged sources/licenses and per-extension selection rather than treating the asset bundle as one current runtime. |
| Hardware/package patches | AIC8800 PKGBUILD pins Radxa `d13d07963cd15d731e2895e8288a04cca6152ac9`, replays upstream Debian patch series and packages DKMS/firmware/modprobe files. Target fixes retain two-hash manifests and `configure-super.py.patch`/`debtap-changes.patch`; they cannot be replayed on later integration revisions (G-10). Keep checksums and matching inputs, no package build/install. |

### Rollback and transport kit

All following paths are existing private compatibility state, never inputs for
public packaging. Use the actual backup emitted by an applicator, not a guessed
new path. Bases below default to `$HOME/.local/state` unless stated otherwise.

| Owner | Existing rollback dependency |
|---|---|
| Switching/Recovery | `${XDG_STATE_HOME:-$HOME/.local/state}/ricy-alternancia/` current `paineis.json`/`atalhos.json`, command lock and installation backups; original integration output `plasma-antes.tar.gz` seed. `restore-installation.py` preserves the install manifest contract. Do not substitute historical full-layout restoration. |
| Shell activation and language | `ricy-notificacoes-backups` manifest/binary/drop-in restored by `enable.py --restaurar`; upstream `/usr/bin/noctalia` remains installed. `ricy-idioma-localizacao-backups` retains profile/settings/drop-in originals; wallpaper/settings reversal is distinct from binary rollback. |
| KDE style and window effects | Contribution `outputs/kde-outlines/` captured style/blur/theme state and restore helper; `ricy-fade-expand-backups`, `ricy-blur-backups`, `ricy-dolphin-corners-backups` with their original settings/plugin manifests. Preserve legacy restore flags. |
| Dolphin/package integration | `ricy-dolphin-backups` used by identity `apply.py --restaurar`; `cachyos-package-installer-backups` used by package `restore-integration.py`. MIME defaults, FileManager1 and launcher selections must restore together. |
| Appearance, lock, terminal, input | `ricy-appearance-backups`, system `/var/lib/ricy-appearance-backups`, `ricy-lockscreen-backups`, `ricy-konsole-backups`, `${XDG_STATE_HOME:-$HOME/.local/state}/ricy-teclado-backups`; keep absence markers and original manifests/permissions. |
| Autostart | `ricy-inicio-automatico-backups` stores replaced units/output scripts. Preserve ordering and installed names; relocation is not permission to reinstall/restart. |

`docs/ricy-kit/` retains 24 historical contribution snapshots at their original
locations, including keyboard-cedilla. `archives/ricy.zip`, both SHA256SUMS and
historical path labels remain untouched. No automatic mirror, new archive or
compatibility shim was introduced. Publication readiness remains UNKNOWN.
Future installer packaging requires an explicit public-file allowlist, portable
resource paths, source/license selection and exclusion of profiles, accounts,
clipboard, backups and destination IDs. The active kit is not that allowlist.

## First source migration — keyboard-cedilla

**Implemented, within this task's authorization for one small low-risk move.**
The three-file directory moved from
`ricy-kit/contributions/keyboard-cedilla/` to
[integrations/keyboard-cedilla](../integrations/keyboard-cedilla/README.md).
The two Python scripts retain their exact bytes and modes; only README commands
and maintained references change. They use `Path.home()`/XDG user directories,
no `__file__` resources, sibling imports, installer caller, unit, desktop entry,
symlink or build. Installed Compose/Brave settings are data consumers independent
of source location. No new abstraction or temporary compatibility is needed.

Current source syntax remains covered by `verify shell` through an explicit
selection of the two relocated files. Foundation regressions check selection
and failure propagation. No recursive scan of private integration state or new
component discovery mechanism was added. Existing user-specific options and
private backup identifiers remain intact; this does not make the keyboard or
Brave configuration a global Ricy default.

**Compatibility limit:** old manual commands for the active source must use the
new README. Historical REINSTALL commands still address the transport snapshot;
a scoped note directs maintained-repository users to the current README. Unknown
external commands outside the examined entry-point scope cannot be certified.
No fallback link was added solely for hypothetical callers.

**Rollback of this source move:** move the three files back to the original
contribution directory and revert this task's reference/source-selection changes
using the Git diff; leave the transport tree and installed preferences alone.
The pre-move Git version preserves script bytes. Configuration rollback remains
the README's original backup/absence-marker procedure; source rollback does not
require changing `.XCompose`, browser flags, units or the running session.

## Migration batches — scoped implementation and future proposals

| Batch | Proposed scope | Entry/exit evidence and rollback |
|---|---|---|
| M-01 — complete | Keyboard three-file source relocation only. | No location-dependent caller; exact script bytes/modes, retained syntax coverage and installed-state preservation. Source move is reversible without runtime work. |
| M-02 — complete, option A approved | Three autostart `.service.in` templates moved into `services/`; existing installer resolves them from its repository root. Runtime scripts/output/profile paths remain anchored. | Exact template bytes/modes and rendering equality confirmed for three IDs, special-character paths, unrelated working directory and symlink alias. Missing-template harness checks added. No installation or daemon-reload. Roll back template placement and installer reads together. See ADR-0006. |
| M-03 — proposal | Selected `window-fade-expand` source/assets/license/validator as a coherent KWin package; activation remains separate. | Map applicator resource lookup and validator/verify callers before moving. Byte/metadata equivalence and 28 offline effect scenarios are needed; real visual/Recovery evidence before any activation. Roll back source paths and harness references; preserve installed effect/settings. Do not include UNKNOWN blur or historical squash assets. |
| M-04 — gated | Current Noctalia patch/build/validators/license, followed separately by shared activator/resource relocation. | Decide source input explicitly (G-02), validate an isolated pinned checkout, preserve all later-variant activation references and binary rollback. Separate build from deployment. No cached-source replacement or shell restart as a path test. |
| M-05 — gated | KDE search/menu adapter, theme/Qt helper inputs and installer families, one coherent dependency cluster at a time. | Approve resource lookup/installed-anchor handling; map D-Bus, MIME, KGlobalAccel retained launchers and sibling imports. Establish helper provenance. Run render/build/component checks without installation, then separately authorized integration/Recovery trials. Never move the private profile with the public seeds. |
| M-06 — gated | Recovery source/forwarders and installer transport composition. | Inventory all three compatibility wrapper anchors and state readers; approve any compatibility lifetime/removal and public allowlist. Offline panels/shortcuts do not prove login/failure recovery. Independent sessions and new Core remain separate architectural decisions. |

### Resource lookup decision — option A approved for M-02

**Accepted and implemented:** user approval “Siga” on 2026-10-11 authorizes
option A for the three-template batch, recorded in
[ADR-0006](adr/0006-service-template-source-lookup.md). Options below preserve
the assessed tradeoffs. Later batches require their own dependency review; this
decision is not a shared resolver contract or blanket relocation approval.

**Problem:** approved destination directories do not specify how existing
installers locate resources once a mixed contribution is split. Autostart reads
templates from its own directory; Dolphin calls a sibling builder; Konsole
imports sibling appearance `common.py`. Moving these blindly breaks preparation
or installed entry points.

**Options:** A. explicit local resource paths in each affected installer, migrated
one batch at a time with exact rendering equivalence and installed runtime anchors
unchanged; B. temporary legacy forwarders/symlinks with a declared compatibility
lifetime; C. shared Core resource resolver/install framework.

**Recommended:** A for M-02: relocate only
`noctalia-test.service.in`, `noctalia-desktop-search.service.in`, and
`ricy-noctalia-integration.service.in` to `services/`. Resolve that source directory
from the existing installer's repository location, while retaining its current
startup/adapter/profile replacements and the three installed legacy IDs. Do not
introduce a Core resolver. Future installed runtime relocation needs its own
consumer/rollback plan; A does not approve it implicitly.

**Impact:** new installer-to-services source dependency and template lookup
contract; no intended login/session behavior change. Offline equality proves
rendering, not installation or recovery. B adds a compatibility maintenance
contract; C invents a common abstraction without demonstrated independent need.
Option A is implemented for M-02 only. The installer now depends on the
repository `services/` directory; copying only `ricy-kit/` or the contribution
will not provide its templates. Template lookup is independent of the current
working directory and has no transport fallback or legacy forwarding link.
Before/after rendering was compared using only the installer's read/render AST
statements in disposable paths; no installation body or systemd command ran.
Installed unit states, PIDs and ExecStart values were compared read-only.

Rollback of M-02 restores the three templates beside `install-autostart.py`,
restores its old template read, and reverts this batch's required-template checks
and documentation together. Keep the completed M-01 keyboard migration intact.
Runtime/source caches, private state and transport history need no rollback.
Other coupled extractions and new contracts remain unimplemented proposals.
