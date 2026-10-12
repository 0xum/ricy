# Dolphin baseline — Ricy file manager

Audit date:2026-10-11 (America/Sao_Paulo). Status: **KNOWN installed/configured
baseline**, read-only. Current direction: [ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md).
The user assesses Dolphin as **about 90% visually complete**. This is the user's
progress assessment, not measured feature coverage, a release gate, or proof
of independent Recovery.

No new visual work, launch, rebuild/install, service restart, file operation,
MIME/default, FileManager1, token-value, or Recovery runtime change occurred in
this task. The current checkout retains earlier uncommitted Dolphin customization
work; it was not reset, published or reapplied during this audit.

## Evidence levels and scope

- **KNOWN:** directly inspected configuration/source, hash equality, installed
  package versions, service/shortcut registration or read-only D-Bus result.
- **INFERRED:** behavior implied by those consumers; no live execution proof.
- **UNKNOWN:** not established by this audit. Historical screenshots/tests do
  not become present runtime evidence.

No Dolphin process was running at the audit snapshot. FileManager1 had no bus
owner, and plasma-dolphin.service was inactive/dead. These observations are not
failures: they establish that activation and live UI behavior were not tested.
The latest attached image is a KDE menu proportion reference, not a current
Dolphin capture. Earlier user approvals and screenshots inform the visual
progress record but are complementary/historical, not runtime certification.

## Installed software and registrations

| Surface | KNOWN current evidence | Limit / ownership |
|---|---|---|
| Software | Dolphin 26.08.2-1.1, KWin 6.7.5-3.1, Kvantum 1.1.8-1.1, Qt 6.12.0-2.1, KIO/Solid 6.30.0-1.1 from pacman queries; dolphin --version reports26.08.2 | Local installation snapshot, not latest upstream claims |
| Wrapper | `$HOME/.local/bin/ricy-dolphin` matches [launch.py](../ricy-kit/contributions/dolphin-noctalia-identity/launch.py). Adds local QT_PLUGIN_PATH, `-plugin ricydolphinui` and installed QSS; GUI adds --new-window, explicit --new-window/--daemon preserved | INFERRED new-process loading; no launch in this audit |
| Desktop entry | User `org.kde.dolphin.desktop`: Exec points to wrapper %u; icon org.kde.dolphin, StartupWMClass dolphin, KDE Meta+E declaration and native identity retained | User override shared by current shell modes; upstream entry remains installed |
| Shortcut | KGlobalAccel Dolphin `_launch` registered with 268435525 (Meta+E); user previously confirmed correct customized opening | Actual key press/cached launcher invocation NOT RUN here |
| Directory default | `xdg-mime query default inode/directory` returns org.kde.dolphin.desktop | Does not establish FileManager1 ownership or every caller |
| FileManager1 | User service executes wrapper --daemon and names plasma-dolphin.service; user70-ricy-aparencia.conf drop-in sets the same ExecStart. systemctl show confirms registration | Bus owner absent/inactive at snapshot; cold start/reveal/browser/portal callers UNKNOWN |
| Dolphin configuration | Native groups inspected: Noto Sans10pt for all three view modes; expandable folders true, LeftPadding20, archives browsing true, selection toggle false, Places icons16/static, previews16, menu bar disabled | Personal URLs/state not published; config alone does not exercise behavior |
| Kvantum | Global KDE-Noctalia; Applications assigns Ricy-Dolphin only to dolphin. Per-app SVG/config installed; translucent_windows/blurring true, window opacity reduction30, popup_blurring false, menu opacity reduction0, toolbar icons22, layout spacing/margin8 | QSS/helper layer overrides many native geometry values; effective composited opacity unmeasured |
| QSS | Installed sheet exactly matches maintained [dolphin.qss](../ricy-kit/contributions/dolphin-noctalia-identity/dolphin.qss), hash below | Handwritten consumer, not live JSON token consumption |
| Qt helper | Local generic libricydolphinui.so exists; installed binary matches cache binary, maintained ui.cpp matches cache ui.cpp; metadata key ricydolphinui and application-name filter dolphin | No rebuild/reproducibility trial or process-mapping evidence now; binary-to-source compilation lineage INFERRED, byte equality KNOWN |
| KWin | Effects.loadedEffects includes native blur and ricydolphinrounding; respective enabled settings true. ricyblur is installed but absent from loaded effects | Loaded registration is not a visual/ABI stress test; no effect change |
| Corners | Installed `/usr/lib/qt6/plugins/kwin/effects/plugins/ricydolphinrounding.so`; [source](../ricy-kit/contributions/dolphin-blur-corners/corners.cpp) targets Dolphin normal/dialog windows, radius 16 restored/0 maximized/fullscreen/tiled | Source policy KNOWN; every live state UNKNOWN |

The existing [identity applicator](../ricy-kit/contributions/dolphin-noctalia-identity/apply.py)
backs up wrapper, desktop, service/drop-in, dolphinrc, theme and helper/QSS state
and installs helper binaries atomically. Its restore route is preserved but NOT
RUN. Recovery file access must remain available if visual customizations fail;
current shared wrapper/Qt/Kvantum and class-specific effects mean independent
failure recovery is **UNKNOWN**, not achieved by this baseline.

## Visual/interaction baseline — configured source, not a new live capture

| Area | Current source/configuration | Evidence limit |
|---|---|---|
| Shell panels | Opaque card-colored unified L behind sidebar/topbar; rounded12, outer 8, no input capture. Main card wraps DolphinViewContainer including scroll/status area; inner padding 8, internal gutter4, outer sides/bottom8 where at window edge | Helper/QSS KNOWN; prior containment/split approval historical |
| Toolbar/navigation | Padding8 vertical/16 horizontal, spacing8, minimum content36; native navigation/Split/search/menu actions retained | Configured source; overflow/RTL not revalidated |
| Breadcrumb/location | Transparent breadcrumb container; native segments28 centered within 36; centered6px chevrons. Editable path36, surface background, accent2px outline/radius 8; combo padding 12/8, editor horizontal12; native completion/clear/check retained | Native clear overrides toolbar padding; all activation modes UNKNOWN now |
| Tabs | Neutral card, active accent/on-accent, hover selection/on-hover; radius 12, gap6, padding6/14; native icons and close button12 with 12px outer inset | Source/native button placement known; overflow/accessibility untested |
| Places | Native KFilePlacesView and original delegate preserved, column adapter only; normal transparent, selected accent/dark text, hover alpha65; semibold,16px icons,6px label gap, spacing3, horizontal padding 12, bottom containment12 | Native signals/models retained; current visible entries are not inferred from old images |
| Devices / Recent | Native Places model handles device and recent files/locations entries; helper only adapts painting/spacing | No custom backend. Device enumeration/mount/unmount and recent contents NOT RUN |
| File/list view | Native KItemList graphics/model; medium-radius 6 rows/header with visible-width clipping. Nested row inset20 + one native row-height per depth; nested arrow extra4; file expansion remains native Children-only | Source known; all modes/depths and widths not revalidated |
| Selection/focus | File hover/selected/selected-hover fill alpha95/170/195; focus accent outline. Native rubber band uses selection alpha65, accent outline alpha150, radius 6, native rectangle/animation opacity | Preserve upstream selection behavior; actual operations NOT RUN |
| Status | Native DolphinStatusBar, small overlay positioning and status offset remain; backing is part of main card, with contained scroll area | Source/last layout captures historical; all messages/error states UNKNOWN |
| Menus | Opaque card/outline radius 12; native rounded surface mask and transparent Window palette; outer padding 12, items vertical4/horizontal12 with margin1, icon offset8, radius 6; accent/dark selection, secondary disabled, transparent4px separators | KDE proportion reference accepted in previous turn; current live submenu corners/RTL UNKNOWN |
| Scrollbars | All Qt scrollbars:6px dark neutral track (#242435), radius 3; secondary thumb alpha128, minimum24; secondary hover, accent press; no arrow buttons | User-confirmed prior appearance; dialogs/oversized menus not all tested |
| Pane divider | Native4px draggable splitter;12px inter-card gap,2px rounded line with 12px end inset. Track color normal, thumb color/alpha on hover, accent during drag | Native mouse resizing retained; user-confirmed neutral gap/line historical |
| Icons | KDE global breeze-dark, Dolphin/native icons and folder colors retained; Qt helper does not recolor application assets. Places16, tabs/toolbar native, toolbar22 configured | Some built-in menu icons differ in painted footprint; full theme coverage UNKNOWN |

## Design-system mapping — values preserved

[Canonical tokens](../themes/tokens/README.md) remain the visual authority;
**tokens.json values/schema/contract and token validators/renderers are unchanged
by this task**. No runtime consumer migration occurred.

| Role / adaptation | Existing Dolphin correspondence | Consumption status |
|---|---|---|
| Surface/card/text | #181825 / #313244 / #cdd6f4 | QSS, ui.cpp, Kvantum literals |
| Secondary/outline | #a6adc8 / #46485c | QSS/helper/Kvantum literals |
| Accent/selection | #cba6f7 / #977dba; dark on-accent #11111b, existing on-hover #000000 | Canonical roles followed by scoped hardcodes |
| Neutral track/menu controls | #242435 | Existing Dolphin/KDE adaptation, not a new global role |
| Spacing/radii | Existing4/8/12/16 geometry; native6 rows,12 panels/tabs/menus,8 input,3 scroll,16 window corners;20 menu padding from earlier revision is superseded by12 | Scoped Qt/KDE adaptation; no global geometry change |
| Typography | Dolphin QSS/view Noto Sans10pt; native Places semibold. KDE global menu/toolbars use JetBrainsMono Nerd Font10pt | Explicit application override differs from global font; do not silently harmonize |
| Materials | Outer shell QSS alpha 178, opaque card 255; Qt/Kvantum translucency configured; native KWin blur loaded | Runtime composition/scale effective alpha unmeasured |
| Token consumers | Offline identity board reads central JSON. Dolphin QSS/helper/theme and installed runtime do not import the JSON | Own prototype token consumer retired; no new adapter introduced |

Dolphin-specific adaptations already exist under application_adaptations.dolphin;
metadata does not prove executable token consumption. Handwritten QSS/ui.cpp,
Kvantum/SVG generation and KWin corner literals remain local/hardcoded surfaces.
The legacy token snapshot/transport manifests are provenance, not editable
second authorities. Only consumer-direction documentation changes in this task.

## Backlog only — no fixes or automatic next phase

1. Confirm all current menus/submenus, corner cutouts, icon/text/shortcut spacing
   and widget actions at supported scales/RTL. Configured mask is not compositor
   certification.
2. Validate panel containment, splitter/scroll placement and outer margins when
   sidebar is hidden, tabs overflow, docks float, filters/messages appear and
   panes resize to minimum width. No spacing change is authorized here.
3. Resolve exact compiled-helper reproducibility/process provenance in a separate
   validation task; keep Qt/KWin ABI updates and atomic installation explicit.
4. Decide whether the Noto Sans application override versus configured KDE
   JetBrainsMono is intentional before any polish. No font change now.
5. Audit literal/central-token drift and consider one separately approved consumer
   adapter; do not migrate all consumers or change token values automatically.
6. Demonstrate cold directory/FileManager1 activation and usable Dolphin when
   helper/theme/QSS fail in a controlled Recovery trial. No service/default or
   session change now. Device/Trash/portal operations remain upstream responsibilities.
7. Reconcile historical README/audit claims with this snapshot; effective opacity,
   blur junctions, icon-theme variations and full state/accessibility coverage
   remain visual verification work, not implemented fixes.

## Retirement and verification

The own application code/QML/CMake/tests/runner/packaging is removed from this
active checkout, without Git-history rewriting or main integration. Earlier
specifications are [historical](history/ricy-files/README.md). ADRs 0008/0009 are
Superseded;0007/0010 Rejected;0003 Superseded. [0011](adr/0011-dolphin-as-ricy-file-manager.md)
is the current policy. No own filesystem/Trash/FileManager1/fork roadmap remains.

Read-only commands used: xdg-mime query, pacman -Q, dolphin --version,
systemctl --user show, qdbus6 NameHasOwner/loadedEffects/shortcut registration,
configuration/source reads and SHA-256 comparisons. No applicator ran.
Before/after private evidence is in the local cache, outside public packaging.

Validation outcomes are recorded in [CHANGELOG](CHANGELOG.md). Live failure
Recovery, every UI/device/Trash state, MIME launch and FileManager1 activation
are NOT RUN. Published portability and complete functional coverage are UNKNOWN.
No backend implementation tests are applicable after retirement.

## Fingerprints at the audit snapshot

| Evidence | SHA-256 |
|---|---|
| source wrapper | `67013fc3b7ebb2986a24585e66a8c6f3ac2bc5459ac71f12390fb1d1ab7a0c84` |
| installed wrapper | `67013fc3b7ebb2986a24585e66a8c6f3ac2bc5459ac71f12390fb1d1ab7a0c84` |
| source QSS | `60058c9ec6237b7a9a00a84bf5d39bdd3d5e159d43c9fea0ee4c628d10d4e8a6` |
| installed QSS | `60058c9ec6237b7a9a00a84bf5d39bdd3d5e159d43c9fea0ee4c628d10d4e8a6` |
| source helper | `44f05cac80ef76363c495544c1cefc7903724148e21b4f2feda947dd9c10e81d` |
| cached helper source | `44f05cac80ef76363c495544c1cefc7903724148e21b4f2feda947dd9c10e81d` |
| cached helper binary | `01d9d831c4112a10b45e05d95784fe115fb7f3a9737689721985ceb0c2200f7a` |
| installed helper binary | `01d9d831c4112a10b45e05d95784fe115fb7f3a9737689721985ceb0c2200f7a` |
| canonical tokens | `e8194379106f4513f56d9f49a1535e66752490f843c783e4ede904fddbe5925e` |

## First visual polish pass — 2026-10-11

This section records the subsequent authorized polish task; the read-only scope
above describes the earlier snapshot. Visual authority remains
[DESIGN-SYSTEM](DESIGN-SYSTEM.md), [SEMANTICS](../themes/tokens/SEMANTICS.md),
[Noctalia grounding](NOCTALIA-VISUAL-GROUNDING.md) and the unchanged canonical
`application_adaptations.dolphin` contract. No new architecture or visual values.

### Current consumer and audit

KNOWN: Super+E/search use the installed Dolphin desktop entry's visual wrapper.
A normal wrapper launch mapped the installed Qt helper and Kvantum style; source
QSS matched the installed sheet before editing. The helper is newer than the
fingerprint above: the separately completed
[tab overflow revision](CHANGELOG.md#2026-10-11--dolphin-tab-overflow-controls)
is preserved. The maintained consumers are the active
[QSS](../ricy-kit/contributions/dolphin-noctalia-identity/dolphin.qss) and
[helper](../ricy-kit/contributions/dolphin-blur-corners/ui.cpp), rather than the
historical transport copies linked in parts of the original snapshot.
Early direct-launch/probe and incomplete isolated-theme captures were rejected
as visual references after the user's correction. Final visual observations
use the installed wrapper with its normal configuration and environment.

| Area / classification | Observed inconsistency or current evidence | First-pass disposition |
|---|---|---|
| Toolbar — hover, selection, color role | Generic checked/pressed fill was overridden by the more specific toolbar hover rule, leaving the old interaction foreground on a faint hover overlay | QSS keeps the existing interaction-fill/on-interaction-fill pair for checked/pressed native actions during hover |
| Controls — spacing | Generic tool buttons and text fields used residual 5px padding outside the approved spacing scale | Use the existing 4px spacing; preserve scoped toolbar, menu, tab and editor overrides |
| Controls — focus, border | Transparent control borders had no explicit focus contour; toolbar hover could suppress it | Accent focus border within the existing 1px border slot, including toolbar/overflow/menu controls and native breadcrumb buttons; no layout shift |
| Controls — color role, hierarchy | Disabled checked tools could keep a filled action backing while using secondary text | Transparent disabled backing/border with existing secondary text; native disabled actions remain inert |
| Top chrome — radius, material/surface, alignment, vertical rhythm | Unified opaque L, inherited toolbar/breadcrumb surfaces, 36px navigator and scoped padding already match approved adaptations | Preserve layout and geometry; no additional bars, separators or shadows |
| Tabs — radius, spacing, hover, selection, close state, focus | Approved active/inactive/hover pairs and latest native close/overflow geometry are present | Preserve treatment and native keyboard/close behavior; no close-icon substitution or new animation |
| Places — typography, hierarchy, spacing, selection, icon treatment | Transparent normal rows, group hierarchy, native 16px icons and device rows match the existing adaptation | Preserve native model/delegate, group titles, row heights and indicators; full device/hover coverage remains UNKNOWN |
| Content — material/surface, alignment, radius, selection | Captured grid/compact/details retain solid cards, native icon/text layout and existing moderate-alpha file states | Preserve row/grid geometry and file-selection roles; no filesystem/model changes |
| Status/navigation surface — truncation, hierarchy, alignment | Small native status overlay abbreviates summaries despite available width; storage/Places labels also elide | Retain native small mode. Full-width native configuration removed summary elision but exposed clipped storage controls; test setting reverted |
| Menus/floating surfaces — material/surface, border, radius, elevation | Approved opaque card/outline, rounded native popup mask and shadowless per-app treatment already exist | Preserve surface geometry/materials; focus contour only for embedded controls. Native popup composition is not fully certified |
| Motion | Installed Kvantum has `animate_states=true`, whereas the grounding describes `false` | Record preexisting conflict; preserve installed preference and add no animation or QSS transition |
| Native configuration | Current DetailsMode LeftPadding is 0, whereas the earlier snapshot recorded 20 | Preserve current value; this pass does not normalize native file geometry from stale documentation |

The QSS change uses existing colors, spacing and radius scopes. It introduces no
runtime token loader, generator, additional token, upstream patch, helper change,
Kvantum edit, KWin rule, wrapper/default/MIME/FileManager1 change or session switch.
Generic padding normalization does not change toolbar minimum content dimensions;
focus uses existing border space. Recovery receives no additional dependency.

### Validation and limits

- **PASS:** `python3 -B ricy-kit/contributions/dolphin-noctalia-identity/validate-polish.py`,
  also with `QT_SCALE_FACTOR=1.5`: actual Qt parsing/painting, checked+hover and
  pressed/disabled/focus precedence, fixed toolbar hit area, native text editing,
  tab keyboard navigation/close signal and menu keyboard invocation. The regression
  fixture fails on pre-pass QSS at checked+hover and passes on deployed QSS. Qt fixtures
  cover QSS; they do not prove installed-helper/compositor behavior.
- **PASS:** installed wrapper startup and mapped helper/Kvantum; native directory
  navigation and tab creation using a private fixture; real grid, compact and
  details captures. No file transfer, mount, Trash or package operation ran.
- **PASS:** canonical token checks, Kvantum INI/SVG parsing, architecture and
  Recovery offline harness. Installed QSS equals the maintained source;
  canonical JSON, helper, launcher and protected registrations remain unchanged.
  Dolphin configuration returned exactly to its pre-task bytes after the rejected
  status test. Normal application launches may persist native window/tab state;
  they are not a filesystem-behavior implementation change.
- **PASS, limited offline fallback:** native Dolphin under isolated D-Bus/config/
  state/data, Fusion style, missing optional helper and missing QSS opens the test
  directory. This demonstrates a manual upstream fallback, not automatic failure
  handling by the shared wrapper or a Plasma Recovery round trip.
- **FAIL, preexisting:** graceful shutdown of the installed customized Dolphin
  produces SIGSEGV in Qt application destruction, with and without the early
  probe. Prior coredumps and the tab-overflow changelog predate this pass. It is
  not repaired or attributed to the QSS edit.
- **UNKNOWN / NOT RUN:** independent live Recovery, every device/mount/storage
  state, real monitor/scale combinations, all popup/submenu composition, Places
  hover/drag/drop, complete keyboard/focus traversal, RTL and reduced-motion
  preference combinations. Offline scale checks are not monitor certification.
- **NOT APPLICABLE:** new helper build, upstream patch, filesystem backend,
  FileManager1/MIME/default migration or global KWin validation for this QSS pass.

### Separate backlog and rollback

1. Repair the preexisting customized-Dolphin teardown crash in a separately scoped
   helper/Qt lifetime investigation. Establish clean exit and independent live
   Recovery before claiming recovery safety end to end.
2. Resolve native small-status summary elision and clipped full-width storage
   indicators. Existing configuration alone was insufficient; investigate native
   sizing and existing styling before proposing a minimal helper/upstream change.
   Preserve message/progress/cancellation and storage behavior.
3. Complete device indicators, native icon contrast, popup/submenu composition,
   all focus states, supported scales/RTL and live failure-Recovery validation.
4. Reconcile the preexisting Kvantum motion and native padding documentary drift
   in a separately evidenced task; neither discrepancy authorizes changing them.

Only the QSS is deployed for this pass, atomically, with an existing-restorer
compatible private backup. Rollback restores the pre-pass QSS and the unchanged
saved dolphinrc; consult the existing
[restorer](../ricy-kit/contributions/dolphin-noctalia-identity/README.md#restore).
The backup manifest contains only these two targets, so it does not replace the
launcher, services, helper or theme. Preserve later user edits before restoring
whole files. Private captures, logs, fixtures and backup paths stay outside the
public kit. First pass ends here; no second phase starts automatically.

## Identity & Motion Pass — Phase 1: Typography — 2026-10-11

**Phase result: PASS for font inheritance and the inspected typography surfaces.**
This supersedes the captured Noto Sans application override above. It is not a
clean-shutdown or independent Recovery certification. Later phases have not
started at this gate.

### Scope, authority and implementation

- **KNOWN:** active `kdeglobals/General/font`, menuFont and toolBarFont all select
  JetBrainsMono Nerd Font 10pt. A new QApplication on the installed KDE Wayland
  platform returns that application font; QFontInfo resolves the same installed
  family. This existing system choice is the application authority. No new font
  was selected; fixed/terminal/code fonts and global KDE settings were not edited.
- **KNOWN:** QSS no longer sets family/size; the helper's KItemListHeaderWidget
  override is removed. Native IconsMode, CompactMode and DetailsMode select
  UseSystemFont=true. Dormant personal ViewFont values remain stored but inactive.
  Places retains inherited-family DemiBold emphasis and its original delegate.
- **KNOWN:** the running Noctalia process's NOCTALIA_CONFIG_HOME identifies its
  private profile. Its existing official shell.font_family now matches Qt. The
  bar has no family override; font_scale=0.85, contextual sizes, settings and all
  unrelated TOML values are preserved. Official config validation/reload succeeds;
  bar, launcher and control-center captures show the new family.
- **INFERRED:** other Ricy applications using native KDE/Qt font inheritance will
  share the same system choice. No continuous cross-toolkit synchronizer exists.
- **UNKNOWN:** every script/glyph fallback and unrelated application, every monitor
  combination, and independent live Plasma Recovery. Shell was inspected at the
  current 1x outputs; its behavior on a physical 1.5x output remains NOT RUN.

[apply-typography.py](../ricy-kit/contributions/dolphin-noctalia-identity/apply-typography.py)
performs an explicit one-shot sync and atomic helper/QSS installation with the
existing restorer manifest. PyQt6 and the existing Qt helper build prerequisites
are installation-time dependencies; neither becomes a new Dolphin runtime
service. The full identity applicator now also enables native system-font use.

Canonical JSON typography/application_adaptations.dolphin.font values remain
unchanged captured references. They no longer describe the deployed application
override; replaying Noto Sans from those snapshots would undo this authorized
synchronization. Qt's active font is authoritative for family/point size; shell
contextual logical-pixel sizes and scales remain local. No token/schema migration
is part of this change.

### Isolated validation and evidence

- **PASS:** existing helper build in a separate cache; installed QSS/source and
  installed/helper output equality. Protected launcher/MIME/FileManager1, native
  models/KIO/Solid, Kvantum composition, KWin and canonical token values unchanged.
- **PASS:** real Dolphin startup through the installed wrapper, all three native
  view modes, toolbar, breadcrumbs/editor/clear control, tabs, Places, native menu
  and status at 1x and process scale1.5. A private diagnostic plugin uses the
  native KActionCollection for mode/tab/editor actions in isolated configuration.
  Actual widget/graphics fonts resolve JetBrainsMono Nerd Font 10pt; Places
  weight600, native metrics17px, navigator36px, header25px and rows21px.
- **PASS:** visual inspection of normal/narrow layouts, native long-name elision,
  alignment and text containment. The wider system family increases native
  breadcrumb/device-label elision; no hit area or geometry was replaced. Native
  small-status summary elision occurs with both old and new helpers/fonts and
  remains the preexisting baseline gap. No status sizing redesign was attempted.
- **PASS:** official Noctalia config validation/reload, live bar/launcher/control
  surfaces at current output scale. Contextual hierarchy and scales preserved.
- **PASS:** validate-polish.py at1x/1.5x; architecture verification, token validator
  and whitespace checks. QSS fixtures prove state/native signals, not live Recovery.
- **FAIL, preexisting:** graceful process shutdown exits139 with the backed-up
  pre-change helper/QSS and with this change. The same private probe completes
  captures before shutdown in both trials. This is not attributed to Typography.
- **NOT RUN:** transfer/mount/Trash operations, live Recovery round trip, physical
  fractional-output combinations, all RTL/glyph cases and complete accessibility.
- **NOT APPLICABLE:** new architectural decision, new font selection, global font
  or icon-theme change, compositor/window animation or filesystem implementation.

Private before/after captures, logs, fixtures and isolated config are in
`~/.cache/ricy-dolphin-identity-motion/typography/`; they are not publication
artifacts. `live-1x-{icons,compact,details,tabs,menu,editor,narrow}.png` and the
corresponding `live-1_5x-*` captures record Qt surfaces; `before-*` supplies the
pre-change comparison, and `noctalia-*` supplies shell observations.

### Rollback

Private restorer-compatible backup:
`~/.local/state/ricy-dolphin-backups/20261011-214727-270924`. Restore with the
existing `apply.py --restaurar BACKUP`, reload Noctalia in its active profile
environment, and reopen Dolphin. Existing windows retain their mapped helper.
Whole-file restore may replace subsequent settings changes; restore passes in
reverse order. Source rollback reverts this phase's commit. No service/default
or KWin migration is required. Live failure Recovery remains UNKNOWN.

## Identity & Motion Pass — Phase 2: Iconography — 2026-10-11

**Phase result: PASS for the scoped chrome overlay and native content fallback.**
Started only after the Typography commit `f7db218`. This is not a clean-shutdown
or independent Recovery certification; Motion has not started at this gate.

[Overlay mapping/provenance](../ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/README.md)
records actual native action names from the live KActionCollection, named Tabler
resources and internal Noctalia aliases. Thirteen selected action assets come
from pinned, MIT-licensed upstream SVGs, preserving geometry/stroke and adapting
only KDE filenames/palette CSS. Current breadcrumbs, tab close/overflow primitives
retain their approved geometric paint and native semantics. Places icons and
all content/state providers remain native. No icon pack or Breeze copy is added.

The existing Dolphin-filtered helper selects the optional valid overlay via
the native process-local KIconTheme/KIconLoader API. No KDE global theme or
dolphinrc theme override persists. The helper now directly links the already
required KDE icon library; its headers join existing build prerequisites. The
rejected per-app rc experiment had inadequate missing-theme fallback and was
fully undone; malformed/black initial SVG adaptations were corrected before
phase validation. These were implementation failures, not architectural choices.

### Isolated validation

- **PASS:** native loader paths at1x and process1.5x: selected actions resolve to
  the overlay, while folder/text-plain resolve to Breeze Dark places/mimetypes,
  drive-harddisk/drive-removable-media to native devices, and org.kde.dolphin to
  hicolor. The overlay contains only Actions SVGs; native thumbnail/preview
  pipelines, device/mount/MTP state and model code are unchanged. Their complete
  runtime state/provider coverage remains UNKNOWN.
- **PASS:** all13 SVGs parse/paint visible strokes, pinned license/provenance/hash
  checks; native QIcon normal/disabled/checked modes and dark-surface contrast
  at1x/1.5x. Disabled glyphs fade through the native engine. Button hit geometry
  stays fixed across disabled/checked/hover/focus state changes.
- **PASS:** real Dolphin toolbar, native menu actions, breadcrumb/editor, tabs/
  overflow, hover/focus and search captures. Native tab close/overflow and
  breadcrumb glyphs retain their original mechanisms, including RTL policy.
  No SVG geometry is used as layout geometry.
- **PASS:** missing-overlay trial with isolated XDG_DATA_HOME and system data dirs
  reports breeze-dark and native actions/content paths; real startup/captures
  have no missing replacement glyphs. Global KDE remains breeze-dark and the
  temporary dolphinrc theme selection is absent.
- **PASS:** helper build/atomic installed equality; architecture/token/whitespace
  checks and existing QSS/state checks. No canonical JSON/value change.
- **FAIL, preexisting:** capture processes still exit139 on graceful teardown;
  Typography's before/after control already reproduced this failure.
- **UNKNOWN / NOT RUN:** all devices/MTP/mount states, thumbnail-provider behavior
  for all formats, physical fractional-output/RTL combinations, complete keyboard
  accessibility and independent live Recovery.
- **NOT APPLICABLE:** content icon substitution, global icon-theme migration,
  shell/font/geometry/KWin/filesystem or default-handler change.

Private captures/logs and native-icon mode matrices are in
`~/.cache/ricy-dolphin-identity-motion/iconography/`: `live-1x-*`, `live-1_5x-*`,
`actions-1x-*`, `actions-1_5x-*`, `modes-1x.png`, `modes-1_5x.png` and
`missing-overlay-*`. Evidence is private rather than published active-kit data.

### Rollback

The final scoped installer printed
`~/.local/state/ricy-dolphin-backups/20261011-215948-522634`; it captures only
the optional overlay's prior absence and Phase1 helper. Existing manifest restore
followed by reopening Dolphin returns the phase to the previous state. Source
rollback reverts this phase's commit. Typography is independently retained.
No service/default/theme-global reset or KWin change is needed.

## Identity & Motion Pass — Phase 3: Motion — 2026-10-11

**Phase result: PASS for inspected paint transitions, interruption and stable idle.**
Started only after Iconography commit `7f9a888`. The overall run still has the
separately recorded preexisting shutdown FAIL and live Recovery UNKNOWN.

### Scope and ownership

The existing Dolphin-only Qt helper owns toolbar/navigation-button hover,
press/release/checked/focus, tab hover/active state, path-editor focus and native
Places hover/selection/focus. `motion.h` uses QVariantAnimation with OutCubic:
fast100ms, hover140ms, state160ms, scaled by native widget duration relative to
normal200ms. These reuse grounding concepts without changing canonical tokens.
Native QSS/style remains responsible for final paint. Controls retain geometry,
hitboxes, accessible/native events and selection/action semantics. Event filters
return false; no file model or upstream provider is replaced.

Stable effects are disabled and native painting is idle. Only transitions blend
cached transparent native frames; interruption restarts from the actual last
presented frame. A one-shot show capture primes initial state. Native Places
data/model/device-state updates and typed path content cancel immediately;
bounded signal connections disconnect on model replacement and target lifetime.
No permanent polling/repaint timer, daemon, framework or QML layer is introduced.
The helper links KDE KConfigCore, already used by Dolphin, for preference reads.
Menu/header motion is deferred. Files/loading/scrolling/thumbnails/drag/drop,
filesystem operations and large file-selection populations are not animated.
KWin retains window open/close/minimize/restore/geometry/compositor ownership.

### Preference evidence

- **KNOWN:** active Qt/Kvantum exposes SH_Widget_Animate=1 and
  SH_Widget_Animation_Duration=200; active Kvantum animate_states=true supersedes
  the historical false snapshot. Both native widget disable hints are respected.
- **KNOWN:** KDE AnimationDurationFactor=0.25 is active. Its positive value remains
  KWin's clock; zero is respected as explicit animation disable. Isolated native
  zero trials show immediate final state, no running hover/tab/Places transition.
- **KNOWN:** current Noctalia profile has no motion override; inspected pinned
  implementation defaults enabled=true/speed=1. Those are shell preferences.
- **UNKNOWN/MISSING:** shared cross-app reduced-motion authority and live reload
  of cached KDE preference. Reopen Dolphin after a KDE preference change. No new
  settings/synchronization system is added; uncertain native disable hints fall
  back conservatively to immediate final paint.

### Isolated and runtime validation

- **PASS:** `validate-motion.py` at1x and process1.5x verifies intermediate pixel
  changes, no-snap reversal,30 rapid reversals, exact final QSS colors, native
  press/release/checked/focus, active tabs, Places delegate/selection retention,
  immediate native content invalidation, unchanged hit geometry, native motion
  disable and30 controls destroyed mid-transition with clean fixture shutdown.
  A measured stable-control paint count guards against repeated idle repaint.
- **PASS:** real Wayland Dolphin captures at1x/1.5x show short toolbar, tab and
  Places transitions and native final state. Native Qt mouse/focus events drive
  the checks; physical mouse/keyboard hardware coverage is NOT RUN.56 sampled
  transition frames per trial supplement mid/reversed/settled captures. Actual
  native state/disabled behavior is checked; parsing/build alone is not evidence.
- **PASS:** real2000-file fixture directory, repeated hover and tabs/Places,
  no motion effect on KItemListContainerViewport. Five consecutive one-second
  stable samples report zero file-view/root-window paints at both scales, with
  approximately0.0036–0.0046 process CPU seconds per one-second sample. The Phase2
  control at1.5x also settles to zero paints. Startup/loading peaks occur before
  stable state in both versions and are not attributed to new motion.
- **Corrected before gate:** the first always-enabled effect caused idle root
  repaints. Stable native bypass and conditional unchanged tab-close masks
  eliminated that feedback. A snapshot experiment outside Qt effect paint
  context failed the isolated fixture and was rejected; final snapshots use
  transparent native widget rendering while disabled. It was never installed.
- **PASS:** helper build, atomic deployment and installed/source-built equality;
  existing QSS checks at both scales, icon/provenance/native fallback checks,
  token identity validation and integrated offline harness.
- **FAIL, preexisting:** graceful diagnostic window teardown still exits139.
  Same probe/control with Phase2 helper also exits139; Typography already
  reproduced it with the pre-pass helper. Repeated probe open/close is therefore
  not a clean real-Dolphin lifetime PASS. Isolated new-control destruction passes.
- **FAIL, preexisting visual:** native file rows can overlap status/header bounds
  in the long-list capture. Phase2 control captures also exhibit this; existing
  clipping/layout is outside this paint-only pass and is not silently repaired.
- **UNKNOWN:** all runtime device/MTP/storage states, thumbnail formats,
  complete RTL/accessibility coverage, cross-app motion preference synchronization,
  all physical fractional-output/compositor combinations and independent Recovery.
- **NOT RUN:** physical mouse/keyboard matrix, filesystem mutation operations,
  full live failure/login/Recovery switching. Private fixture selection/read tests
  do not certify these contracts.
- **NOT APPLICABLE:** new architecture, content icon replacement, new type family,
  global settings migration, KWin/window animations or further Dolphin redesign.

Private probe sources, isolated configs, logs and PNG evidence remain in
`~/.cache/ricy-dolphin-identity-motion/motion/`. `verified-1x-*`,
`verified-1_5x-*` and `verified-disabled-*` record the final candidate; the
`final-before-1_5x-*` Phase2 control and earlier iteration records retain failures
instead of hiding them. No private runtime captures are committed to the kit.

### Rollback and integrated outcome

The initial Motion helper-only installation saved Phase2 at
`~/.local/state/ricy-dolphin-backups/20261011-231749-708289`. Subsequent atomic
installs preserve their own printed manifests. To remove all Motion iterations,
restore that initial manifest with existing `apply.py --restaurar BACKUP` and
reopen Dolphin; Typography/Iconography remain. Restore other phases in reverse
order if needed. Source rollback reverts the Motion commit; reproduction scripts
always build current source. No service/default/global-theme reset is required.
The final transparent-snapshot build was installed with additional backup
`~/.local/state/ricy-dolphin-backups/20261011-232158-039103`; installed SHA-256 is
`dbd9a003559c1c502765eb624cc2f54c3c5e938d3f2cb1d08017c09d72475f47`.

Integrated regression: system-aligned typography, optional Tabler chrome plus
native KDE content inheritance, paint-only interruptible motion and stable idle
are PASS within the described evidence. `scripts/verify all` with the matching
Noctalia5.2.1 source/patch passes architecture, shell and Recovery offline with
zero failures/unavailable checks. Static scope review preserves filesystem/
FileManager1/MIME/default-handler/KIO/Solid/native model/Recovery contracts and
all canonical token bytes; it does not replace unrun live contract tests. KWin
and its window motion are untouched. Stop here; no later redesign phase begins.

### Changed repository files across all three phases

- `docs/CHANGELOG.md`
- `docs/DESIGN-SYSTEM.md`
- `docs/DOLPHIN-BASELINE.md`
- `docs/NOCTALIA-VISUAL-GROUNDING.md`
- `ricy-kit/contributions/dolphin-blur-corners/README.md`
- `ricy-kit/contributions/dolphin-blur-corners/build-ui.py`
- `ricy-kit/contributions/dolphin-blur-corners/motion.h`
- `ricy-kit/contributions/dolphin-blur-corners/ui.cpp`
- `ricy-kit/contributions/dolphin-blur-corners/validate-motion.cpp`
- `ricy-kit/contributions/dolphin-blur-corners/validate-motion.py`
- `ricy-kit/contributions/dolphin-noctalia-identity/README.md`
- `ricy-kit/contributions/dolphin-noctalia-identity/apply-icons.py`
- `ricy-kit/contributions/dolphin-noctalia-identity/apply-motion.py`
- `ricy-kit/contributions/dolphin-noctalia-identity/apply-typography.py`
- `ricy-kit/contributions/dolphin-noctalia-identity/apply.py`
- `ricy-kit/contributions/dolphin-noctalia-identity/dolphin.qss`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/LICENSE`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/README.md`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/index.theme`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/provenance.json`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/application-menu.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/dialog-close.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/document-close.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/edit-find.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/go-next.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/go-previous.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/go-up.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/tab-new.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/view-list-details.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/view-list-icons.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/view-list-tree.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/view-refresh.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/icons/Ricy-Dolphin/scalable/actions/view-split-left-right.svg`
- `ricy-kit/contributions/dolphin-noctalia-identity/validate-icons.py`
- `themes/tokens/SEMANTICS.md`

The private active Noctalia configuration, Dolphin view-font flags, installed
QSS/helper and optional overlay are deployment state outside this tracked list.
Canonical token JSON, window effects, provider/handler/default registrations and
Recovery implementation have no changes in this pass.

## Motion transition color regression — 2026-10-11

**Original intermediate-color behavior: FAIL. Correction: PASS in the tested
Qt/KIO and native Dolphin color sequences at1x/1.5x.** A user screenshot revealed
gray Places selection and faded icons/text during interaction. This is a Motion
regression introduced by `0c687a8`, not a preexisting palette problem. The original
Phase3 validation did not compare common selected pixels/alpha through rapid
native hover transitions; its PASS was insufficient for this case.

The control uses the installed pre-correction helper, identical QSS/config and
native Documents/Places surfaces. It reproduces gray selection in the window:
the selected pixel begins at #cba6f7/alpha255 and deviates in all24 sampled frames,
with alpha falling to153 and image colors washing out. Native background
composition makes those altered image pixels appear gray in the window.

### Local correction

`motion.h` replaces opacity-modulated CompositionMode_Plus with complementary
integer interpolation of premultiplied channels. Clamping/opacity no longer
changes common opaque color pixels. `PlacesResultPaint` also supplies explicit
view/index and scoped native Places context, so style dispatch does not depend
on a painter device being a QWidget during offscreen capture. This follows the
existing file/header paint-context convention, with stack lifetime/restoration.
No new palette values, settings, geometry, model/provider/delegate replacement,
Noctalia, KWin, default/handler or architectural contract is introduced.

### Validation and limits

- **PASS:** updated `validate-motion.py` compiles the real UI style and Places
  adapter, retaining existing interaction/interruption/disable/lifetime checks.
  At1x/1.5x, selected accent/opacity remains consistent in intermediate capture
  and24 rapid hover changes; settled nonselected rows have no residual backing.
  The previous source fails this same test with a washed-out mid-frame color.
- **PASS:** real Wayland Dolphin Documents/Places before/after screenshots and
  native Qt input sequence. Both corrected scales preserve #cba6f7/alpha255 in
  all24 sampled frames (zero bad frames), while the original produces24 bad
  frames. No physical mouse movement is required by this private probe.
- **PASS:** QSS/state/geometry fixtures at both scales; helper build/atomic
  install equality; architecture/token checks and whitespace. Canonical token
  JSON and content icon/providers remain unchanged.
- **UNKNOWN:** live idle/performance comparison in these color trials. An
  unrelated tab-hover animation remained active during the purported idle sample
  in both old and corrected helpers; a later1.5x trial also received333 mouse
  moves. These samples are not stable-idle evidence. The isolated stable-control
  repaint test still passes; previous Motion idle records retain their scope.
- **FAIL, preexisting:** native diagnostic process teardown still exits139 in
  both versions. This correction does not certify real Dolphin shutdown.
- **NOT RUN:** complete hardware/input/RTL/device matrix and live Recovery.
  The extra native KDE-zero trial produced no usable probe record; current
  isolated native-style disable checks pass, without a new live-disable claim.
- **NOT APPLICABLE:** redesign, icon/font migration, new architecture or KWin
  changes. This is a local correction within the existing helper.

Private evidence is in `~/.cache/ricy-dolphin-places-color-fix/`:
`before-1x-{mid15,settled}.png`, `before-1x.log`, `before-fixture.log`,
`after-1x-{mid15,settled}.png`, `after-1x.log`, corresponding `after-1_5x-*`
and `settled-*` traces. Intermediate diagnostic/fixture attempts are retained
with their failures. No screenshots/profile state are published in the kit.
Only `motion.h`, `ui.cpp`, the existing motion validator/driver and their
documentation change. New Dolphin processes load the correction; existing
mapped helper libraries remain valid and require closing/reopening the window.
The scoped helper installer preserves a private manifest of the pre-fix library:
`~/.local/state/ricy-dolphin-backups/20261011-234907-430907`.
Restore that printed manifest using existing `apply.py --restaurar BACKUP`,
then reopen Dolphin. Source rollback reverts the correction commit alone.
