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
