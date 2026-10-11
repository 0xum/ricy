# Konsole: animated text cursor

This contribution meets the user's correction: the requested cursor is Konsole's animated text cursor. The Bibat pointer of the appearance contribution remains an additional preference captured.

Status observed in Konsole 26.08.2-1.1:

- `konsolerc`: standard profile `PlasmaBlur.profile`; Disabled menu bar.
- Plasma Blur Profile: `[Terminal Features] AnimatingCursorEnabled=true`.
- Source: JetBrainsMono Nerd Font 10 pt; palette `PlasmaBlur`.
- Palette Catppuccin Mocha, `Opacity=0.85` and `Blur=true`.
- Wrapper and app input use `QT_STYLE_OVERRIDE=kvantum`.

Property confirmed in local executable by `/usr/bin/konsole --list-profile-properties` and [Official code of this version](https://github.com/KDE/konsole/blob/v26.08.2/src/profile/Profile.cpp). The profile does not explicitly define BlinkingCursorEnabled, CursorShape or CustomCursorColor: its values remain inherited from the FALLBACK profile. An additional blinking or cursor color setting has not been invented.

## Play in destination

```bash
sudo pacman -S --needed konsole kvantum ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit/contributions/konsole-animated-cursor"
python apply.py
```

Run as a desktop user without sudo. The script checks if the destination Konsole recognizes the animation option before changing preferences. Install only profile/palette, wrapper and launcher; merge DefaultProfile and MenuBar in konsolerc, preserving other keys and groups. Previous files and absences are stored in private folder 0700 under `$HOME/.local/state/ricy-konsole-backups/DATA-HORA/`.

Close and open Konsole to load settings. At the next installation, the shell comes from the target user; the profile does not fix user, directory, boot command or history. The blur also depends on the compositor. The rest of the Ricy already includes Kvantum and the required font.

## Check and Restore

```bash
kreadconfig6 --file konsolerc --group 'Desktop Entry' --key DefaultProfile
kreadconfig6 --file "$HOME/.local/share/konsole/PlasmaBlur.profile" --group 'Terminal Features' --key AnimatingCursorEnabled
/usr/bin/konsole --profile PlasmaBlur
```

The expected result of the first two commands is `PlasmaBlur.profile` and `true`To undo, use the backup printed by the applicator:

```bash
python apply.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
```

Reversion restores the affected files and removes those that did not exist before. It can replace later editions in these archives; it does not remove Konsole.

Verification: option support in installed executable, exact copy of active profile and palette, Python/desktop/Bash syntax, and application/restoration in disposable HOME, preserving other preferences. There was no change in Konsole windows or settings in use, nor new animation visual test.
