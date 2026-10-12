# Ricy semantic visual roles

Grounding date: 2026-10-11 (America/Sao_Paulo). This dictionary formalizes the
existing [contract](README.md), schema1 / contract1.0.0.
[DESIGN-SYSTEM](../../docs/DESIGN-SYSTEM.md) owns intent;
[tokens.json](tokens.json) remains the only consumable value source.
Semantic names below are documentary vocabulary, not additional JSON keys,
executable aliases, or a runtime loader. Existing paths/types/values/meanings
are unchanged. Choose a consumer scope before resolving a role.

KNOWN means inspected canonical data/source, not a new live capture. INFERRED
marks classification from that evidence. MISSING means no canonical value or
portable policy; it does not mean zero, false, black, or transparent. UNKNOWN
means unproven behavior. Candidate integrations are unapproved options, not
PLANNED implementation. Evidence: [AUDIT](AUDIT.md),
[Dolphin baseline](../../docs/DOLPHIN-BASELINE.md), and
[Noctalia grounding](../../docs/NOCTALIA-VISUAL-GROUNDING.md).

## Colors: token → role → consumers

| Canonical path | Ricy semantic role | Existing consumer examples | Noctalia correspondence |
|---|---|---|---|
| `colors.accent` | color.action: active/focus/progress emphasis | Shell toggles; Dolphin active tabs, Places, menus | Direct: primary / mPrimary |
| `colors.on_accent` | color.on_action: content on accent | Active tabs, Places, menu actions | Direct: on_primary / mOnPrimary |
| `colors.surface` | color.background: base/chrome fill | Shell bar/attached panels; Dolphin outer window/editor | Direct: surface / mSurface |
| `colors.card` | color.content_background: neutral content grouping | Shell cards; Dolphin content, unified L, menus | Direct: surface_variant / mSurfaceVariant; no implied shadow |
| `colors.on_surface` | color.content: primary text/icons | Shell and Dolphin text | Direct: on_surface / mOnSurface |
| `colors.secondary_text` | color.content_secondary: supporting text/icons | Shell captions; Dolphin headers, menu disabled text, scroll thumb | Direct: on_surface_variant / mOnSurfaceVariant; not a universal disabled recipe |
| `colors.outline` | color.contour: subtle edge/separator | Enabled shell contours; Dolphin card/header/menu | Direct: outline / mOutline |
| `colors.hover_selection` | color.interaction_fill: existing hover/selection paint | Shell hover; Dolphin file selection, tab/Places/breadcrumb hover | Direct color: hover / mHover; approximate state semantics because selection also uses accent |
| `colors.on_hover_selection` | color.on_interaction_fill: content on opaque hover | Dolphin hovered tabs; KDE highlight text | Direct: on_hover / mOnHover; not every translucent hover uses black text |
| `colors.error` | color.feedback_error | Critical/destructive feedback | Direct: error / mError |
| `colors.success` | color.feedback_success | Positive feedback | Approximate: captured mTertiary/terminal green; upstream tertiary is an accent |
| `colors.warning` | color.feedback_warning | Warning feedback | No direct core palette role; captured terminal yellow is provenance |
| `colors.information` | color.feedback_information | Informational feedback | No direct core palette role; captured terminal blue is provenance |

Correspondence uses [official palette roles](https://docs.noctalia.dev/noctalia/theming/palette/)
and the public KDE-Current palette linked in the grounding. Foreground intent
does not prove contrast after composition with arbitrary wallpaper.

| Additional concept | Evidence / treatment |
|---|---|
| secondary / on_secondary | KNOWN public palette repeats accent/on-accent. Approximate compatibility alias; no separate Ricy action hierarchy. |
| tertiary / on_tertiary | Public tertiary matches success and its foreground repeats on-accent. MISSING canonical on-success; no universal tertiary accent. |
| on_error | Public palette repeats on-accent. MISSING canonical on-error; equality does not establish a reviewed error-filled control. |
| shadow | Public mShadow is black. MISSING canonical shadow color/recipe; on-hover black is not a shadow token. |
| Container/fixed/inverse/scrim roles, light mode, wallpaper-derived accent | No reviewed equivalent Ricy hierarchy/policy; do not add tones or modes merely to complete upstream templates. |
| Ricy junctions, file-selection alpha variants, native device/application icons | No direct palette equivalent; preserve scoped geometry, states, and native behavior. |

## Surfaces and materials

First classify the surface's purpose, then its scoped material, contour/radius,
and shadow owner. Floating placement alone determines none of those values.

| Surface role | Meaning | Existing basis |
|---|---|---|
| surface.base | Outer backing/chrome, including attached shell | `colors.surface`; material is scoped |
| surface.content | Grouped readable content/cards | `colors.card`, `materials.cards`; primary text stays `colors.on_surface` |
| surface.floating | Separate panel/popup above surrounding content | Presentation role: shell panels use base fill, Dolphin menus use card; no new color |
| surface.control | Interactive element within another surface | Consumer's normal/hover/selected/focus states |
| surface.inherited | Transparent widget over its owner's backing | Dolphin breadcrumb/status/toolbar children; no independent blur/shadow |

| Material role | Existing references | Status / limits |
|---|---|---|
| material.solid | `materials.cards`, `materials.detached_panels`, `application_adaptations.dolphin.content_card`, `application_adaptations.dolphin.sidebar_topbar` | KNOWN opaque fill; not every window |
| material.glass | `materials.attached_shell_background`, `materials.notification_background`, `application_adaptations.dolphin.surface` | KNOWN alpha/blur intent; composited result UNKNOWN here. Preserve shell.70 versus Dolphin178/255 |
| material.state_overlay | `application_adaptations.dolphin.file_selection`, `application_adaptations.dolphin.places_buttons.hover_alpha_255`, `application_adaptations.dolphin.navigation.breadcrumb_hover_alpha_255` | INFERRED existing interaction overlay on solid backing; no independent compositor blur |
| material.inherited | Transparent breadcrumb/status/toolbar backing; zero-alpha scoped navigation/menu-window fields | INFERRED classification; parent remains painted |
| material.soft | Upstream concept only | MISSING Ricy preset/values; no approximate alpha assigned |

| Current example | Surface → material / scope |
|---|---|
| Noctalia attached panels/taskbar | base → glass; explicit contact edges/bar corners |
| Noctalia detached panels | floating/base → solid; surface fill |
| Noctalia internal cards | content → solid; optional existing contour |
| Noctalia taskbar/tray menus | INFERRED floating purpose/attached placement → glass backing; internal cards remain solid where present; preserve menu/drawer anchors |
| Native Noctalia popups/dropdowns | floating → existing popup treatment; complete deployed coverage UNKNOWN |
| Dolphin sidebar/toolbar backing | content → solid unified L; child widgets inherit it |
| Dolphin content | content → solid main card containing view/scroll/status |
| Dolphin tabs | control → existing solid state fills |
| Dolphin menus | floating/content → solid; transparent outer corner cutouts, popup blur disabled |
| Dolphin status/breadcrumb chrome | inherited → inherited |

Fill alpha, shadow alpha, state overlay and animation opacity are independent.
Transparency never reduces the whole window's text/icons. Blur needs compositor
capability and a legible opaque fallback for future consumers; these roles do
not activate it. Attached junctions remain consumer geometry.

## Borders, radii and spacing

Native bases remain `geometry.native_radius_logical_px`, multiples of the
existing small base. Shell radius = base × local scale ×
`geometry.shell_corner_radius_scale`, applied once. Dolphin and fixed bar
corners retain their scoped logical-pixel values without that multiplier.

| Role | Native shell evidence / canonical basis | Scoped Dolphin reference |
|---|---|---|
| radius.control | Button default: `geometry.native_radius_logical_px.medium` | `application_adaptations.dolphin.rows.radius_max`, `application_adaptations.dolphin.context_menu.item_radius`; Places/input retain8px adaptation |
| radius.card | Box card: `geometry.native_radius_logical_px.extra_large` | `application_adaptations.dolphin.content_card.radius` |
| radius.panel | PanelManager/Box panel: `geometry.native_radius_logical_px.extra_large` | `application_adaptations.dolphin.sidebar_topbar.radius`; fixed bar/notification contact edges are exceptions |
| radius.popup | Native context-menu chrome: `geometry.native_radius_logical_px.large`; dialog may use extra-large | `application_adaptations.dolphin.context_menu.radius`, `application_adaptations.dolphin.context_menu.native_surface_mask_radius`; attached menus retain panel scope |
| radius.window | MISSING universal app radius | `application_adaptations.dolphin.native_window_radius`, `application_adaptations.dolphin.maximized_fullscreen_tiled_radius`; KWin owner |
| border.subtle | `colors.outline`, `materials.outline.width_logical_px`, where enabled | Preserve `application_adaptations.dolphin.header.outline_alpha_255` and scoped card/menu outlines |
| border.interactive | Existing control contour; state fill remains separate | Places/navigation normal outline alpha0; MISSING universal hover-border width |
| border.focus | `colors.accent`; native Style focusRingWidth is source evidence | `application_adaptations.dolphin.navigation.editor_outline`, `application_adaptations.dolphin.navigation.editor_outline_width`; retain native file focus geometry |

Primitive correspondence is KNOWN in pinned files listed in the grounding;
cross-toolkit classification is INFERRED. Canonical interactive/focus widths
for every toolkit are MISSING; do not generalize the editor width. Equal
numbers do not authorize converting a scoped token into a global dependency.

Spacing uses `geometry.native_spacing_logical_px`. Card/panel insets remain
distinct `geometry.native_card_padding_logical_px` and
`geometry.native_panel_padding_logical_px`. Dolphin layout groups keep their
existing values. Do not round14px to a spacing step or impose it on app menus.

## Shadow and elevation

| Role | Meaning / owner | Canonical availability |
|---|---|---|
| elevation.none | No child shadow: embedded cards, Dolphin L/content/status/toolbar; explicit shadowless upper support and Kvantum menus | Keep existing policies; not proof all shell shadows are off |
| elevation.floating | Separate panels/popups/menus/windows | Consumer decides whether/who paints shadow; no mandatory recipe |
| shadow.opacity / shadow.blur / shadow.direction / shadow.color | Only relevant to consumers already painting shadows | MISSING shared Ricy values; upstream evidence is in grounding |

No current need establishes elevation.low; no preset is invented. Noctalia
owns shell-rendered shadows and component toggles. QSS/Kvantum menus keep their
shadowless treatment. KWin/decoration integration owns normal window shadows,
outer corners and background blur; children must not add competing shadows.
Qt helper owns popup masks, distinct from KWin window radius. Complete deployed
shell/compositor recipes remain UNKNOWN.

## Motion

These roles describe purpose/preferences; they do not start animations.

| Role | Existing basis / rule | Status / limit |
|---|---|---|
| motion.enabled | Existing native shell motion preferences; toolkit reduced motion where available | Respect disable/reduced motion and final state; MISSING canonical boolean; no settings write |
| motion.speed / motion.duration_scale | `motion.source` records base speed1; shell duration divides by effective speed | Preference inputs with reciprocal meaning; MISSING canonical numeric fields; no global Ricy synchronizer |
| motion.fast | `motion.native_durations_ms.fast` | KNOWN100ms base |
| motion.normal | `motion.native_durations_ms.normal` | KNOWN200ms base |
| motion.slow | `motion.native_durations_ms.slow` | KNOWN400ms base |
| motion.enter | `motion.application_icon_hover.duration_enter_ms` for app/search hover; native panel reveal uses normal | Contextual; MISSING universal enter duration |
| motion.exit | `motion.application_icon_hover.duration_leave_ms` for hover leave; native panel hide uses normal with existing easing | Contextual; MISSING universal exit duration |
| motion.easing.standard | `motion.application_icon_hover.easing`, `motion.taskbar_window_indicator.easing` | Existing EaseOutCubic reference for emphasis; not a mandate to replace panel exit, springs or KWin easing |

Shell speed2 halves base duration; disabled animation settles at final state.
Upstream effective preference/clamp belongs to the consumer. App adapters must
not depend on a running Noctalia service to read identity. Native menu/launcher
enter/exit easings remain contextual; Dolphin receives no new animations.
Current Kvantum animate_states=false is scoped source evidence.

Preserve `motion.application_icon_hover`, `motion.taskbar_window_indicator`,
`motion.app_icon_state_actions` and fixed hit areas. `motion.kwin_window_actions`
has a different owner/clock: its observed.25 factor is not widget speed.
Cross-app preference synchronization remains UNKNOWN.

## Typography and states

| Role | Binding | Status / scope |
|---|---|---|
| type.caption | `typography.native_sizes.caption`, `typography.shell_family` | KNOWN shell13 logical px; native shell menus use caption |
| type.body | `typography.native_sizes.body`, `typography.shell_family` | KNOWN shell14 logical px before scale |
| type.title | `typography.native_sizes.title`, `typography.shell_family` | KNOWN shell16 logical px; header stays distinct |
| type.label | Inherit current control's family/size | INFERRED purpose; MISSING independent size/weight/tracking; no global body/caption substitution |
| type.application_body | `application_adaptations.dolphin.font` | KNOWN Noto Sans10pt QSS/view adaptation |
| type.kde_default | `typography.kde_family`, `typography.kde_size_pt` | KNOWN captured JetBrainsMono Nerd Font10pt preference |

Mini/header stay `typography.native_sizes.mini` and
`typography.native_sizes.header`. `typography.ui_scale`,
`typography.bar_content_scale`, `typography.bar_font_scale` are scoped reference
inputs, not settings to install. Logical px and pt are distinct. Global
line-height/weight/tracking and separate label scale are MISSING. Places'
`application_adaptations.dolphin.places_buttons.font_weight` is not a shared
semibold token. Deployed font fallback coverage is UNKNOWN.

| State | Existing semantic rule |
|---|---|
| Normal | Readable content on classified backing; Places/breadcrumb normal fill stays transparent |
| Hover | Consumer interaction alpha/foreground; not selected everywhere |
| Selected/active | Accent/on-accent for Places/tabs/menus; file selection keeps hover-selection with three scoped alpha variants |
| Focus | Accent contour where painted; preserve keyboard geometry independently of selection |
| Disabled | Native Qt/Kvantum behavior; Dolphin menus use secondary text. MISSING universal disabled opacity |
| Pressed/error | Scoped scrollbar press and feedback roles; MISSING universal pressed fill/filled-error foreground |

No painting, motion, icon recoloring or contrast certification follows merely
from assigning these documentary roles.

## Authorized application typography synchronization

The [Typography phase](../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-1-typography--2026-10-11)
supersedes the deployed Noto Sans QSS/view override described above.
`application_adaptations.dolphin.font` and captured family fields retain their
original values as reference evidence. Current type.application_body inherits
the active KDE/Qt font; the shell shares its family through official configuration
and keeps native contextual sizes/scales. No token values, names or contract
versions change. Do not overwrite the active system choice from the snapshot.
