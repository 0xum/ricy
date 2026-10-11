# Visual token source audit

Date: 2026-10-11 (America/Sao_Paulo). Scope: maintained public/reference sources,
not private profiles/backups or a new session capture. KNOWN means inspected
source; runtime claims below are attributed to the earlier
[contribution audit](../../docs/CONTRIBUTION-AUDIT.md). INFERRED and UNKNOWN are
explicit. The [contract](README.md) lists exact consumable paths and semantics.

## Authority and extraction

The previous structured authority is the retained
[identity snapshot](../../ricy-kit/contributions/noctalia-visual-identity/tokens.json).
Its shared palette agrees with the integration's
[KDE-Current palette](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/KDE-Current.json).
The pinned Noctalia cache at commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4` was inspected read-only:
`src/ui/style.h` defines the spacing, padding, radii, font sizes and native
durations; `src/ui/style.cpp` implements radius × local scale × corner scale.
The [build script](../../ricy-kit/contributions/app-icon-reordering/build.sh)
records the version/source selection. The cache's cumulative diff is not the
current single-space source patch; inherited Style constants alone were used.

KNOWN: [tokens.json](tokens.json) now owns consumable values. Shared groups were
preserved exactly; derived shell radii are calculated instead of repeated.
Dolphin's repeated shared hex colors become color-role references, preserving
their resolved values. File-selection alpha was filled from the current helper;
Konsole's distinct surface/alpha was filled from its existing asset. Nonvisual
shell behavior, regional preferences, wallpaper ownership and kit-relative
`sources` paths are not exported as app tokens. No existing JSON was rewritten.

## Category findings

| Category | Canonical existing value/source | Duplication or hardcode | Treatment |
|---|---|---|---|
| Colors | Identity snapshot's 13 semantic colors; integration `KDE-Current.json.dark` agrees | Root and contribution palettes; KDE `.colors` RGB values; Kvantum config/SVG; Dolphin QSS/helper; board SVG; installers/generator | Promote shared roles unchanged. Preserve all existing runtime copies. Dolphin neutral `#242435`, terminal/login `#1e1e2e`, ANSI cyan `#94e2d5` and upstream theme colors remain scoped, not new shared roles. |
| Spacing | Style xs/sm/md/lg 4/8/12/16; card and panel padding 14 | Style constants and snapshot; TOML taskbar item spacing 6; Qt menu layout 2, icon spacing 3 and menu frames 4/6; Dolphin margins/gutters/padding 8/12 and row insets 3/2 | Export native cadence and existing scoped geometry. These component values are not evidence for a new global scale. |
| Radius | Style base 3/6/9/12; captured corner multiplier 1.3 | Snapshot repeats 3.9/7.8/11.7/15.6; TOML corners 6/0 and support 8; Kvantum SVG corners 12/6; Dolphin QSS 8/12, helper row cap 10, KWin corners 16 | Compute derived shell values; keep fixed/adapted radii scoped. No universal rounding replacement. |
| Typography | Noto Sans; native shell 11/13/14/16/20 logical px | TOML repeats family; KDE/GTK preferences and Konsole profile repeat JetBrainsMono Nerd Font 10 pt; Dolphin QSS repeats Noto Sans 10 pt; board has illustration-specific sizes | Keep units and scopes. No px-to-pt conversion or global font reset. |
| Motion | Style 100/200/400 ms; shell cumulative patch 140/160 ms and finite state durations; selected KWin effect 320 ms, scale .85 | Same behavior serialized in snapshot, cumulative/old patches, effect JS, config applicators and validators | Export existing cadence and named adaptations. Historical squash effects are not current identity. Respect motion preferences; no common animation engine. |
| Opacity/transparency | Attached shell/notifications .70; solid cards/detached panels 1; opaque text | TOML .70; board `.7`; Dolphin QSS alpha178 and helper alpha90/155/150/95/170/195; snapshot; Konsole .85 | Preserve 8-bit alpha exactly, including 178/255 versus .70. Keep indicator fade and terminal opacity separate from surface fill. |
| Blur | Reference `Effect-blur` strength5/noise2; material blur requests | Appearance preferences repeat settings; source/older tokens describe ricyblur; Kvantum blur flags, Konsole `Blur=true`, shell TOML | Export compositor-setting units and current audit attribution. No portable blur radius/sigma exists; new-app support and shared continuity remain UNKNOWN. |

## Concrete source/consumer inventory

Paths below are maintained evidence, not an instruction to rerun applicators.

| Source / existing consumer | Evidence and status | Central consumption after this task |
|---|---|---|
| [Root palette](../../ricy-kit/outputs/noctalia-test/KDE-Current.json), [integration palette](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/KDE-Current.json) | Duplicate shell/terminal color definitions; full private palette equivalence UNKNOWN (G-05/shared-material audit) | No |
| [Root TOML](../../ricy-kit/outputs/noctalia-test/config.toml), [integration TOML](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/config.toml) | Family, scale, fixed bar corners and fill alpha repeat. Root search support is currently radius0; contribution has radius8. Runtime uses a private profile (G-02), not either entire template verbatim | No; divergence preserved |
| [KDE scheme](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/kde-outlines/KDE-Noctalia.colors), [Kvantum config](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/kde-outlines/KDE-Noctalia/KDE-Noctalia.kvconfig), [menu SVG](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/kde-outlines/KDE-Noctalia/KDE-Noctalia.svg) | RGB/hex variants, menu geometry/alpha and upstream theme inheritance; selected menu assets grounded in G-05 | No |
| [Kvantum generator](../../ricy-kit/generate-kvantum-variant.py), [preparation](../../ricy-kit/prepare-environment.py), [destination preparer](../../ricy-kit/contributions/noctalia-kde-integration-and-menus/prepare-destination.py) | Hardcoded menu roles/12 and6 radii; seed copying/config mutation. Historical or MIGRATE tooling; unsafe as an audit test because it writes settings/assets | No |
| [Dolphin QSS](../../ricy-kit/contributions/dolphin-noctalia-identity/dolphin.qss), [Qt helper](../../ricy-kit/contributions/dolphin-blur-corners/ui.cpp), [corners](../../ricy-kit/contributions/dolphin-blur-corners/corners.cpp) | Palette, insets, font, alpha and radii literals. Latest source: opaque main/L panels, equal-width places. Exact installed compiled-helper provenance UNKNOWN (G-05) | No |
| [Noctalia cumulative patch](../../ricy-kit/contributions/app-icon-reordering/noctalia-ricy.patch), [window effect](../../ricy-kit/contributions/window-fade-expand/assets/kwin/effects/ricywindowactions/contents/code/main.js), [effect applicator](../../ricy-kit/contributions/window-fade-expand/apply-animations.py) | Hover/indicator/state literals and native preference handling; current source/deployed shell divergence G-02; installed window effect matches G-04 | No |
| [Appearance preferences](../../ricy-kit/contributions/login-lock-cursor-appearance/preferences.json), [SDDM configuration](../../ricy-kit/contributions/login-lock-cursor-appearance/assets/sddm/mocha-limine/theme.conf), [Konsole profile](../../ricy-kit/contributions/konsole-animated-cursor/assets/PlasmaBlur.profile), [terminal palette](../../ricy-kit/contributions/konsole-animated-cursor/assets/PlasmaBlur.colorscheme) | KDE/GTK font and blur settings; distinct login/terminal surface; full ANSI palette remains an adaptation. Plasma/login/lock assets retain upstream origins | No |
| [Identity SVG](../../ricy-kit/contributions/noctalia-visual-identity/reference.svg) | Schematic reference with palette/type/radius/alpha literals; historical caption mentions ricyblur | Yes, offline generation from central JSON/template; unchanged bytes |
| [Transport kit](../../docs/ricy-kit/AGENTS.md) and historical cumulative contributions | Preserved independent variants; no automatic equivalence or synchronization | No |

## Discrepancies and limits

- **KNOWN:** legacy `integration.shared_blur_effect=ricyblur` and the board/older
  guide describe an earlier implementation. G-03 observed native blur loaded
  and the selector failed. New `blur` metadata cites that observation; no effect
  is repaired, selected or reloaded. Strength5/noise2 remain settings references,
  not a new live reading or proof of continuous sampling.
- **KNOWN:** early Dolphin documentation describes translucent internal panels
  and content-width places chips. Latest QSS/helper and the snapshot's later
  adaptation use opaque card/L panels and equal-width places. Old sections are
  preserved as history; new consumers must not restore them from prose.
- **KNOWN:** the snapshot records a header radius only indirectly, while helper
  `chip()` clamps it to `min(10, height/2)`. Tabs and main/L panels use 12. No
  blanket 12 px radius is assigned to every Dolphin widget.
- **KNOWN:** `Style::disabledOutlineAlpha=.5`, focus/border widths and many widget
  geometries exist upstream beyond the captured token contract. They are not
  universal disabled/focus policies for future apps. Full per-widget state
  tokenization is deferred; no unsupported defaults were invented.
- **INFERRED:** direct JSON/build-resource consumption is sufficient for a first
  app adapter because the values already exist and no runtime service is needed.
  Toolkit, resource packaging and material integration for Files remain UNKNOWN.
- **NOT RUN:** live visuals, app interactions, monitors/scaling, login/unlock,
  session switching and recovery. No install/applicator was executed. Static
  value and byte equality establish the small migration's scope only.


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
