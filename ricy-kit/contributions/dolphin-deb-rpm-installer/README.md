# Dolphin: local DEB/RPM installer in CachyOS

This contribution is a playback copy of the installer created in this session, not an official CachyOS tool. Open a package in Dolphin: the window prepares the conversion, displays the metadata and provides **Install**. The button calls `pkexec /usr/bin/pacman -U --noconfirm`; Confirmation is the button itself and Polkit requests authentication. Do not use `dpkg -i` nor `rpm -i`.

## Installation at destination

Use CachyOS x86_64 with KDE Plasma, Python 3.14 observed, Qt 6 and agent Polkit of the session. The exact versions observed are in `observed-versions.txt`; are not mandatory versions for future systems. Do the commands in Bash. Run the integration scripts as the desktop user without sudo.

Check out the kit hashes before preparing:

```bash
cd "$HOME/Projects/ricy/ricy-kit"
sha256sum -c SHA256SUMS
```

Before installing dependencies, manage a record of DESTINATION packages:

```bash
umask 077
backup_pacotes=$(mktemp -d "$HOME/ricy-pacotes-antes-XXXXXXXX")
pacman -Q > "$backup_pacotes/pacotes.txt"
pacman -Qqe > "$backup_pacotes/explicitos.txt"
printf '%s\n' "$backup_pacotes"
sudo pacman -Syu
sudo pacman -S --needed dpkg rpm-tools binutils fakeroot pkgfile namcap python-pyqt6 desktop-file-utils
```

`bash`, `pacman`, `python`, `libarchive` (bsdtar), `zstd`, `curl`, `gawk`, `grep`, `sed`, `coreutils`, `tar`, `gzip`, `binutils`, `fakeroot`, `pkgfile`, `namcap` are used by the converter. Polkit provides pkexec and KDE provides kbuildsycoca6. Git/base-devel are used only to build the AUR package below.

Install Debtap by AUR after reading your PKGBUILD and installation file:

```bash
sudo pacman -S --needed git base-devel
build_debtap=$(mktemp -d "$HOME/debtap-build-XXXXXXXX")
git clone https://aur.archlinux.org/debtap.git "$build_debtap/debtap"
cd "$build_debtap/debtap"
cat PKGBUILD debtap.install
makepkg --verifysource
makepkg -si
```

This session was built `debtap 3.6.3-1`, sources with SHA-512 verified. AUR can change: distributed scripts include local copy of version 3.6.3 with the corrections applied, but the base update remains necessary.

```bash
# Base initialization: Debian/Ubuntu/AUR index downloads, about
# 1,1 Uncompressed GiB observed in /var/cache/debtap on this machine.
# IPv4 and waiting limits solve the block observed in access to Ubuntu.
sudo bash -c 'curl() { /usr/bin/curl -4 --connect-timeout 15 --max-time 180 "$@"; }; export -f curl; /usr/bin/debtap -u'
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-deb-rpm-installer"
python install-integration.py
```

Upstream base uses HTTP URLs and `curl -k`, as in the original code; IPv4/timeout wrapper does not correct this behavior. Requires network access. Copy `app/debtap` uses the base of `/var/cache/debtap` and `/var/cache/pkgfile`.

The preparer creates local backup with directory 0700 ed `$HOME/.local/state/cachyos-package-installer-backups/<data-hora>/`, including previous files, absences, MIME defaults and package list. Do not reuse backups from another user. A new execution creates a new backup without deleting the previous ones. The script replaces your own scripts and two desktop entries; adjusts only the three requested defaults by keeping the other MIME values.

Final files:

- `$HOME/.local/share/cachyos-package-installer/{backend.py,installer.py,normalize_control.py,debtap}`.
- `$HOME/.local/share/applications/cachyos-local-package-installer.desktop`.
- `$HOME/.local/share/kio/servicemenus/cachyos-install-package.desktop`Executable.
- `$HOME/.config/mimeapps.list`: `application/vnd.debian.binary-package`,
`application/x-debian-package`, `application/x-rpm` point to `cachyos-local-package-installer.desktop`.
- Cache: `$HOME/.cache/cachyos-package-installer/conversion-*` and
`last-conversion.log`Conversions are serialized by `conversion.lock`.
- No service, autostart, daemon, Polkit rule or Fish configuration
The shell Bash is only imposed on the converter processes.

Templates `.desktop.in` use `@INSTALLER@`; the preparer writes the absolute paths of the escaped destination user. The portable Debtap resolves the normalizing script next to the file itself. The kit does not contain source user names, personal backups, caches, application logs or Parsec executables.

## Conversion, limitations and corrections

DEB is converted by Debtap. `normalize_control.py` removes CRLF and deploys dependencies fields; identifies common libraries by ABI in `/usr/lib` and by the owner in the pacman/pkgfile, choosing declared alternatives. Avoids the private Proton providers and tools of another architecture observed in the Parsec attempt. There is explicit mapping for common libraries and libavcodec/libavformat/libavutil; it does not cover all Debian names. Debian versions with epoch/revision are compared by upstream, with `vercmp`; limits only `>=`/`>>` This is a heuristic, not a universal equivalence between distribution versions.

RPM is consulted with local temporary rpmdb, extracted by rpm2archive for binary file and per filter tarfile `data`; generates intermediate DEB and uses the same flow. RPMs with scriptlets / triggers are refused, without ignoring them. Archive dependencies need an identified provider; other complex dependencies and incompatible architectures are refused. Binary capture avoids showing bytes gzip as text. Conversion occurs without root.

`app/debtap` preserves copyright and GPL-license2.0; complete licence included. `debtap-changes.patch` describes differences against `/usr/bin/debtap 3.6.3`: regex of the current pkgfile indexes, normalizer, native resolution, size without presupposing directories of 4096 bytes on Btrfs, range of `cut`, Explicit bash in fakeroot and tar/zstd failure check. TERM=dumb prevents tput warnings. The version `/usr/bin/debtap` It's not overwritten.

**Perdence observed:**  `pacman -Qkk parsec` reported divergent UID/GID in 15 Package entries installed, although not reported content divergence in this execution. Current corrections do not explicitly normalize UID/GID in tar/mtree. The kit preserves this state without stating that it is resolved. Before expanding usage, audit the generated package and its ownership metadata. We do not correct this pending during documentation as requested.

There is no guarantee for all packages, Debian scripts, dynamic dependencies loaded via dlopen or source distribution settings. Pacman -Up confers resolution/architecture but does not prove that the program works or replaces the conflict check at the time of installation. Conversions never use `--nodeps` or `--overwrite`. Converted application updates require new files; do not follow Debian/Fedora repositories automatically.

## Destination verification (to be executed)

```bash
python -c 'from PyQt6.QtWidgets import QApplication; print("PyQt6 available")'
gio mime application/vnd.debian.binary-package
gio mime application/x-rpm
desktop-file-validate "$HOME/.local/share/applications/cachyos-local-package-installer.desktop"
```

Open a reliable DEB in Dolphin; you should get to **Install**, presenting native metadata. Before confirming, check name, version and dependencies. For RPM with scripts, expect an explanatory refusal. After installation, `pacman -Q nome`, `pacman -Qkk nome` and app opening are separate checks. To inspect without installing: `pacman -Qip arquivo.pkg.tar.zst`, `pacman -Up arquivo.pkg.tar.zst`, `bsdtar -tvf arquivo.pkg.tar.zst` and `bsdtar -xOf arquivo.pkg.tar.zst .PKGINFO`.

Tests actually performed in the source: Python/Bash syntax, desktop-file, GUI offscreen, DEB/RPM minimum test without installing, RPM refusal with scriptlet, Parsec real played in missing Fish/TERM environment reaching the Install button without tput/cut errors and without Proton/cross compiler; MIME verification defaults and hash of Parsec file. The later installation is confirmed in the current state/pacman.log, not a new installation made to document. There is no confirmation in this Parsec streaming/login chat or real migration on another machine. New installer/restoration scripts have been statistically validated, not executed on the current session.

## Undo in destination

Close the installer after completion of the operation. Use the path printed by the preparer (previous backups are maintained):

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-deb-rpm-installer"
python restore-integration.py "$HOME/.local/state/cachyos-package-installer-backups/<data-hora>"
```

This restores complete backup files and removes targets that previously did not exist by updating KDE caches. You can replace other later edits in these MIME files; review the backup if you want to restore only the three entries. Do not remove packages, converted apps, cache or backup. No backup, return to Ark is possible if it is installed:

```bash
xdg-mime default org.kde.ark.desktop application/vnd.debian.binary-package
xdg-mime default org.kde.ark.desktop application/x-debian-package
xdg-mime default org.kde.ark.desktop application/x-rpm
```

Converted applications are removed by pacman, for example `sudo pacman -R parsec`. Please refer to the package log before the change to remove only what has been added and is not used by other programs. Do not automatically remove binutils/fakeroot/pkgfile/Python/Qt: some already existed or are now shared. `sudo pacman -Rns dpkg rpm-tools debtap namcap` is a possibility only if these packages have been added to the destination and are no longer required; review the transaction. Do not perform this indiscriminately. The converter cache can be deleted after closing the window; this loses the converted files and logs. `/var/cache/debtap` remains even after removing debtap, and can be removed manually if there are no other converter users. `/var/cache/pkgfile` are shared and must be maintained.

## Summary History

First terminal tools were installed, incomplete interpretation of the double-click request. Discover/PackageKit, Alien and rpmtoarch were consulted, but not installed. The final implementation is local PyQt6. The first debtap update was stuck in Ubuntu; it was interrupted and repeated with IPv4/timeout. The first minimum tests did not cover Fish, CRLF or Parsec dependencies; actual failures motivated the corrections included. None of the test packages was installed. Scripts/investigative materials remain at source in `~/.cache/package-support`, but they are not necessary to the kit and were not copied.
