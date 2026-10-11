# Current contribution grounding

Audit date: 2026-10-11 (America/Sao_Paulo). This is the maintained classification
of existing contributions, their consumers, and their variants. The short
ownership/destination map is [COMPONENTS](COMPONENTS.md). Architecture and recovery
contracts remain in [ARCHITECTURE](ARCHITECTURE.md), [INVARIANTS](INVARIANTS.md),
and [RECOVERY](RECOVERY.md). The original grounding audit changed documentation
only; the [first cleanup](#first-safe-cleanup) below records subsequent build and
development safeguards without changing the observed runtime classification.

## Classification and evidence

Subsequent source migration (2026-10-11): the keyboard contribution now lives in
[integrations/keyboard-cedilla](../integrations/keyboard-cedilla/README.md). The
active-kit tree now contains 23 contribution directories; all 24 logical
contributions and all 24 transport snapshots remain accounted for. See the
[migration record](MIGRATION-PLAN.md#first-source-migration--keyboard-cedilla).
Subsequent M-02 migration: three autostart source templates now reside in
`services/`; the existing installer reads them through the approved
[ADR-0006](adr/0006-service-template-source-lookup.md) lookup. Installed units,
runtime scripts and transport snapshots retain their original paths.
Original observations below retain their original scope/date.

Subsequent window-identity correction (2026-10-11): the maintained
[reordering source](../ricy-kit/contributions/app-icon-reordering/README.md)
now marks KWin UUIDs as exact identities. The current cumulative RICY-001/UUID
revision was built in an isolated checkout and activated with the existing
application-preserving activator. The running executable matches that build;
its KWin tracking adapter and status IPC are available. This supersedes only
G-02's earlier-binary observation and the reordering source's pending-activation
classification: the corrected source/build is ACTIVE. The original cache and
previous binary backup remain rollback/provenance material. Other runtime
observations below are unchanged. The user reported successful real-session
icon focus after activation; agent-operated clicks/captures and live Recovery
remain NOT RUN. See [CHANGELOG](CHANGELOG.md) for validation and limits.

Subsequent token task (2026-10-11): [ADR-0005](adr/0005-consumable-visual-tokens.md)
promotes the existing identity to a consumable source in
[themes/tokens](../themes/tokens/README.md) and migrates the offline identity
board with identical bytes. The tables below retain the pre-centralization
grounding; their token-location/reservation descriptions are superseded only by
that scoped promotion. Runtime observations and other classifications remain
unchanged. See the [visual source audit](../themes/tokens/AUDIT.md).

| Class | Meaning in this audit |
|---|---|
| ACTIVE | Used by the current installation through a running process, registered entry point, selected configuration/asset, or maintained development reference. The consumer type is explicit; a reference is not runtime code. |
| RECOVERY | Required by the existing return/rollback path or the Plasma/Dolphin recovery contract, including when also called during normal startup. |
| MIGRATE | Valid retained functionality or preparation tooling with a previously documented target destination, but not the implementation selected by the current runtime. This is not authorization to migrate or activate it. |
| HISTORICAL | A superseded variant, reproduction snapshot, or earlier implementation retained for provenance and comparison. Its functionality may survive in an ACTIVE cumulative implementation. |
| REMOVE | Proven to have no current consumer, recovery purpose, or necessary historical value. No contribution meets this threshold in this audit. |
| UNKNOWN | Evidence cannot establish one of the above classes. Preserve and investigate; do not interpret this as REMOVE. |

Each directory has a primary class; explicitly listed parts override that class.
This is necessary for folders that contain both historical builds and current
activators. ACTIVE and RECOVERY describe the observed installation, while future
destinations are PLANNED according to the existing migration map. They do not
prove portability, correct interaction, authentication, or crash recovery.

KNOWN below means a file/reference or read-only observation supports the claim.
INFERRED identifies a conclusion from that evidence. UNKNOWN is used for missing
proof. Historical README test results were not rerun merely by reading them.

Original grounding scope: all **24** directories under `ricy-kit/contributions/`, all corresponding
directories in `docs/ricy-kit/contributions/`, both kits' root scripts/outputs,
the archive, private generated material (including three materialized community
plugins), root entry points, the agent harness, and reserved target directories.
Files are grouped by their actual consumer;
assets, licenses, validators, and restorers stay with their owning contribution.
Private profile/backup contents are not reproduced here. No files were moved or
removed, no installer/activator ran, and no service/session was restarted.

## Observed installation and conflicts

Read-only observations on this installation, not claims about every Ricy host:

| ID | KNOWN evidence | Implication / remaining limit |
|---|---|---|
| G-01 | `systemctl --user show` reports `noctalia-teste.service` and `noctalia-busca-desktop.service` running, `ricy-noctalia-integracao.service` enabled/active (exited), and `plasma-plasmashell.service` running. Integration ExecStart names `noctalia-autostart/start-automatically.sh`; adapter ExecStart names the contribution's `outputs/noctalia-test/desktop-search.py`. The D-Bus owner PID for `org.kde.krunner` matches the adapter MainPID. | The contribution output tree is the selected runtime integration. The legacy word `teste` in identifiers does not make these units historical. Panels, interactive search, and recovery after failure were not tested. |
| G-02 | The running Noctalia process uses `$HOME/.local/lib/ricy-noctalia/noctalia`. Its bytes match the preserved cache's `build-ricy/noctalia`. That cache is at pinned commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`; `git diff --binary HEAD` matches the **transport** `app-icon-reordering/noctalia-ricy.patch`, but differs from the active-tree patch updated for RICY-001. | The deployed cumulative variant is the earlier reordering implementation. The current source policy is MIGRATE pending activation; live single-space compliance is UNKNOWN. Byte equality connects artifacts, but is not a fresh reproducible-build attestation. The transport tree itself is not being executed. |
| G-03 | KWin's `loadedEffects` includes `blur`, `ricywindowactions`, `scale`, `smoothwindowgeometry`, and `ricydolphinrounding`, but not `ricyblur`. `ricy-blur-continuidade.service` is enabled and **failed**. Its current-boot journal records failure calling `org.kde.kwin.Effects.isEffectLoaded` on `/Effects`. | Native blur is the observed implementation. `blur-continuity` cannot be classified ACTIVE or confidently HISTORICAL: a registered consumer still attempts to run it. Whether it should be repaired, migrated, or retired is UNKNOWN. No repair or effect reload occurred. |
| G-04 | Installed `ricywindowactions` JS and metadata equal `window-fade-expand/assets/`; `Effect-scale` has Duration=320 and InScale/OutScale=0.85. | This is the selected window-animation variant. The squash-style package in the icon contributions is historical, although their shell motion remains in the cumulative Noctalia variant. |
| G-05 | KDE selects Kvantum/KDE-Noctalia; installed menu SVG equals the integration asset. Dolphin MIME default, FileManager1 service, and `plasma-dolphin.service` drop-in select the Ricy Dolphin launcher; Kvantum assigns Ricy-Dolphin to Dolphin. Installed QSS equals the current source after excluding comments; launcher differs only in its docstring. No Dolphin process was present in the process inventory. | Dolphin identity is selected, but interactive usability and the exact provenance of the installed compiled Qt helper are UNKNOWN. Registration is not a running-window test. |
| G-06 | DEB/RPM MIME defaults select `cachyos-local-package-installer.desktop`; its app files are installed. Debtap is byte-identical to the contribution copy. The three Python files differ in translated messages; manual diffs and AST comparison with string contents excluded preserve the structure. | Package integration is registered and retained. The installed UI strings lag the repository's en-US source. No package was converted/installed, and structural comparison does not certify all behavior. |
| G-07 | Konsole selects PlasmaBlur.profile and installed profile/palette equal the contribution assets. Ricy's XCompose block and Brave's X11 flag exist. SDDM selects mocha-limine/Bibata; Plasma selects mocha-blur and a local lock-screen QML exists. The Noctalia unit selects the contribution's private profile, LC_TIME=en_US.UTF-8, and TZ=America/Sao_Paulo; profile shell language is `en` and wallpaper drawing is disabled. | These are selected configurations/assets. Cursor animation, compose input, browser rendering, login, unlock, weather, and calendar interactions were not exercised. Full palette equivalence is UNKNOWN: the expected public palette basename was not found in the private profile. |
| G-08 | `windowsarrows` is enabled and `isScriptLoaded` returns true. `smoothwindowgeometry` is loaded. `adaptivepanelwidth` is installed but disabled and `isScriptLoaded` returns false; the reinstallation guide explicitly disables it after the optional extension step. | Treat the three bundled extensions separately. The appearance installer still enables all three with its optional flag; that recipe is not an exact replay of the current installation. |
| G-09 | `aic8800-usb-dkms-ricy` is installed; `aic_load_fw`, `aic8800_fdrv`, and `aic_btusb` appear in `/proc/modules`. DKMS reports installed builds for the two documented kernels. | Hardware support is active on this machine. Network connection, Bluetooth pairing, and the other kernel's boot behavior were not tested. |
| G-10 | The correction manifest's Debtap target equals its replacement digest. The integration's `configure-super.py` equals neither manifest digest; later autostart/switching changes use their own shortcut logic. | Do not replay `apply-fixes.py` against the current kit: its guard rejects later revisions. Preserve the manifest as a versioned prerequisite for a matching earlier destination, not a current runtime manifest. |
| G-11 | Three community plugin implementations are materialized in the private profile. `noctalia msg plugins list` reports NoctaProton VPN, Proton Pass, and YouTube Music enabled. Their TOML manifests declare service/widget/launcher entry points and dependencies. Several required CLI executables were not found in the task's PATH. | Registration is KNOWN; actual runtime consumers, successful execution and usable functionality remain UNKNOWN. Classify each plugin individually below. The other registry entries are catalog offerings, not materialized Ricy components. No account, cookie, credential, or plugin-setting contents were exported. |

The diagnostic `./scripts/doctor` returned exit 2 with its two expected UNKNOWN
categories (live recovery and full RICY-001 compliance). It does not certify the
desktop, and its unit list does not include the failed blur unit; G-03 comes from
separate unit/effect/journal queries.

## Contributions in the active kit

Links in this table point to the **active-tree** README. Consumers outside the
repository are described relative to `$HOME` to avoid copying private state.
Destinations preserve the existing [migration plan](MIGRATION-PLAN.md).

| Contribution / primary class | Consumers and evidence | Dependencies and relationships | Variant and future destination | Recovery impact |
|---|---|---|---|---|
| [noctalia-kde-integration-and-menus](../ricy-kit/contributions/noctalia-kde-integration-and-menus/README.md) — **ACTIVE** | Search unit executes its `desktop-search.py`; switching calls output wrappers and installs menu/clipboard entries. Selected Qt menu assets: G-01/G-05. | Noctalia CLI/IPC, Python/PyGObject, D-Bus/KGlobalAccel, Plasma, Qt/Kvantum; consumed by autostart, switching, appearance, and Dolphin identity. | Runtime output/profile owner, not another shell patch. Preparation tools: MIGRATE. PLANNED `integrations/kde/`, `services/`, `themes/`. | High: adapter occupies KRunner's name, shortcuts/panels are shared. Keep restorers and original backup seed. |
| [noctalia-autostart](../ricy-kit/contributions/noctalia-autostart/README.md) — **ACTIVE** | Enabled integration unit executes `start-automatically.sh`; installed shell/search units derive from its templates (G-01). | user systemd, Plasma/KGlobalAccel readiness, integration output wrappers, switching. Shell restart policy, adapter binding, and KillMode preserve current lifecycle. | Replaces manual-only startup. Source wrappers have been forwarded to switching; installer must precede switching on a fresh destination. PLANNED `services/` + `installer/`. | High: protected startup calls return on error; login preference and fallback share units. `recover-at-login.sh` is RECOVERY, not an independent watchdog. |
| [plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md) — **RECOVERY** | Root/installed command wrappers and integration start/return wrappers call `ricy`/`integration.py`; `panels.py` is imported. Panel/shortcut snapshots exist. | systemd-run, flock, Python/PyGObject, qdbus6, KGlobalAccel, plasmashell, integration outputs, autostart. | Current panel-only snapshot/merge replaces full old-layout restoration. PLANNED `recovery/plasma/` + `integrations/kde/`. | Critical: preserves wallpaper/widgets and remaps colliding IDs; shell/adapter stop and KRunner return remain coupled. `restore-installation.py` restores older behavior and is not normal shell return. |
| [notification-continuity](../ricy-kit/contributions/notification-continuity/README.md) — **ACTIVE, split** | `enable.py` is the activator/restorer explicitly called by all later shell variants; deployed binary/drop-in exist (G-02). Notification/Home behavior is carried by the cumulative shell. | Pinned Noctalia 5.2.1, Meson/Ninja/C++, shell/search units and profile; optional `sync-wallpaper.py` reads Plasma's static image. | `build.sh` + notification-only patch are **HISTORICAL**; retained activator is ACTIVE and its restoration branch RECOVERY. Wallpaper sync is retained preparation (**MIGRATE**), not a running watcher. PLANNED `shell/noctalia/`; integration helper boundary remains as documented. | Keep upstream `/usr/bin/noctalia`, binary/drop-in backups, application-preserving restart, and separate wallpaper/settings rollback. |
| [taskbar-menu-composition](../ricy-kit/contributions/taskbar-menu-composition/README.md) — **HISTORICAL** | Current shell inherits app-menu composition; no installed service builds/runs this directory. Later cumulative patch replaces its build input. | Noctalia + notification/Home changes; activated through notification helper. | First cumulative successor to notifications. Functionality remains in reordering; do not stack patches. PLANNED surviving behavior: `shell/noctalia/`. | Old build activation would regress newer interactions/policy; keep reproduction/license/reversal evidence. |
| [tray-menu-composition](../ricy-kit/contributions/tray-menu-composition/README.md) — **HISTORICAL** | Current cumulative shell contains the tray menu and drawer-return changes; old builder is not selected. | Noctalia DBusMenu and previous menu composition; notification activator. | Full cumulative successor to taskbar menus. Surviving behavior: PLANNED `shell/noctalia/`. | Tray actions belong to apps; preserve behavior and rollback rather than applying an old full variant. |
| [app-icon-interactions](../ricy-kit/contributions/app-icon-interactions/README.md) — **HISTORICAL** | Hover/icon scaling survives in current cumulative source; directory's old builder is not selected. | Noctalia Style/AnimationManager and tray/menu variants. | Full cumulative successor adding hover; PLANNED surviving behavior `shell/noctalia/`. | Applying old patch loses later actions/order; stable hit areas remain relevant. |
| [taskbar-app-actions](../ricy-kit/contributions/taskbar-app-actions/README.md) — **HISTORICAL** | Current shell's KDE adapter carries UUID restore/minimize/close; current action validator is retained in reordering. | Noctalia compositor adapter and KWin window/script APIs; earlier interactions. | Full cumulative successor; historical tests/build here, surviving behavior PLANNED `shell/noctalia/` + `integrations/kde/`. | Middle-click/close must respect save dialogs and exact UUID; never close user work to audit. |
| [app-indicator-animations](../ricy-kit/contributions/app-indicator-animations/README.md) — **HISTORICAL** | Indicator/minimized-state serialization survives in reordering; installed window effect is G-04's later variant. | Noctalia motion + KWin; notification activator; KDE-derived effect. | Cumulative shell variant plus earlier squash-style `ricywindowactions`. Both build/effect files are superseded; surviving shell behavior PLANNED `shell/noctalia/`. | Old effect installer replaces the same package/config keys as the current effect; preserve historical backups/licenses. |
| [app-icon-states](../ricy-kit/contributions/app-icon-states/README.md) — **HISTORICAL** | Icon state motion survives in reordering; reordering fixes the slot background and adds persistent drag. | Native Noctalia MotionService/AnimationManager, indicator/actions, previous KWin effect. | Full cumulative shell successor; bundled window package is still the earlier variant. PLANNED surviving shell behavior `shell/noctalia/`. | Do not replace current shell/effect with this intermediate implementation. |
| [app-icon-reordering](../ricy-kit/contributions/app-icon-reordering/README.md) — **ACTIVE, split** | Earlier reordering binary is running (G-02). Current directory owns reference build/validators; its updated patch is not the running source diff. | Pinned Noctalia 5.2.1/commit, Meson/Ninja/C++, KWin adapter; notification activator, window-fade-expand for current effects. | Earlier deployed cumulative functionality ACTIVE; current RICY-001 patch/build is **MIGRATE** pending activation. Its `apply-animations.py`/window assets are **HISTORICAL**. PLANNED `shell/noctalia/`. | Exact source-diff guard rejects the preserved old cache. Keep binary/cache rollback; build does not activate. Do not infer single-space runtime compliance from source. |
| [window-fade-expand](../ricy-kit/contributions/window-fade-expand/README.md) — **ACTIVE** | Installed JS/metadata match; `ricywindowactions`/Scale loaded and scale settings match (G-04). | KWin scripted effects/config, qdbus6/kwriteconfig6; PyQt6 only for offline validator. Shell reordering is complementary. | Current effect-package replacement; does not replace/rebuild shell. PLANNED `compositor/kwin/`. | Shared with Plasma. Preserve effect/key backups; no compositor restart is needed by its applicator. Interaction/visual validation NOT RUN here. |
| [blur-continuity](../ricy-kit/contributions/blur-continuity/README.md) — **UNKNOWN** | Registered selector unit failed; ricyblur absent and native blur loaded (G-03). | Pinned KWin 6.7.5/headers/Qt/KF6/C++, D-Bus Effects API, installed plugin/helper; shell panel/notification geometry. | Separate upstream-derived plugin, not a cumulative Noctalia patch. Previously mapped PLANNED `compositor/kwin/`, but repair/retirement and functional validity now UNKNOWN. | ABI/API-sensitive and shared with Plasma/Dolphin. Native fallback is observed; automatic failure handling is not proven by this failed unit. Keep plugin/helper/backup; no removal recommendation. |
| [dolphin-noctalia-identity](../ricy-kit/contributions/dolphin-noctalia-identity/README.md) — **ACTIVE** | Dolphin default/launcher, FileManager1, service drop-in and per-app Kvantum theme selected (G-05). | Dolphin/KIO, Kvantum KDE-Noctalia, QSS; calls sibling `build-ui.py` to install ricydolphinui atomically. | Current source incorporates successive Dolphin adjustments; earlier README appearances are HISTORICAL stages, not alternatives to apply. PLANNED `integrations/kde/` + `themes/`. | High: this is the current file-manager path, also needed for fallback. Dolphin is the chosen base under ADR-0011; keep launcher/theme restore and `/usr/bin/dolphin`. |
| [dolphin-blur-corners](../ricy-kit/contributions/dolphin-blur-corners/README.md) — **ACTIVE, split** | Identity launcher requests Qt helper; ricydolphinrounding is loaded/enabled (G-03/G-05). Exact installed Qt binary/source equivalence UNKNOWN. | Qt Widgets/Kvantum for `ui.cpp`; KWin 6.7.5 ABI/headers for independent `corners.cpp`; identity applicator. | Two complementary components, not two versions of one plugin. Latest source uses native delegate, atomic install, opaque L/main panels; earlier chip/panel experiments HISTORICAL. PLANNED `integrations/kde/` + `compositor/kwin/`. | High: Qt helper can affect Dolphin stability; native KWin corners are optional decoration, not required for file access. No Dolphin process/window was tested. |
| [dolphin-deb-rpm-installer](../ricy-kit/contributions/dolphin-deb-rpm-installer/README.md) — **ACTIVE** | Three package MIME defaults and desktop/service-menu entries select installed local app (G-06). | Python/PyQt6, debtap/indexes, dpkg/rpm conversion tools, bsdtar/binutils/fakeroot/pkgfile, pkexec/pacman, KDE caches; correction bundle supplies Debtap. | Standalone app/desktop integration, not Dolphin core or an own file manager. Repository translations are not all deployed. PLANNED `integrations/kde/` + `installer/`. | Optional package workflow; ordinary file access must not depend on conversion. Preserve MIME backups; no conversion/installation in this audit. |
| [target-implementation-fixes](../ricy-kit/contributions/target-implementation-fixes/README.md) — **MIGRATE, split** | Matching-destination preparers/reinstallation guide consume the guarded correction bundle; corrected Debtap is already consumed through package installer. Current Super target no longer matches manifest (G-10). | SHA-256 manifest, integration's earlier configure-super, sibling Debtap and index downloads. | Versioned preparation bridge, not a universal current-kit repair. Debtap behavior ACTIVE through sibling; `update-indexes.sh` retained maintenance, not daemon. PLANNED `installer/`. | Blind replay can overwrite shortcuts or fail its guards. Never regenerate historic hashes to legitimize later revisions. |
| [login-lock-cursor-appearance](../ricy-kit/contributions/login-lock-cursor-appearance/README.md) — **ACTIVE, split** | SDDM/mocha-limine, Plasma/mocha-blur, Bibata, Qt/KDE appearance selected (G-05/G-07); lock applicator consumes installed login theme. | SDDM/Breeze/Qt, Plasma, fonts/fontconfig, GTK themes, Kvantum integration assets; common.py used by its applicators and Konsole. | Asset/config export with MIGRATE destination applicators. Optional KWin subcomponents classified below; public wallpaper setter is MIGRATE opt-in tooling. PLANNED `themes/` + `integrations/kde/`. | Critical login/lock/shared appearance surface. Preserve system/user backups, KDE native authentication, theme/font licenses; do not restart SDDM to audit. |
| [login-matched-lock-screen](../ricy-kit/contributions/login-matched-lock-screen/README.md) — **ACTIVE** | Local lock-screen QML exists; login theme supplies its appearance (G-07). Actual next-lock selection/authentication UNKNOWN. | Installed Plasma/Breeze lock QML and SDDM theme, sibling appearance; generated local shell symlinks preserve other upstream parts. | Native lock adaptation with Qt.callLater authentication-start correction; earlier immediate-true attempt HISTORICAL. PLANNED `themes/` + `integrations/kde/`. | Critical: retain native authentication and restore.py. Presence is not proof that unlocking works. |
| [konsole-animated-cursor](../ricy-kit/contributions/konsole-animated-cursor/README.md) — **ACTIVE** | Selected PlasmaBlur profile/palette are byte-identical to assets; Konsole process present (G-07). | Konsole animation property, Kvantum, JetBrainsMono, compositor blur; imports appearance/common.py. | Terminal text cursor is distinct from Bibata pointer; not a shell patch. PLANNED `themes/` + `integrations/kde/`. | Diagnostic terminal must remain usable; apply/restore preserves packages and unrelated keys. Animation itself NOT RUN. |
| [keyboard-cedilla](../integrations/keyboard-cedilla/README.md) — **ACTIVE** | XCompose Ricy block and Brave X11 preference present (G-07). | Existing us(alt-intl)/Compose handling, optional Brave package wrapper/XWayland. | Two complementary app paths, not replacement keyboard layouts. Sources now reside in `integrations/keyboard-cedilla/`; installed preferences and transport snapshot are unchanged. User-specific opt-in, not a global product default. | Preserve input/preferences and backups. Does not configure virtual consoles or SDDM account; actual typing NOT RUN. |
| [noctalia-language-and-localization](../ricy-kit/contributions/noctalia-language-and-localization/README.md) — **ACTIVE** | Selected unit has its date/time environment and profile language (G-07). | Noctalia private settings/TOML, locale, unit drop-in; imports notification helper for safe restart; weather network service only for weather. | Preferences/template + applicator; no system-wide region migration. PLANNED `shell/noctalia/` + `integrations/`. | Preserve keyboard/region/accounts, settings backup and application-preserving restart. Weather/event retrieval NOT RUN; location is a per-installation choice. |
| [noctalia-visual-identity](../ricy-kit/contributions/noctalia-visual-identity/README.md) — **ACTIVE reference** | DESIGN-SYSTEM, themes/tokens README and agents consume tokens.json/reference.svg/guide. No runtime token-loader/generator found. | Existing shell Style/TOML/palettes, Qt/Kvantum/Dolphin adaptations and animation references. | Maintained identity authority; SVG is a schematic, not a screenshot. Central runtime token consumption is PLANNED `themes/tokens/`. Older Dolphin/blur appendix is historical evidence. | Shared identity can affect recovery tools; preserve upstream licenses and distinguish source values from installed appearance. |
| [driver-aic8800](../ricy-kit/contributions/driver-aic8800/README.md) — **ACTIVE on this hardware** | Package, loaded modules and DKMS registrations confirmed (G-09). | Kernel/headers, DKMS/compiler, pinned Radxa USB source/firmware, BlueZ; optional hardware integration independent of shell/menus. | PKGBUILD/build/modprobe support, not a generic desktop dependency. PLANNED `integrations/hardware/`. | Removing it can lose network/Bluetooth on this host. Preserve firmware/source pins and diagnostics; no connectivity/other-kernel boot claim. |

## Subcomponents and shared/generated material

These entries prevent a directory's primary label from hiding a different role.

| Item / class | Consumer, dependencies, and relation | Future destination / recovery limit |
|---|---|---|
| Appearance `assets/kwin/scripts/windowsarrows` — **ACTIVE** | KWin reports script loaded (G-08); optional user.py recipe compiles its native module and assigns Super+arrows. Shares global shortcuts with Plasma. | PLANNED `compositor/kwin/` + KDE shortcut integration. Preserve version/ABI and native shortcut backup; no shortcut interaction test. |
| Appearance `assets/kwin/effects/smoothwindowgeometry` — **ACTIVE** | Installed effect is loaded (G-03/G-08); complementary to window-fade-expand, not its predecessor. | PLANNED `compositor/kwin/`. Shared Plasma geometry behavior; no motion test. |
| Appearance `assets/kwin/scripts/adaptivepanelwidth` — **HISTORICAL** | Installed but disabled/unloaded; recipe can still install/enable it, while REINSTALL disables it (G-08). Earlier Plasma-panel customization; no current consumer established. | Historical variant for the present installation; whether to reuse it in future Plasma Recovery is UNKNOWN. Preserve source/license; do not call it active or remove it. |
| Contribution `outputs/noctalia-test/desktop-search.py`, open-menu/open-clipboard, desktop entries — **ACTIVE** | Unit/D-Bus ownership and switching-installed entries select these paths (G-01). Adapter controls search/support on the active monitor, not an independent compositor. | PLANNED `integrations/kde/` + `services/`; keep KRunner restoration and shortcuts. |
| Contribution `outputs/noctalia-test/start-test.sh`, return-to-plasma, recover-at-login — **RECOVERY** | Current start/return wrappers forward to switching; integration invokes them. Login guard avoids restoring Plasma while autostart is enabled. | PLANNED `recovery/plasma/`/integration. Historical filenames are compatibility identifiers, not proof of old logic. |
| Contribution `configure-super.py`/`configure-clipboard.py` — **MIGRATE** preparation / **RECOVERY** retained restore interfaces | Read by preparation/earlier integration recipes; current integration.py captures/transfers/restores shortcuts itself. configure-super has later revisions outside the two-hash fix manifest. | Preserve compatibility/backup handling in `integrations/kde/`/`installer/`; no new general shortcut framework approved. |
| Contribution `config.toml`, KDE-Current.json and KDE-Noctalia assets — **ACTIVE** assets / **MIGRATE** seed tooling | Preparers/style/appearance/Dolphin installers consume these files; active unit uses private work profile, not public config directly. Theme menu SVG match confirmed; full private profile/palette equivalence UNKNOWN. | PLANNED `shell/noctalia/` + `themes/`/`installer/`. Seeds are not live preference authority; preserve personal overrides. |
| Root [start.sh](../start.sh), [switch.sh](../switch.sh) — **ACTIVE** entry points; [return.sh](../return.sh) — **RECOVERY** | Forward to the active switching command; installed `ricy`, `voltar-ao-noctalia`, `voltar-ao-plasma` and Ricy menu entries use the same contribution. | Common `core/` destination remains conditional, not an approved new abstraction. Absolute paths and return compatibility must survive any future move. |
| Root-kit `outputs/noctalia-test/` start/return wrappers — **RECOVERY** compatibility; other root scripts/config/palette — **HISTORICAL** | switching/install.py explicitly maintains both forwarding wrappers. Current units/profile point to the contribution tree; root's other outputs belong to the earlier test recipe. Unknown external callers must not be erased based on this inventory. | Old root tree is not the selected profile/adapter. No blanket deletion/unification; preserve compatibility paths and historical restorers. |
| Root-kit `outputs/kde-outlines/` — **HISTORICAL** recipe snapshot | Earlier generator/restorer uses it; current appearance installers use contribution assets. Equivalent-looking SVG/config files are not evidence of synchronized ownership. | Preserve origin/licenses. Current selected theme is supplied by the contribution; do not run root restore-kde-style.sh as normal shell return. |
| [prepare-environment.py](../ricy-kit/prepare-environment.py), [generate-kvantum-variant.py](../ricy-kit/generate-kvantum-variant.py) — **HISTORICAL** | Earlier root-output preparation/generation, superseded by contribution prepare-destination/apply-style and packaged theme assets. Generator also writes installed Kvantum; it is not a harmless renderer. | Valid functionality survives in mapped installer/theme tools; these exact recipes are history. Do not run against the active kit or treat root preparation as current recovery. |
| Contribution preparers/installers/build tools not separately overridden — **MIGRATE** tooling supporting their parent class | Reproduction guide and sibling scripts consume them on a prepared destination; they are not resident daemons. Their validators/licenses/restorers retain the parent's lineage. | Existing parent destinations only. Installation order, source pins, licenses and rollback stay coupled; do not execute to validate docs. |
| All `docs/ricy-kit/` contributions/root outputs/scripts — **HISTORICAL** transport snapshots | Reinstallation/history readers consume them; no current service points here. Each corresponding contribution has the same responsibility/dependency family as above, but its snapshot differs. G-02 makes its old reordering diff useful provenance for the deployed binary. | Future public installation material under `installer/` requires a separate audit. Do not copy its old full-layout return scripts into the active kit. |
| [archives/ricy.zip](../archives/ricy.zip), [ricy.md](ricy.md), REINSTALL and VISUAL-IDENTITY records, both SHA256SUMS — **HISTORICAL** evidence | Historical reconstruction/attribution/reinstallation readers. Archive may include private state; manifests use original path labels/digests. Guides contain valid surviving functionality but dated commands/current-state claims need this audit. | Preserve locally, do not regenerate/distribute private archive or use historic checksums as live manifests. No architecture migration implied. |
| Active contribution `work/noctalia-profile/` config/state — **ACTIVE**, private | Unit environment explicitly selects these paths. Source templates and runtime overrides have independent lifecycles. | Public profile migration needs an allowlist. No clipboard, notification history, accounts, usage, or complete private config was exported here. |
| Private plugin source catalogs `sources/community/repo` and `sources/official/repo` — **ACTIVE discovery data** | Noctalia plugin registry/store consumes catalog records; two nested Git repositories are source catalogs, not two enabled plugin implementations. Three implementations are materialized separately (G-11). | Upstream discovery/cache, not independent Ricy components. No approved relocation/publication destination; preserve within private work. Catalog listing does not make every offered plugin an existing contribution. |
| Materialized `riversyx/noctaproton-vpn` 1.0.0 — **UNKNOWN** | Runtime registry reports enabled; manifest declares service/bar/panel/shortcut consumers (plugin API 24). Declared dependencies: proton-vpn-cli, nmcli, Python; no Proton VPN executable found under the checked names. Intended host is Noctalia; no successful service/interaction proof. | Optional third-party integration, independent of Ricy's switching/driver. Future architectural inclusion/destination UNKNOWN. VPN changes can affect connectivity; no network/account action was taken and no recovery reliance is established. |
| Materialized `lucasoe/proton-pass` 0.1.0 — **UNKNOWN** | Registry enabled; manifest declares `/pass` launcher provider (plugin API 3), excluded from global search. Requires proton-pass-cli; pass-cli absent from task PATH. Consumer registration exists, successful launcher/authentication use unproven. | Optional third-party launcher provider, not a replacement for the KDE desktop-search adapter. Future architectural inclusion/destination UNKNOWN; no established recovery dependency. No vault/account data inspected. |
| Materialized `aabidk20/yt-music` 0.4.0 — **UNKNOWN** | Registry enabled; manifest declares widget, panels and service (plugin API 28). Dependencies: yt-dlp, mpv, mpv-mpris, jq, curl, nc; yt-dlp/nc absent from task PATH. Successful host/service/playback consumption unproven. | Optional third-party media integration; no cumulative shell relationship or approved target destination. No established recovery dependency. No playback, cookies, account data or downloads inspected. |
| Original `plasma-antes.tar.gz`, captured shortcut/style files, current panel/shortcut snapshots, restoration manifests/backups — **RECOVERY** | Switching installer uses original panel seed when needed; actual return uses current state snapshots. Appearance/activation restorers consume their own backup manifests. | Keep private, at existing paths. A seed is not the normal return layout, and old archives can overwrite newer preferences. |
| Old activity marker/wallpaper-restoration output — **RECOVERY** compatibility | Marker is still written/tested by integration/login guards; wallpaper script remains an earlier restoration artifact, not the panel-only return implementation. | No copying destination IDs/images to public material. Preserve until all legacy recovery consumers are audited. |
| Existing `__pycache__/` — **UNKNOWN** consumer / regenerable cache | Python imports may consult caches; no necessary source/history value established, but absence of a current consumer was not proven. | Not a contribution or publication input. No REMOVE verdict from cache presence alone; no cache deleted. |
| scripts/verify, scripts/doctor, scripts/test-foundation.py, AGENTS/CLAUDE, .agents skills/references and Git selection rules — **ACTIVE** development harness | Agents/maintainers invoke validators and read the rules; not desktop services. Dependencies: Python/Bash, optional PyQt6/source cache, Markdown sources; privacy selection described in GIT-BASELINE. | Existing `scripts/`/agent documentation; test fixtures are not live recovery. No new daemon/tool framework. |
| core/, shell/noctalia/, compositor/kwin/, services/, themes/tokens/, integrations/, recovery/plasma/, installer/, tools/ — **UNKNOWN implementation; PLANNED reservations** | Only rules/README reservations found. Current implementations are above; the own Files prototype is retired; common core logic remains undecided. Documentary consumers are agents. | Existing planned destinations, not active runtime components. Do not count reservations as migrated implementations or infer a new API. |
| External KWin — **ACTIVE** infrastructure; Plasma desktop/wallpaper — **ACTIVE**; Plasma panels/KRunner/tools and Dolphin package — **RECOVERY** | Running compositor/plasmashell, existing switching contracts, installed Dolphin/System Settings and Plasma session entry. Qt/KDE/Kvantum are shared dependencies, not disposable copies of contributions. | Accepted target remains KWin + Noctalia with Plasma/Dolphin Recovery. Separate session/fallback remain PLANNED; Dolphin is the file manager; current recovery remains coupled. |

## Cumulative lineage and independent components

The shell lineage is:

```text
notification-continuity
  -> taskbar-menu-composition
  -> tray-menu-composition
  -> app-icon-interactions
  -> taskbar-app-actions
  -> app-indicator-animations
  -> app-icon-states
  -> app-icon-reordering (earlier cumulative diff: deployed)
  -> app-icon-reordering (RICY-001 source revision: not deployed)
```

Each shell build supplies a **complete cumulative diff against the same pinned
upstream commit**, not an incremental patch to stack on another variant.
Notification's activator/restorer is reused throughout; old directories remain
valuable records without owning the selected cumulative build.

KWin's lineage is independent: the squash-style `ricywindowactions` packages in
indicator/states/reordering are historical; `window-fade-expand` supplies the
selected package under the **same effect ID** plus native Scale settings.
`smoothwindowgeometry`, `ricydolphinrounding`, and native blur are complementary.
`ricyblur` is a separate attempted replacement for native blur and is currently
unresolved. Shell rebuilds do not automatically replace window effects.

Integration progression is root manual test -> contribution integration ->
permanent autostart -> panel-only switching. Shared identifiers/output paths
persist, but return algorithms differ. Destination fixes are version-specific
prerequisites, not another runtime layer to replay after switching.

Dolphin source contains cumulative edits to one Qt helper/QSS/theme, with an
independent optional KWin corner plugin. Earlier transparent panels, delegate
replacement, and header-chip experiments in README records are historical. The
latest documented/source treatment preserves the native delegate and installs
the helper atomically. Exact deployed Qt binary provenance remains UNKNOWN.
These historical adjustments do not define an own application; ADR-0011 now selects Dolphin.

## First safe cleanup

Date: 2026-10-11 (America/Sao_Paulo). **No item is classified/approved REMOVE;
no file was deleted or moved.** Historical status permits separating development
entry points, not deleting provenance, rollback, or UNKNOWN consumers.

KNOWN dependency review before changes:

| Surface | Evidence and cleanup consequence |
|---|---|
| References and scripts | Repository searches found historical build/activation commands in the seven local READMEs and cumulative successor references. No current unit or root wrapper selects those builders. Historical recipes now carry grounding warnings; the builders require explicit isolated reproduction. |
| Absolute/runtime paths | Installed user units select autostart, the integration output adapter, and `$HOME/.local/lib/ricy-noctalia/noctalia`; root/installed commands select switching. Historical builders previously shared `$HOME/.cache/ricy-noctalia-src-5.2.1` with the deployed provenance cache. They now reject that cache, repository paths, and symlink aliases before any version probe/download/build. |
| Mixed-role consumers | `notification-continuity/enable.py` supplies activation and binary/drop-in rollback to later variants. Its `sync-wallpaper.py` retains preparation/restore functionality. These files stay in normal source checks; only its HISTORICAL builder is gated. Current reordering build/validators, switching, autostart, Dolphin and UNKNOWN blur/plugin material remain intact. |
| Hashes/manifests/history | The old patches are tracked in Git; pre-cleanup builders are available at `1fb1918`. Both original SHA256SUMS and the version-specific correction manifest are historical evidence, not current checksums. Their bytes, transport recipes, archive, assets/licenses, and private backup/state paths are preserved. No duplicate snapshot or regenerated manifest was created. |
| Rollback dependencies | Binary/source-cache provenance, notification restore, historical effect restoration interfaces, switching's panel/shortcut snapshots, compatibility output wrappers, upstream Noctalia, Plasma and Dolphin remain preserved. Old effect installers still contain valid rollback interfaces and were not disabled or substituted for window-fade-expand. |

Normal `verify shell` source selection now omits the six HISTORICAL cumulative
folders, notification's old builder, reordering's old effect installer, and the
two historical root generators. All seven build guards still receive syntax
checks. This explicit selection is based on the classifications above and does
not reinterpret missing references, caches, or UNKNOWN as REMOVE. New fixture
regressions check retained consumers and build rejection before side effects.
See [DEVELOPMENT](DEVELOPMENT.md#historical-reproduction) for opt-in reproduction
and the maintained source/effect entry points. Transport/history copies retain
their original bytes and are explicitly outside normal development/build.

Validation results and live-session limits are recorded in
[CHANGELOG](CHANGELOG.md). Offline checks and unchanged runtime fingerprints do
not prove interactive behavior or recovery after a persistent failure.

## How to use and refresh this audit

Before touching an item, follow its class **and part-level overrides**, then its
local AGENTS/README and the mapped subsystem rules. Never infer ACTIVE from a
directory name, README phrase such as “current,” an enabled but failed unit,
or a file's presence in the transport copy. Never infer REMOVE from lack of a
textual reference alone: installed wrappers, D-Bus, MIME, user units, dynamic
loaders, and restoration manifests are consumers too.

Read-only refresh commands include:

```bash
./scripts/doctor
systemctl --user show noctalia-teste.service noctalia-busca-desktop.service \
  ricy-noctalia-integracao.service ricy-blur-continuidade.service \
  --property=Id,ExecStart,FragmentPath,DropInPaths,ActiveState,UnitFileState,MainPID
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.loadedEffects
qdbus6 org.kde.KWin /Scripting org.kde.kwin.Scripting.isScriptLoaded windowsarrows
qdbus6 org.kde.KWin /Scripting org.kde.kwin.Scripting.isScriptLoaded adaptivepanelwidth
xdg-mime query default inode/directory
xdg-mime query default application/x-rpm
pacman -Q aic8800-usb-dkms-ricy
dkms status
noctalia msg plugins list
```

Artifact comparisons also used `git rev-parse HEAD`/`git diff --binary HEAD` in
the preserved source cache, SHA-256/byte comparisons of installed artifacts,
selected configuration keys, and the failed unit's current-boot journal. These
reads did not apply patches. Compare against the appropriate tree and identify
which installed artifact was examined; matching a historic diff is not a current
source-policy validation. Do not publish private inspection output wholesale.

No migration, deletion, repair, or new architecture is approved by a class label.
Unresolved items are G-02 deployment/policy, G-03 blur disposition, G-05 Qt-helper
provenance/usability, individual private plugins, full palette equivalence, and
end-to-end login/return/failure recovery. Safe documentation work is complete;
these operational questions remain explicit UNKNOWNs for separate tasks.

## Validation performed in this task

| Result | Command/check and scope |
|---|---|
| PASS | `./scripts/verify architecture`: required structure, Python harness syntax, documentation links and local AGENTS documentation references. |
| PASS | Inventory coverage: all 24 active contribution directories have explicit rows in this audit and COMPONENTS; the transport tree has the same 24 directory names. Three materialized community plugins have individual rows. |
| PASS | `./scripts/verify shell` syntax subcheck: 83 source/config candidates. The command's overall exit is 2 because of the unavailable source-based check below, not a syntax failure. |
| PASS | `./scripts/verify recovery` (exit 0): offline panel capture/merge preservation and 28 isolated KWin effect scenarios. No real windows were manipulated. |
| PASS | `git diff --check` and SHA-256 comparison against the task's initial filesystem snapshot: only Markdown documentation/rules changed, with no existing file moved or removed. Original implementation, assets, state, backups and manifests retained their bytes. |
| FAIL — preexisting observation | G-03's enabled blur selector is in failed state, with a D-Bus method-lookup error in the current-boot journal. This is an observed runtime failure, not a failure introduced by documentation checks. |
| UNKNOWN — diagnostic | `./scripts/doctor` (exit 2): live recovery and complete session single-space compliance remain unproven. Diagnostic presence/state queries are not functional tests. |
| NOT RUN | Source-based Noctalia action/native checks: `./scripts/verify shell` (exit 2) rejects the preserved cache's mismatch with the current patch. No source download, build, patch application or activation was performed. |
| NOT RUN | Interactive login/unlock, shell switching/crash recovery, Dolphin, package conversion/installation, plugin use, keyboard input, connectivity and visual comparisons; this task only audits and documents. |
| NOT APPLICABLE | New component/validator regression suites and ADR creation: no implementation, test harness or architectural decision changed. External links and Markdown anchors are outside the foundation link validator's scope. |

See [CHANGELOG](CHANGELOG.md) for the change record. These results do not upgrade
UNKNOWN component classifications or historical README tests to PASS.
