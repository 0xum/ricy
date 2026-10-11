# Dolphin with identity Noctalia

Kvantum's exclusive Ricy-Dolphin variant, derived from KDE-Noctalia/Catppuccin MIT installed. Background #181825, text #cdd6f4, secondary #a6adc8, contour #46485c, control cards #313244 and featured #977dba/#cba6f7. 10 pt in the interface and in the three file modes. Controls of the bar, fields and tabs have corners of 8 px. Menus preserve the existing KDE-Noctalia compact variant. Breeze Dark Icons and preserved archive operations.

The theme is assigned only to dolphin in Kvantum/Applications. Launcher ricy-dolphin injects Qt sheet and transparency helper. Desktop, FileManager1 service and drop-in plasma-dolphin.service use the launcher. The current version requires sister contribution dolphin-blur-corners, which contains the Qt compiler. Background 0,70 with blur, area of translucent, rounded archives of 12 px and native external corners of 16 px by the optional KWin effect. The side uses chip involving icon + name; lines, hover, selection/focus and file header use rounded capsules, keeping the drawings and native events. Read your README for compilation, evidence, version update, and reverse corners.

Global KDE source, archive operations, MIME and Noctalia preserved. Breeze maintains native title/buttons. Existing processes without alpha require closing and reopening Dolphin to load everything; the applicator preserves open windows. Direct execution of /usr/bin/dolphin do not inject helper/QSS: use normal launcher or ~/.local/bin/ricy-dolphin. No Dolphin system file is replaced.

## Reproduce

Prerequisites: Plasma Wayland, Dolphin, Qt/Kvantum, KDE-Noctalia installed, Noto Sans, Qt6/headers, g++, pkg-config, Python, qdbus6, kwriteconfig6, kbuildsycoca6 and user systemd. 5.2.1, KWin 6.7.5.

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
