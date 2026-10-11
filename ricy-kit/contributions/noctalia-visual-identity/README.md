# Ricy’s visual identity — Noctalia reference

Existing reference caught in 10/10/2026. Use this guide before harmonizing other parts of the system. Noctalia defines the shell language; KWin is the compositor of the Plasma Wayland session. This document records the appearance and guides future changes. It does not install themes or applies preferences.

The visual signature is dark, bluish and discreet, featuring Mauve, rounded cards, light icons and continuity between embedded panels and bars. The depth comes from the difference between surfaces and the background blur.

## Palette and states

Active palette: `KDE-Current`, dark mode, custom source. The values below were checked in the active file and in the public integration template.

| Use | Color | Noctalia role |
|---|---|---|
| Shell background |  `#181825`  | mSurface |
| Neutral cards and controls |  `#313244`  | mSurfaceVariant |
| Main text and icons |  `#cdd6f4`  | mOnSurface |
| Text and secondary icons |  `#a6adc8`  | mOnSurfaceVariant |
| Ace Mauve, active, normal progress |  `#cba6f7`  | mPrimary / mSecondary |
| Text on accent |  `#11111b`  | mOnPrimary / mOnSecondary |
| Hover and selection |  `#977dba`  | mHover |
| Hover/selection text |  `#000000`  | mOnHover |
| Subtle contour |  `#46485c`  | mOutline |
| Success |  `#a6e3a1`  | mTertiary / terminal.green |
| Critical error/urgency |  `#f38ba8`  | mError |
| Warning |  `#f9e2af`  | terminal.yellow |
| Information |  `#89b4fa`  | terminal.blue |

Use the accent for selection, main action, focus and progress. Extensive texts use the main color; subtitles use the secondary. Preserve semantic colors for error, warning and success. The current KDE selection and native hover use the darkest selection color, while active Noctalia toggles use clear Mauve. This difference is part of the captured reference.

## Materials, contours and blur

| Area | Existing treatment |
|---|---|
| Taskbar, search support and panels that inherit the bar | Background `#181825`, opacity 0,70, compositor's blur |
| Notifications | Background 0,70, blur, without contour, next to the taskbar |
| Internal cards |  `#313244`, opacity 1,00, subtle contour when enabled |
| Floating/disapplying panels | Opacity 1,00 in mode `shell.panel.transparency_mode=solid`  |
| Kvantum Menus | Compact, opaque, no menu shadow or popup_blurring |

Opacity 0,70 is the fill color of the surface, not the opacity of texts, icons or the whole window. The color perceived varies with the content under it. `transparency_mode=solid` keeps the cards solid; an embedded panel that inherits the slider continues with background 0,70. Avoid interpreting this option as an order to make all elements translucent.

The `ricyblur`, derived from KWin 6.7.5, provides a common monitor sampling for Noctalia surfaces when a panel/warning appears. Junctions use `panel_overlap=0` to avoid a pixel with two fill layers. Same color/opacity in two windows, by itself, does not guarantee continuous blur. The effect treats the Noctalia class; **does not automatically extend this shared background to new or third party applications**. Adaptation requires analysis of the component and compositor. Consult the Blur-Continuity contribution.

Shadow is dependent on the component: the upper support has no shadow; Kvantum menus have no popup shadow; native panels keep their own rules. Do not consider all shadows turned off as current state.

## Geometry and scale

Values are logical pixels, not physical capture pixels. Current base: `accessibility.ui_scale=1`, `shell.corner_radius_scale=1.3`.

| Element | Existing rule |
|---|---|
| Taskbar | Lower, 44 px, reserve 44 px, always visible |
| Corners of the Taskbar | Superiors 6 px; lower straight |
| Search for the magnifying glass | Fitted next to the click on the bar |
| Noctalia Control | Fitted next to icon on the right |
| Search by Super/digitation | Launcher of 560 px and upper support of 640 × 16 px |
| Upper support | Corners 8 px, distance 8 top px; search monitor only |
| Notification | Bottom right corner, zero offsets; bottom left concave corner out and right right |
| Right-click application menu | Noctalia panel attached to the icon; size by content, no scrolling |
| Tray Item Options | Fitting Noctalia panel; dimensions by content; set and drawer share the same horizontal axis when returning on the same monitor |
| Clipboard | Floating panel in the center |

Style's native radii: 3 / 6 / 9 / 12 px, multiplied by local scale and corner_radius_scale; scale IU 1 uses 3,9 / 7,8 / 11,7 / 15,6 px. Bars have explicit radii of 6 and 8 px, without replacing these values with the overall radius of the cards. The content scale of the bar is 1,5 and the font scale of the bar 0,85; are parameters different from the general UI scale.

Native spacings: 4 / 8 / 12 / 16 px; card padding/boarding 14 px. Use this cadence for new components and adapt the size to the content. Reference monitors have 1920 px logical width. The support margin 640 results in width 640; on another monitor use `(largura lógica - 640) / 2`, limited to zero, and review the launcher if you change the scale.

Continuity is geometric: contact edges have a single junction, without dark milling, double overlap or corner that cut the connection inside. Notification is an intentional asymmetry; do not generalize four rounded corners for components connected to the bar.

## Typography, icons and movement

Noctalia: **Noto Sans**. Native base sizes before scale: mini 11, caption 13, body 14, title 16 and header 20 px. Do not convert these values into points without considering the implementation/scale of toolkit.

KDE and menus: **JetBrainsMono Nerd Font, 10 pt**; GTK records the same family and size 10. They are current preferences, preserved in this contribution. For the next settings, Noto Sans is the shell UI reference; the single-spaced font remains suitable for the terminal and should be handled consciously in the applications. Changing global or content sources requires a self-adjustment.

Noctalia Control Icons use simple, readable drawing, with state highlight. System icon theme: Breeze Dark; colorful application icons maintain your identity. Avoid redefining the icon of each application as Mauve.

Icons from taskbar applications and the search magnifying glass use visual scale **0.88 at rest and 1.0 on hover**, with a **140 ms / EaseOutCubic** transition. They retain click area, spacing and application indicators. Tray/menus, volume, clock, network and the Noctalia button retain their existing behavior. Workspace badges and groups are excluded from Ricy by RICY-001; see [the audit](../../../docs/WORKSPACE-AUDIT.md). The hover scale respects the shell's global motion/speed preference.

Native animation constants: 100 / 200 / 400 ms, with base speed 1. They are transition references, not real latency measures. Keep the indicator active, focus and the notification time bar readable in each state. The timer and hover pause remain native.

## Application interaction in the taskbar

In KDE/KWin, left click restores/focuss the minimized window, minimizes the visible window in focus and brings forward the visible window that is behind another window. Fixed icon without window starts the application. In groups, prioritizes the active window to minimize; without active, preserves selection/cycle to restore/focus. Middle button asks to close a window, respecting save dialogs; right click opens the composite menu and drag orders fixed. The selection uses exact UUID when available. Search and other activation callers continue only restoring/focusing. Play with the taskbar-app-actions contribution, which preserves the approved composition and hover.

The purple indicator reacts to the state: **active 1/1, open inactive 0,55/0,82, minimized 0,28/0,65**, in opacity/scale; no window, zero opacity. Transition **160 ms / EaseOutCubic**, preserved in reconstructions of the tiles. Windows use **fade and expansion centered**, scale **0,85→1** when opening/restoring or **1→0,85** Close/minimize, OutCubic/InCubic. Base duration **320 ms**, following KDE speed; global factor 0,25 Preserved corresponds to about 80 ms. Open/close uses native Scale; minimize/restaure uses ricywindowactions with reversal and continuity of blur per track. Real geometry preserved. Current reference of effects: **window-fade-expand**; source Noctalia: **app-icon-reordering**.

Application icons also respond with finite motions per action: **open 420 ms / bounce; restore 360 ms / bounce; focus 260 ms / pulse; minimize 220 ms / compression; background 200 ms / reduction; close fixed 240 ms / contraction; remove not fixed 220 ms / dissolve**. Base times follow shell preferences. Hover remains separate without changing click area; slots use Node without painting, avoiding black background. No loop at rest.

Applications can be rearranged with left button and drag on the flat track. A space indicates the destination; the icon accompanies the cursor. Order saves in the profile and preserved between reloads, regardless of attachment. Gestures consumed do not activate/minimize when dropping. Search/tray/controls maintain position. User confirmed drag in the actual session. Current cumulative reference: **app-icon-reordering**; details/tests/limitations in your README.

## Application in the next parts of the system

Use the color papers, the hierarchy between surface/card, accent and geometry as a reference for each implementation. Register what has been applied and what remains dependent on toolkit; keep the layout and behaviors already approved by changing their appearance.

| Area | Observed status / direction of next adjustments |
|---|---|
| Shell Noctalia | Main reference; preserve bar, search, notifications and continuity |
| Qt/KDE | KDE-Noctalia + Kvantum KDE-Noctalia active; evaluate decoration, dialogues and controls in real applications |
| GTK | active adw-gtk3-dark; complete color and component harmonisation not yet demonstrated |
| Plasma | active mocha-blur; review remaining elements by component |
| Terminal | Catppuccin/blur/cursor own preferences recorded in existing contributions; maintain monospaced legibility |
| Login and blocking | Appearance already documented in own contributions; not revalidated in this catch |
| OSD | Nottalia OSD disabled; choose implementation to suit in a later setting |
| Navigators/applications of third parties | Theme and content depend on each app; do not assume following KDE theme makes them fully harmonized |

To validate an adjustment, observe normal/hover/focus/selection/disabled, text and icons on light/dark backgrounds and junctions as the contents under the panel change. Check opening/closing, active monitor and scale. A capture with a uniform background does not alone demonstrate the continuity of the blur.

Preserved region: Noctalia dates/UI in English, America/Sao_Paulo zone, Cosmópolis/SP-BR, metric weather and events enabled without connected account. These preferences follow the reference, without defining the palette.

## Files, fonts and use in Ricy

- `tokens.json`: structured values, roles and rules for future agents/tools. It is reference, not a config.toml Substitute.
- `reference.svg`: Vector board with palette and a schematic junction. It is neither a session capture nor an OpenGL blur playback.
- `README.md`: this guide, also published as `Documents/ricy/VISUAL-IDENTITY.md`.

Sources checked: config.toml and KDE-Current.json active/public integration; settings.toml private only to check relevant overrides without copying it; style.h/style.cpp, config_types.cpp and panel/bar rules of the Noctalia 5.2.1 source; kdeglobals, Kvantum and current GTK/Plasma preferences; notification contributions, blur, wallpaper and language/location. Native sizes are code constants, not pixel-to-pixel measurements of all components.

This contribution does not change services, themes, fonts, settings or applications. To remove the reference, remove your document link and your archive from the kit by updating the manifest. Future changes should register your own reversal and the backups of the changed component. Preserve the Ricy history.


## Adaptation applied to Dolphin — 10/10/2026

Ricy-Dolphin/Kvantum is unique to the application: Noto Sans 10 pt, surface #181825 alpha 178/255, existing blur ricyblur, area of archives #313244 alpha 40/255 with contour #46485c and radius 12 px. Qt helper enables the translucent surface before creating it. It does not reduce opacity of texts/icons.

The side involves icon + name on a chip wide by content: highlight #977dba (alpha 95 hover, 170 selection, 195 Both). Lines have bottom #313244 alpha 90, radius 10 px and margins 3 horizontal px/2 vertical px. Hover, selection and rounded focus also cover the icon; focus uses solid #cba6f7. Header has common capsule #313244 alpha 155, contour #46485c alpha 150 and Noto Sans, preserving native labels/arrow. They are adaptations to Dolphin widgets, not token changes from shell. Breeze keeps title and native buttons.

Ricydolphinrounding effect uses KWin native radius 16 px only in Dolphin; maximized zero-ray/fullscreen/tiling. Recompile when updating KWin 6.7.5. Details and reversal: dolphin-nottalia-identity and dolphin-blur-canto contributions. User-approved initial chips; icons/header still without final approval.
