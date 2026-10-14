# Technical Changelog

Record significant changes in short entries. Minimum fields:
Model/Agent, Date, Purpose, Validation performed. Do not sign source files.

## 2026-10-14 — Align Dolphin Configure panels and selectors with the existing identity

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-14 (America/Sao_Paulo).
- **Purpose:** Adapt the native Configure dialog to the existing unified header/
  sidebar L, solid central cards, 8px gutters and 12px card padding/radii. Preserve
  KDE search/page/form/tab ownership and Defaults/OK/Apply/Cancel. Follow the user's
  selector feedback with a centered paint-only chevron and an opaque popover,
  using native Qt styled rows and established selection colors. Extend the
  user-requested field-glyph cleanup throughout Ricy Dolphin: selectors and
  integer/fractional steppers lose square backings while native slots, actions,
  limits, keyboard and field modes remain intact. Install only
  helper/QSS with private rollback. Follow the user's glass-gutter and outline
  feedback with the existing alpha178/255 base and a 1px popup outline/12px inset.
  Link Dolphin's existing KF6WindowSystem to enable blur on Configure and disable
  it on the solid popover; no additional runtime package, compositor patch,
  token, defaults, settings writer or Recovery path. Preserve the adopted system Papirus policy.
- **Validation performed:** Work-in-progress checkpoint at the user's request.
  PASS native Configure geometry/glass alpha, outline/insets/solid popover,
  field arrows and numeric mouse/keyboard/limit checks, resize/RTL, search,
  page/tab navigation and Apply/Cancel at 1x/1.5x. PASS motion/plugin lifetime,
  QSS interaction regressions, system icon inheritance, build/source/installed
  equality, architecture and whitespace. Inspected client-rendered captures of
  real Configure pages and popover; live probe reports native blur available
  and requested on Configure. Final visual acceptance, real preference
  persistence, full compositor/multiple-monitor coverage and Plasma Recovery
  remain NOT RUN. This checkpoint does not mark the visual work complete.

## 2026-10-14 — Adopt system Papirus icons and remove the Dolphin Tabler overlay

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-14 (America/Sao_Paulo).
- **Purpose:** Apply the user's approval after the preview. Dolphin follows the
  current KDE/Qt system theme (`Papirus-Dark`) by default, including dock close.
  Remove the forced overlay/direct SVG and the source/installed Tabler icon
  assets; preserve their history and private rollback backup. Update the scoped
  and full applicators so they retire only that icon directory. Keep Kvantum,
  QSS, layout/state colors, native actions, defaults, FileManager1, shortcuts,
  canonical tokens and Plasma Recovery paths. No new runtime dependency; the
  helper no longer directly links KF6IconThemes. Noctalia control glyphs remain.
- **Validation performed:** PASS native system inheritance despite a valid
  leftover legacy overlay and simulated Qt/KDE theme reconfiguration; native
  close geometry/legibility/state colors, motion and plugin shutdown at 1x/1.5x;
  build/source/installed equality, retired installed overlay absence and retained
  Kvantum style. PASS default live launch without preview flags: KDE/Qt both
  Papirus-Dark with navigation/folder/menu/view/close paths under Papirus-Dark;
  inspected client-rendered capture. PASS Python syntax, architecture and whitespace.
  The glyph check now allows five RGB channel values of antialiasing difference
  while preserving minimum visible size and centered geometry. Real Settings
  notifications, complete visual states/compositor and Plasma Recovery are NOT RUN.

## 2026-10-14 — Preview system Papirus icons without replacing Tabler

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-14 (America/Sao_Paulo).
- **Purpose:** Preserve the default Tabler overlay and add `--system-icons` to
  the existing Dolphin wrapper for the user's Papirus trial. The opt-in process
  follows KDE/Qt icons, including dock close, while preserving native actions,
  layout and state colors. Atomically install only helper/wrapper with a private
  manifest backup. No global setting, shortcut/default/FileManager1, compositor,
  token or additional runtime/Recovery dependency changes.
- **Validation performed:** PASS isolated default and preview native loader/
  Qt icon resolution with native theme reconfiguration, existing motion/close/
  plugin lifetime regression, helper build and installed equality. PASS real
  Dolphin probe: KDE/Qt both Papirus-Dark and navigation, folder, menu, view and
  close paths under Papirus-Dark. PASS architecture and whitespace. Real Settings
  theme-change notification and Plasma Recovery round trip are NOT RUN.

## 2026-10-13 — Route Dolphin shortcuts by the active shell

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Implement the clarified policy: Plasma Super+E uses native
  Breeze Dolphin and its launcher uses Ricy Dolphin; Noctalia uses Ricy for
  both. Extend the existing capture/transfer/restore to Meta+E, migrate the
  active older shortcut snapshot once without replacing saved shell keys,
  refresh Dolphin's stale desktop-action cache on transfer and retain its
  persistent registered action on return. Preserve visual assets, global
  defaults, wallpaper/panels and existing boundaries/dependencies. Back up
  source and private shortcut state using the existing switching backup route.
- **Validation performed:** PASS isolated capture/transfer/restore, empty
  original, older/partial migration and reentry; startup and offline recovery
  regressions; live shortcut-only Noctalia/Plasma/Noctalia round trip with
  snapshot preservation and one owner per phase; actual refreshed Noctalia
  action opens the Ricy helper/QSS and its live capture was inspected. The
  preceding native action test confirmed Breeze without the helper/QSS.
  PASS architecture and whitespace. User-reported PASS on 2026-10-13: the
  requested behavior passed after reboot. Agent physical key input,
  complete shell-switch/Recovery round trip or backup restoration after this
  change are NOT RUN. The first live invocation exposed a stale native launch
  cache; refreshing the Dolphin component corrected it and the rerun passed.

## 2026-10-13 — Restore Super+E to native Plasma/Breeze Dolphin

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Follow the user's clarified preference for native Dolphin on
  Super+E. The existing shortcut was active but launched the Ricy wrapper.
  Add a local, hidden native-Breeze launcher alias and assign Meta+E only to
  it, preserving the customized menu/default/FileManager1 route and other
  shortcuts. Preserve KWin, Noctalia, Plasma and open applications; no session
  switch or global appearance change. Back up files and action assignments
  with a scoped private restoration script.
- **Validation performed:** PASS desktop-entry validation, one live Meta+E
  owner and persisted assignment; invoke the actual KGlobalAccel action and
  confirm a new native Dolphin process with Breeze mapped, no Ricy helper or
  stylesheet; inspect its live capture; unchanged menu/clipboard shortcuts,
  restoration-script syntax, architecture and whitespace. NOT RUN physical
  key input, fresh login, restoration execution or full Recovery round trips.

## 2026-10-13 — Remove normal hover-selection badges from Ricy Dolphin

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Disable native `ShowSelectionToggle` through a nonpersistent,
  process-local shared KConfig preference in the existing Ricy helper. Remove
  normal file/folder hover badges while retaining native click/keyboard
  selection and explicit selection mode. Preserve Plasma's disk preference,
  geometry, icons, dependencies and Recovery boundaries. Atomically replace
  only the helper with a private restorer-compatible backup and open a new
  Ricy window.
- **Validation performed:** PASS native Dolphin isolated before/after hover
  comparison (one toggle becomes zero), Ctrl+A through native accessible
  selected states, disk preference preservation on shutdown and unrelated
  saves; existing close-button/motion/plugin-lifetime checks at 1x, helper build
  and source/installed equality, architecture and whitespace. NOT RUN live
  pointer hover across all view modes and Recovery round trips.

## 2026-10-13 — Round the embedded terminal surface and add an inset shadow

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Round the native Konsole display inside Dolphin's TerminalPanel
  to 8px and paint a subtle 4px inset shadow. Centralize the scoped recipe and
  justification while retaining the existing external card and approved close
  button. Preserve native input, profile, accessibility, scrollback and resize;
  no standalone Konsole, global theme, KWin or Recovery dependency change.
  Atomically install only the helper with a private backup and open a new
  Ricy window.
- **Validation performed:** PASS actual Konsole-part corner exposure, inset
  pixels, unchanged center/font/colors, keyboard/shell output, scrollback,
  resize and standalone exclusion at 1x/1.5x; existing close-button/motion/plugin
  lifetime checks at both scales; live 1x Dolphin compositor capture inspected;
  build/source/installed equality, tokens, architecture and whitespace checks.
  NOT RUN live 1.5x desktop, sustained terminal-output/CPU trials and Recovery
  round trips.

## 2026-10-13 — Restore the rounded close button and reduce its icon

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Restore the 24px button with the existing 8px radius and reduce
  only the Tabler icon canvas to 16px. Preserve balanced vertical gaps, native
  actions, and state color pairs. Atomically replace only the helper with a
  private backup and open a new Ricy window; Plasma and Recovery dependencies
  remain unchanged.
- **Validation performed:** PASS native geometry, balanced gaps, centered
  legible glyph, state pairs, close/reopen, RTL, motion/plugin lifetime at
  1x/1.5x; isolated hover capture, installed equality, architecture, whitespace.
  NOT RUN live compositor capture and Recovery round trips.

## 2026-10-13 — Reduce the dock close button and balance vertical gaps

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Reduce the native close control to the requested 18px. Include
  the existing 4px card-top gutter in its vertical center and align title text
  to the same center, preserving the Tabler glyph, state colors, trailing inset,
  and panel padding. Atomically replace only the helper with a private backup;
  open a new Ricy window. Plasma and Recovery dependencies remain unchanged.
- **Validation performed:** PASS production-QSS 18px geometry, balanced gaps
  within pixel rounding, centered/legible glyph, state colors, native close/
  reopen, RTL, motion/plugin lifetime at 1x/1.5x; isolated capture, installed
  equality, architecture, and whitespace. NOT RUN live compositor capture and
  Recovery round trips.

## 2026-10-13 — Correct the Dolphin dock close icon and compact alignment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Use the existing Tabler close SVG directly in a centered 20px
  icon canvas and compact 24px native control. Preserve the trailing/title-row
  alignment and native actions while pairing glyph colors with existing button
  states. Replace the ineffective indirect native icon-size override. Install
  only the helper atomically with a private backup and open a new Ricy window.
  No new asset, dependency, global theme, Plasma, or Recovery contract change.
- **Validation performed:** PASS production-QSS geometry, centered/legible
  glyph, paired hover/pressed colors, close/reopen, RTL, motion/plugin lifetime
  at 1x/1.5x; inspected isolated normal/hover/pressed captures; helper and Tabler
  asset equality, architecture, and whitespace. NOT RUN live compositor capture
  and Recovery round trips.

## 2026-10-13 — Align unlocked Dolphin headers and the terminal junction

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Style the native unlocked-panel close buttons with 28px hit areas
  and existing visual states, align title text using the active widget font,
  and stop the Places backing above the terminal so its header/top gap share a
  uniform base surface. Preserve locking, native close/reopen and dragging,
  terminal profile/content, card padding, and Plasma. Atomically install only
  QSS/helper with a private backup and open a new Ricy process. Ownership,
  dependencies, launchers, KWin, and Recovery contracts remain unchanged.
- **Validation performed:** PASS production-QSS native dock geometry, state
  colors, close/reopen, RTL, motion/plugin lifetime, and QSS/locked-title checks
  at 1x/1.5x; isolated native Dolphin header/terminal captures, build,
  source/installed equality, architecture, and whitespace. NOT RUN live
  compositor capture of final headers, exhaustive drag arrangements,
  floating/vertical docks, live 1.5x desktop, and Recovery round trips.

## 2026-10-13 — Reuse the split-folder drag line between Dolphin panels

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Share the existing 2px divider renderer between split-folder
  handles and native auxiliary dock separators, including existing state colors
  and end insets. Preserve native resizing, card padding, and Plasma. Atomically
  install only the Ricy helper with a private backup and open a new split window.
  No ownership, dependency, KWin, or Recovery contract change.
- **Validation performed:** PASS native dock-primitive paint/color/thickness/
  inset checks and motion/plugin-lifetime checks at 1x/1.5x; isolated Dolphin
  rendering; live 1x split-folder/Information capture; source/installed equality,
  architecture, and whitespace. NOT RUN exhaustive live drag/release, floating
  docks, live 1.5x desktop, and Recovery round trips.

## 2026-10-13 — Align Dolphin auxiliary-panel padding

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Match Information/Folders/Terminal card gutters and inner padding
  to the existing file card. Share edge detection and real layout margins in
  the existing Ricy helper; preserve native panel controls and the Plasma
  appearance. Atomically install only QSS/helper with a private backup and open
  a new Ricy process, preserving existing windows and Recovery dependencies.
- **Validation performed:** PASS live 1x Folders/Information/file-card capture,
  isolated native panel rendering, installed/source equality, QSS state checks
  at 1x/1.5x, motion/plugin-lifetime checks at 1x, architecture, and whitespace.
  NOT RUN live terminal/floating panels, live 1.5x desktop, and Recovery.

## 2026-10-13 — Align Ricy Dolphin settings and auxiliary panels

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Extend existing Qt/QSS visual roles to settings, toolbar editing,
  and Information/Folders/Terminal panels. Preserve native controls and terminal
  rendering. Correct disk-space text clipping caused by inherited vertical
  layout margins, and align zoom/capacity paint with existing colors and radii.
  Atomically install only QSS and the existing helper with a private backup;
  refresh QSS only in Ricy processes and open a new process for helper loading.
  Ownership/dependencies remain unchanged; no global KDE, launcher, KWin,
  canonical-token, or Recovery dependency change.
- **Validation performed:** PASS native Dolphin captures of the two dialogs,
  auxiliary panels, and readable status controls at 1x; extended QSS state and
  keyboard tests plus motion/plugin-lifetime checks at 1x/1.5x; architecture,
  whitespace, and source/installed equality. NOT RUN live scaled desktop,
  complete settings/popup coverage, file operations, and Recovery round trips.

## 2026-10-13 — Remove the Ricy Dolphin main-panel outline

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** Make the existing DolphinViewContainer border transparent only
  in Ricy QSS, preserving its geometry and other visual properties. Updated the
  installed stylesheet and the running Ricy process through the existing D-Bus
  setter; native Plasma/Breeze receives no stylesheet update. Ownership and
  Qt/QSS dependencies remain unchanged; a private QSS-only backup retains the
  existing restorer manifest format. No Recovery dependency is introduced.
- **Validation performed:** PASS source/installed/runtime stylesheet equality,
  existing QSS interaction checks at 1x, and architecture validation. Visual
  NOT RUN: the target window was not visible in desktop captures. Live Recovery
  and file operations NOT RUN; no related behavior changed.

## 2026-10-13 — Apply the documented terminal appearance for fish

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** apply the existing Ricy terminal appearance to the Konsole windows
  running the user's fish shell, conditional on documented configuration.
- **Changes:** use the maintained konsole-animated-cursor applicator to install
  PlasmaBlur profile/palette, Kvantum wrapper and application entry. Select the
  profile as default and preserve unrelated konsolerc settings. The documented
  preset uses Catppuccin Mocha, JetBrainsMono Nerd Font 10pt, .85 opacity, blur
  request and animated cursor support. No fish-specific Ricy prompt preset was
  found; preserve the user's CachyOS/Pure prompt and fish configuration.
- **Validation performed:** PASS supported AnimatingCursorEnabled property,
  exact profile/palette asset equality, desktop-file validation and fish config
  syntax. PASS byte equality of personal fish config/universal variables before
  and after application. PASS a fresh default-profile Konsole window running
  fish, reporting Plasma Blur and mapping Kvantum; visually inspected font,
  palette and terminal surface. Existing terminal windows were not closed.
  Backup emitted by the maintained applicator. NOT RUN every terminal launch
  route, all ANSI combinations, cursor-motion timing or new-login recovery.

## 2026-10-13 — Keep two shell-switching entries in the application menu

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** remove duplicate/test script entries from the user's launcher and
  keep only the proven Return to Noctalia and Return to Plasma actions.
- **Changes:** back up and remove three legacy menu/clipboard/return entries and
  the redundant visible toggle entry. Hide the package's direct Noctalia daemon
  launcher with a user-local NoDisplay override. Keep the active menu/clipboard
  desktop IDs as NoDisplay helpers for Super/Super+Space/Super+V. Apply NoDisplay
  to their maintained templates and the installer's optional toggle entry so a
  switch or reinstall does not reintroduce visible duplicates. Preserve runtime
  scripts, service paths, package files and recovery commands.
- **Validation performed:** PASS desktop-file-validate for the two visible
  launchers, hidden helpers and package override; application-entry inspection
  confirms exactly two visible Ricy actions; live shortcut registry retains all
  three menu/clipboard bindings. PASS architecture and whitespace checks.
  NOT RUN another shell round trip or login in this menu-only cleanup; both
  retained actions were already exercised earlier in this session.

## 2026-10-13 — Fix Noctalia startup after a cold login

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** prevent Noctalia initialization from aborting after reboot when
  installed static shell/search units are not loaded yet.
- **Changes:** make `reset-failed` preparation nonfatal. The subsequent shell
  start and readiness checks remain mandatory, with existing Plasma recovery on
  actual failure. Restore the user-requested Noctalia autostart preference.
  No new watchdog, delay, session boundary or layout change.
- **Validation performed:** KNOWN current-boot journal and a direct invocation
  reproduce `Unit not loaded` for reset-failed. PASS a regression that fails on
  the prior integration and passes after the fix; a separate case confirms that
  real shell-start failure still propagates and calls recovery. PASS architecture
  and recovery validators, live startup in the affected boot, shell/search/
  integration active, IPC responsive and persistent autostart target enabled.
  PASS captured layout and centered control preserved. NOT RUN another reboot
  or login after this correction; persistent shell-failure recovery remains
  outside this test. Original source/validator backed up privately.

## 2026-10-13 — Refresh the Dolphin shortcut cache and compare shell modes

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** make Meta+E launch the Ricy-customized Dolphin and verify that
  Plasma and Noctalia use the same Dolphin appearance.
- **Changes:** the installed desktop override, FileManager1 service and systemd
  drop-in already pointed to the visual wrapper. The existing KGlobalAccel
  service-action component retained an earlier `/usr/bin/dolphin` launch entry.
  Back up the shortcut/desktop files, rebuild the KDE service cache, clean up
  only the Dolphin component and register its `_launch` action with Meta+E.
  Preserve application identity, MIME defaults, other shortcuts and source assets.
- **Validation performed:** PASS reproduction through the actual cached shortcut
  action: the original launch lacked the Ricy helper. PASS refreshed invocation
  in both Noctalia and Plasma: wrapper arguments, mapped Qt helper, Kvantum and
  stylesheet source were correct. PASS identical QSS and theme/helper hashes
  across shell modes, and one Meta+E registration. Return to Noctalia with the
  centered control preserved. Only agent-created Dolphin test windows were
  closed. NOT RUN physical keyboard input, new login, every file operation or
  all visual/interaction states.

## 2026-10-13 — Restore the captured Noctalia preferences and center its control

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** restore the user's saved Ricy layout from the 2026-10-12
  integration snapshot. The initial migration preserved an older local profile
  and omitted the versioned UI overrides; matching that older backup did not
  reproduce the captured Ricy layout.
- **Changes:** restore captured base configuration, palette, settings, four plugin
  payloads and selected community template while preserving private runtime data.
  Adapt saved monitor identifiers to the destination's two 1920x1080 outputs
  and the wallpaper path to a user-owned asset. Per explicit user clarification,
  place `control-center` alone in `bar.default.center`; move the captured center
  clock to the end group. Retain captured capsule treatment, 42px thickness,
  scales, font and border preferences. Preserve the original source snapshot.
- **Validation performed:** PASS all snapshot payload checksums, configuration
  validation, effective configuration export, active shell/search/integration and
  visual inspection of both bars with the Noctalia icon centered. PASS restored
  monitor placement and visible desktop widgets. Destination/profile/template
  backup saved before application. NOT RUN every plugin/account operation,
  template destination, all interaction states, login and failure recovery.

## 2026-10-13 — Migrate the installed legacy desktop to the GitHub kit

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-13 (America/Sao_Paulo).
- **Purpose:** update this CachyOS desktop using `https://github.com/0xum/ricy`,
  revision `9815558313809c31887bbc55e3a8717bac31d039`.
- **Changes:** build and activate the maintained cumulative Noctalia 5.2.1
  patch; install persistent shell/search/session integration and panel-only
  switching, preserving the legacy profile, private state and original panel
  backup. Disable the legacy full-layout session monitor and route its return
  wrappers to the maintained switching command. Remove legacy shortcut defaults
  to avoid duplicate menu/clipboard registrations. A session drop-in preserves
  applications and selects the migrated profile while an existing child process
  keeps the former transient shell unit alive. Apply the maintained Dolphin
  identity/helper and window fade/expansion assets, with installer backups.
- **Local compatibility fixes:** make the KConfig reader accept valid valueless
  deletion entries such as `BorderSize[$d]`. Keep the Qt generic plugin parentless
  because Qt owns its shutdown lifetime; parenting it to QApplication caused
  double deletion. Add a real generic-plugin shutdown regression to the existing
  isolated motion validator. No compositor replacement or new architecture.
- **Validation performed:** PASS isolated release build and `scripts/verify all`
  with the matching cumulative source, zero failures or unavailable checks;
  Dolphin motion, QSS/icon validation and generic-plugin shutdown regression;
  real Dolphin opening and clean exit; systemd unit validation, running executable
  hash equality, shell IPC and search adapter activation. PASS live Plasma/Noctalia
  round trip: panels restored then hidden, KWin PID and wallpaper preserved;
  final shell/search/integration active and login preference enabled.
  NOT RUN reboot/login, persistent shell-failure recovery, all file operations,
  all visual states and monitor scales. Optional compiled KWin corner/blur
  plugins were not installed. Private backup paths remain in the local update
  record rather than public source documentation.

## 2026-10-12 — Integrate Noctalia Night Light with KWin

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-12 (America/Sao_Paulo).
- **Purpose:** make the Noctalia control available and reflect the native filter
  already configured in KWin instead of requiring Wayland gamma-control support.
- **Changes:** the existing GammaService observes KWin Night Light properties
  through the existing session bus. Left-click uses the native KGlobalAccel
  pause/resume action; right-click opens KDE Night Light settings. KWin retains
  temperature/schedule ownership. Noctalia configuration reloads cannot override
  that backend; unsupported forced-mode IPC returns an error. Property signals
  update the UI; bounded periodic refresh handles service loss and return.
  The cumulative patch, component dependency record, contribution guide, and
  shell validation harness include this integration. No new daemon, package,
  visual token, compositor patch, or session path was introduced.
- **Validation performed:** PASS isolated incremental release build using
  unchanged prior compiled inputs and rebuilt affected consumers; clean-index
  cumulative patch replay; private D-Bus tests of night/day state, pause/resume,
  external changes, configuration reload, unavailability, and service return;
  `RICY_NOCTALIA_SOURCE=<matching-source> ./scripts/verify shell`;
  `./scripts/verify architecture`; `./scripts/verify recovery` offline;
  39 foundation regressions and architecture validation of the exact staged tree;
  live pause/resume through Noctalia IPC and KWin properties, restored to 4500 K;
  unchanged KWin configuration and preserved application processes; active menu
  visual inspection and user confirmation. Activation used the existing
  backup/restore tool and the shell remains active without automatic restarts.
  NOT RUN hover/focus, other monitor scales, persistent failure Recovery/login.
- **Recovery:** KWin continues owning the filter independently of the shell;
  upstream Noctalia, KDE settings, earlier source/build, and the activator's
  binary/drop-in backup are preserved. See
  [the contribution guide](../ricy-kit/contributions/app-icon-reordering/README.md#kwin-night-light).


## 2026-10-12 — Refresh current Noctalia preference backup

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-12 (America/Sao_Paulo).
- **Purpose:** include the user's subsequent saved Noctalia changes.
- **Changes:** refreshed snapshot settings and checksum after comparing all
  captured config/state payloads with the active profile. The only changed file
  was settings.toml: the explicit theme.source override was removed. Installed
  plugin payloads, base configuration and selected VS Code template were equal.
  No runtime settings or recovery data were modified.
- **Validation performed:** PASS payload checksums, active payload equality,
  enabled-plugin coverage, TOML/JSON parsing, architecture and whitespace.
  Live restoration and Recovery round trip NOT RUN; runtime behavior UNKNOWN.

## 2026-10-12 — User-requested Noctalia configuration snapshot

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-12 (America/Sao_Paulo).
- **Purpose:** preserve current Noctalia preferences, installed plugins and
  dependency versions in the local repository at the user's explicit request.
- **Changes:** opt-in [snapshot](../ricy-kit/contributions/noctalia-kde-integration-and-menus/snapshots/2026-10-12/README.md)
  of base config/palette, UI overrides, four plugin payloads, VS Code template,
  wallpaper and dependency inventory/checksums. Existing private histories,
  credentials, runtime data and recovery backups remain excluded and untouched.
  No runtime migration, installation, restart or canonical token change.
- **Validation performed:** PASS architecture, payload SHA-256 checks, TOML/JSON
  parsing, current configuration equality, enabled-plugin coverage and whitespace.
  PASS available shell syntax checks; NOT RUN shell action checks because the
  default source cache differs from the pinned cumulative patch. UNKNOWN local
  resolution for mpv-mpris, proton-pass-cli, paru and yay. Live restoration,
  Recovery round trip and redistribution review NOT RUN.

## 2026-10-11 — Dolphin motion color regression correction

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** correct user-reported gray Places selection and faded colors
  introduced by the Motion pass; its prior visual validation missed this case.
- **Changes:** complementary premultiplied-channel interpolation preserves common
  opaque colors/alpha; explicit native Places view/index/paint context keeps
  style identity during capture. Existing validator compiles the actual style
  and adapter and checks selected pixels/opacity through rapid hover and settle.
- **Validation performed:** PASS current Qt/KIO motion and QSS checks at 1x/1.5x,
  native before/after reproduction (24/24 bad original frames,0/24 corrected at
  each scale), build/install equality, architecture/tokens and whitespace.
  FAIL preexisting shutdown139; live idle sample UNKNOWN due active tab hover/
  mouse input, full hardware/RTL/Recovery NOT RUN. No palette, geometry, model,
  provider/default, shell, KWin or canonical token changes.
- **Evidence/rollback:** [correction record](DOLPHIN-BASELINE.md#motion-transition-color-regression--2026-10-11).

## 2026-10-11 — Dolphin Identity & Motion Pass: Motion

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** add subtle paint-only chrome transitions after the validated
  Typography and Iconography commits, preserving native behavior and Recovery.
- **Changes:** event-driven QVariantAnimation in the existing Qt helper;
  transparent native snapshots, interruption from presented paint, fast/hover/
  interaction-state cadence, native Qt hints/KDE explicit disable, stable native
  painting and safe control/model connection lifetime. Avoid redundant tab-close
  mask invalidation. Scoped helper-only atomic installer with private rollback.
- **Validation performed:** PASS isolated Qt/KIO intermediate pixels/reversal/
  exact final state, geometry, input/state/disable/lifetime and idle paints at
  1x/1.5x; real Dolphin chrome captures,2000-file read/repeated-hover comparison,
  five stable samples with zero window/file paints at both scales, native KDE
  disable, helper build/deployment, QSS/icon/token checks and full offline harness
  (zero failures/skips). Early effect idle feedback and rejected snapshot failure
  were corrected before the gate, retaining their evidence.
- **FAIL, preexisting:** real graceful shutdown139 and long-list status/header
  overlap reproduced with Phase2 control. UNKNOWN live Recovery, physical input/
  fractional/RTL/accessibility matrix and cross-app motion preference reload.
  Filesystem mutation/Recovery switching NOT RUN; further redesign NOT APPLICABLE.
- **Evidence/rollback:** [phase and integrated record](DOLPHIN-BASELINE.md#identity--motion-pass--phase-3-motion--2026-10-11).

## 2026-10-11 — Dolphin Identity & Motion Pass: Iconography

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** align small Dolphin action glyphs with Noctalia's Tabler language
  while preserving KDE content/state assets and Recovery fallback.
- **Changes:**13 Actions-only SVGs with pinned upstream hashes/MIT attribution;
  optional native process-local helper selection and scoped atomic installer.
  No global icon setting, persistent Dolphin theme key, content substitution or
  geometry change. Existing native breadcrumb/tab primitive glyphs remain.
- **Validation performed:** PASS native paths/content inheritance, SVG paint/
  licensing/scope checks, native modes/contrast/stable geometry at 1x/1.5x, live
  toolbar/menu/breadcrumb/tabs/overflow/search, missing-overlay Breeze fallback,
  helper build/installed equality, QSS states and architecture/token checks.
- **FAIL, preexisting:** shutdown139 remains; all device/thumbnail formats, full
  RTL/accessibility/physical scales and independent live Recovery NOT RUN/UNKNOWN.
  Rejected rc fallback and initial SVG errors were corrected before the gate.
- **Evidence/rollback:** [phase record](DOLPHIN-BASELINE.md#identity--motion-pass--phase-2-iconography--2026-10-11).

## 2026-10-11 — Dolphin Identity & Motion Pass: Typography

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** synchronize existing Dolphin/Noctalia typography with the active
  KDE/Qt application family instead of selecting another font.
- **Changes:** remove QSS family/size and native-header hardcodes; enable native
  system font in all three modes, preserving dormant ViewFont and Places emphasis.
  Explicit one-shot installer atomically installs existing helper/QSS and changes
  only those font flags and official Noctalia family, with private rollback.
  Contextual shell sizes/font_scale, canonical token values and protected
  infrastructure/defaults remain unchanged.
- **Validation performed:** PASS phase-scoped typography: active KDE/Qt resolution,
  isolated helper build, installed equality, live native Dolphin modes/chrome/menu/
  editor/tabs/Places/status at 1x and process1.5x, Noctalia bar/launcher/controls,
  config validation/reload, QSS/state checks at both scales, architecture/tokens
  and whitespace. Native status elision remains preexisting.
- **FAIL, preexisting:** shutdown139 reproduced with backed-up helper/QSS and the
  updated helper/QSS; not attributed to Typography. Live independent Recovery,
  operations/devices, physical fractional monitors and complete RTL/glyph coverage
  NOT RUN/UNKNOWN. No new architecture was needed.
- **Evidence/rollback:** [phase record](DOLPHIN-BASELINE.md#identity--motion-pass--phase-1-typography--2026-10-11).

## 2026-10-11 — Dolphin toolbar menu-arrow insets

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** inset toolbar dropdown indicators and resolve duplicate arrows
  and separator clipping reported by the user after the initial QSS adjustment.
- **Changes:** ordinary menu indicators retain a 6px box and 4px inward/bottom
  offsets. Split buttons explicitly style both the transparent menu surface and
  its single centered 6px glyph, preventing the native/custom double paint.
  A 16px menu region provides edge clearance; split-button right padding grows
  from 8px to 12px, preserving the measured primary action width while enlarging
  the menu target. Existing approved values are reused. Native icons, actions
  and popup modes remain; no helper, KWin, launcher/default or filesystem change.
- **Validation performed:** PASS Qt before/after previews for three popup modes,
  single-arrow inspection and primary-action geometry (76px retained; menu region
  grows 12px to 16px); existing QSS/state fixture, architecture/token checks and
  whitespace. Installed QSS equals source, with private atomic rollback backups.
- **NOT RUN:** complete live popup interactions, all scales/RTL and live Recovery.
  Live stylesheets are refreshed when an instance is available, without closing
  windows. The original inset-only split-button rule is superseded by this fix.

## 2026-10-11 — Rounded Dolphin path dropdown

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** widen the compact path-dropdown button so its approved rounded
  hover backing fits, matching the root breadcrumb button reference.
- **Changes:** the existing Qt helper reserves a 24px width for
  KUrlNavigatorDropDownButton, retaining the existing 28px height, radius6 and
  hover-selection alpha65 treatment. Upstream derives the natural width from
  half the natural height; the earlier helper height override left the button
  too narrow. The user's clarification supersedes the initial glyph-only edit;
  glyph geometry/stroke are restored and no oversized backing is painted outside
  the control. Native menu, keyboard handling and breadcrumb behavior remain.
  Atomic helper-only installation with private existing-restorer-compatible backups.
- **Validation performed:** PASS helper compilation, native KUrlNavigator Qt
  fixture with ten breadcrumb/editor toggles and unchanged URL/editor; controlled
  hover in a real Dolphin window using the installed wrapper and a uniquely named
  private diagnostic plugin confirms 24x28 bounds and unclipped rounded backing.
  PASS architecture/token checks and whitespace. No token or KWin change.
- **NOT RUN:** all scales/RTL, complete dropdown-menu keyboard interactions and
  live Recovery. Existing windows retain their mapped helper; new processes load
  the change. The documented shutdown SIGSEGV remains outside this visual edit.

## 2026-10-11 — Dolphin first visual polish pass

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** correct confirmed QSS spacing/state inconsistencies in the current
  installed Dolphin while retaining approved layout, native behavior and the
  separately updated tab-overflow helper.
- **Changes:** normalize residual generic padding from 5px to existing 4px; preserve
  checked/pressed toolbar interaction fill/foreground during hover; explicit
  accent focus contours in existing border slots; unfilled disabled tools.
  Atomically deploy only QSS with a private existing-restorer-compatible backup.
  The native full-width status experiment exposed clipped storage controls and
  was reverted; dolphinrc equals its initial bytes. No token, helper, theme,
  launcher, MIME, FileManager1, filesystem implementation or KWin change.
- **Validation performed:** PASS Qt QSS painting/state precedence and native
  editor/tab/menu interactions at 1x/1.5x; installed-wrapper startup, directory/tab
  navigation and live grid/compact/details captures; token checks, architecture,
  Recovery offline, Kvantum INI/SVG parsing and changed-file whitespace checks.
  PASS limited native offline fallback with missing optional visual layers and
  Fusion under isolated D-Bus/config/state/data; not automatic Recovery.
- **FAIL (preexisting):** customized Dolphin shutdown SIGSEGV in Qt application
  destruction, also present before edits and documented by the tab-overflow task.
- **UNKNOWN / NOT RUN:** independent live Recovery, every device/hover/focus state,
  complete popup composition, live scale/monitor/RTL/reduced-motion combinations.
  No complete Recovery-regression claim. No new compiled layer or backend test
  applies. Wrong/incomplete early test captures were discarded after user correction.
- **Record/backlog:** [first-pass audit](DOLPHIN-BASELINE.md#first-visual-polish-pass--2026-10-11)
  documents categories, current-source differences, unchanged ownership/dependencies,
  recovery implications and deferred status/lifetime work. No second phase.

## 2026-10-11 — Dolphin tab overflow controls

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prevent tab close controls from overlapping overflow arrows and
  provide 8px trailing spacing using existing Dolphin/Qt ownership and spacing.
- **Changes:** horizontal scroll subelement geometry reserves 64px; native 24px
  arrow buttons have an 8px gap and 8px edge inset. Close-button paint/hit masks
  exclude clipped controls and reset after scrolling/resizing. Installed only
  the Qt helper atomically with a restorer-compatible private backup; existing
  windows retain their mapped helper. No new architecture or Recovery dependency.
- **Validation performed:** PASS helper build, 18 Qt overflow layouts across
  three widths/LTR/RTL/three selections, native close/scroll clicks and restored
  masks after overflow removal; live Dolphin capture/probe confirms geometry.
  PASS `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py`
  and `git diff --check` for the changed files.
- **FAIL (preexisting):** live probe teardown SIGSEGV in Qt application
  destruction reproduced with the preserved pre-change helper as well as this
  change, including window close. Captured geometry passes; clean process exit
  does not. No unrelated teardown fix is claimed.
- **Publication validation:** PASS architecture/token checks and helper build
  against the selected Git index in an isolated export. An existing audit link
  to the intentionally excluded private ZIP was changed to a plain path; no
  archive contents were added. Unrelated visual-grounding edits remain local.
- **NOT RUN:** all monitor scales, live drag/reorder and live Recovery.
  Offline checks do not certify the session. Transport snapshots are preserved.


## 2026-10-11 — Dolphin final-tab containment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** keep the final tab border inside the shell panel when no overflow
  arrows are shown.
- **Changes:** bound the horizontal Qt tab-bar allocation with an 8px trailing
  gutter, mirrored for RTL; preserve content geometry and existing overflow
  controls. Installed the helper atomically with a restorer-compatible backup.
  No new architecture, tokens, compositor change or Recovery dependency.
- **Validation performed:** PASS helper build; eight Qt allocations across
  four widths/LTR/RTL with and without overflow; native last-tab close;
  previous 18 overflow cases and close/scroll/mask regressions; live Dolphin
  seven-tab capture/probe with hidden arrows and an 8px trailing gutter;
  `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py` and
  changed-file `git diff --check`.
- **FAIL (preexisting probe limitation):** live capture process exit 139 at
  teardown; the previous comparison reproduced failure with the prior helper.
- **NOT RUN:** all monitor scales, live drag/reorder and live Recovery.
  Existing processes retain their mapped helper; new windows load this update.


## 2026-10-11 — Dolphin rounded purple overflow indicator

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** replace the thin blue tab-overflow line with the existing purple
  accent, a 4px width and rounded ends.
- **Changes:** Qt helper paints the native tear primitive and reserves its wider
  horizontal rectangle. Qt retains visibility/placement and native tab controls.
  No token, compositor, architecture or Recovery dependency changed. Installed
  the helper atomically with a restorer-compatible private backup.
- **Validation performed:** PASS helper build; LTR/RTL pixel checks for accent,
  4px geometry, rounded tips and native visibility; 18 overflow layouts and
  native close/scroll regressions; live Dolphin capture;
  `./scripts/verify architecture`, `python3 -B themes/tokens/validate.py` and
  changed-file `git diff --check`.
- **FAIL (preexisting probe limitation):** live capture-process teardown again
  exited 139; the previous baseline comparison reproduced the same failure.
- **NOT RUN:** all display scales, live Recovery and every tab interaction.
  Existing windows keep the mapped helper; open a new window for the update.

## 2026-10-11 — Noctalia Visual Language Grounding

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** formalize existing Ricy visual roles using official Noctalia v5+
  concepts while preserving themes/tokens as the canonical authority.
- **Changes:** updated [DESIGN-SYSTEM](DESIGN-SYSTEM.md), added the documentary
  [semantic dictionary](../themes/tokens/SEMANTICS.md) and
  [grounding assessment](NOCTALIA-VISUAL-GROUNDING.md). Recorded
  KNOWN/INFERRED/MISSING findings, color correspondences, surfaces/materials,
  border/radius/shadow ownership, contextual motion/type/states, App Theming/
  KColorScheme feasibility, Dolphin CURRENT → role → existing token mapping
  and READY FOR DOLPHIN POLISH references. The existing token validator now
  resolves documentary canonical paths; it does not implement semantic aliases.
  No new architecture/generator contract was selected or made normative.
- **Validation performed:** PASS `./scripts/verify architecture`,
  `python3 -B scripts/test-foundation.py` (39 disposable-fixture regressions),
  `python3 -B themes/tokens/validate.py` (95 documentary token references plus
  existing schema/units/provenance/equality checks),
  `python3 -B themes/tokens/render-reference.py --check` (identical SVG),
  five isolated reference-validator probes (valid scalar/group and rejection
  of missing scalar/scoped leaf, empty references and scalar traversal),
  47 local documentation links/three heading anchors and diff whitespace.
  Official URLs were accessed and the pinned upstream template/Style source
  was inspected read-only. Repository/selected runtime fingerprints confirm
  unchanged canonical JSON, existing identity assets and 49 selected installed
  configuration/asset files; unrelated preexisting work was preserved.
- **Harness scope:** `./scripts/verify all` exited2 with no failures and one
  unavailable check. PASS maintained source syntax/historical guard syntax,
  offline Recovery panel merge and 28 window-effect scenarios. This does not
  certify a live session.
- **FAIL:** none remaining. The initial foundation regression rejected new
  direct links to outputs excluded from its fixture. Grounding now cites the
  maintained provenance inventory and records those inspected paths as text;
  the unchanged foundation suite passes. An initially incorrect external
  Theme path was corrected to the official navigation target.
- **NOT RUN:** Noctalia action/native regressions through the default harness
  cache, which does not match the current cumulative patch; no cache was
  rebuilt/replaced for this documentation task. Visual/scale/RTL interactions,
  application propagation, live session and failure Recovery were not exercised.
- **UNKNOWN:** generated output equivalence/end-to-end app theming, full private
  palette equivalence, composited opacity/blur continuity, full shadow toggles,
  helper lineage and independent live Recovery. Missing semantic values remain
  unassigned rather than borrowing upstream defaults.
- **NOT APPLICABLE:** runtime deployment, visual changes, generator/consumer
  migration, KWin changes, new daemon/engine/ADR and automatic Dolphin polish.
- **Recovery:** no applicator/hook/installer, profile/theme selection, service
  restart, file-manager launch or compositor action ran. Canonical JSON remains
  schema1/contract1.0.0 byte-identical; QSS/Kvantum/KColorScheme and existing
  restoration paths remain intact. Rollback affects only this step's
  documentation and reference-validator edits; no runtime dependency was added.

## 2026-10-11 — Taskbar actions preserve the clicked KWin window

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** fix separate Brave/Dolphin icons activating another window of
  the same application, particularly across two monitor bars.
- **Changes:** the cumulative Noctalia 5.2.1 patch (pinned commit
  `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`) marks nonempty KWin UUIDs as exact
  identities. This uses the existing authoritative task identity for
  focus/minimize/close, preventing monitor/placement reconciliation from
  substituting a same-app window. No runtime dependency, ownership boundary,
  design value, window effect or session architecture changed. The native
  validator now covers the compiled KDE adapter/model/action path on a private
  D-Bus KWin fixture; `dbus-run-session` is an offline-test dependency only.
- **Validation performed:** PASS isolated release build, clean patch replay
  (26 source files), `verify architecture`, `verify shell` with the matching
  isolated source, `verify recovery` offline, 39 foundation regressions,
  32 compiled KDE identity/action scenarios, 17 JS action scenarios,
  22 ordering scenarios, 20 icon-motion scenarios, 15 indicator/historical
  effect scenarios, native single-space/drag regressions, active service
  configuration validation and diff whitespace. The new regression failed
  against the preserved earlier build with a substituted window UUID and
  passed against the corrected build. GCC emitted an unrelated warning in
  unchanged upstream `theme/fixed_palette.cpp`; compilation completed.
  PASS user-reported real-session icon focus after activation ("Passed");
  the exact application/monitor/title combinations were not independently recorded.
- **Activation:** the existing notification-continuity activator backed up the
  previous binary/drop-in and restarted the shell with its temporary
  application-preserving KillMode. This also deploys the previously accepted
  cumulative RICY-001 source revision. PASS running-executable/build byte
  equality, previous-binary backup equality, original cache/diff/binary
  preservation, active shell/search/Plasmashell units, new-shell ownership of
  the KWin tracking adapter, and valid live status IPC. Thirty-eight captured
  child PIDs remained alive; one transient PID ended between snapshots, so
  the initial blanket child-PID assertion was too broad. No real window was
  closed/minimized for validation.
- **NOT RUN:** agent-operated physical clicks/visual captures, all
  scales/orientations, persistent shell failure, login and a live
  Plasma/Dolphin Recovery round trip. Process/IPC readiness does not certify
  those interactions or independent Recovery.
- **NOT APPLICABLE:** KWin/effect installation, session migration, token
  changes and transport-tree synchronization.
- **Recovery:** restore using `notification-continuity/enable.py --restaurar`
  with the private backup printed by the activator. The original cache,
  upstream `/usr/bin/noctalia`, private settings, Plasma/Dolphin tools and
  existing return paths are preserved. Historical transport/manifests remain
  unchanged. Private profiles, binaries and backups are excluded from this commit.

## 2026-10-11 — Dolphin selected; own Ricy Files retired

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** execute the user's explicitly approved direction: Dolphin is the
  Ricy file manager; retire the own application and record its current baseline
  without visual or runtime work. User assesses Dolphin visual progress at 90%.
- **Changes:** Accepted [ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md), updated
  RICY-005/architecture/components/recovery/design/development rules. ADRs 0003,
  0008 and 0009 are Superseded; unaccepted 0007/0010 are Rejected. Removed 24 tracked
  prototype files (C++, QML, CMake, packaging, tests and exclusive runner) from
  the active checkout. No own build directory existed there. Retired 07–10 gates;
  specifications/evaluation/prototype README preserved as [history](history/ricy-files/README.md).
  The code was not in main, was not merged into it, and remains in Git history.
  Unmerged browser/UI worktrees were left intact as historical work.
- **Baseline:** [DOLPHIN-BASELINE](DOLPHIN-BASELINE.md) distinguishes installed
  registration/configuration, inferred behavior and unproved runtime behavior;
  records hashes, colors/geometry/materials/controls, token hardcodes and gaps
  only as backlog. No automatic next stage. Earlier uncommitted Dolphin work
  remains intact; no applicator ran in this task.
- **Validation performed:** PASS architecture (57 mandatory files, 420 links),
  foundation regression suite (39 checks, including rejection of the retired
  application reservation), token/provenance checks, offline Recovery panel
  merge and 28 window-effect scenarios, historical moved-document links,
  installed Dolphin before/after hashes and diff whitespace.
  Canonical JSON/validators/renderers/identity board remain byte-identical in
  this task; only token README consumer-direction documentation changed.
- **FAIL:** none in the executed checks.
- **UNKNOWN:** independent live Recovery when visual helpers/themes fail,
  process-loaded helper/source reproducibility and full functional/visual coverage.
- **NOT RUN:** live UI/cold launch/FileManager1/device/Trash/portal operations,
  failure switching/login, all scales/RTL. No Dolphin process/FileManager1 owner
  was present at the read-only snapshot; no application was launched to fill gaps.
- **NOT APPLICABLE:** own backend implementation/build tests after retirement;
  external-link/latest-upstream verification for the local installed baseline.
- **Recovery:** installed wrapper/desktop/default/service/theme/QSS/helper and
  dolphinrc unchanged by this task; no KWin/Plasma/Noctalia action. Historical
  transport/manifests and private rollback state preserved. This source/document
  change is reviewable in Git without rewriting any history.

## 2026-10-11 — Dolphin menus follow configured KDE proportions

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** match the user's configured KDE menu density and spacing.
- **Changes:** panel padding 12, item vertical padding4/margin1 and horizontal
  padding 12; native icon inset retained; transparent4px separator gaps.
- **Validation performed:** PASS Qt menu capture/fixture, architecture/token
  validation and diff whitespace. NOT RUN all live submenus, RTL or scales.
- **Recovery:** QSS applied to existing windows with private whole-file backup;
  no helper, session or compositor change in this revision.

## 2026-10-11 — Dolphin popup corner transparency and icon spacing

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** remove native popup backing from rounded corner cutouts and
  give context-menu icons more left breathing room.
- **Changes:** radius 12 native menu surface mask, transparent Window palette
  and no background autofill; icons and text shift inward8px together.
- **Validation performed:** PASS helper build/atomic application, Qt menu
  fixture (transparent corners/mask, icon capture, keyboard/native actions),
  architecture/token checks and diff whitespace. NOT RUN all live submenus,
  RTL or display scales.
- **Recovery:** existing private backup/whole-file rollback; new process
  required for helper changes. No shell/compositor or historical kit changes.

## 2026-10-11 — Dolphin menus, scrolling and panel containment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** match context menus, scrollbars, selection and draggable panel
  divisions to the existing identity; fix clipping and stale Meta+E launches.
- **Changes:** rounded opaque popup with native actions, compact rounded
  scrollbar track/thumb, rounded translucent drag selection; card backing
  around the full view container with real layout insets and contained scrolls.
  Internal gaps reduced while preserving outer 8px margins. Native divider
  paints track color normally, thumb color on hover and accent during drag.
  GUI launches use a new process; existing KDE shortcut cache refreshed.
- **Validation performed:** live menu/split captures; native Qt fixtures for
  menu actions, scrollbar keyboard input, selection and splitter interactions.
  User confirmed Meta+E, scrolls, reduced gap and neutral divider. PASS
  architecture/token validation and diff whitespace. NOT RUN all scales, RTL,
  floating docks, every popup/dialog or live Recovery.
- **Recovery:** existing atomic installer and private whole-file backups;
  no session/compositor changes. Qt helper changes require a new process.

## 2026-10-11 — Dolphin breadcrumb and path input alignment

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** align native breadcrumbs and give the editable path the
  Noctalia search-input treatment with padded internal content.
- **Changes:** transparent breadcrumb container, centered28px native segments;
  36px surface path field, accent2px border, radius 8, internal horizontal
  padding and a clear action independent of toolbar sizing/padding.
- **Validation performed:** PASS helper build/atomic application, live Dolphin
  captures including centered native clear button,10 native KIO mode switches,
  architecture verification, token validation and diff whitespace.
  NOT RUN all widths, RTL, scales or live recovery.
- **Recovery:** existing private backups/whole-file rollback; historical
  transport snapshots, compositor and Noctalia remain unchanged.

## 2026-10-11 — Dolphin rounded rows and navigation header

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's request for less pill-shaped file rows
  and better header padding, breadcrumbs and editable location-bar styling.
- **Changes:** radius 6 across row backing/focus/clipping; padded toolbar
  and outlined neutral location bar. Both KIO height limits remain36px
  across mode changes, fixing lower-edge clipping. Canonical adaptations
  and provenance validation updated; Places/tabs/nesting behavior retained.
- **Validation performed:** PASS helper build, live breadcrumb hover/path
  captures, and native KIO fixture (10 mode toggles, URL/editor retained).
  PASS `./scripts/verify architecture`, `python3 themes/tokens/validate.py`
  and `git diff --check`.
  NOT RUN all widths, nested levels, RTL, monitors/scales or live recovery.
- **Recovery:** existing atomic applicator/whole-file backups retained;
  no KWin, shell, default or transport-kit change.

## 2026-10-11 — Dolphin Places match Noctalia search results

- **Model/Agent:** Codex (GPT-6).
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's search-result reference and subsequent
  smaller-icon request, preserving Dolphin navigation and the unified L.
- **Changes:** transparent/borderless normal rows, accent/on-accent selection
  without focus, semibold labels, 16px icons and native6px label gap. The
  native default delegate stays installed/alive; a column paint adapter
  forwards native behavior. Canonical tokens and provenance validation
  reflect this approved adaptation; transport copies/manifests stay intact.
- **Validation performed:** PASS Qt helper build and native KIO fixture
  (default delegate identity, unfocused dark selection,21 navigations); live
  Dolphin normal-row capture and final user visual approval. PASS
  `./scripts/verify architecture`, `python3 themes/tokens/validate.py` and
  `git diff --check`.
  NOT RUN all devices, drag/drop, scales/monitors or session recovery.
- **Recovery:** existing atomic applicator and private file backups retained;
  no shell/KWin/default migration.

## 2026-10-11 — Accepted bounded native Trash and completed milestone 08

- **Model/Agent:** Codex (GPT-6), coordinator.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** record the user's explicit option A approval for ADR-0009 and
  finish the reviewed MVP specification before executable development.
- **Changes:** ADR-0009 is Accepted with approval evidence and strict send-to-trash
  scope; KIO retains the other selected responsibilities. Milestone 08 is COMPLETE,
  with reconciled architecture/UX/filesystem/testing requirements and sequential
  AC09/AC10 gates. Updated maintained references; ADR-0007 remains Proposed.
- **Validation performed:** PASS `./scripts/verify architecture` (zero failures/
  skips) and `git diff --check`; prior milestone 08 review findings remain resolved.
  NOT RUN application build/runtime/operations or live recovery at this checkpoint.
- **Preservation:** no default/FileManager1/Dolphin/Plasma/session change or native
  backend implementation in this checkpoint. Accepted Trash is not a framework,
  purge, overwrite, deletion/restore API or authority to replace other KIO roles.

## 2026-10-11 — Accepted Files architecture and reviewed milestone 08 draft

- **Model/Agent:** Codex (GPT-6), coordinator with separate architecture, UX,
  filesystem and testing review subagents.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** record the user's explicit option A approval for ADR-0008 and
  specify the MVP with conflict, partial-result, cancellation, applicable rollback,
  destructive protection, symlink, mount, permission and KIO-failure contracts.
- **Changes:** marked ADR-0008 Accepted with approval evidence; kept ADR-0007
  Proposed. Added [FILES-MVP](history/ricy-files/FILES-MVP.md), MVP/LATER/OUT OF SCOPE, private module
  boundaries, navigation/selection/UX/token/launch contracts, bounded operation
  semantics and AC09/AC10 acceptance criteria. Updated foundation-era Files
  restrictions only for the approved isolated scope and synchronized maintained
  architecture/component/design/development/recovery/migration references.
- **Safety findings:** KIO 6.30 rename uses check-then-rename; require private
  Linux no-replace policy for rename/same-mount move. Generic recursive KIO
  traversal has no mount-confinement hook; recursive copy/cross-mount move are
  LATER. KIO trash can purge old entries via configured policies. Qt 6.12 trash
  avoids that policy but has a replace-capable orphan-payload commit. Added
  Proposed ADR-0009 for a bounded native standard-trash adapter with exclusive
  metadata/no-replace payload commit, reconciliation and no-purge/no-delete
  fallback. This is extra backend ownership, awaiting explicit approval.
- **Review reconciliation:** PASS scoped written architecture, UX, filesystem and
  testing reviews after clarifying candidate/committed navigation, rename-ID
  remapping, protected operands, unsupported name encoding, byte metadata,
  ambiguous commit cleanup, fixture Home/mount/trash containment, positive volume
  cases, deterministic collision races and mixed skip/cancel result oracles.
  Review PASS is not implementation acceptance.
- **Validation performed:** PASS `./scripts/verify architecture` (zero
  failures/skips), scoped current-document links, `python3 themes/tokens/validate.py`
  and `git diff --check`. PASS before/after SHA-256/mode preservation of the
  1,113-file baseline, except intended documentation/local-rule edits; only two
  new milestone 08 documents were added. ADR-0007 bytes remain unchanged.
- **Limits/checkpoint:** 07 COMPLETE and Accepted; 08 written contract reviewed,
  final exit pending ADR-0009; 09–10 NOT STARTED. Builds/runtime/real KIO primitives,
  trash/volumes/Wayland and login/failure recovery are NOT RUN; new app
  Component/Visual execution is NOT APPLICABLE to this document-only task. Live
  recovery remains UNKNOWN. No application, native backend, package installation,
  service/default/FileManager1/Dolphin/Plasma change or private-state mutation
  occurred. Rollback of this work removes specification/proposal/reference/rule
  edits; preserve recorded ADR-0008 acceptance unless the user revokes it.

## 2026-10-11 — Ricy Files milestone 07 technical proposal

- **Model/Agent:** Codex (GPT-6), coordinator with three independent research/review
  subagents for toolkit/models, filesystem safety and desktop/design integration.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** investigate the requested initial Files roadmap and prepare the
  technical decision required before milestone 08, preserving sequential gates.
- **Changes:** added [FILES-TECHNICAL-ARCHITECTURE](history/ricy-files/FILES-TECHNICAL-ARCHITECTURE.md)
  and Proposed ADR-0008; linked them from the Files reservation, architecture,
  components and ADR index. Compared Qt Quick/C++ with selected KIO/Solid, pure Qt,
  Widgets/KIO and PySide/QML. Recommended a standalone Qt Quick/C++17 application,
  local model/job/token/device/launch adapters, own QML conflict presentation,
  bounded local/trash capability, opaque initial surface and distinct identity.
  No architecture was accepted, contract frozen or application implemented.
- **Findings:** KIOCore/KIOGui reuse does not provide stock conflict dialogs or
  eliminate worker/helper dependencies. Explicit association resolution is needed
  to avoid OpenUrlJob's missing-handler fallback. Cancellation does not imply
  rollback. KIO package closure is broader than selected link targets. Qt/KF6
  are present, but CMake/ECM are absent; package presence is not build readiness.
  ADR-0007, session/default isolation and C-002/C-003 remain pending/unresolved.
- **Validation performed:** PASS independent architectural/toolkit/testing,
  filesystem/safety and desktop/recovery/design proposal reviews; nonblocking
  executable-contract details remain milestone 08 work. PASS
  `./scripts/verify architecture` (zero failures/skips), targeted proposal/ADR/Files
  README relative-link checks, `python3 themes/tokens/validate.py` and
  `git diff --check`. PASS before/after tracked-file SHA-256/mode comparison:
  all 1,111 baseline files retain bytes/modes except the five intended navigation
  and changelog documentation edits; new files are the two proposal documents.
- **Limits and checkpoint:** runtime listing, launch, file operations, media/trash,
  Wayland visuals, login/switching and recovery trials are NOT RUN. New application
  Component/Visual builds are NOT APPLICABLE to this documentation-only stage.
  Recovery runtime functionality remains UNKNOWN; preservation is limited to
  unchanged sources and absence of task-induced runtime/settings mutations.
  No installation, service/default change, token change, private-kit copying or
  publication occurred. ADR-0008 awaits explicit approval; milestones 08–10 are
  NOT STARTED. Rollback removes proposal/navigation/changelog edits only.

## 2026-10-11 — Future Files integration assessment and proposed boundary

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prepare the future Ricy Files integration architecture without
  implementing the application or changing defaults, MIME associations or Dolphin.
- **Changes:** added FILES-INTEGRATION with source/installed-registration evidence
  for directory opens, launcher, FileManager1, MIME/defaults, desktop entries,
  removable/remote devices, trash, package handlers, themes, external actions and
  Plasma Recovery. Added ADR-0007 as Proposed with alternatives, recommended
  session-scoped selection, required Files contracts, Dolphin/KDE-exclusive
  adapters, external package ownership, migration gates and recovery implications.
  Linked the proposal from architecture, components, recovery and the ADR index.
  Accepted ADR-0003 and current ownership/defaults remain unchanged; no session,
  bus topology, toolkit, backend or new daemon implementation is selected.
- **Validation performed:** PASS `./scripts/verify architecture` (56 mandatory
  files, three script syntax checks, 384 local links, zero failures/skips); PASS
  `git diff --check`; PASS content fingerprint equality for 1,073 inspected
  runtime/source files, including installed directory/package associations,
  Dolphin desktop/D-Bus/systemd overrides, wrapper, dolphinrc and Kvantum
  assignment. Read-only MIME queries and source/registration inventory performed;
  primary FileManager1, MIME, Desktop Entry, Trash, portal and KDE service-menu
  documentation reviewed. No private configuration contents exported. Component
  builds/Visual checks are NOT APPLICABLE to this documentation-only change.
- **Limits:** source and registration observations do not prove interactive
  directory/reveal/properties, device/trash/portal behavior or independent
  Recovery. Live trials and default migration are NOT RUN. Approval is pending;
  documentation rollback removes the proposal and its navigation references only.
  Existing uncommitted changes, private backups/state and historical kits remain
  preserved.

## 2026-10-11 — Approved service template extraction (M-02)

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** implement the user's approval of option A for the next small batch,
  making services the owner of three source unit templates.
- **Changes:** moved the three autostart `.service.in` files into `services/`
  with exact bytes/modes. The existing installer resolves this resource directory
  from its own repository location; only its lookup changes. Added ADR-0006,
  source dependency/copy limits, recovery/rollback documentation and mandatory
  template availability checks with three missing-file harness regressions.
  Runtime scripts/profile/state paths and installed legacy IDs remain anchored.
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (38 behavioral checks). `./scripts/verify all`
  returned exit 2 with zero failures: PASS 65 source syntax candidates, seven
  historical guards, offline panel preservation and 28 window-effect scenarios;
  NOT RUN Noctalia source tests because the preserved cache differs from the
  expected patch. PASS exact source template bytes/modes and before/after
  production read/render equality for six units across ordinary and
  special-character paths, unrelated cwd and symlink aliases; only selected AST
  statements executed in disposable fixtures, never the installation body.
  PASS `git diff --check`, installed unit states/MainPIDs/ExecStart equality,
  and static source/asset/transport/archive/installed-unit fingerprint comparison.
  FAIL broad live-state fingerprint equality: private settings/clipboard files
  changed during observation; the cause is UNKNOWN, contents were not exported
  and no restoration was attempted. That live state is outside the narrower
  passing static comparison. FAIL preexisting blur selector state remains.
- **Limits and rollback:** NOT RUN installation, daemon-reload, service restart,
  login/switching, persistent-failure recovery or interactive/visual trials.
  New daemons, Core abstractions and environment changes are NOT APPLICABLE.
  Copying only the active kit/contribution is no longer sufficient for this
  maintained installer: its checkout must include `services/`. Historical
  transport templates, manifests and archive are preserved without fallback
  links or synchronization. Source rollback restores template placement and
  installer lookup together; retain the completed M-01 keyboard migration.
  No installed-state rollback is needed for the source-only extraction.

## 2026-10-11 — Incremental migration preparation and keyboard source move

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** turn the existing grounding/component map into concrete incremental
  batches across the approved subsystems, with one independently safe source move.
- **Changes:** expanded MIGRATION-PLAN with file-level payload/installer ownership,
  script/unit/desktop/symlink edges, pinned builds, rollback state and transport
  limits. Core has no justified extraction candidate. Moved only keyboard-cedilla's
  README and two opt-in applicators into `integrations/keyboard-cedilla/`;
  script bytes/modes remain identical. Updated maintained references, relocation
  map and a scoped historical reinstallation note. Kept explicit syntax coverage
  and added two harness regressions for moved-source selection/failure propagation.
- **Findings:** session/Recovery wrappers contain absolute contribution paths;
  mixed families have sibling imports/build calls and private backup contracts.
  Installed blur ExecStart still uses `iniciar.py`, whereas the current recipe
  copies `start.py`; existing selector failure was preserved. Current Noctalia
  source/deployed provenance mismatch and Dolphin-helper UNKNOWN remain gates.
  Next template extraction has a concrete resource-lookup proposal awaiting
  approval; no common resolver, shim, new daemon or independent session was added.
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (35 behavioral checks in a disposable
  fixture); `./scripts/verify all` returned exit 2 with zero failures: PASS syntax
  (65 candidates), seven historical guard checks, offline panel preservation and
  28 window-effect scenarios; NOT RUN Noctalia source checks because the preserved
  cache does not match the current patch. PASS moved README/reinstallation-note
  relative links and `git diff --check`. PASS before/after fingerprint comparison:
  1,573 source/asset/private-kit/transport/archive/installed-entry-point/input
  files and symlinks retain bytes/targets/modes, accounting for relocated scripts;
  only the relocated README differs within that 1,574-item baseline. PASS installed
  unit states, MainPIDs and ExecStart equality. FAIL preexisting registered blur
  selector state remains unchanged; no repair was attempted.
- **Limits and rollback:** NOT RUN live typing/browser rendering, switching,
  persistent failure, login/unlock, Dolphin interaction or visual trials. Runtime
  Integration/Environment changes are NOT APPLICABLE to this source-only move.
  Both transport manifests, archive, private profile/state/backups and installed
  preferences remain intact. Revert source placement/references/harness changes
  together; no session or settings rollback is necessary. External ad hoc callers
  outside the examined entry-point scope remain UNKNOWN. Remaining coupled
  extractions, public packaging and architectural decisions are proposals only.

## 2026-10-11 — Consumable Ricy visual tokens

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** prepare existing Ricy identity for future owned applications,
  especially Files, without redesign, live appearance changes or bulk migration.
- **Changes:** promoted existing visual values into `themes/tokens/tokens.json`
  with schema1/contract1.0.0, explicit units and scoped adaptations. Shared
  Dolphin colors reference canonical roles; derived shell radii are calculated.
  Added source/hardcode audit, consumption contract, offline renderer/validator
  and ADR-0005. The existing SVG board is the sole migrated consumer; generated
  output is byte-for-byte identical. Updated design, component, architecture,
  migration and Files documentation without choosing a toolkit or implementing
  an application.
- **Findings:** native Style provides the spacing/type/radius/motion cadence;
  existing runtime sources retain hardcodes. Shell fill .70, Dolphin alpha 178/255
  and Konsole .85 remain distinct. Native KWin blur is attributed to grounding
  G-03; old ricyblur records are historical and new-app blur support remains
  UNKNOWN. Root/contribution search-support radii differ and were preserved.
- **Validation performed:** PASS `python3 themes/tokens/validate.py` (contract,
  references/units, retained-snapshot SHA-256, value/adaptation equality,
  source-backed additions, SVG XML and accent propagation); PASS
  `python3 themes/tokens/render-reference.py --check` (exact retained SVG bytes);
  PASS `./scripts/verify architecture`, token-script syntax, targeted documentation
  links and `git diff --check`. NOT RUN live visuals, monitors/scaling, motion,
  session switching, login/unlock or recovery trials. Runtime Integration,
  Recovery and Environment checks are NOT APPLICABLE to this offline-only change.
- **Preservation/rollback:** original token JSON and SVG bytes, transport kit,
  historical manifests, private profiles/state/backups and live consumers remain
  intact. No applicator, installation or service/compositor activation occurred.
  Revert this task's source/template/tooling/documentation edits to roll back;
  recovery has no new token-loader dependency.

## 2026-10-11 — First safe cleanup of historical development paths

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** use the approved grounding to prevent historical variants from
  being mistaken for the current build, while preserving the active desktop and
  Plasma/Dolphin Recovery. No item meets REMOVE; no file was deleted or moved.
- **Changes:** gated seven historical Noctalia builders behind explicit opt-in
  and an absolute isolated source, rejecting repository/cache paths and symlink
  aliases before probing/downloading/building. Normal source selection omits only
  explicit HISTORICAL recipes; mixed-role activation/restore helpers and UNKNOWN
  material stay selected. Guard syntax remains checked. README/agent entry points
  distinguish current source, deployed binary, selected effect and historical
  transport recipes. Added fixture regressions for isolation/source selection;
  fixed fixture link validation with an empty archive placeholder, without
  copying the private ZIP. See the
  [dependency review](CONTRIBUTION-AUDIT.md#first-safe-cleanup) and
  [reproduction workflow](DEVELOPMENT.md#historical-reproduction).
- **Validation performed:** PASS `./scripts/verify architecture`; PASS
  `python3 scripts/test-foundation.py` (33 behavioral checks). `./scripts/verify all`
  returned exit 2: PASS maintained-source syntax (65 candidates), all seven guard
  syntax checks, offline panel capture/merge preservation and 28 window-effect
  scenarios; NOT RUN Noctalia source tests because the preserved cache differs
  from the current patch. PASS `git diff --check` and before/after SHA-256/symlink
  comparison: none of the 1,606 baseline files disappeared; only the intended
  development scripts/docs changed. Installed units/wrappers, binary/cache,
  snapshots, both manifests, patches, assets, archive and private kit material
  retain their bytes. User-unit states, PIDs and ExecStart values remain identical.
  Doctor returned exit 2 with its two expected UNKNOWN categories. FAIL preexisting
  blur-selector service state remains unchanged; no repair was attempted.
- **Limits:** NOT RUN live switching, persistent-failure recovery, login/unlock,
  interactive Dolphin and visual trials; no session/service was restarted.
  Builds/downloads and historical activation were NOT RUN; guard tests used a
  sentinel build body in a disposable fixture. New architecture, migration and
  visual design are NOT APPLICABLE. Unchanged bytes/state and offline tests do
  not certify interactive recovery. No extra historical copy or regenerated
  SHA256SUMS was created; Git retains the pre-cleanup recipes at `1fb1918`.

## 2026-10-11 — Current contribution grounding

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** distinguish actual consumers, recovery dependencies, migration
  inputs and historical variants across all existing Ricy contributions without
  moving/removing files or changing runtime behavior.
- **Changes:** added [CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md) with individual
  classifications for all 24 contribution directories, corresponding transport
  snapshots, three materialized community plugins and shared/generated material.
  Records consumers, dependencies, relationships, cumulative lineage, recovery
  impact, previously mapped future destinations and explicit UNKNOWNs. COMPONENTS
  now carries class labels; architecture, recovery, migration, design and agent
  entry points link to the maintained evidence. No REMOVE verdict was justified.
- **Findings:** running Noctalia matches the earlier reordering variant preserved
  in the transport diff, not the current single-space source patch; native blur
  is loaded and the registered ricyblur selector is failed. Window-fade-expand
  matches the installed effect. Source/installed translations, version-specific
  destination corrections, disabled adaptivepanelwidth, and unproven community
  plugin functionality are recorded without replaying installers or repairs.
- **Validation performed:** PASS `./scripts/verify architecture`, inventory
  coverage, `git diff --check`, and SHA-256 preservation comparison. PASS shell
  syntax subcheck (83 candidates); `./scripts/verify shell` returned exit 2 with
  source-based Noctalia tests NOT RUN because the cache differs from the current
  patch. PASS `./scripts/verify recovery` (exit 0), including panel preservation
  and 28 isolated window-effect scenarios. `./scripts/doctor` returned exit 2
  with two UNKNOWN diagnostic categories. FAIL preexisting blur-selector state
  was observed separately through systemd/KWin/current-boot journal reads.
  NOT RUN live login, unlock, switching/failure recovery, interactive Dolphin,
  plugin use, package installation, input/connectivity and visual validation.
  New implementation/validator regressions and ADRs are NOT APPLICABLE.
- **Preservation:** only Markdown documentation and agent routing changed; one
  documentation file added. No implementation, token, manifest, installed unit,
  profile, private state, backup, asset or historical record was rewritten. No
  existing file was moved or removed; no service/compositor was restarted.

## 2026-10-11 — RICY-001 workspace exposure audit

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** remove safe Ricy-owned workspace exposure while preserving KWin
  infrastructure and Plasma/Dolphin Recovery. The
  [pre-change inventory](WORKSPACE-AUDIT.md) classifies product UI, internal APIs,
  shared recovery surfaces and uncertain external/runtime behavior.
- **Changes:** updated the current cumulative Noctalia 5.2.1 patch to block the
  workspace widget and aliases, force a flat taskbar, remove explicit desktop
  activation fallback, workspace commands/scroll bindings, workspace settings and
  desktop-triggered bar reveal. Legacy keys still parse; taskbar/window-switcher
  visible-desktop membership remains internal. The compiled CLI rejects legacy
  workspace verbs locally, including when an earlier shell is running. Public
  templates disable grouping/labels; current identity references exclude these
  surfaces without changing numeric design values. Historical patches, transport
  kit, manifests, private profile/state and installed recovery settings are preserved.
- **Harness:** added isolated source selection through `RICY_NOCTALIA_SOURCE` and
  extended the native drag validator with single-space policy regressions.
  Foundation fixtures retain linked patch files and isolate source-override tests.
- **Validation performed:** PASS isolated Meson/Ninja release build; PASS
  `RICY_NOCTALIA_SOURCE=<isolated-source> ./scripts/verify all` (zero failures and
  zero unavailable offline checks), including native widget/alias/picker/settings,
  legacy-profile/drag, CLI rejection, 17 window-action scenarios, panel preservation
  and 28 window-effect scenarios. PASS `python3 scripts/test-foundation.py`
  (17 scenarios), order (22), motion (20), indicator/effect (15), and compiled
  validation of both public TOML templates. PASS clean pinned patch replay: all
  26 cumulative source files match the validated checkout; ten differ from the
  previous cumulative variant. PASS exact patch/source diff comparison and original
  cache preservation. PASS source `git diff --check` and repository
  `git -c core.whitespace=-blank-at-eol diff --check` (unified-diff blank context
  markers are intentional patch syntax).
- **Limits:** NOT RUN live visual, gestures, session switching, persistent failure,
  login and Dolphin recovery trials. The new binary was compiled separately and
  was not activated. Shared KWin shortcuts, native desktop menus/settings and
  possible gestures remain preserved; complete live RICY-001 compliance is UNKNOWN.
  NOT APPLICABLE compositor ABI/replacement and new architecture: neither changed.

## 2026-10-11 — Refresh menu launcher after file rename

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** repair menu activation after the English file rename.
- **Evidence:** the installed desktop entry already referenced `open-menu.sh`,
  but KWin's embedded KGlobalAccel retained the previous service object and
  attempted the removed filename. Application database rebuilding and action-only
  re-registration were insufficient.
- **Changes:** recreated only the menu launcher component, restoring its active
  and default shortcuts from a private snapshot; documented the required refresh
  in [FILE-RENAMES](FILE-RENAMES.md). No compositor, shell, or session restart.
- **Validation performed:** PASS desktop-entry validation, executable target,
  active/default shortcut comparison, registered `_launch` invocation, and
  Noctalia's live `activePanelId=launcher` response. No new missing-program error
  appeared in the journal after the successful invocation. PASS architecture
  verification and `git diff --check`.
- **Limits:** NOT RUN full login/crash recovery; live validation covers menu activation.

## 2026-10-11 — English file names

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** extend the en-US policy to existing project file names at the
  user's explicit request, superseding the previous path-preservation exception.
- **Changes:** renamed 227 files across the repository root and both kits using
  74 English basename mappings. Updated callers, imports, installers, launcher
  references, palette names, patches, validators, and documentation. Added
  [FILE-RENAMES](FILE-RENAMES.md) with the complete mapping and compatibility limits.
  Existing directory names were already in English. Historical SHA256SUMS and
  private backup/state paths remain unchanged; operational manifest paths and
  replacement digests use current sources. Existing systemd IDs remain compatible
  through an explicit mapping to English template names.
- **Recovery implications:** five installed unit/launcher files referenced old
  repository paths. Their references were corrected after creating private backups
  outside the repository; systemd configuration was reloaded without stopping or
  restarting services. No session switch or installation was performed.
- **Validation performed:** PASS `./scripts/verify all` and
  `python3 scripts/test-foundation.py` (17 scenarios); PASS `git diff --check`.
  PASS all 227 rename destinations, old-path absence, and executable permissions;
  PASS parsing 123 Python files, Bash syntax for 69 scripts, and 36 JSON files in
  the public source selection. PASS installed systemd unit verification and
  absence of obsolete filename references in current sources (historical manifests
  and the rename map are intentional exceptions).
- **Limits:** NOT RUN live session/login/crash recovery. Other installed copies
  require their own reference updates or deliberate reinstallation.

## 2026-10-11 — en-US project language

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** use US English for project content and public-facing interfaces,
  while allowing pt-BR in chats according to the user's preference.
- **Changes:** translated project documentation, ADRs, local agent rules/skills,
  comments, script diagnostics, interface labels, metadata, and visual-reference
  text in the active and transport kit trees. Added `[Always use en-US as the language.]`
  to AGENTS, README, and DEVELOPMENT, with routing through the ricy/documentation skills.
  Existing paths, identifiers, private state, licenses, upstream localization catalogs,
  and historical SHA256SUMS remain preserved. The restore confirmation now displays
  and accepts `y/N`. Operational correction-manifest hashes were updated for translated
  sources; the active kit's preexisting modified target remains protected from replacement.
- **Validation performed:** PASS `./scripts/verify architecture` and
  `./scripts/verify all` (required files/links, syntax, 17 Noctalia scenarios,
  panel capture/merge, and 28 isolated KWin scenarios); PASS
  `python3 scripts/test-foundation.py` (17 scenarios); PASS `git diff --check`.
  Both kits' changed sources passed checks: 121 Python files, 43 Bash files,
  16 JSON files, and 2 SVG/XML files. Python AST comparison confirmed no
  changes beyond string constants/comments. PASS transport correction patch
  applicability and replacement-file hash checks. The active correction target's
  preexisting hash mismatch remains rejected. Installer labels/layout were
  inspected in an offscreen Qt window without selecting a package; the translated
  SVG reference was rendered and visually inspected.
- **Recovery implications:** shell/session selection, backups, and recovery paths
  remain in place. No installation, service restart, or session switching was performed.
- **Limits:** NOT RUN live session/login/crash recovery or full desktop visual review.
  The installer UI was inspected offscreen without selecting or installing a package.
  No publication or migration was performed.

## 2026-10-11 — Local Git baseline

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** establish an auditable Git baseline on `main`, with explicit source
  and asset selection, without a remote, publication, reorganization, or runtime change.
- **Changes:** conservative `.gitignore`, record in [GIT-BASELINE](GIT-BASELINE.md),
  and Git state update in DEVELOPMENT. Selected 1,098 files; excluded 1,939 local files
  from the index while preserving them on disk. Backups, clipboard, notification
  history, profile/work, bytecode, and ZIP containing private state are outside the
  baseline. Templates, patches, evidence, and assets remain.
- **Validation performed:** PASS `./scripts/verify architecture` (52 required files
  and local links); PASS `./scripts/verify all` (83 syntax candidates, 17 Noctalia
  scenarios, panel capture/merge, and 28 KWin scenarios); PASS
  `python3 scripts/test-foundation.py` (17 scenarios). All exited 0. Heuristic search
  of 1,098 staged files, including 244 decompressed SVGZ files, found no evident
  credentials. No gitlinks in the index; executable permissions preserved.
- **Preservation:** initial SHA-256 inventory; no preexisting file removed or with
  changed permissions. Only DEVELOPMENT and this CHANGELOG were edited by the task.
  Private notification history changed during the session through external activity;
  it was not written, reverted, or versioned by the task.
- **Limits:** NOT RUN live session/recovery; NOT APPLICABLE visual validation and
  installation because behavior did not change. Licenses, personal/machine references,
  and portability still require review before publication; the local baseline does
  not certify that all content is safe to publish.

## 2026-10-11 — Agent-first foundation

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** formalize the requested architecture around existing kits, with
  invariants/ADRs, a map of 24 contributions, progressive rules/skills, diagnostics,
  and offline checks, without migrating runtime or changing the session.
- **Changes:** AGENTS/CLAUDE, architectural docs, documentary reservations, seven
  skills, local rules, scripts/verify, and scripts/doctor. README gains an architectural
  entry point; preexisting text is preserved. No legacy file removed.
- **Validation performed:** `./scripts/verify architecture` and `./scripts/verify all`
  passed (exit 0): structure/links, syntax of 83 kit files, 17 Noctalia scenarios,
  panel capture/merge regressions, and 28 isolated KWin scenarios.
  `python3 scripts/test-foundation.py`: 17 behavioral checks passed.
  The seven skills passed `skill-creator/scripts/quick_validate.py` using a temporary
  virtual environment with PyYAML 6.0.3, without a new runtime dependency.
  `./scripts/doctor`: expected exit 2, two UNKNOWN items (live recovery and complete
  RICY-001 compliance); package/unit queries completed. The first quick_validate
  did not run in system Python because PyYAML was missing; it was repeated successfully
  in the isolated environment.
- **Limits:** login, switching, and crash recovery were not tested in this documentary
  change. C-001 through C-005 are recorded discrepancies, not runtime fixes.
- **Preservation check:** 51 new files; README was the only preexisting file edited by
  the task, retaining its entire previous text. SHA-256 comparison of 2,978 initial
  files also found a change in the active profile's `notification_history.json`
  during the session. The task did not write or revert that state. The other 2,976
  files retained their hashes; no preexisting file was removed or had permissions changed.

## 2026-10-11 — Context by consequence

- **Model/Agent:** Codex (GPT-6), agent for this task.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** reduce universal reading without changing architectural authority or
  approval. CLAUDE imports AGENTS; root/DEVELOPMENT/index and local routers load
  sources by impact. The component-development, testing, documentation,
  noctalia-development, and visual-development skills have more specific triggers;
  KWin retains invariants/recovery and consults the map by domain. DESIGN-SYSTEM
  only conditions invocation of the visual skill; visual values and guarantees remain.
- **Context before → after:** a local visual change previously chained architecture,
  invariants, the map, and general skills; it now uses the AGENTS hierarchy,
  DESIGN-SYSTEM, and local code/docs/tests. New architecture still requires
  ARCHITECTURE, INVARIANTS, relevant ADRs, a boundary map, and explicit approval.
- **Validation performed:** `./scripts/verify architecture` and `./scripts/verify all`
  passed (exit 0); `python3 scripts/test-foundation.py` passed all 17 scenarios;
  the seven skills passed quick_validate.py in the existing virtual environment.
  The `@AGENTS.md` import was checked statically; loading through Claude Code was
  not executed. Live session/recovery tests remain NOT RUN.
- **Runtime Changes:** None. Invariants, ADRs, architecture/recovery sources,
  validators, and implementation preserved; no new or removed file.
