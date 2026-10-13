# Dolphin with identity Noctalia

## 2026-10-13 — Rounded native terminal surface

The existing helper clips only the embedded Konsole display and paints its
subtle inset shadow. QSS/card geometry and the native terminal profile remain
unchanged. See the [implementation and checks](../dolphin-blur-corners/README.md#rounded-embedded-terminal-with-inset-shadow--2026-10-13).
The helper-only backup uses `apply.py --restaurar BACKUP`; reopen Ricy Dolphin
after restoration. Plasma and global KDE settings receive no change.

## 2026-10-13 — Unlocked panel controls and terminal spacing

The existing QSS styles native dock close-button backings with the established
card, hover, and accent roles. The helper owns their 28px hit area, 16px glyph,
title alignment, and the uniform junction above the bottom terminal; see the
[implementation and validation record](../dolphin-blur-corners/README.md#unlocked-dock-headers-and-terminal-junction--2026-10-13).
This supersedes the former QSS-only title padding. Native panel locking,
close/reopen, terminal content, and card padding are preserved. The private
QSS/helper backup follows `apply.py --restaurar BACKUP`; reopen Ricy Dolphin to
load restored files. Plasma and global KDE settings receive no change.

## 2026-10-13 — Match auxiliary-panel padding to file cards

Information, Folders, and Terminal panels now reuse the file card's 8px inner
padding and 4px top/interior side gutters, with 8px bottom/window-edge gutters.
The existing helper applies matching real layout margins after lazy layout
creation; QSS alone does not reserve QWidget layout space. Edge properties are
shared with file cards, including terminal panels spanning both window edges.
This supersedes the earlier auxiliary-panel inset without outer gutters.

PASS: live 1x Dolphin capture of Folders/Information alongside the file card,
isolated native panel rendering, source/installed equality, QSS checks at
1x/1.5x, motion/plugin-lifetime checks at 1x, architecture, and whitespace.
Live terminal padding, floating panels, live 1.5x desktop, and Recovery NOT RUN.
Only Ricy QSS/helper changed; existing user windows retain their mapped helper.
A new Ricy process was opened to load the matching pair. Private QSS/helper
backup and the existing `apply.py --restaurar BACKUP` route preserve rollback;
reopen Ricy Dolphin after restoration. Plasma and global theme settings remain
unchanged.

## 2026-10-13 — Settings, auxiliary panels, and status controls

The existing Ricy-only QSS now extends the established surface/card, text,
accent, focus, and radius roles to settings and toolbar configuration dialogs.
Buttons, list navigation, combo/spin fields, and group frames retain native
actions and keyboard behavior. Check/radio indicators remain native. Information,
Folders, and Terminal panels use borderless solid cards; embedded terminal text,
font, profile, and rendering remain native. The existing Qt helper gives these
panels an 8px content inset after their lazy layouts become available.

The zoom slider uses the existing accent and outline. The native disk-space
layout formerly left only 14px for its text inside a 30px status row. The helper
removes its inherited vertical margins; the scoped status button uses compact
padding. Only the disk-space KCapacityBar receives flat capsule paint from its
native value, preserving providers and tooltips. Other KDE capacity bars keep
their native style. New processes are required for helper changes; live QSS
updates alone do not reload the mapped helper.

PASS: native Dolphin captures of settings, toolbar configuration, auxiliary
panels, and readable disk-space/zoom controls at 1x; source/installed helper and
QSS equality; existing motion/lifetime and extended QSS keyboard/state checks
at 1x and 1.5x; architecture and whitespace checks. Narrow windows still use
native text elision and metadata wrapping. Composited popup coverage, all
settings pages, a live 1.5x desktop, transfers, and Recovery round trips NOT RUN.
This extends the existing Qt/QSS adaptation without changing ownership,
canonical tokens, global KDE/Kvantum settings, launchers, or KWin code. The
private QSS/helper backup uses `apply.py --restaurar BACKUP`; reopen Ricy Dolphin
after restoring. The native Plasma/Breeze process receives no Ricy helper or QSS.

## 2026-10-13 — Borderless main content panel

The Ricy-only `DolphinViewContainer` outline is transparent. Its existing 1px
border slot preserves content geometry; fill, radius, padding, and margins stay
unchanged. This QSS rule also applies to each content pane in split view. The
native Plasma/Breeze process receives no stylesheet update. Ownership and
dependencies remain the existing Dolphin Qt/QSS adaptation.

PASS: source, installed QSS, and the running Ricy process stylesheet match;
existing QSS interaction checks and architecture checks pass. Visual NOT RUN:
the target window was not visible in desktop captures. Live Recovery NOT RUN.
The private QSS-only backup uses the existing `apply.py --restaurar BACKUP`
manifest format; reopen Ricy Dolphin after restoration. No global KDE theme,
launcher, helper binary, or file-access dependency changes.

Kvantum's exclusive Ricy-Dolphin variant, derived from KDE-Noctalia/Catppuccin MIT installed. Background #181825, text #cdd6f4, secondary #a6adc8, contour #46485c, control cards #313244 and featured #977dba/#cba6f7. The interface and all three file modes inherit the active KDE/Qt application font. Controls of the bar, fields and tabs have corners of 8 px. Menus preserve the existing KDE-Noctalia compact variant. Breeze Dark Icons and preserved archive operations.

The theme is assigned only to dolphin in Kvantum/Applications. Launcher ricy-dolphin injects Qt sheet and transparency helper. Desktop, FileManager1 service and drop-in plasma-dolphin.service use the launcher. The current version requires sister contribution dolphin-blur-corners, which contains the Qt compiler. Background 0,70 with blur, area of translucent, rounded archives of 12 px and native external corners of 16 px by the optional KWin effect. The side uses chip involving icon + name; lines, hover, selection/focus and file header use rounded capsules, keeping the drawings and native events. Read your README for compilation, evidence, version update, and reverse corners.

Global KDE source, archive operations, MIME and Noctalia preserved. Breeze maintains native title/buttons. Existing processes without alpha require closing and reopening Dolphin to load everything; the applicator preserves open windows. Direct execution of /usr/bin/dolphin do not inject helper/QSS: use normal launcher or ~/.local/bin/ricy-dolphin. No Dolphin system file is replaced.

## Reproduce

Prerequisites: Plasma Wayland, Dolphin, Qt/Kvantum, KDE-Noctalia installed, the active system font, Qt6/headers, g++, pkg-config, Python, qdbus6, kwriteconfig6, kbuildsycoca6 and user systemd. 5.2.1, KWin 6.7.5.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-noctalia-identity"
python apply.py
```

The applicator preserves previous files in private backup 0700 and assignments of other applications. Apply QSS via D-Bus to open Dolphin processes without closing them. New windows by launcher also load the new variant; old windows may require reopening to update theme/file sources. Do not restart the daemon or close windows, avoiding interrupting transfers. Reapplications create new backups; reverse in reverse order.

## Restore

```bash
python apply.py --restaurar "$HOME/.local/state/ricy-dolphin-backups/DATA-HORA"
```

Restores entire files and previous absences; can replace later editions of the same files. Reabra Dolphin to load the previous state. In the first opaque version there were two applications: reverse 20261010-210632-242640 And then 20261010-210604-287127. Do not remove packages or change personal files.

## Verification carried out

Inspected captures of a new window before/after: proportional source, sidebar/unified background, rounded controls. Conferred attribution Kvantum, three mode fonts, stylesheet in process, desktop-file-validate and systemd-analyze --user verify. SVG XML, Python syntax and configuration checked. Only conference windows created by the agent have been closed. The existing Home window has been preserved. For current blur and corner validation, see dolphin-blur-corners/README.md. Not tested transfers, all actions, new sessions, all dialogs/monitors or other installation. No final user visual confirmation for icons + header. Initial chips have been approved. Captures and backups are not published in the kit.

Primary theme reference per application and Kvantum options: https://github.com/tsujan/Kvantum/blob/master/Kvantum/doc/Theme-Config ViewFont/UseSystemFont source: https://github.com/KDE/dolphin/blob/master/src/settings/dolphin_detailsmodesettings.kcfg


## Sidebar side padding — 11/10/2026

KFilePlacesView receives padding-left/right 8 px on the Qt sheet. Viewport backend moves together titles, icons, chips and capacity bars without shifting only the design of the delegate. Applicator created private backup ~/.local/state/ricy-dolphin-backups/20261011-085235-777886. New window capture confirmed backwards titles/icons/chip; sidebar does not touch the left. QSS also applied to existing instances without closing them. Source/helpers and header spacing preserved. Revert: apply.py  --restaurar BACKUP and reopen Dolphin. Not tested scrollbars/drag-drop in all widths.


Update 11/10/2026: helper installed by atomic exchange, preserving library mapped by open windows. Native delegate of preserved sidebar. Expandable folders/navigation on enabled compacted; '+' selection disabled. Chips cut to viewport with child indentation to the father's icon. Evidence, approval, limits and backups in the final section of the brother README.


Update 11/10/2026: tabs like Noctalia buttons (#)313244 neutral, #cba6f7 active/#11111b text, #977dba hover), radius12/range6; sidebar/topbar on alpha0 background,70 and panel of archives #181825 Alpha96 with radius12. Subfolder arrows4px further in. Current state uses KWin native blur; previous references to ricyblur describe history. Details/evidence/backups in README dolphin-blur-corners, final section.


### Review — opaque panel and tab closure — 2026-10-11

Main area uses #313244 solid (alpha) 255), as Noctalia panel referenced by the user. Sidebar/topbar remain on #181825 alfa178, with preserved native KWin blur. Helper repositions the native tab buttons before painting, with 12px of external indentation (includes 3px margin); preserves closing signals and actions. Previous QSS subcontrol did not move the button in the actual Dolphin. Capture/probe in the application confirmed RGBA panel(49,50,68,255), shell alfa178 and retreat12 in the three tabs. Final backup: ~/.local/state/ricy-dolphin-backups/20261011-092428-218159; previous in this sequence: 20261011-092338-169456. Helper uses atomic installation; new code requires new window.


### Revision — sidebar/topbar on an L panel; side buttons — 2026-10-11

At user request, sidebar and topbar now share a single opaque panel #313244, equal to the main panel. ShellPanel is a child QWidget behind the controls: draws the entire L with radius12, margin8 and gutter8 for the archival area, without receiving input or changing the layout. Geometry accompanies the visible containers (including more than one area), resizing and concealing the dock; without sidebar drawing only the topbar panel. The outer margin continues on the alpha178, translucent shell with preserved KWin bluff. This review replaces the internal transparency of the previously registered sidebar/topbar.

Side items are buttons of uniform width: neutral #242435, hover #977dba, selected #cba6f7, contour #46485c, radius8.Native icons24, list spacing1 and vertical indentation2 leave 6px between buttons. Side padding 12; HighlightedText #11111b palette, preserving native drawing of active/inactive text and icons. KFilePlacesView keeps its original delegate, clicks, shortcuts, drop, capability indicators and device actions. Icon size is recorded by KIO in dolphinrc, included in backups.

Checks: helper compiled/installed atomically; capture in the real Dolphin confirms continuous L and buttons; lateral test passed21 clicks/21 navigations without switching delegate. Fixture Qt confirms connected arms, free clipping for content, no mouse capture, resize and hidden sidebar. Not validated all RTL layouts or floating docks. Final backup: ~/.local/state/ricy-dolphin-backups/20261011-093607-825801. Before this sequence: 20261011-093205-549123followed by 093320-666039 and 093439-242103 (even date prefix). To reverse the entire sequence, restore in reverse order. New code requires new window.


## 2026-10-11 — Places aligned with Noctalia search results

KNOWN: user-approved normal rows are transparent and borderless; selection
uses accent with on-accent text, including when Places lacks focus. Hover
uses the existing hover-selection color at alpha65. Radius8 and panel/L
geometry are preserved. Native icons are 16px; semibold labels keep a 6px
icon gap. The native 24px-icon row slot is retained, with list spacing3
(6px between rows). These values update only the Dolphin adaptation in
the canonical token source; retained legacy/transport snapshots and
SHA256SUMS are historical and remain unchanged.

The helper retains the original default KFilePlacesView delegate and its
KIO timers/connections. A column-only paint adapter forwards size, painting,
help and editor events to that still-live delegate, normalizes the item
origin for KIO's label geometry, and supplies the selected text palette.
It does not replace/delete the default delegate or intercept navigation.
Applicator installation remains atomic with the existing private backup
and restore path. Most recent pre-application backup:
`~/.local/state/ricy-dolphin-backups/20261011-181156-397343`; earlier
iterations in this revision: 180945-849849, 181007-994984, 181148-655625
(with the same date prefix). Restoring whole files can replace later changes.

Validation: PASS helper build; Qt/KIO fixture asserts default delegate
identity, semibold labels and dark selected text without focus, then passes
21 clicks/21 navigations. Live Dolphin capture verifies the search-style
normal rows; user confirmed the final smaller-icon/padding revision.
NOT RUN all devices, drag/drop, every scale/monitor or session recovery.
No KWin effect, shell/default switch or transport-kit synchronization.


## 2026-10-11 — Rounded rows and padded navigation header

KNOWN: file/folder row backing, selection, focus and visible/nested clipping
now share radius6 (the existing native medium radius), rather than capsule
radius10. Existing visible-width bounds and parent-icon nesting inset remain
unchanged. The shared header backing also uses radius6. Places/tabs retain
their approved treatments.

The top toolbar uses spacing8 and vertical/horizontal padding8/16; action
buttons retain minimum20px content with padding4/8. The location bar uses
the existing scoped neutral #242435, outline, radius8 and height36, with
internal layout padding4/8. Breadcrumb hover is hover-selection alpha65,
radius6; the native path editor has padding4/8, radius6 and accent focus.
KIO's mode switch resets the navigator's fixed height: the helper keeps
both height limits at36, preventing the earlier bottom-edge clipping and
keeping the two modes aligned with toolbar actions. Native segment menus,
URL completion and editing are retained.

PASS: helper build/atomic application, live Dolphin captures of breadcrumbs
(including hover) and editable path, and Qt/KIO fixture with10 mode toggles,
visible native editor and unchanged URL. Captures/probes remain private.
NOT RUN all nested depths, overflow layouts, RTL, monitors/scales or session
recovery in this revision. Canonical scoped tokens are updated; legacy
transport copies/manifests are unchanged. Latest private backup:
`~/.local/state/ricy-dolphin-backups/20261011-182112-225971`. Earlier backups
in this revision are181607-044728,181738-794586 and181910-844955 with the
same date prefix. Existing whole-file rollback applies; reopen Dolphin
for helper-code changes. No compositor or shell/session switch.

## 2026-10-11 — Aligned breadcrumbs and path input

Breadcrumbs now have a transparent container and centered28px native buttons
inside the36px navigator. The user accepted the breadcrumb alignment. Editable
mode alone uses surface (#181825), accent2px border and radius8. The combo has
left/right padding12/8; its native editor has horizontal padding12 and zero
vertical padding. The native clear button overrides inherited toolbar minimum
dimensions and padding, keeping its icon vertically centered.

PASS live Dolphin capture: folder/text inset and centered clear icon. The
native clear button is22x18 at y7 inside the32px editor, matching their centers.
PASS native Qt/KIO fixture:10 mode switches with editor/URL retained. PASS
architecture verification, token validation and diff whitespace. NOT RUN all
widths, RTL, scales or live recovery. Latest private backup:
`~/.local/state/ricy-dolphin-backups/20261011-183250-171013`. Existing atomic
application/whole-file rollback remains; transport kit/manifests, compositor
and Noctalia are unchanged.

## 2026-10-11 — Native menus, scrolling and contained panels

KNOWN: Dolphin context menus use an opaque card/outline panel with radius12,
padding8 and radius6 accent-selected action rows. Native popup flags, submenus,
shortcuts and folder-color widget actions are retained; translucent window
corners allow the rounded panel to expose the desktop.

All Qt scrollbars use a6px dark neutral (#242435) track, radius3 and a minimum
24px thumb. The thumb uses existing secondary text at50% opacity, with secondary
hover and accent press. The user accepted the scrollbar treatment. Native drag
selection uses radius6, hover-selection alpha65 and accent-outline alpha150,
retaining Dolphin's rectangle/hit testing and animation opacity.

The card backing belongs to DolphinViewContainer, which contains the native
viewport, scrollbars and status area. Actual layout insets reserve the painted
gutter plus8px content padding; the Places dock reserves12px at its bottom.
Internal card gutters are4px; outer window edges remain8px, including the
rightmost pane and sidebar-hidden left edge. Split panels have a12px gap with
a native4px splitter. Its2px rounded line uses track color normally, the thumb
color/opacity on hover, and accent during drag; native resizing remains intact.
The user accepted the neutral line/gap and requested these interaction states.

GUI wrapper launches add --new-window to avoid reusing a process with an old
mapped helper. Explicit --new-window and FileManager1 --daemon are preserved.
The existing KDE Dolphin shortcut component was refreshed in the live session
after its cached service continued launching /usr/bin/dolphin; Meta+E is still
assigned to Dolphin and the user confirmed the corrected appearance. This is
a shared existing KDE integration, not a claim of independent Recovery.

Validation: live Dolphin menu and split-panel captures; native Qt fixtures for
menu keyboard activation, submenu/widget actions, rounded selection painting,
scrollbar orientations/keyboard scrolling, divider states and native resizing.
Static architecture/token/whitespace checks are recorded in CHANGELOG. NOT RUN
all display scales, RTL, floating docks, every popup/dialog or live recovery.
Private captures/probes remain outside the repository. Latest private backup:
`~/.local/state/ricy-dolphin-backups/20261011-192442-284891`. Whole-file rollback
and atomic helper installation remain; helper updates need a new process.
Historical transport snapshots/manifests, Noctalia and KWin remain unchanged.

## 2026-10-11 — Popup corner cutouts and icon inset

Menus/submenus now suppress native background autofill, use a transparent
Window palette role and a radius12 surface mask matching the existing rounded
QSS backing. The panel fill/border remain; corner cutouts are excluded from
the native surface. Native icons move8px inward and label left padding is20px
(existing12px plus8px), preserving the icon/text gap rather than compressing it.

PASS helper compilation/atomic application and Qt menu fixture: transparent
corner pixels, corner-excluding mask with rounded edge retained, visible native
icon inset, keyboard action, submenu and widget action. PASS architecture/token
checks and diff whitespace. NOT RUN every live submenu, RTL or display scale.
Latest private backup: `~/.local/state/ricy-dolphin-backups/20261011-192959-179609`.
Helper surface changes need a new process; QSS is applied to existing windows.

## 2026-10-11 — KDE menu proportions

The user's configured KDE-Noctalia Menu/MenuItem geometry provides the reference:
12px panel framing and4px item vertical padding. Dolphin now uses panel padding12,
item padding4/12 and vertical margin1, replacing the taller6px-padding rows.
The8px native icon inset remains; text padding returns to12px to match the
reference's closer icon/text relationship. Separators are transparent4px gaps.
The existing rounded surface, colors, native actions and corner cutouts remain.
PASS Qt capture and menu fixture (icon inset, transparent corners, keyboard
action and native submenu/widget action), architecture/token/whitespace checks.
NOT RUN all live submenus, RTL or display scales. QSS updates existing windows.
Private backup: `~/.local/state/ricy-dolphin-backups/20261011-193208-529316`.


## 2026-10-11 — Tab overflow and containment

The existing Qt helper reserves space for overflow arrows, masks close controls
on clipped tabs, keeps the final tab inside the shell when all tabs fit, and
uses the existing purple accent for a wider rounded overflow indicator.
See the [helper implementation and validation record](../dolphin-blur-corners/README.md#2026-10-11--tab-overflow-spacing)
for geometry, LTR/RTL checks, visual evidence and the preexisting probe-teardown
failure. Ownership and Recovery dependencies remain unchanged.

The helper was installed atomically with restorer-compatible private backups.
Use `apply.py --restaurar BACKUP` with the backup printed by installation;
whole-file rollback can replace later helper updates. Existing processes keep
their mapped helper; launch a new Dolphin window for the update. No private
backup contents, compiled helpers or captures are included in the repository.

## First visual polish pass — 2026-10-11

The current audit, state classification, rejected native status experiment,
Recovery limits and separate backlog are recorded in
[Dolphin baseline](../../../docs/DOLPHIN-BASELINE.md#first-visual-polish-pass--2026-10-11).
QSS now normalizes residual generic padding to the existing 4px spacing, preserves
checked/pressed toolbar interaction colors through hover, supplies accent focus
contours without changing border geometry, and keeps disabled tools unfilled.
Approved tabs, Places, file states, popup materials and the newer tab-overflow
helper remain intact. Values remain owned by the canonical token contract.

This pass installs only QSS atomically. Do not run the full applicator as a test:
it also rewrites launchers/services and native configuration. The normal native
small status mode is retained; the tested full-width setting was reverted.
Existing wrapper/helper/theme Recovery coupling and the preexisting Qt teardown
crash are not solved by appearance changes. The private rollback manifest follows
this contribution's existing restorer format and targets only QSS and dolphinrc.

Offline checks (PyQt6 required; no desktop settings or file operations changed):

```bash
python3 -B ricy-kit/contributions/dolphin-noctalia-identity/validate-polish.py
QT_SCALE_FACTOR=1.5 python3 -B ricy-kit/contributions/dolphin-noctalia-identity/validate-polish.py
```

These exercise real Qt state precedence, painting and native editor/tab/menu
signals. They do not load the helper or prove compositor masks, device behavior
or live Plasma Recovery. Captures use the registered wrapper's normal environment;
incomplete isolated-theme captures are not current visual references.


## 2026-10-11 — Toolbar dropdown arrow padding

Ordinary toolbar menu indicators use existing 6px glyph boxes with 4px inward/
bottom offsets. Split buttons style the menu surface and its centered arrow
jointly so Qt does not paint both native and custom indicators. The menu region
uses 16px with compensating 12px right padding: the measured primary action width
remains 76px while the menu target grows from 12px to 16px. This supersedes the
initial inset-only rule that caused duplicate arrows and separator clipping.
Native icons, actions and popup modes are retained. QSS is installed atomically
with private rollback backups; available live sheets are refreshed without
closing windows. PASS Qt preview/state checks, single-arrow visual inspection,
primary geometry and architecture/token checks. NOT RUN full live menus, RTL,
all scales or Recovery. No helper, KWin or launcher/default change.

## Identity & Motion Pass — Typography

Family/size hardcodes have been removed from QSS and the native header helper.
The normal applicator selects UseSystemFont=true in all native view modes and
preserves dormant personal ViewFont settings. Places keeps inherited-family
semibold. The explicit, scoped one-shot installer also synchronizes the official
Noctalia shell family; it does not change shell sizes/scales or KDE font settings:

```bash
python3 -B ricy-kit/contributions/dolphin-noctalia-identity/apply-typography.py \
  --noctalia-config /absolute/path/to/active/noctalia/config.toml
# In the running shell's NOCTALIA_CONFIG_HOME/NOCTALIA_STATE_HOME environment:
noctalia config validate
noctalia msg config-reload
```

PyQt6 queries the active Qt platform font; the helper uses the existing build
prerequisites. No daemon/watcher is introduced. Do not use an offscreen platform
or substitute captured token families when synchronizing an active desktop.
Source and installation ownership remain in the existing contributions.

See the [phase validation and rollback record](../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-1-typography--2026-10-11).
Typography is PASS in its inspected scope; the preexisting shutdown FAIL and live
Recovery UNKNOWN remain explicit. The installer prints a private backup compatible
with `apply.py --restaurar BACKUP`; then reload Noctalia and reopen Dolphin.

## Identity & Motion Pass — Iconography

An optional13-glyph Actions-only XDG overlay supplies Tabler chrome identity.
The existing Dolphin-only helper selects it in-process when valid; missing
overlay preserves the system Breeze theme, and missing names inherit Breeze/
hicolor. Native content/Places/device providers remain unchanged. No global
icon setting or persistent dolphinrc theme override is written.

Use `apply-icons.py` for a scoped helper/overlay installation and the printed
private manifest for existing `apply.py --restaurar BACKUP` rollback. Reopen
Dolphin for helper changes; the full applicator includes the same optional
payload for reproduction. Qt/KF6IconThemes headers are required to build.

[Mapping, licensing, provenance and fallback](icons/Ricy-Dolphin/README.md) and
[phase evidence](../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-2-iconography--2026-10-11)
record PASS within scope and the outstanding shutdown FAIL/Recovery UNKNOWN.
`python3 -B ricy-kit/contributions/dolphin-noctalia-identity/validate-icons.py`
checks scope, provenance and nonempty Qt SVG paint without installing.

## Identity & Motion Pass — Motion

The existing Dolphin-filtered helper adds paint-only, interruptible chrome
transitions. QSS retains the final state, native input/model semantics and geometry
are unchanged, and the effect is disabled during stable native painting.
Run `python3 -B ricy-kit/contributions/dolphin-noctalia-identity/apply-motion.py`
to build/install only this helper atomically, with a printed restorer-compatible
backup. No QSS, font, icon, default-handler or KWin setting is written by this
installer. All phase installers rebuild the current helper source; source phase
rollback therefore also requires reverting the corresponding commit.

Qt Widgets and existing KDE KConfigCore/IconThemes development headers/libraries
are required; Dolphin already uses these native libraries. The helper does not
require Noctalia to run. [Phase evidence and limits](../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-3-motion--2026-10-11)
and [implementation checks](../dolphin-blur-corners/README.md#identity--motion-pass--motion)
record results separately from the preexisting shutdown failure and untested live
Recovery. Reopen Dolphin after restoring a backup; existing mapped libraries
remain valid until their process exits.
