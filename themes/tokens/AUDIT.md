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
