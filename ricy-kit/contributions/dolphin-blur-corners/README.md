# Dolphin: transparency with Qt and KWin native corners

## Identity & Motion Pass — Motion

`motion.h`, used by `ui.cpp`, owns only QWidget chrome interpolation inside the
existing Dolphin generic plugin. KWin/corners.cpp retains window ownership.
Toolbar/navigation buttons, tabs, path-editor focus and native Places viewport
states use short QVariantAnimation crossfades, starting from the last presented
frame on interruption. Native QSS/style draws final content; geometry and events
stay upstream. Native Places model/device/content changes and path text changes
cancel immediately. No file viewport/content/loading/scroll/drag animation is
installed. Menus and headers retain existing state painting without new motion.

Native Qt SH_Widget_Animate/SH_Widget_Animation_Duration control availability and
local duration scaling; explicit KDE AnimationDurationFactor=0 disables immediately.
Positive KWin factors are not repurposed as widget speed. No Noctalia synchronization
or settings writes are added. Config preference changes may require reopening
Dolphin; live cross-app reload is UNKNOWN. A zero-delay, one-shot show capture
primes initial native paint, and there is no permanent timer/polling. Stable
effects are disabled, allowing normal native painting. State/connections are
owned by controls and cleaned up with them; model replacement disconnects the
previous bounded set of native signal connections.

```bash
python3 -B ricy-kit/contributions/dolphin-blur-corners/validate-motion.py
QT_SCALE_FACTOR=1.5 python3 -B ricy-kit/contributions/dolphin-blur-corners/validate-motion.py
```

The isolated Qt/KIO fixture verifies actual intermediate pixels, interruption,
exact final paint, press/release/checked/focus, native tabs/Places, no repeating
idle paints, disable, fixed geometry and destruction during transitions. It does
not certify the compositor or live Recovery. See the [runtime/visual/CPU comparison](../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-3-motion--2026-10-11)
and scoped `apply-motion.py` in the sibling contribution for installation/rollback.
No canonical identity tokens, layout, filesystem providers or desktop services
change. Historical observations below retain their original scope; the font
hardcode and prior motion absence are superseded by the phase records.

### Motion color regression correction

The original painter-opacity/Plus combination changed common colors and alpha
during interrupted transitions. The helper now interpolates premultiplied image
channels using complementary integer weights, preserving identical opaque pixels
exactly. The native Places paint adapter explicitly retains its view/index and
paint context when KIO draws through QApplication's style into an image.
Geometry, providers, action semantics and palette tokens are unchanged.

The motion validator now compiles the actual `ui.cpp` style/adapter, rather than
testing the animation class alone. It verifies the selected accent and opacity
during capture and24 rapid hover changes, followed by absence of residual hover
backing. See the [correction evidence](../../../docs/DOLPHIN-BASELINE.md#motion-transition-color-regression--2026-10-11).
This supersedes the earlier PASS for intermediate color consistency.

Update of the dolphin-identity-nottalia contribution. The first opaque version was rejected by the user. The current appearance uses background #181825 with alpha 178/255 (~0,70) and compositor blur. The area of archives has contour #46485c, radius 12 px and light fill #313244 (40/255), allowing the blur to remain visible. Texts/icons do not receive window opacity.

Two small and independent components:

- ui.cpp: Generic Qt plugin loaded only by -plugin argument
Launcher Dolphin. Before creating the surface of DolphinMainWindow, WA_TranslucentBackground activates. Allows you to apply the Qt sheet from the opening without preventing the alpha channel. Also installs a Kvantum QProxyStyle for chips: hover/side selection involves icon + name, with content width; list selection/focus accompanies the entire chip, including icons. The native delegate remains responsible for text, section headers, volume actions, capacity bars, tooltips and drag/drop. A QGraphicsEffect per item draws background #313244 (90/255), radius up to 10 px, horizontal margin 3 px and vertical 2 px; drawSource maintains native content. Applied to items with width
  >140 and height <=64 px, covering lines of detail/compacts without putting a
Background in large thumbnails. AlternativeBase/Transparent base remove rectangular zebra. An effect on the header draws the common capsule #313244 (155/255), contour #46485c (150/255) and source Noto Sans 10 The style keeps native labels and arrow sorting, with hover rounded by column. It does not intercept clicks, selection, expansion, sorting or geometry of columns.
- corners.cpp: ricydolphinrounding effect for KWin 6.7.5Attributes BorderRadius
native 16 only normal windows/dialogues of class dolphin/org.kde.dolphin. Fullscreen, partial/complete maximization and tinting receive zero radius. Observe changes in decoration and state; download restores previous radii. Use the renderer and native blur clipping. Do not add shaders, paint passes, polling or animations. isActive=false because it acts by events.

Existing ricyblur provides native blur for applications outside the shell; its shared background remains restricted to Noctalia. Ricyblur has not been modified, nor restarted KWin or Noctalia. Breeze still draws title and buttons, with solid title and KDE font; no new decoration has been created.

## Reproduce

Use KDE-Noctalia/Kvantum installed by the script. To compile the Qt helper: Qt6 Widgets/headers, pkg-config and g++ (qt6-base/base-devel in CachyOS). apply.py of the sister contribution executes build-ui.py, installs the library in the private directory of Dolphin and updates the launcher. The kit contains fonts without .so Precompiled.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-noctalia-identity"
python apply.py
```

To the outside corners, KWin headers 6.7.5/KF6/Qt6/KDecoration3, Vulkan, libepoxy/libdrm/Wayland and compilation tools (dependencies of the Ricy bluff):

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-blur-corners"
python build.py
# The path follows XDG_CACHE_HOME, if defined:
sudo install -D -m 0755 "$HOME/.cache/ricy-dolphin-corners-build-6.7.5/ricydolphinrounding.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricydolphinrounding.so
python enable-corners.py
```

The compiler refuses KWin from another version. Review/recompile when updating KWin; do not copy the old binary. If vulkan-headers is missing, you can specify the included folder compatible with RICY_VULKAN_HEadERS. This session reused the official Vulkan headers already documented in the Ricy cache. Installing the plugin was authenticated by Polkit. Qt helper is installed without sudo.

Use the normal launcher. Existing Dolphin processes may not have an alpha channel and need to be fully closed/reopened to load the helper and theme. Applicator applies the sheet in open instances without closing them; it cannot promise retroactive transparency on opaque created surfaces. It does not interrupt transfers or restart the daemon automatically. /usr/bin/dolphin do not inject helper/QSS; use ~/.local/bin/ricy-dolphin.

## Verify / Restore

```bash
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.isEffectLoaded ricydolphinrounding
qdbus6 org.kde.KWin /RicyDolphinRounding org.ricy.DolphinRounding.status
python enable-corners.py --restaurar "$HOME/.local/state/ricy-dolphin-corners-backups/DATA-HORA"
```

Status is read only: class, type, maximization/tiling and radius, no filenames or titles. The restorer restores the presence/absence of the key in kwinrc and loading status. Unloads the effect and returns the native radii. Do not remove the disk library; after downloading, you can remove it with sudo rm on the installed path. To reverse appearance, use apply.py  --restaurar the sister contribution, then reopen Dolphin. Successive reversals must be made in reverse order. It does not replace fully kwinrc.

Final corner backup in this session: ~/.local/state/ricy-dolphin-corners-backups/20261010-211849-253315. Backup before new appearance with blur: ~/.local/state/ricy-dolphin-backups/20261010-211018-558522. To return to the state prior to chips, reverse the backups in reverse order 20261010-213035-906999, 20261010-212959-440141 and 20261010-212842-374549. Then, to return to the state prior to the blur, reverts 20261010-211713-181764, 20261010-211458-875287 and 20261010-211018-558522. The sister contribution README records the backups of the first opaque version.

## Evidence and limits

Native compilation of both components completed. New window by helper showed alpha 178 RGBA capture background; previous QSS version showed alpha
255. Desktop captures checked blur behind Dolphin with text and icons
clear, rounded and translucent archive area. Individual window captures do not show the composite background and are not enough to check blur.

Native status confirmed lightning. 16 in all normal Dolphin windows observed. Disposable Qt client with Dolphin app-id confirmed normal=16, maximized=0 and restored=16. It was closed when finished; it did not process files. Do not measure frames, nor test all dialogues, monitors/scales, visual tilting or new installation. The user approved the initial chips and asked that they also involve the icons and that the header be adjusted. This final revision was inspected in captures: rounded arrowheader, rounded lines, round solid selection and focus. The inclusion of the side icon is implemented in the painting rectangle, without final visual confirmation of the user. Not tested all cases of renaming, drag/drop, reordering/resizing columns, transfers or very large directories; no cost measurement of QGraphicsEffect. Geometry reading confirms the native configuration, without claiming a pixel measurement of the corners.

The first attempt to update QSS found an instance closed between listing and D-Bus command. Configuration was already applied; the final script treats this race without interrupting the update of the other instances. Ricydolphincorners/ricydolphinshape prototypes were downloaded/disabled and their libraries removed; the final effect uses another name to avoid reuse of the code loaded by Qt. There is no restart of the compositor. Sources of an external effect of corners were consulted in the cache, but no code of this project was used.

Primary sources consulted: KDE KWin v6.7.5 Window:::setBorderRadius, WindowItem::updateBorderRadius, ItemRendererOpenGL and Blur effect; Kvantum Style::setSurfaceFormat/Theme-Config; Dolphin viewing classes. Own implementation under MIT. Base theme credits remain in the brother kit.


## Header hover adjustment — 11/10/2026

Dislocated hover 8 px for before the native start of the column, with vertical insert 3 px and clipping in the common backup (5 horizontal px/3 px vertical). Solves text leaning at the beginning and overflow visual on the wide/rolled columns. HeaderChip provides the limits during drawSource; native labels and sorting remain. Helper recompiled and installed without restarting existing windows. Qt offscreen drawing test confirmed padding before text, upper and lower insert and overflow clipping. No visual validation of all hovers in the actual window; new window opened by launcher for conference. Backup: ~/.local/state/ricy-dolphin-backups/20261011-083312-062208. Revert: apply.py  --restaurar BACKUP and reopen Dolphin.


## Hover Size/Modified — 11/10/2026

Hover includes the native rectangle of the margin sorting arrow 6 px. Last column identified by padding End painting (section-1), or End position of the column itself; its hover reaches the right internal border of the header. Name keeps the previous inserts. Without using translated strings of the columns. Qt test offscreen passed to identify the last column, fill to the right margin, external/vertical limits and arrow inclusion. Backup ~/.local/state/ricy-dolphin-backups/20261011-084408-791214. Revert with apply.py  --restaurar BACKUP and reopen Dolphin.


## Correction: Size text only — 11/10/2026

Enlightened request: Size should have a short chip only around the text, without including arrow. Replaces the arrow inclusion rule of the previous revision. Intermediate columns use SE_HeaderLabel, native alignment/direction and width of the deleted text + 8 px padding on each side. Name and extension of last Modified column preserved. Arrow continues natively drawn. Helper recompiled/installed; Offscreen test checked chip smaller than column, text inside and no fillout next to arrow. Last column continues filling up to the right margin. No final visual confirmation of user. Backup ~/.local/state/ricy-dolphin-backups/20261011-084526-161433. Restore with apply.py  --restaurar BACKUP and reopen Dolphin.


## Size: width of the column without arrow — 11/10/2026

Order correction: chip occupies the width of the Size column, not only the text. Intermediate columns use native rect with insert 3 px on each side, without the negative displacement that swallowed the arrow of the anterior column. When the column itself has sorting arrow, this space is excluded with margin 4 px. Name and Modified preserved. Replaces the rule of width by text. Compilation/installation and offscreen test passed: start inside the column, fill in beyond the label, previous area without hover and arrow reserve. Backup ~/.local/state/ricy-dolphin-backups/20261011-084620-426269. Revert with apply.py  --restaurar BACKUP and reopen Dolphin. No final visual confirmation; old processes need to reopen.


## Internal Padding of the Size text — 11/10/2026

Chip keeps the column width and the limit that deletes the previous arrow. Now the intermediate column label is backed down to ensure 8 px internal at the beginning/end, without moving the chip over the arrow. Name and Modified preserved. Helper recompiled/installed. Qt painting test offscreen passed to fill in the width, reserve the arrow and first pixel of the text at least 8 px after chip edge. New window by open launcher. Backup ~/.local/state/ricy-dolphin-backups/20261011-084751-069063; restore with apply.py  --restaurar Backup and reopen.


## Name: space to the right of the arrow — 11/10/2026

User approved Size padding. Hover of the first column Name now extends the right border on 6 px, keeping clipping on the common header. Size and Modified preserved. Helper recompiled/installed. Offscreen test checked finite extension to the right and maintained Size checks, padding and last column. Backup ~/.local/state/ricy-dolphin-backups/20261011-084856-807309; restore with apply.py  --restaurar Backup and reopen, no final approval from Name.


## Uniform spacing between header chips — 11/10/2026

User approved Size and requested symmetry of spacing. HeaderChipRect centralized geometry: chips end at column limit +3 px; the following starts at this limit +9 px, keeping 6 px between them. Name conserves margin of the arrow, last column reaches the right internal margin. All use vertical insert 3 px and content with minimal padding 8 px; intermediate/final backed labels, without shifting chip over the previous arrow. The arrow of the column itself, when necessary, has area reserved to the part. It does not change width/hit-test of the columns. Compilation/installation and Qt offscreen test confirmed 6 px in both ranges, height/y equal, Modified to the end, text with padding and Size occupying width. ~/.local/state/ricy-dolphin-backups/20261011-085034-172903; restore with apply.py  --restaurar BACKUP and reopen Dolphin. Still no visual confirmation of this spacing; does not measure all sorting/RTL/scroll scenarios.


## Contribution — Stable sidebar, expansion and nested chips — 2026-10-11 (America/Sao_Paulo)

User confirmed that the crash of the sidebar stopped; approved chips accompanying the visible width and the final indentation to approximately the parent folder icon. Removed PlacesDelegate/setItemDelegate: no longer swap native KFilePlacesView. ChipStyle query index/text/icon via public view/model during painting. Preserves connections and events KIO. Core coredumpctl/gdb indicated treatment of KIO events; there are not enough debug symbols for the exact line. Native test KIO QtTest passed 21 clicks/21 UrlChanged signals.

Another cause of crash in updates: copy2 overwrites library inode .so mapped by open processes. Installer now copies to tempfile in the same directory and trades for os.replace. Reapplication preserved previous process 315482 live, without corrupting the loaded library. This replaces in-place installation; previous visual checks did not cover that risk.

Final configuration dolphinrc: DetailsMode/ExpandableFolders=true and LeftPadding=20; General/ShowSelectionToggle=false/BrowseThroughArchives=true. .md it was hover selection, not expansion, and it was shut down. 6 px, dash1,5 #a6adc8 only for PE_IndicatorBranch State_Children; right/low closed/open. Common files have no arrow. QStyleSheetStyle Qt discarded branch with simple QStyleOption; graphics items now use ChipStyle directly, widgets keep QSS. Real Dolphin test in private fixture expanded folder via click, 2→3 lines, indented child and chevron. Compacted navigation enabled; native model expands tree directories, not compressed files. These can be opened via KIO when supported; no arrow without functional action. Not tested all formats.

RowChip intersects items with viewport visible in local coordinates. Rounded background/clip/focus accompany visible width; over cut content. sourcePixmap NoPad with context measures depth by native branch slots. Crop reaches hover/cache selection, redesigned focus on chip to maintain contour after indentation. End state approved: root insert3px; son adds 20px gutter + depth × line height. At height22px, first level begins ~45px, in the parent folder icon; next advance22px. Replaces attempt8px for rejected level as small. Inset3px right, vertical2px/ray up to10px; content/columns not moved. Real viewport captures checked expansion, chevron and indentation. User approved width and indentation.

Probe temporary Qt explicitly loaded and fixture in cache do not enter the kit. Probe library and copy extracted from core removed at the end; preserved user-managed windows. Not tested RTL, hundreds of levels, file scales/formats, transfers, drag/drop or performance.

Backups in ~/.local/state/ricy-dolphin-backups, restore in reverse order to return before the sequence: 20261011-090752-444876, 20261011-090705-662420, 20261011-090614-400487, 20261011-090454-088355, 20261011-090310-602007, 20261011-090132-953293, 20261011-085727-916570- Use it. apply.py  --restaurar BACKUP and reopen. Restorer replaces entire files, and can replace later edits. Do not reapply old installer that overwrites .so. Probe in backups remains private/inactive; launcher only uses ricydolphinui. It can delete libricyprobe.so while restoring snapshot with probe.

Sources/applicant/Readmes synchronized in active/portable kits; hashes checked preserving other inputs. Not included .so, screenshots, core or backups.


## Contribution — Panel and tabs as Noctalia buttons; nested arrows — 2026-10-11 (America/Sao_Paulo)

Request: topbar/sidebar with blur, delimited panel content and tabs with color/Noctalia button format. Also preserve adjustment of nested arrows made before the request amplification. Tabs: neutral #313244/#cdd6f4, outline #46485; active #cba6f7 with text #11111b; hover #977dba/text #000000. Radius12 px, padding6/14 px and margin3 px (range6 px). Swap the tabs pill radius14/translucent Mauve from the previous attempt by buttons as reference. QTabBar::close-button reserve right8/12px; compact tabbar buttons; QTabWidget::pane without edge; helper setDrawBase(false) eliminates baseline. Icons and closing/reordering maintain native behavior.

Root QMainWindow keeps #181825 alpha178/255 (~0,70), sidebar/topbar remain transparent on this background, with alpha channel before creating the surface.181825 alpha96/255 over root, contour #46485c, radius12 and margin/padding8. Replace panel #313244 alpha40; alpha composite measured in window capture ~207/255. Topbar/sidebar measured178/255. Texts and icons do not receive global opacity. Real Dolphin capture new with several tabs showed Mauve/neutral buttons and delimited panel. At the time of this native KWin blur revision is loaded (blueEnabled=true/force5), ricyblur is not loaded or enabled. This state was found in the session and preserved: not reactivated ricyblur, not restarted compositor or Noctalia. Do not confuse this current observation with the previous states documented in this contribution.

Arrows of dislocated subfolders4px inside (RTL opposite direction), when the branch is beyond the root slot; preserved root arrow. Geometry/hit-test native expansion does not change; shift fits in the expansion slot. Cut of daughter chips and content accompanies viewport as approved.

Compilation/helper installed checked and preserved atomic installation. Qt tabs test confirmed preserved defined icons, back down button and deactivated base. Fixture uses synthetic icon, does not validate all Breeze icons. Real Dolphin capture confirmed palette/layout; not tested all tabs, monitors, RTL or all folder levels. A later active window capture caught Codex because the user switched focus; not used as Dolphin evidence. Visual approval of this still pending review.

Private backups in ~/.local/state/ricy-dolphin-backups: end 20261011-091610-462637; to return to the state before this sequence, restore in reverse order also 20261011-091325-096396 and 20261011-091239-713431- Use it. apply.py  --restaurar BACKUP and reopen. Restorer replaces entire files and can replace later edits. Active/portable kits and synchronized local tokens; hashes preserve too many entries. Captures/tests stay in the private cache, without binaries/state/screenshots in the kit.


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


## 2026-10-11 — Tab overflow spacing

KNOWN: the existing Qt helper now reserves a 64px overflow strip for two native
24px scroll buttons, an 8px gap and an 8px trailing inset. Qt's style subelement
rectangles control both tab clipping and native scroll layout; RTL mirrors the
same geometry. Close buttons outside the visible strip receive a mask outside the widget bounds, excluding its hit/paint area; buttons regain their full shape when scrolling/resizing exposes them. Native
signals, tab selection/reordering and the existing 12px close inset remain.
No palette, token, launcher, KWin or Recovery dependency changed. Ownership stays
with the Dolphin Qt helper; plain Dolphin remains independent of this helper.

PASS helper compilation, 18 Qt overflow layouts (300/600/900px, LTR/RTL,
first/middle/last selection), native close/scroll clicks, mask restoration after
removing overflow, and a live Dolphin capture/probe confirming 24px buttons and
8px edge inset. PASS architecture/token checks and diff whitespace. NOT RUN all
monitor scales, live drag/reorder and live Recovery. FAIL probe-process teardown:
SIGSEGV in QGuiApplicationPrivate destruction occurred with both the changed
helper and the preserved pre-change helper, including normal window close.
This preexisting result limits the live validation; it is not a passing exit test.
Only the installed helper was replaced atomically, with a restorer-compatible
private backup at the private backup printed during installation.
Existing processes retain their mapped helper; open a new Dolphin window for this
change. Historical transport snapshots/manifests remain unchanged.


## 2026-10-11 — Contained tab strip without overflow

KNOWN: the Qt helper bounds the horizontal QTabWidget tab-bar allocation with
an 8px trailing gutter, mirrored for RTL. This reserves actual layout space even
when the scroll arrows are hidden, preventing the final tab border from extending
past the shell panel. Existing tab padding, palette, native close/reorder signals,
content-pane geometry and overflow arrow spacing remain. Ownership stays with
the existing Qt helper; no Recovery dependency or KWin change is introduced.

PASS helper build, eight Qt tab-container allocations across four widths and
LTR/RTL with/without overflow, last-tab close, and the previous 18 overflow cases.
PASS live Dolphin capture/probe with seven tabs, hidden arrows and an 8px trailing
bar gutter. PASS architecture/token checks and diff whitespace. The live capture
process again failed at teardown (exit 139); the prior comparison reproduced this
with the pre-change helper. Clean live shutdown remains FAIL for that probe.
NOT RUN all display scales, live drag/reorder and Recovery. Atomic helper backup:
the private backup printed during installation. Open a new Dolphin
window to load the helper; the existing whole-file restorer supports this backup.
Historical transport snapshots/manifests remain unchanged.


## 2026-10-11 — Rounded accent overflow indicator

KNOWN: the Qt helper paints native tab-tear indicators with the existing accent
`#cba6f7`, a 4px width and capsule ends (half-width radius), with 3px vertical
insets. The horizontal tear allocation grows from 2px to 4px so the wider stroke
fits its native clipping geometry. Qt still controls indicator visibility and
placement; arrows, tab actions, shell materials and Recovery dependencies remain.

PASS helper build, LTR/RTL pixel checks for accent color/4px allocation/rounded
tips/native visibility, 18 overflow regression layouts and native close/scroll
clicks, and a live Dolphin capture. PASS architecture/token/whitespace checks.
The existing live capture-probe teardown failure (exit 139) recurred; clean live
shutdown is not validated by this capture. NOT RUN all display scales, live
Recovery and every tab interaction. The installed helper was replaced atomically;
private rollback backup: the private backup printed during installation.
New Dolphin processes load this change. Historical transport snapshots stay intact.


## 2026-10-11 — Rounded path-dropdown control

The user clarified that the purple backing, rather than the chevron glyph, was
intended to match the rounded root breadcrumb button. The glyph-only adjustment
is superseded and reverted. KUrlNavigatorDropDownButton now reserves the existing
24px control width, with its existing 28px height and shared radius6/alpha65 hover
paint. This contains the backing inside the actual widget instead of enlarging
paint beyond the native narrow bounds. Native glyphs, menus and keyboard actions
remain upstream-owned; file expansion arrows are unaffected.

PASS helper build, native breadcrumb/editor fixture, and controlled hover capture
in a real installed-wrapper Dolphin window: 24x28 bounds and rounded, unclipped
backing. PASS architecture/token checks and whitespace. NOT RUN all scales/RTL,
complete dropdown keyboard interactions or live Recovery. Only the helper is
installed atomically with private restorer-compatible backups; no KWin, token,
QSS or additional Recovery dependency. New processes load this correction.

## Identity & Motion Pass — optional chrome overlay

The Qt helper now selects a valid optional Ricy-Dolphin icon overlay through the
process-local native KDE icon loader. Missing overlay leaves the system theme;
content/device/application icons remain inherited native assets. KF6IconThemes
headers/library supplement the existing Qt build prerequisites; Dolphin already
requires the native library. No compositor/effect source or ABI change occurs.
See [mapping and license](../dolphin-noctalia-identity/icons/Ricy-Dolphin/README.md)
and [validation/rollback](../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-2-iconography--2026-10-11).
