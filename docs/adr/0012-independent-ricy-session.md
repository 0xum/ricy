# ADR-0012 — Independent Ricy session

Status: **Accepted; runtime implementation pending** — user decision
on 2026-10-14 (America/Sao_Paulo).

Authorization: the user explicitly removed KDE's role as a backup and defined
Ricy as its own session. This supersedes [ADR-0002](0002-plasma-recovery.md) and
amends the Plasma Recovery clauses of [ADR-0011](0011-dolphin-as-ricy-file-manager.md).
Dolphin remains the chosen file manager; its upstream responsibilities do not change.
The user subsequently approved the proposed architecture, including option B:
the same account and personal files, isolated session configuration, explicit
sharing of application preferences, and sequential graphical logins. The request
to publish this documentation does not install or activate the session.

## Context and evidence

**KNOWN:** the current [switching integration](../../ricy-kit/contributions/plasma-noctalia-switching/integration.py)
changes panels and shortcuts inside Plasma. It explicitly shares visual settings,
uses plasmashell D-Bus, and addresses panel files through `$HOME/.config`.
The [Noctalia unit](../../services/noctalia-test.service.in) follows plasmashell;
the [login integration](../../services/ricy-noctalia-integration.service.in)
is enabled on `plasma-workspace.target`. The existing style applicator writes
shared KDE/Kvantum settings. Noctalia's profile is isolated, but the desktop is not.

Read-only installation observations on 2026-10-14: only `plasma.desktop` exists
in `/usr/share/wayland-sessions`; the active desktop reports KDE/Wayland;
Noctalia and its login integration are inactive, and login integration is disabled.
KDE has light window colors, Papirus icons and a light Aurorae decoration, while
Kvantum selects KDE-Noctalia. These are observed preferences, not a new baseline
to distribute or an attribution of which program last wrote them.
The display-manager service resolves to `plasmalogin.service`; historical SDDM
recipes do not describe this installation's current login manager.

The private Noctalia profile currently disables wallpaper, lockscreen, OSD and
its polkit agent. Its built-in/community app-theme templates are disabled.
Shared Dolphin desktop and FileManager1/systemd overrides use the Ricy wrapper.
The exact startup and security behavior without Plasma services is **UNKNOWN**.

## Decision

- Ricy is a dedicated login session built on KWin/Wayland and Noctalia. It must
  not require starting the Plasma desktop and then hiding its panels.
- KDE Plasma is an independent desktop when installed. It is not Ricy's backup
  or a required failure destination. Removing its installed packages is outside
  this decision.
- Session-owned themes, shell settings, effects, shortcuts and startup policy
  must be scoped to their respective environments. Selecting Ricy must not
  overwrite Plasma's chosen appearance, and vice versa.
- Shared upstream KDE infrastructure and applications are permitted. KWin,
  Dolphin, Qt/KF and selected KDE services are dependencies, not evidence that
  Ricy is running inside the Plasma desktop session.
- Ricy owns its session lifecycle and failure policy. Diagnosis, file access
  and rollback must remain possible without an automatic switch to Plasma.
- Preserve the single-space experience, existing design authority and Dolphin
  choice. Reliable file access when optional visual customization fails remains
  required within Ricy.

The accepted architecture is **PLANNED**, not implemented. Current shell-switching
commands and snapshots remain transitional runtime assets until replacements
are validated; removing the backup concept does not authorize deleting them.

## Approved implementation contract

**Problem:** provide the independent session and theme isolation without
resetting the user's application profiles or depending on plasmashell.

**Options evaluated before approval:**

| Option | Benefit | Cost / limitation |
|---|---|---|
| A. Separate login entries with shared configuration | Small initial change | Does not solve theme/settings interference; insufficient for this decision |
| B. Same account, isolated session configuration, explicit shared application settings | Separate desktop preferences with access to the same personal files/apps | Requires an audited sharing allowlist and correct environment propagation to launched and D-Bus/systemd-activated processes |
| C. Separate user accounts | Stronger separation of settings and user services | Separate credentials, permissions and application profiles; exceeds the requested environment separation |

**Selected and approved:** B, with sequential graphical logins. Retain the current Plasma
configuration as its baseline, create a private Ricy configuration namespace,
and share personal files/application settings only through an explicit inventory.
Exact paths and the application-sharing inventory must be established during
implementation within this approved boundary; none are deployed by this ADR.
Do not use a blanket copy/symlink of `.config` or an automatic theme snapshot swap.

The [XDG Base Directory specification](https://specifications.freedesktop.org/basedir/0.8/)
defines configuration search and write locations; changing `XDG_CONFIG_HOME`
also affects compliant applications, not only the desktop. It does not isolate
programs that hardcode `$HOME/.config`, global settings stores, or existing
activated processes. Session-specific application desktop entries and FileManager1
activation must also be reviewed; a configuration directory alone is insufficient.
The [systemd desktop integration guidance](https://github.com/systemd/systemd/blob/main/docs/DESKTOP_ENVIRONMENTS.md)
requires considering user-service lifecycle and environment. Concurrent graphical
sessions for the same account are outside the initial proposal. Keep the standard
user runtime directory; do not claim per-session D-Bus/user-manager isolation.

**Impact and ownership:**

| Area | Required implementation work / owner |
|---|---|
| Login and lifecycle | Ricy-owned entry point and scoped units under installer/services; use the installed login manager and KWin, without replacing the manager or introducing a daemon by assumption |
| Wallpaper and shell | Noctalia-owned wallpaper/background where supported by the pinned implementation; remove the plasmashell dependency only after validation |
| Security and desktop services | Explicit owners for locking/unlocking, polkit, portals/screensharing, power/suspend, notifications and session exit; reuse compatible upstream services where verified |
| KDE integration | Audit KGlobalAccel, search, launch environment, autostarts and D-Bus activation; do not assume Plasma targets are suitable session targets |
| Themes and applications | Scoped KDE/Qt/GTK/Kvantum settings and effects; retain Ricy tokens and user keyboard/region settings; review shared data paths, desktop overrides and Dolphin FileManager1 routing |
| Failure handling | Ricy shell restart/exit policy, terminal/file access and installer rollback; no automatic Plasma launch |
| Compatibility | Retain current wrappers, unit IDs, private profile/state, snapshots and restore tools during migration; retire only after a separately validated replacement |

No lock, authentication, portal, power or wallpaper implementation is selected
merely by listing its owner. Compatibility with installed KWin/Noctalia and
the actual login manager must be demonstrated before activation.

## Incremental validation and constraints

1. Implement within the approved contract, inventory shared settings and identify
   startup/security dependencies in the pinned sources and installed units.
2. Implement an isolated configuration/bootstrap fixture and test propagation,
   shortcut/activation routing, startup failure and deterministic rollback.
3. Prepare the login entry and scoped units with private backups; validate syntax
   and service dependencies before enabling them. Do not alter the active session
   merely to validate this document.
4. Validate a real Ricy login: wallpaper, Noctalia, Dolphin, terminal, lock/unlock,
   polkit, portals, suspend/resume, logout and shell/compositor failure paths.
5. Validate Ricy → logout → Plasma → logout → Ricy: each keeps its own appearance,
   settings and launch policy; no leftover adapter/shortcut owners. Exercise a
   persistent user manager and failed Ricy startup as well as the normal path.
6. Retire shared shell-switching startup only after the session paths pass. Keep
   private history/backups and update compatibility documentation rather than
   deleting historical manifests or transplanting the active profile.

Current validation scope is architectural documentation and read-only environment
inspection. All independent-session runtime, visual and failure trials are
**NOT RUN**. Existing offline panel tests do not validate the new session.
