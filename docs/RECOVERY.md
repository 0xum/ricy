# Recovery

## Contract and state
Ricy Session (TARGET / PLANNED): **dedicated KWin/Wayland + Noctalia + Dolphin**.
KDE Plasma, when installed, is an **independent desktop, not Ricy's backup**.
[ADR-0012](adr/0012-independent-ricy-session.md) supersedes
[ADR-0002](adr/0002-plasma-recovery.md). Ricy must own its failure handling,
diagnosis and rollback without requiring an automatic Plasma launch.
The architecture and configuration-isolation model are approved; lifecycle/security mechanisms are not yet
implemented. Native file access must remain usable if optional visual helpers fail.

CURRENT / KNOWN: switching occurs within Plasma Wayland. Plasmashell remains
responsible for wallpaper/desktop; return uses Ricy scripts, user systemd,
D-Bus, KGlobalAccel, and panel/shortcut snapshots. No isolation against KWin,
login, or Ricy-script failure has been demonstrated.

All Plasma Recovery references below describe current transitional behavior or
dated evidence, not the new product requirement. Preserve the existing scripts,
snapshots, packages and login access during migration. A safe rollback of the
current installation is distinct from requiring KDE as Ricy's backup desktop.

[ADR-0011](adr/0011-dolphin-as-ricy-file-manager.md), amended by ADR-0012,
selects Dolphin in Ricy. Access to files must not require an own Ricy application,
filesystem/Trash implementation or FileManager1 service. Ricy visual adaptations
are permitted, but native file access must remain usable if those adaptations fail.

The [baseline](DOLPHIN-BASELINE.md) confirms that the existing user desktop
override, FileManager1 service and systemd drop-in still use the visual wrapper
and are shared by the current shell modes. That coupling is preserved in this
documentation/retirement task. Cold activation, unavailable helper/theme and
login/failure recovery are NOT RUN; independent Recovery remains UNKNOWN.
ADRs0007/0008/0009 and the own prototype are historical, not current contracts.

KNOWN update 2026-10-13: the user selected native Dolphin/Breeze for Plasma's
Meta+E and Ricy Dolphin for the application launcher; Noctalia uses Ricy for
both. The existing switching code transfers/restores this shortcut and extends
older snapshots without replacing saved shell keys. The native launcher alias
executes the installed Dolphin directly with Breeze, independent of the visual
helper. PASS actual native launch, Noctalia Ricy launch and shortcut-only
restore/transfer; the user reported the requested behavior passed after reboot
on 2026-10-13. Full shell-switch and failure recovery after this update remain
NOT RUN. Shared menu/default/FileManager1 coupling remains;
this narrow shortcut exception does not prove complete Recovery isolation.

The [contribution grounding](CONTRIBUTION-AUDIT.md) identifies RECOVERY consumers
and part-level exceptions. On the audited installation, native blur is loaded,
the ricyblur selector is enabled but failed. Its original earlier-binary
observation was superseded by the isolated cumulative RICY-001/UUID activation
recorded in [CHANGELOG](CHANGELOG.md); the previous source/cache/binary backup
remains available. These observations do not prove
failure recovery or authorize resetting services/effects. Historical root and
transport return recipes can restore old full layouts; normal return remains
the panel-only switching contribution. Do not substitute one for the other.

## Existing return path — accessible session
In a terminal within the session, as the desktop user, from the project root:

```bash
./return.sh
# Alternative installed by the kit:
ricy plasma
```

Run one alternative, not both routinely. These commands **change** the session:
they disable Noctalia login integration, stop shell/adapter, and restore panels,
shortcuts, and KRunner. Plasmashell may restart briefly. Preserving KWin and apps
is the code's intent; the foundation task does not test switching.
The [command](../ricy-kit/contributions/plasma-noctalia-switching/ricy) and
[implementation](../ricy-kit/contributions/plasma-noctalia-switching/integration.py)
are the evidence. Current root wrappers use this installation's absolute path.

Read-only diagnostics:
```bash
./scripts/doctor
systemctl --user is-active plasma-plasmashell.service
journalctl --user -u ricy-noctalia-integracao.service
```

An active service does not guarantee visible panels, login, or working Dolphin.
`ricy status` returns Plasma when the Noctalia unit is inactive, including after
failures: do not use that result alone as proof of recovery.

## Failures and critical dependencies
| Failure point | Known behavior / limit |
|---|---|
| Invalid Noctalia config | Integration validates before hiding panels; failures at this stage do not prove recovery of the entire session. |
| Shell/adapter fails during switching | The protected block in `start()` calls `restore()`; the command disables the preference if restart fails. Not every exception is inside that block. |
| Shell crashes after switching | Units have a restart policy; UNKNOWN: guaranteed fallback after persistent failure. |
| Missing/corrupted snapshot or unavailable D-Bus | Return may fail; preserve backups and investigate the error instead of overwriting the layout based on assumptions. |
| KWin/login/user-session failure | UNKNOWN: independent Ricy failure handling has not been validated. ADR-0012 does not require a Plasma fallback session. |
| Customized Dolphin / incompatible plugin | Launcher, QSS, Qt plugin, and KWin effect exist; consult contribution restorers instead of removing Dolphin. |

Current snapshots are in `${XDG_STATE_HOME:-$HOME/.local/state}/ricy-alternancia/`.
The installer documents backups and restoration in
[plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md).
The historical `plasma-antes.tar.gz` seed must not be replaced. Do not restore
old complete archives for switching: they could overwrite wallpaper/widgets.
For Dolphin, consult [identity](../ricy-kit/contributions/dolphin-noctalia-identity/README.md)
and [plugins](../ricy-kit/contributions/dolphin-blur-corners/README.md).
Do not invent backup paths; use the path emitted by the actual installer.

## Protected surfaces
Plasma/Dolphin packages, KWin and plugin ABI, display manager, units/targets,
D-Bus, KGlobalAccel, shortcuts, appletsrc/plasmashellrc, MIME/FileManager1 defaults,
launchers, and backups require explicit recovery analysis before changes.
`./scripts/verify recovery` checks in-memory panel merging; it does not open
windows, alter the session, or prove end-to-end recovery. A later trial should
check panels/shortcuts, Dolphin, System Settings, open apps, and login, with
backups and a return plan.

## Service template source relocation

[ADR-0006](adr/0006-service-template-source-lookup.md) moves only three autostart
source templates to `services/`. The maintained installer now requires the
repository's services directory beside the active kit. Current start/return
scripts do not read these source templates at runtime; installed units, names,
environment, readiness, panel/shortcut snapshots and backup manifests retain
their existing contracts. No installation, reload or session switch accompanied
the move. Source rollback restores templates and installer reads together; no
installed-state restoration is needed for this source-only change. Offline
rendering equality does not prove login or failure recovery.
