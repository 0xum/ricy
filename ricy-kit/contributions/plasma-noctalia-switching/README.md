# Toggle Plasma and Noctalia Preserving Ricy

This contribution replaces the integral restoration of the old backup used by previous scripts. The wallpaper, desktop widgets and general settings remain shared in Plasma. Each entry in Noctalia saves the latest Plasma panels and their geometry groups; the return restores only these groups without restoring complete files from an old installation. The existing private, custom binary, state and Noctalia drop-ins remain in use. It does not restore colors, fonts, effects, or app appearance.

## Install in a prepared destination

After preparing Noctalia/KDE and installing `noctalia-autostart`:

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/install.py"
```

Requires the Plasma Wayland session, its three units already installed, Python/PyGObject, qdbus6, systemctl, flock and kbuildsycoca6. The installer does not change the current environment. Run again after reinstalling the old autostart scripts. The paths are calculated from the location of the kit and the target user.

## Use

```bash
ricy noctalia   # select Noctalia and enable it for the next login
ricy plasma     # select Plasma and disable Noctalia autostart
ricy alternar   # switch to the other shell; also the default action of `ricy`
ricy status     # mostrar Plasma ou Noctalia
```

The commands are in `$HOME/.local/bin`; if this directory is not in PATH, use the full path. Also exist `voltar-ao-noctalia`, `voltar-ao-plasma`, `$HOME/Projects/ricy/start.sh`, `return.sh`, `switch.sh` and three entries in the menu: **Back to Noctalia**, **Back to Plasma**, **Toggle Plasma and Noctalia**.

The old wrappers of the active kit start forwarding for this implementation. Each change runs in a separate transitory unit from the shell, to continue even when the command was opened by the Noctalia menu and the shell is closed. The service and profile names remain the same. Plasmashell briefly restarts to sync KConfig and restore panels; KWin and applications remain open. Only collects panels after confirming shell, searching and shortcuts. Failure during this step recovers Plasma; failure by the command also disables the Noctalia preference in the login. Super, Super+Space and Super+V shortcuts are captured before the transfer and returned at every cycle.

Private backups, shortcuts and panel groups stay in `${XDG_STATE_HOME:-$HOME/.local/state}/ricy-alternancia/`; do not distribute this folder. The panel snapshot updates when there are live panels; entering a session again already Noctalia does not replace it with an empty layout. Collapses with widget/desktop IDs created later are remapped. The original backup `plasma-antes.tar.gz` it is never modified; it only serves as panels seed when migration starts in an old session already without panels.

## Verify

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/verify.py"
ricy status
systemctl --user is-active plasma-plasmashell.service
```

Noctalia must have active shell/adapter and zero Plasma panels; Plasma must have its panels and KRunner. The wallpaper must remain in both directions. The installer prints the backup; integration errors appear in `journalctl --user -u ricy-noctalia-integracao.service`.

## Undo alternation installation

First run `ricy plasma`. Then use the backup path issued:

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/restore-installation.py" \
  "$HOME/.local/state/ricy-alternancia/backups/DATA-HORA"
```

The restorer only restores wrappers/command entries and the alternation state. It does not replace captured appletsrc/plasmashellrc for diagnosis, preserving the current desktop. It does not delete the Noctalia profile, effects, appearance or backups. The old replaced scripts again have the original limitation: they can restore an old wallpaper/layout. To keep alternating, keep this contribution installed.

It is not a session/compositor exchange: Noctalia is integrated to KDE/KWin. Desktop changes themselves are shared. login/block appearance remains independent; its restorers remain in other contributions.
