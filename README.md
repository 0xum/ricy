# Ricy

An opinionated desktop for CachyOS, built on KWin/Wayland, with Noctalia as the
primary shell and Dolphin as the file manager, targeting its own login session.
KDE Plasma is a separate desktop, not Ricy's backup.

**Current state:** Noctalia is integrated into the Plasma session, which still
provides the wallpaper/desktop. The separate Ricy Files prototype is retired.
The independent session is accepted but not implemented; see
[ADR-0012](docs/adr/0012-independent-ricy-session.md). The user assesses Dolphin
visual work as about 90% complete;
see the [read-only baseline](docs/DOLPHIN-BASELINE.md), not a certification of
all functions or recovery.

**Architecture:** KWin remains infrastructure; Ricy uses a single workspace.
Ricy owns its session settings and failure handling. Existing Plasma switching,
installed packages and backups remain intact during migration. Legacy
discrepancies and recovery limits are documented.

**Development:** agent-first, with evidence and incremental changes.
Start with [AGENTS.md](AGENTS.md); [CLAUDE.md](CLAUDE.md) reuses the same rules.

**Project language:** [Always use en-US as the language.] Project files,
documentation, and public-facing interfaces use US English. Chats may use pt-BR.
See the complete [language policy](AGENTS.md#project-language).

- [Architecture](docs/ARCHITECTURE.md), [invariants](docs/INVARIANTS.md), and [ADRs](docs/adr/README.md).
- [Components](docs/COMPONENTS.md), [contribution grounding](docs/CONTRIBUTION-AUDIT.md), and [design system](docs/DESIGN-SYSTEM.md).
- [Development and validation](docs/DEVELOPMENT.md), [recovery](docs/RECOVERY.md), and [migration](docs/MIGRATION-PLAN.md).

`./scripts/verify all` runs offline checks; `./scripts/doctor` diagnoses without
changing settings. This does not certify that the entire session works.

## Existing organization and records

Project organized on October 11, 2026.

- `start.sh`: selects Noctalia for the session and subsequent logins.
- `return.sh`: returns to Plasma.
- `switch.sh`: switches between Plasma and Noctalia.
- `ricy-kit/`: this machine's active kit, with local profile, state, and backups.
- `docs/`: records, visual identity, reinstallation instructions, and preserved transport kit.
- `archives/ricy.zip`: preserved original transport archive.

The `ricy`, `voltar-ao-noctalia`, and `voltar-ao-plasma` commands remain available in
`~/.local/bin`. Shortcuts and services were updated to this project's paths.
Before preparing another computer, reconcile historical documentation and transport
recipes against the [grounding](docs/CONTRIBUTION-AUDIT.md). The transport tree is
historical evidence, outside the normal build/development path; publication and
portability remain unproven. The active kit contains private state and backups.

The historical record preserves paths used in previous sessions.
The organization record and copies of modified files are in
`~/.local/state/profile-organization/2026-10-11/`.

Shortcut repair on October 11, 2026: menu and clipboard entries were reloaded
in the KDE session cache (locale en_US.UTF-8), preserving Super and Super+Space.
The Noctalia service uses `KillMode=process` to preserve applications it launched
when the shell stops. This protection is also in both kits' templates.
Noctalia and the search adapter remained running during this repair.
Record: `~/.local/state/profile-organization/2026-10-11/shortcut-repair/`.
