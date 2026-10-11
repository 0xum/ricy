# Ricy visual tokens

KNOWN: [tokens.json](tokens.json) is the canonical consumable source of Ricy
identity, contract **1.0.0**, schema **1**. It promotes existing values without
redesigning them. [DESIGN-SYSTEM](../../docs/DESIGN-SYSTEM.md) is the normative
entry point; [AUDIT](AUDIT.md) records provenance, hardcodes and discrepancies.
[ADR-0005](../../docs/adr/0005-consumable-visual-tokens.md) records this task's
authorized scope. Ricy owns visual roles; upstream owns toolkit primitives.

The legacy contribution's [JSON snapshot](../../ricy-kit/contributions/noctalia-visual-identity/tokens.json)
remains byte-for-byte intact for compatibility and provenance. Its values are
no longer a second editable authority. The transport copy is historical and is
not synchronized. No file, profile, backup or manifest was moved or renamed.

## Contract and units

This is ordinary UTF-8 JSON, using the existing vocabulary. It is not DTCG,
Noctalia configuration, a Qt theme, or a toolkit selection for Files. Parse it
with the consumer's JSON library. Check `schema_version == 1` and supported
`contract_version` before using it; missing required roles or an unsupported
major must produce a clear error, not silent substitute literals. Additive
optional fields are compatible; changing required paths, types, units or role
meaning requires a new major. Visual value changes still require their own
review and validation even when the structure stays compatible.

Color strings under `colors` are opaque **sRGB `#rrggbb`**. Material `color`
values reference a key in `colors`; resolve them with `tokens.colors[role]`.
Scoped application color fields use either a role name or an explicit scoped
hex value. Fields ending in `_ref` are dotted scalar paths into this document;
the two current references reuse KDE typography in the Konsole adaptation.
There is no implicit alias expansion, inheritance, expression evaluation or
runtime loader. Do not copy resolved palettes back into handwritten sources.

Geometry and shell font sizes use **logical px**, before local UI scaling;
they are not physical pixels or points. KDE/Dolphin font sizes explicitly use
**pt**. Durations use **ms** before the relevant motion preference multiplier.
Opacity uses **[0, 1]**; `_alpha_255` uses integer **[0, 255]**, divided by 255
when a toolkit requires a fraction. `178/255` is not exactly `0.70`.

## Available tokens and semantics

| Path / family | Existing values and meaning | Scope |
|---|---|---|
| `colors.surface`, `card` | `#181825`, `#313244`: shell background and raised/neutral content | Shared identity |
| `colors.on_surface`, `secondary_text` | `#cdd6f4`, `#a6adc8`: primary and secondary content | Shared identity |
| `colors.accent`, `on_accent` | `#cba6f7`, `#11111b`: active controls, focus/progress, content on accent | Shared identity |
| `colors.hover_selection`, `on_hover_selection` | `#977dba`, `#000000`: existing hover/selection pair | Shared identity; selected toggles and Dolphin places use accent instead |
| `colors.outline` | `#46485c`: subtle contours | Shared identity |
| `colors.success`, `error`, `warning`, `information` | `#a6e3a1`, `#f38ba8`, `#f9e2af`, `#89b4fa` | Semantic feedback |
| `geometry.native_spacing_logical_px` | `xs=4`, `sm=8`, `md=12`, `lg=16` | Native spacing cadence |
| `geometry.native_card_padding_logical_px`, `native_panel_padding_logical_px` | Both 14; separate semantic roles | Native card/panel inset |
| `geometry.native_radius_logical_px` | `small=3`, `medium=6`, `large=9`, `extra_large=12` | Native base radii |
| `geometry.shell_corner_radius_scale` | 1.3; radius = base × local scale × corner scale | Captured shell treatment; compute, do not store derived radii |
| `geometry.taskbar`, `top_search_support`, `notification`, `taskbar_context_menu`, `tray_context_menu` | Existing 44 px bar, 6/0 corners, 640×16 support with radius 8, attached-menu geometry and junction rules | Shell adaptations, not application layout defaults |
| `typography.shell_family`, `native_sizes` | Noto Sans; mini 11, caption 13, body 14, title 16, header 20 | Shell UI reference reusable by future Ricy UI |
| `typography.kde_family`, `kde_size_pt` | JetBrainsMono Nerd Font, 10 pt | Captured KDE preference, not the default font for every app |
| `typography.ui_scale`, `bar_content_scale`, `bar_font_scale` | 1.0, 1.5, 0.85 | Captured reference scales; respect the user's current scale |
| `motion.native_durations_ms` | fast 100, normal 200, slow 400 | Native transition cadence |
| `motion.application_icon_hover` | 140 ms / EaseOutCubic; visual scale 0.88→1 | Taskbar app/search icons only; fixed layout and hit area |
| `motion.taskbar_window_indicator` | 160 ms / EaseOutCubic; opacity/scale pairs 1/1, .55/.82, .28/.65, 0/.55 | Active, inactive, minimized, not running |
| `motion.app_icon_state_actions` | 420/360/260/220/200/240/220 ms | Launch/restore/focus/minimize/background/close-pinned/close-unpinned; finite shell actions |
| `motion.kwin_window_actions` | 320 ms, scale .85, InCubic/OutCubic, opacity 0→1 | Compositor window effects, not widget animations; .25 duration factor is an observation |
| `materials.attached_shell_background`, `notification_background` | Surface fill .70, blur requested | Shell only; never reduce text/icon or whole-window opacity |
| `materials.cards`, `detached_panels`, `outline` | Opaque cards/panels; outline width 1 logical px | Detached-panel solid policy; paint contour only where already enabled |
| `blur.settings` | Strength 5, noise 2, unit `kwin_effect_setting` | Existing KWin reference, not CSS/Qt blur radius or Gaussian sigma |
| `blur.observed_backend`, status fields | Native KWin blur; shared sampling/new-app support UNKNOWN | Audited observation, not runtime detection or effect activation |
| `application_adaptations.dolphin` | Noto Sans 10 pt; surface alpha 178; opaque card/L panel; 12/8/16 px scoped radii; row/header/selection alpha and tab/place geometry | Existing Dolphin adaptation only; color fields reuse shared roles except neutral `#242435` |
| `application_adaptations.konsole` | `#1e1e2e`, opacity .85, blur request, KDE monospaced font references | Existing terminal adaptation, not a shared surface replacement |

At local scale 1, shell radii are 3.9/7.8/11.7/15.6 logical px. Apply that factor
once; device-pixel conversion belongs to the toolkit. Fixed bar radii and Dolphin
radii do not inherit it. Apply typography's own UI/font scaling; do not use the
radius multiplier for text. Bar font/content scales are separate scoped inputs.

No universal disabled-opacity, focus geometry, spacing for every widget,
toolkit easing implementation or portable blur kernel is defined here. Preserve
native behavior until the specific consumer's adaptation is reviewed. Repeated
numbers with different meanings are not interchangeable tokens.

## Current and planned consumers

| Consumer | Status and consumption |
|---|---|
| Existing identity `reference.svg` | KNOWN offline migrated consumer: [template](reference.svg.in) + [renderer](render-reference.py) read canonical colors, font roles, sizes, padding, derived radii and fill alpha. Generated bytes equal the retained SVG. Diagram layout remains illustration geometry. |
| Design documentation and agents | KNOWN direct canonical reference through DESIGN-SYSTEM and this contract |
| Noctalia Style, public TOML and KDE-Current JSON | KNOWN existing consumers of duplicated native constants/configuration; no central runtime import yet |
| Qt/KDE/Kvantum, Dolphin QSS/helper, KWin effects | KNOWN existing role adaptations with hardcodes; no runtime migration in this task |
| Konsole, GTK, Plasma, login/lock themes | Existing adaptations/settings; upstream assets retain identity/licensing; no central runtime import or full harmonization claim |
| Ricy Files (`apps/file-manager/`) and future Ricy apps | PLANNED JSON consumers through a toolkit-specific adapter when their implementation is approved; no application or toolkit selected here |

## How future Ricy applications consume identity

Read the versioned JSON at build time or bundle that exact canonical file as an
application resource. Package the source file with the app: installed apps must
not depend on this checkout, private kit paths, shell caches or the availability
of Noctalia. Record the consumed contract version. Generated toolkit output is
derived, not a second editable source; an app-specific adapter should map roles
to existing toolkit primitives and remain local to the app until reuse is proven.

Start with shared palette roles, native spacing, Noto Sans UI sizes and native
motion cadence. Document local radius/scale choices using the existing reference.
Preserve primary text, focus and selection semantics. Respect current scale,
font availability and reduced-motion preferences in the toolkit; captured scale
and speed are reference values, not global settings to write. Do not apply shell
taskbar geometry, icon gestures, Dolphin delegate specifics or KWin effects to
ordinary controls just because they appear in the file.

A minimal build-time read (paths supplied by the build, not hardcoded in an
installed application) is:

```python
import json

with open(token_source, encoding="utf-8") as stream:
    identity = json.load(stream)
if identity["schema_version"] != 1 or identity["contract_version"].split(".")[0] != "1":
    raise ValueError("Unsupported Ricy visual token contract")
surface = identity["colors"]["surface"]
body_size_logical_px = identity["typography"]["native_sizes"]["body"]
content_gap_logical_px = identity["geometry"]["native_spacing_logical_px"]["sm"]
```

Transparency affects fill only. Blur requires compositor/window integration
and a legible opaque fallback, using the existing surface role. Do not activate
ricyblur, rewrite KWin preferences or assume shell shared sampling extends to an
application. Files' actual material integration remains UNKNOWN until validated.
Do not change Dolphin/MIME/FileManager1 or recovery dependencies to consume tokens.

## Validation, regeneration and rollback

Scripts resolve their own resources; run these examples from the repository root:

```bash
python3 themes/tokens/validate.py
python3 themes/tokens/render-reference.py --check
./scripts/verify architecture
```

The validator checks structure, references/units, retained-snapshot SHA-256,
before/after value equality, source-backed additions and exact SVG output. The
migration equality guard is intentional: an approved future visual change must
revise its provenance/guard and audit explicitly, rather than silently weakening
the check. `--check` is read-only. To regenerate the reviewed board explicitly:

```bash
python3 themes/tokens/render-reference.py --output ricy-kit/contributions/noctalia-visual-identity/reference.svg
```

The renderer uses Python's standard library and writes only the selected output;
without `--output` it emits SVG to stdout. No desktop generator, installer or
runtime SDK is introduced. To roll back this centralization, revert its source,
template, renderer and documentation edits; the old JSON/SVG bytes and all live
consumers remain intact. Recovery does not gain a token-loader dependency.
Static equality proves this board and captured values, not a real desktop's
visual behavior. Visual/session/recovery trials were NOT RUN.
