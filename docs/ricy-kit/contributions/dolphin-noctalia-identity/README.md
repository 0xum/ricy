# Dolphin with identity Noctalia

Kvantum's exclusive Ricy-Dolphin variant, derived from KDE-Noctalia/Catppuccin MIT installed. Background #181825, text #cdd6f4, secondary #a6adc8, contour #46485c, control cards #313244 and featured #977dba/#cba6f7. 10 pt in the interface and in the three file modes. Controls of the bar, fields and tabs have corners of 8 px. Menus preserve the existing KDE-Noctalia compact variant. Breeze Dark Icons and preserved archive operations.

The theme is assigned only to dolphin in Kvantum/Applications. Launcher ricy-dolphin injects Qt sheet and transparency helper. Desktop, FileManager1 service and drop-in plasma-dolphin.service use the launcher. The current version requires sister contribution dolphin-blur-corners, which contains the Qt compiler. Background 0,70 with blur, area of translucent, rounded archives of 12 px and native external corners of 16 px by the optional KWin effect. The side uses chip involving icon + name; lines, hover, selection/focus and file header use rounded capsules, keeping the drawings and native events. Read your README for compilation, evidence, version update, and reverse corners.

Global KDE source, archive operations, MIME and Noctalia preserved. Breeze maintains native title/buttons. Existing processes without alpha require closing and reopening Dolphin to load everything; the applicator preserves open windows. Direct execution of /usr/bin/dolphin do not inject helper/QSS: use normal launcher or ~/.local/bin/ricy-dolphin. No Dolphin system file is replaced.

## Reproduce

Prerequisites: Plasma Wayland, Dolphin, Qt/Kvantum, KDE-Noctalia installed, Noto Sans, Qt6/headers, g++, pkg-config, Python, qdbus6, kwriteconfig6, kbuildsycoca6 and user systemd. 5.2.1, KWin 6.7.5.

```bash
cd "$HOME/ricy-kit/contributions/dolphin-noctalia-identity"
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
