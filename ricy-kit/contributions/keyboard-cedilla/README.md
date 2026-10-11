# Cedilla on the international US keyboard

The destination uses `us(alt-intl)` and an English interface. The original English
composition interprets an acute accent followed by c/C as ć/Ć. This applicator
configures `$HOME/.XCompose` to produce ç/Ç, preserving the layout, language, and
other compositions. In a new file, it includes `"%L"`; in an existing file, it
preserves user rules and appends the Ricy block.

```bash
cd "$HOME/Projects/ricy/ricy-kit"
python contributions/keyboard-cedilla/apply.py
python contributions/keyboard-cedilla/apply-brave.py
```

Run without sudo. Fully reopen Konsole and Brave: existing processes may retain
the previous table. In Brave, also stop the background process; logging out and
back in is another way to reload applications. Test the acute accent key followed
by `c` and `Shift+C`: `ç`, `Ç`.

The applicator is idempotent and saves the previous file (or an absence marker) in
`$XDG_STATE_HOME/ricy-teclado-backups/DATA-HORA`, defaulting to `$HOME/.local/state`.
To undo, restore the backup's `XCompose` into `$HOME/.XCompose`; if
`XCompose.ausente` exists, remove the created file. Reopen applications afterward.
For later changes, remove only the block delimited by `BEGIN/END Ricy` to preserve them.

This fixes graphical-session composition; the virtual console keyboard and
separate SDDM account retain their own settings. An ABNT2 physical layout requires
`br` configuration, not this US adjustment.

Reference: [libxkbcommon — Compose and dead keys](https://xkbcommon.org/doc/current/group__compose.html).

## Brave in KDE Wayland

The user confirmed the cedilla in Konsole, but native Wayland Brave still produced ć.
Chromium's internal character composer uses its own table for events not consumed
by an IME. Reopening the browser alone does not make that path use .XCompose.

`apply-brave.py` selects `--ozone-platform=x11` in
`$XDG_CONFIG_HOME/brave-flags.conf` (default `$HOME/.config`). The CachyOS/Arch
package launcher reads this file; the selection uses XWayland within KDE Wayland.
The script preserves other flags and saves the previous state in
`ricy-teclado-backups`. Fully reopen Brave after applying. This path may change
browser scaling/rendering on HiDPI screens.

To undo, restore the backup's `brave-flags.conf`; if
`brave-flags.conf.ausente` exists, remove the created file. To preserve later changes,
remove only the `--ozone-platform=x11` line. Reopen Brave.

Primary Chromium references:
[Wayland input path](https://chromium.googlesource.com/chromium/src/+/HEAD/ui/ozone/platform/wayland/host/wayland_input_method_context.cc) and
[character composer](https://chromium.googlesource.com/chromium/src/+/HEAD/ui/base/ime/character_composer.cc).
