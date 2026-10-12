# Current Noctalia configuration snapshot

Captured on 2026-10-12 at the user’s explicit request for a local repository
backup. Ownership remains with the existing Noctalia/KDE integration contribution;
this is captured preference data, not a canonical design-token update or runtime
migration. The original private profile and recovery backups remain in place.

## Contents and evidence

- `config/noctalia/`: exact active base configuration and custom palette.
- `state/noctalia/settings.toml`: exact saved UI overrides, including enabled
  plugins, widgets, monitor placements, regional preferences and theme templates.
  Noctalia combines these overrides with the base configuration; copying only
  config.toml would lose current settings.
- `state/noctalia/plugins/materialized/`: all four installed plugin payloads,
  including upstream manifests, translations, scripts, thumbnails and available
  license files. IDs and upstream filenames are preserved for compatibility.
- `state/noctalia/community-templates/vscode/`: selected community template.
- `assets/limine-splash.png`: wallpaper referenced by the captured settings.
- `manifest.json`: plugin versions, API declarations, licenses, dependency
  resolution, active executable checksum, source scope and payload checksums.
- `packages.txt`: installed versions of resolved dependencies and their local
  pacman dependency closure, including Noctalia, KWin/Plasma and the configured
  font. This inventory contains package names/versions, not bundled binaries.

KNOWN: payload bytes were copied from the active kit profile. The installed
package reports Noctalia 5.2.1; the running Ricy executable is a separately patched
binary. Use the maintained [cumulative source](../../../app-icon-reordering/README.md)
and its isolated build instructions; the package alone does not reproduce Ricy.
Plugin dependency entries come from installed manifests and local pacman/command
queries. UNKNOWN entries are unresolved locally, not proof that the plugin is
broken; alternatives and optional features can make dependencies conditional.
Package presence and plugin API declarations do not prove runtime compatibility.
Existing upstream license declarations are retained; missing standalone license
texts are not replaced with invented licenses. Redistribution review is NOT RUN.

## Restoration scope

This is an opt-in backup, never an automatic installer. With the shell stopped
through the existing recovery workflow, first back up the destination profile.
Copy `config/noctalia/` to `$NOCTALIA_CONFIG_HOME/noctalia/`, and copy the included
`state/noctalia/` files to `$NOCTALIA_STATE_HOME/noctalia/`. These variables point to
separate config and state roots in the current user service. Preserve other state
files; do not replace the whole private state directory. Use the existing
[recovery guidance](../../../../../docs/RECOVERY.md) for session switching.

The absolute wallpaper path must exist at `/usr/local/share/ricy/limine-splash.png`
or be adjusted in the destination settings. Monitor names/geometry, application
order, palette ID and local region are personal captured values, not portable
defaults. Templates may write settings for other applications when enabled;
review their destinations before activation. Install needed packages separately,
reviewing plugin READMEs for optional dependencies; do not blindly install every
entry in packages.txt or activate the shipped polkit rule.

Clipboard, notifications, activity history, plugin runtime data, credentials and
account sessions were excluded. Existing private backups are untouched. No shell,
service, plugin, package, wallpaper or recovery setting was activated or changed.
Runtime restoration and real-session recovery validation: NOT RUN.
