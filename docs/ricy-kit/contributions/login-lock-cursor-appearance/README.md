# Login, blocking, cursor and appearance — capture of 09/10/2026

This contribution exports the effective appearance of this computer to another installation CachyOS/KDE Plasma Wayland. The consolidated guide is in `REINSTALL.md`, together with `ricy.md`. None of these installers were applied to the original session during export.

## Settings included

| Component | Catched State |
|---|---|
| Sign-in screen | SDDM, local theme `mocha-limine`based on Breeze Qt 6  |
| Login Background |  `limine-splash.png`, image included in the kit, filling with proportional cutout |
| Login: watch/form | Clock on, immediate form, concealment after 60 s of inactivity, soon hidden |
| Login: colors | Groups `Colors:*`/`ColorEffects:*` SDDM account: Catppuccin Mocha Mauve; selection `#cba6f7`  |
| Login: source/icons/style | JetBrainsMono Nerd Font 10 en; Breeze Dark; widget |
| Mouse pointer (extra) | Modern Classic Bibat 2.0.6, size 16, KDE/GTK/SDDM and XCURSOR |
| Lock | Limine background, watch always visible, immediate form/60 s, media and reveal hidden password |
| Lock Authentication | Existing adaptation preserves `uiVisible: false` and use `Qt.callLater` after mounting |
| KDE Fonts | JetBrainsMono Nerd Font 10 en: general, mono, menus, bars, minors and titles |
| KDE/GTK Icons |  `breeze-dark`, effective preference inherited from KDE defaults |
| Qt Applications | Kvantum `KDE-Noctalia`, palette `KDE-Noctalia` already distributed in the kit |
| Plasma Appearance | Local theme `mocha-blur`; global package `Catppuccin-Mocha-Mauve` and its splash screen |
| Window decoration | Breeze, BorderSize None, BorderSizeAuto false, NoPlugin false |
| GTK applications |  `adw-gtk3-dark`, dark preference, source/cursor/icons above, sound `ocean`, DPI 96  |
| Fontconfig | Hinting on, hintslight and antialiasing; captured visual file |
| Blur KWin | Active, strong. 5, noise 2  |
| Optional extensions | adaptivepanelwidth, smoothwindowgeometry and windowsarrows, selected fonts and shortcuts included |

`preferences.json` contains only desktop account appearance keys. `greeter-preferences.json` contains the visual groups actually read from `/var/lib/sddm/.config/kdeglobals` by privileged reading. The login palette is different from the KDE-Noctalia palette of applications; both have been preserved. `kwin-preferences.json` contains only the shortcuts required for arrows.

The cursor requested by the user is Konsole's animated text cursor. Its profile/palette and applicator stay in the sister contribution `konsole-animated-cursor/`, included in the reset tab. Bibat is an additional mouse pointer preference, captured in this contribution.

Included Assets: Login QML/metadata, Full Bibat, Limine wallpaper, Four Faces JetBrainsMono Nerd Font (Regular/Bold/Italic/BoldItalic), Local Plasma/splash themes and sources of KWin extensions. Kvantum and KDE scheme are reused from contribution `noctalia-kde-integration-and-menus` from the same kit. GTK, Breeze icons, Qt/KDE components and Ocean sounds come from the destination packages.

No personal avatar, password, SDDM user history, PAM, autologin with user name, monitor/desktop IDs, mouse specific acceleration, source backups, caches, or clipboard history. The custom SDDM session folders of this machine are not imported: select the Plasma Wayland session offered by the new installation.

## Install in destination

Use the consolidated roadmap of `REINSTALL.md`. For only this contribution, first install KDE/GTK dependencies in a Plasma Wayland session:

```bash
sudo pacman -S --needed sddm plasma-workspace breeze breeze-icons kvantum qt6-5compat qt6-svg python fontconfig adw-gtk-theme ocean-sound-theme
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
sudo python system.py
python user.py
python ../login-matched-lock-screen/apply.py
```

`system.py` installs SDDM/cursor/source/wallpaper theme and merges visual preferences into `/etc/sddm.conf`, `/etc/sddm.conf.d/95-mocha-limine.conf` and the SDDM account. Solves UID/GID of `sddm` in the destination, no matter numerical IDs of this machine. The background passes to `/usr/local/share/ricy/limine-splash.png` and the source `/usr/local/share/fonts/ricy/`. Do not restart the login manager.

`user.py`, run without sudo, save the affected files before installing the themes and merge the KDE/GTK keys. Define cursor in kcminputrc, GTK 2/3/4, environment.d and cursor inheritance in icons/default. Keeps other keys from existing files. Do not apply the full defaults of the global theme: the old defaults still quote Aurorae/another cursor, but the captured effective state uses Breeze and Bibata. If later apply a global theme by KDE, run again `user.py` to return to this state.

The lock is installed by the existing applicator. It reads the installed login theme, generates QML from the destination KDE and interrupts before typing if the expected snippets change. Reapply after updating Plasma. Do not copy the local shell folder generated on this host to another KDE version.

Do a new session to load cursor, font, splash, icons and style. Do not use `systemctl restart sddm` from within a session you wish to preserve.

## Window Extensions (optional)

To also take the effects and behavior of the current Super Arrows:

```bash
sudo pacman -S --needed gcc pkgconf qt6-base qt6-declarative kwin kconfig
python user.py --extensoes-kwin
```

The script recompiles windowsarrows in a temporary folder, using headers and destination libraries, before changing preferences. Do not distribute `.so` Antique. Also installs adaptivepanelwidth/smoothwindowgeometry, applies its flags and disables the concurrent maximize effect. Sets Super+arrows for the script and releases the same combinations of native quick Tile. Preserves maximize Super+PgUp, minimize Super+PgDown and restore Super+Backspace. Resume to load module and shortcuts. API/ABI KWin changes may require adaptation; source code is included.

## Desktop Wallpaper (optional)

Noctalia continues to leave the wallpaper in charge of Plasma. To choose Limine on the desktops of the new installation, before preparing integration:

```bash
bash apply-wallpaper.sh
```

The script lists the local desktops by the Plasma API. It changes the image on the desktops present; the previous wallpaper can be chosen again by the System Settings. It does not create a layout backup of its own. If you prefer to preserve the image of the new installation, do not perform this step. The Noctalia integration should be prepared after that choice to register the correct image in your local wallpaper preservation script.

## Undo in destination

Use the backup paths printed by the installers; each execution generates a new backup. If you applied the extensions to a later execution, first undo this execution, then the previous execution of the appearance:

```bash
python ../login-matched-lock-screen/restore.py "$HOME/.local/state/ricy-lockscreen-backups/DATA-HORA"
python user.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python system.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

Restorers replace the affected files/themes and remove those that did not exist before. Restore is integral to each stored file and can replace later edits in those files. In the system backup, original UID/GID are also saved. Installed packages are not removed. Backups are private, with folder 0700; keep them in the facility that generated them.

## Verification and limits

Effective local settings, equivalence of user/system bibata copies and theme dependencies were checked. Application and restoration of scripts were exercised in disposable roots/home, including greeter palette, preservation of other keys, GTK with duplicate key, existence and absence. The generation/restoration of the block was exercised in disposable HOME; `uiVisible: false`, Qt.callLater and 60 s checked. The windowsarrows module was recompiled in temporary folder with the local KWin.

There was no visual reapplication in the actual session, resumption SDDM, new blockage or password test in this export. ricy.md. A complete new installation and the behavior of extensions in another version have not been tested. `observed-versions.txt` are catch references, not guarantee of future compatibility.

Original licenses/notices were kept. Bibata: GPL-3.0, upstream font https://github.com/ful1e5/Bibata_Cursor/tree/v2.0.6 ; Catppuccin KDE: MIT, https://github.com/catppuccin/kde ; QML Breeze/Plasma theme: KDE LGPL warnings; SDDM metadata declares CC-BY-SA. Complementary texts stay in `licenses/`. Fonts include OFL. Limine Wallpaper has been copied from the local cachyos-wallpapers package; keep your assignment while transporting this personal backup.
