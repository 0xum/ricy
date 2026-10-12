# Noctalia Visual Language Grounding

Date: 2026-10-11 (America/Sao_Paulo). Scope: official Noctalia visual concepts,
current tokens/identity, Dolphin baseline, QSS and Kvantum. No runtime change,
deployment, or Dolphin polish is part of this step. [DESIGN-SYSTEM](DESIGN-SYSTEM.md)
owns intent; [themes/tokens](../themes/tokens/README.md) owns consumable values.
[SEMANTICS](../themes/tokens/SEMANTICS.md) formalizes roles without replacing
token names/values or creating an executable alias schema.

## Sources and evidence limits

Official sources were read on the grounding date. These rolling v5+ pages are
references, not proof of the pinned build or deployed Ricy settings:

| Official source | Grounding subject |
|---|---|
| [Overview](https://docs.noctalia.dev/noctalia/) | Native v5; Quickshell v4 documentation is legacy |
| [Theme](https://docs.noctalia.dev/noctalia/theming/) | Palette sources and separate app/shell mode |
| [Palette](https://docs.noctalia.dev/noctalia/theming/palette/) | Role/foreground pairs mapped in SEMANTICS |
| [Shell](https://docs.noctalia.dev/noctalia/configuration/shell/) | Typography, corner scale, borders, shadows, materials, motion preferences |
| [App Theming](https://docs.noctalia.dev/noctalia/theming/app-theming/) | Template/output lifecycle |
| [Template Reference](https://docs.noctalia.dev/noctalia/theming/templates/) | Variables, formats, hooks, CLI and native post-actions |
| [GTK/Qt/KColorScheme](https://docs.noctalia.dev/noctalia/templates/official/gtk-qt/) | Official application integration routes |

Local evidence: [canonical JSON](../themes/tokens/tokens.json),
[source audit](../themes/tokens/AUDIT.md), [identity guide](VISUAL-IDENTITY.md),
[Dolphin baseline](DOLPHIN-BASELINE.md),
[public palette/profile provenance](../themes/tokens/AUDIT.md#concrete-sourceconsumer-inventory),
[Dolphin QSS](../ricy-kit/contributions/dolphin-noctalia-identity/dolphin.qss),
[Qt helper](../ricy-kit/contributions/dolphin-blur-corners/ui.cpp),
[Kvantum/KDE reference provenance](../themes/tokens/AUDIT.md#concrete-sourceconsumer-inventory).
Private profile/palette contents were not published. Installed observations
remain attributed to the baseline, not reasserted as new live validation.

Inspected public output paths, relative to
`ricy-kit/contributions/noctalia-kde-integration-and-menus/`:
`outputs/noctalia-test/KDE-Current.json`, `outputs/noctalia-test/config.toml`,
`outputs/kde-outlines/KDE-Noctalia/KDE-Noctalia.kvconfig`, and
`outputs/kde-outlines/KDE-Noctalia.colors`. These retained output artifacts are
provenance rather than normal source/fixture payloads; the maintained inventory
above supplies their evidence links without expanding the harness's copy scope.

The local upstream cache was inspected read-only at Noctalia5.2.1 commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`, selected by the
[maintained build recipe](../ricy-kit/contributions/app-icon-reordering/build.sh).
The cache contains an older cumulative patch; only these upstream primitives
and templates were used, not its shell behavior as deployed-Ricy evidence:

- `src/ui/style.h`, `style.cpp`; `src/ui/controls/button.cpp`, `box.cpp`,
  `context_menu.cpp`; `src/ui/popup_chrome.cpp`;
  `src/shell/panel/panel_manager.cpp`: type, geometry, contextual motion.
- `src/shell/surface/shadow.h`, `src/config/config_types.h`;
  `src/render/animation/motion_service.cpp`, `motion_service.h`,
  `animation_manager.cpp`: shadow primitive/defaults and global motion.
- `assets/templates/builtin.toml`, `gtk/gtk3.css`, `gtk/gtk4.css`,
  `gtk/apply.sh`, `qt/qtct.conf`, `kde/kcolorscheme.colors`, `kde/undo.sh`;
  `src/theme/cli.cpp`, `fixed_palette.cpp`, `template_engine.cpp`,
  `kde_color_scheme.cpp`: generation, palette expansion and activation.

## Audit: KNOWN / INFERRED / MISSING

MISSING means no canonical value/portable policy, even if a scoped upstream
constant exists. UNKNOWN describes unproven behavior.

| Category | KNOWN evidence | INFERRED classification | MISSING / UNKNOWN |
|---|---|---|---|
| Colors | 13 canonical roles; public primary/secondary share accent; tertiary matches success | Action/content/feedback independent of toolkit names | On-error/on-success/shadow/light palette not canonical; full private palette equivalence UNKNOWN |
| Typography | Shell Noto Sans11/13/14/16/20 logical px; Dolphin Noto Sans10pt; KDE JetBrainsMono Nerd Font10pt | Caption/body/title and contextual label purposes | Independent label size, global weights/line-height/tracking MISSING |
| Spacing | Native4/8/12/16; separate14px card/panel padding; scoped Dolphin layout | Cadence differs from semantic insets | Universal density/control layout MISSING |
| Radius | Native3/6/9/12 × local scale ×1.3; fixed bar6/0; Dolphin3/6/8/12/16 | Control/card/panel/popup/window with scope | Universal app radius MISSING; live scale coverage UNKNOWN |
| Borders | Outline color/1px material; source Style focus2px/emphasized3px; Dolphin editor2px, transparent normal Places/navigation outlines | Subtle/interactive/focus purposes | Shared interactive/focus widths MISSING; source constants are not automatically tokens |
| Opacity | Shell.70; solid cards/detached panels; Dolphin178/255 and overlays | Fill/state/shadow/animation alpha are separate | Effective stacked Qt/Kvantum opacity UNKNOWN |
| Materials | Attached glass intent; detached solid; opaque Dolphin L/content/menu | Surface purpose plus scoped material | Soft Ricy preset MISSING |
| Blur | Strength5/noise2 compositor units; native blur in baseline | Material intent needs capability/fallback | Portable kernel MISSING; cross-window sampling/app support UNKNOWN |
| Shadows | Public mShadow black; upper support shadow=false; Kvantum menu/tooltip depth0 and shadowless_popup=true | Floating placement need not cast shadow | Canonical recipe MISSING; full deployed toggles/recipe UNKNOWN |
| Motion | Native100/200/400; hover140, indicator160; scoped actions/KWin320 | Global preference plus contextual enter/exit | Canonical enabled/speed and universal enter/exit/easing MISSING; cross-app sync UNKNOWN |
| States | Places/file/tab/menu normal/hover/selected/focus differ | Shared purpose, contextual paint | Universal disabled/pressed and full contrast coverage MISSING/UNKNOWN |

Discrepancies remain explicit: root search-support radius0 versus contribution/
canonical8; historical ricyblur versus later native blur observation; earlier
translucent Dolphin panels/chips versus opaque L/transparent Places; older menu
padding8/20 versus current12. The source audit and baseline supersede those
historical descriptions; nothing was silently normalized here.

## Reusable concepts and compositor boundary

Ricy reuses semantic foreground/background pairs, purpose-based surfaces,
optional contours, existing native scale and consumer motion preferences.
The dictionary records direct/approximate mappings and unsupported roles.
No additional Material tones, second/third action hierarchy, automatic
wallpaper colors or light scheme is adopted.

The shell model separates solid/soft/glass panel treatment, border/shadow
toggles and attached styling. Ricy retains attached glass/detached solid; soft
has no values. Upstream shadows separate direction/alpha and component opt-in.
Pinned source defaults are down/0.55 with fixed12px blur; painted alpha multiplies
background opacity. The renderer paints black directly, so mShadow palette
equality is not proof that every shell shadow consumes that palette role.
These are upstream source/defaults, not captured Ricy settings or new tokens.
[Official Shell reference](https://docs.noctalia.dev/noctalia/configuration/shell/).

KWin remains infrastructure under RICY-002. Noctalia visual semantics do not
establish Wayland layer policy, blur regions/shared sampling, native masks,
KWin effect selection, Dolphin radius16 handling or ABI compatibility.
Other-compositor recommendations and screen-corner overlays are not inherited.
No native blur, ricyblur, selector, effect, corner helper or setting changes
occur. Future integration implications belong to [RECOVERY](RECOVERY.md).

## App Theming feasibility — evaluated, not adopted

**Finding:** Noctalia can be an optional consumer/generator of Ricy identity.
It does not currently read Ricy tokens. Its shipped mappings cannot reproduce
current Dolphin/Kvantum identity unchanged. This assessment introduces no
cross-component generation contract.

App Theming renders app files on palette/mode changes. Built-in IDs are opt-in;
community templates add fetched/cached inputs; user templates specify paths/
hooks. Templates follow theme.mode rather than shell_mode. Disabling built-ins
can remove generated files and undo includes/selections: enable/disable are
mutations, not inspections. [Official App Theming](https://docs.noctalia.dev/noctalia/theming/app-theming/).

Variables address color role, mode and format, including hex/RGB. The engine
exposes additional Material roles and accepts precomputed --theme-json input.
Config processing supports pre/post hooks and native post-actions; post hooks
may run even for unchanged output. Hooks can overlap unless serialized. The
kde-color-scheme action merges colors into kdeglobals and signals KDE apps.
Rendering and application are distinct evaluation scopes.
[Official Template Reference](https://docs.noctalia.dev/noctalia/theming/templates/).

The GTK route uses adw-gtk3/generated CSS; its hook imports CSS and updates
GTK/GNOME preferences. Generic Qt output is a palette. Noctalia recommends
KColorScheme for KDE apps including Dolphin; Plasma has a native scheme route.
qt6ct-kde is another environment-specific route, not authorization to replace
Ricy's Plasma platform integration.
[Official GTK/Qt/KColorScheme guide](https://docs.noctalia.dev/noctalia/templates/official/gtk-qt/).

Pinned implementation findings: KNOWN source; generation/activation NOT RUN.

| Artifact/mechanism | Observation | Ricy implication |
|---|---|---|
| gtk3/gtk4 catalog | Outputs noctalia.css, same apply.sh with mode and hook_async=false | Shared import/preference writer must stay serialized; affects other apps |
| GTK4 warning variables | Warning colors reference tertiary/tertiary_container | Ricy's captured tertiary is success green; warning requires its own explicit mapping, not blind template reuse |
| qt catalog/qtct.conf | qt5ct/qt6ct color arrays include fixed neutral literals | Generic QPalette does not replace KDE groups or Kvantum visuals |
| kcolorscheme catalog | Outputs XDG_DATA_HOME/color-schemes/noctalia.colors; post_action=kde-color-scheme | Shipped catalog generation can activate global colors; --builtin-config is not output-only preview |
| KDE template | Button/View/Window/Selection/Tooltip/Header/Complementary/effects/WM groups | Useful target format, but mapping needs per-consumer comparison |
| KDE selection | primary/on_primary | Conflicts with retained KDE hover_selection/on_hover_selection; Dolphin Places/tabs use accent. One pair does not reproduce every scoped state |
| KDE backgrounds | surface_container tiers/background and derived roles | Ricy's two surfaces do not define that hierarchy; unmodified template changes values |
| Fixed palette CLI | Requires pairs absent from canonical JSON; fixed_palette.cpp expands additional tones | Ricy tokens are not Noctalia theme JSON verbatim; completing pairs/accepting tones needs a separate decision |
| KDE activation/undo | kde_color_scheme.cpp merges kdeglobals and notifyChange; undo.sh has cleanup behavior | Template disable is not proof of exact whole-file rollback; preserve existing backups |
| QSS/helper/Kvantum | Dolphin paint/alpha/geometry remain in QSS/ui.cpp/style config/SVG | Color generation alone cannot migrate geometry or certify appearance |

Templates/hooks were read, not executed. No CLI generation, apply/undo hook,
scheme selection, package installation or environment export ran. Installed
CLI compatibility, output equality and end-to-end propagation remain UNKNOWN.

Candidate direction, **unapproved and non-normative**:

```text
themes/tokens/tokens.json (Ricy authority)
  → documented semantic roles/scoped adaptations
  → optional explicit Noctalia-compatible mapping/templates
  → staged KColorScheme / QSS / Kvantum / app output
  → separately reviewed application and rollback
```

| Future option | Benefit | Tradeoff / decision boundary |
|---|---|---|
| Keep canonical direct reads/current consumers | Existing ADR-0005 suffices for this grounding | Runtime hardcode drift remains |
| Evaluate isolated rendering with explicit Ricy inputs/custom templates | Reuses an engine/target formats without daemon | Requires complete mapping, pinned version and output comparison |
| Adopt live Noctalia propagation | Palette events update apps | New dependency/ownership/global mutation contract; architecture-change approval and Recovery validation required |

Recommendation for a **future investigation**, not adoption: compare staged,
output-only generation against current assets before selecting propagation.
An isolated test must omit hooks/post-actions, dynamic commands, automatic
includes and active destinations. The shipped catalog does not satisfy that
condition unchanged. QSS/Kvantum geometry/SVG, Qt helper and KWin remain scoped
even if colors are generated. Recovery must work from packaged assets without
Noctalia or this checkout. No daemon or second theming engine is justified.

Architecture assessment: this step documents existing semantics within
ADR-0005 and adds static reference checks. No new required token path,
runtime dependency, ownership boundary or generation architecture is normative.
Selecting the candidate pipeline, mode synchronization, generator ownership or
global activation requires a separate proposal/explicit approval under
[architecture-change](../.agents/skills/architecture-change/SKILL.md).
No such selection was made; this grounding needs no further approval to finish.

## Dolphin: CURRENT → semantic role → TARGET TOKEN/CONTRACT

CURRENT is configured source/baseline. TARGET identifies existing references
for a later approved polish task; it is not a new appearance or migration.

| CURRENT | Semantic role | TARGET TOKEN / CONTRACT |
|---|---|---|
| Outer QMainWindow alpha178; configured translucency | surface.base / material.glass | `application_adaptations.dolphin.surface`, `colors.surface`; fill-only alpha; effective composition UNKNOWN |
| Opaque sidebar/topbar L | surface.content / material.solid / radius.panel | `application_adaptations.dolphin.sidebar_topbar`; Qt helper containment |
| Transparent toolbar children and native actions | surface.inherited / controls | `application_adaptations.dolphin.toolbar`; native actions/input |
| Transparent breadcrumb, hover overlay, editable surface/accent outline | surface.inherited / state_overlay / border.focus | `application_adaptations.dolphin.navigation`; native editing/completion |
| Neutral/active/hover tabs; native icons/close | surface.control / action / interaction_fill | `application_adaptations.dolphin.tabs`; state-specific foreground |
| Main card contains view/scroll/status | surface.content / solid / radius.card | `application_adaptations.dolphin.content_card`, `application_adaptations.dolphin.panel_layout`; upstream view/model |
| File rows/header paint | surface.control / border.subtle | `application_adaptations.dolphin.rows`, `application_adaptations.dolphin.header`; scoped radius/alpha |
| File selected/hover/both versus selected Places | interaction_fill versus action | `application_adaptations.dolphin.file_selection`, `application_adaptations.dolphin.places_buttons`; exact state differences |
| Breadcrumb/tab/menu hover differences | Contextual hover/selection | navigation/tabs/places/context-menu groups; no universal alpha |
| Devices/recent entries/indicators | Native status affordance on content | `application_adaptations.dolphin.places_buttons` for row paint only; KFilePlacesView/Solid own icons/models/actions; no device-status token |
| Transparent DolphinStatusBar within main card | surface.inherited / native content | `application_adaptations.dolphin.panel_layout`; native messages/style; no invented status color |
| Opaque rounded context menu; transparent corner cutouts | floating/content / solid / radius.popup | `application_adaptations.dolphin.context_menu`; Qt popup mask, existing Kvantum shadowless/popup_blurring=false |
| Native rubber band | state_overlay / border.focus | `application_adaptations.dolphin.rubber_band`; native hit testing/animation |
| Scrollbars/divider drag | Scoped neutral/hover/pressed | `application_adaptations.dolphin.scrollbars`, `application_adaptations.dolphin.panel_layout` |
| Outer restored/maximized/fullscreen/tiled corners | radius.window / compositor geometry | `application_adaptations.dolphin.native_window_radius`, `application_adaptations.dolphin.maximized_fullscreen_tiled_radius`; no KWin change |
| Noto Sans QSS/view and Places semibold | type.application_body / scoped label | `application_adaptations.dolphin.font`, `application_adaptations.dolphin.places_buttons.font_weight`; keep pt units/KDE preference difference |

MISSING roles remain unavailable; native device/focus/disabled/status/icon
behavior must not be replaced to populate a table. Live coverage, helper
lineage and independent failure Recovery remain UNKNOWN per the baseline.
No Dolphin Visual Polish starts automatically.

## READY FOR DOLPHIN POLISH

- Palette pairs: `colors.surface`, `colors.card`, `colors.on_surface`,
  `colors.secondary_text`, `colors.accent`, `colors.on_accent`,
  `colors.hover_selection`, `colors.on_hover_selection`, `colors.outline`.
- Surface/material/radius/border roles in [SEMANTICS](../themes/tokens/SEMANTICS.md),
  resolved through `application_adaptations.dolphin.surface`,
  `application_adaptations.dolphin.content_card`, `application_adaptations.dolphin.sidebar_topbar`,
  `application_adaptations.dolphin.context_menu`.
- State/layout/type groups: `application_adaptations.dolphin.navigation`,
  `application_adaptations.dolphin.toolbar`, `application_adaptations.dolphin.tabs`,
  `application_adaptations.dolphin.places_buttons`, `application_adaptations.dolphin.rows`,
  `application_adaptations.dolphin.header`, `application_adaptations.dolphin.file_selection`,
  `application_adaptations.dolphin.rubber_band`, `application_adaptations.dolphin.scrollbars`,
  `application_adaptations.dolphin.panel_layout`, `application_adaptations.dolphin.font`.
- Native Qt/KDE/Dolphin models/actions/icons/focus and KWin-owned corners/blur;
  [ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md) Recovery independence requirement.

## Validation and rollback

Use token/provenance/SVG checks and the architecture/foundation harness.
The token validator resolves exact canonical paths cited here and in SEMANTICS;
it does not evaluate aliases or validate a hypothetical generator. Local
links/anchors are checked separately from the harness's foundation scope;
official URLs were accessed. Run results are in [CHANGELOG](CHANGELOG.md).

Rollback is limited to documentary/reference-validator edits. Canonical JSON,
schema/version, identity assets and runtime profiles/themes/QSS/KColorScheme/
KWin remain unchanged. Selected repository/runtime file fingerprints were
compared locally; that does not continuously monitor every private state file.
Visual/live Recovery tests are NOT RUN: no visual/runtime change. App propagation
remains UNKNOWN; generator migration/execution is NOT APPLICABLE to this scope.
