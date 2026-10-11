# Windows: fade and expansion

Visual reference provided by the user:
[Slick Window Arrangement](https://windhawk.net/mods/slick-window-arrangement).
Scope confirmed: Open/restor and close/minimize windows.

| Action | Scale | Opacity | Curve |
|---|---|---|---|
| Open or Restore |  0,85 → 1,00  |  0 → 1  | OutCubic |
| Close or minimize |  1,00 → 0,85  |  1 → 0  | InCubic |

Basic duration **320 ms**, with the center of the window itself as a reference. Transformation is visual: position and real size do not change. It does not require icon geometry and does not move the window to the taskbar or other monitor. Global KDE preference preserved: AnimationDurationFactor=0,25 in the registered session results in approximate reference duration **80 ms**. animationTime applies KDE preferences, including movement reduction; does not change kdeglobals.

Minimize/restaurate uses the new variant of the local ricywindowactions effect, with Scale and Opacity, maintaining the native reversion by redirect. If the reversal fails, cancels before starting the new direction. Repeated events do not stack animations. Blur remains until both tracks are finished; old or other effects IDs are ignored. Close during a transition cancels the trails of minimizing/restoring, preserving the native Scale blur if it has already started closing.

Open/close uses **KDE Native Scale**, now configured with 320 ms and scale 0,85. You can also animate dialogs according to KDE native filters. Close occurs when the application accepts the request, including confirmation of saving. Minimize/restaurate follows only normal windows that appear in the bar; panels, popups and full screen effects keep their filters. Fade, Squash and Magic Lamp are disabled to prevent duplicate effects.

Noctalia remains with the approved binary of the icons-apps-reorder contribution. Drag, saved order, animations/hover of icons, purple indicator and shell compositions maintained. ricyblur and smoothwindowgeometry remain loaded. Maximize, resize and move windows have not been adjusted in this step.

## Apply and Reverse

Run as session user without sudo:

```bash
cd "$HOME/ricy-kit/contributions/window-fade-expand"
python validate.py
python apply-animations.py
```

Installer saves copy of the previous package and only the ten keys changed in ~/.local/state/ricy-fade-expand-backups/DATA-HORA. Install the local package in ~/.local/share/kwin/effects/ricywindowactions and configures kwinrc. Reloads only the effects and reconfigures KWin without restarting compositor or shell, and preserves open applications. If the activation fails, restores the backup. It does not require recompile Noctalia.

To return to the previous behavior of this session:

```bash
python apply-animations.py --restaurar "$HOME/.local/state/ricy-fade-expand-backups/20261010-205749-431612"
```

On another machine, use the backup path printed by the installer. Reversion restores package, present/absent keys and Scale configuration. Private backups and preferences are not part of the kit. When playing the current session, use the App-icon-reordering compiler for Noctalia and this installer for window animations.

## Verification and references

28 scenarios run the real JS in QJSEngine: fade/scale, intact geometry, speed, configuration limits, reversal and fallback, repeated events, trail ID blur, path closing, filters and coordinated installation. A disposable Qt window in the actual session confirmed Scale opening, restore/minimize/restaurate, fast sequence minimize/restaurate, common activation without minimizing and closing with Scale. ricywindowactions was active in the actions of minimizing/restaurate. Installed package coincides with the kit, configuration was checked and ricywindowactions/Scale/ricyblur effects remain loaded. No script errors appeared in the consulted journal.

Do not measure frame the scale/opacity in session or validate all applications, dialogues, monitors or scales. Values and reversal are covered by JS isolated; the actual window validates integration and states. This adjustment has not yet received visual confirmation from the user.

A [Slick Window Arrangement font](https://github.com/ramensoftware/windhawk-mods/blob/main/mods/slick-window-arrangement.wh.cpp) describes sliding and snapping while moving. The effect requested here was implemented with the native KWin API; no Windows code was copied. KDE primary references:
[Scale](https://github.com/KDE/kwin/blob/v6.7.5/src/plugins/scale/package/contents/code/main.js)
and [Squash](https://github.com/KDE/kwin/blob/v6.7.5/src/plugins/squash/package/contents/code/main.js). Local effect derives from KDE reversible structure, maintaining Vlad Zahorodnii credit and GPL-license2.0-or-later in code and license file. Compatible with KWin session 6.7.5; review while updating the compositor. Kit without binaries, accounts, screenshots, clipboard, bytecode or private preferences.
