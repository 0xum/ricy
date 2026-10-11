# Nottalia started automatically in KDE

Names `noctalia-teste.service` and `start-test.sh` are historical: after this installer, Noctalia is permanent and starts on login. Menu entries and messages no longer use the test label.

This contribution replaces manual start mode by login, as requested after restart. Plasma remains active for desktop/wallpaper; integration starts Noctalia, adapter and shortcuts and collects panels only after IPC is ready.

## Install

Prepare it first. `noctalia-kde-integration-and-menus` and apply the corrections of the contribution `target-implementation-fixes`. In this prepared copy of the kit:

```bash
python contributions/noctalia-autostart/install-autostart.py
```

Run as a desktop user in Plasma Wayland. The installer stores the previous files in `$HOME/.local/state/ricy-inicio-automatico-backups/`, installs three units in `.config/systemd/user`, updates five integration scripts, validates the units and enables/starts integration.

- `ricy-noctalia-integracao.service` is enabled on `plasma-workspace.target`.
Waits for plasmashell and KGlobalAccel and performs integration, with recovery of Plasma in case of error during execution.
- `noctalia-teste.service` becomes permanent, using the isolated profile
Ready. Restarts failure and also initiates the adapter.
- `noctalia-busca-desktop.service` is permanent and follows the shell.
`Type=exec` and verifies the effective ownership of `org.kde.krunner`; does not declare `BusName`, avoiding conflict with KRunner's native unit.

The units follow `graphical-session.target`. The adapter restarts when restarting the shell. Old login recovery does not restore Plasma while the autostart is enabled.

The Super log waits up to two seconds for the effective creation of the action in KGlobalAccel. This covers the creation of desktop entries in the login. Original shortcuts and backups JSONs continue to be captured in the destination.

## Back to Plasma

```bash
contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/return-to-plasma.sh
```

This operation also disables the autostart for the next logins. To return to Noctalia and reactivate preference:

```bash
systemctl --user enable ricy-noctalia-integracao.service
systemctl --user restart ricy-noctalia-integracao.service
```

In this facility, `$HOME/Projects/ricy/return.sh` and `$HOME/Projects/ricy/start.sh` offer these operations. Existing style backup and layout backup have been maintained.

## Verification carried out

Units checked by `systemd-analyze --user verify`; integration enabled with symlink in KDE target; start by unit ended successfully. Cycle back to Plasma (two panels, autostart disabled) and autostart tested. Restart of shell also restarted the adapter; D-Bus owner PID coincided with the adapter and Query query opened the search. Invalid TOML configuration was temporarily entered: integration restored the two panels/KRunner, and the original profile was restored and successfully started.

The login enable was checked. A complete reboot after this change was not executed by the agent during the user session.
