# Corrections in the implementation of the destination

This contribution complements the historical archives without replacing their copies in the distributed kit. It was applied to the active copy in `$HOME/ricy-kit`.

## Apply before preparing another destination

At the root of the kit, check the hashes and then apply the corrections:

```bash
sha256sum -c SHA256SUMS
python contributions/target-implementation-fixes/apply-fixes.py
```

The applicator validates all files before writing. Only accepts the original version or the corrected version; repeat the application is allowed. After applying, the original hashes of the two changed files cease to match the package, as already happens with the files. `.desktop` after preparing the destination.

Continue with the README of `noctalia-kde-integration-and-menus` and the README of `dolphin-deb-rpm-installer`. Use only the given Noctalia contribution: the old copy in `outputs/` from the root does not receive these corrections.

## Changes

- `configure-super.py`: flame `doRegister` and `setShortcut` before
`setForeignShortcut`In the destination, the foreign call alone did not register Super. Super and Super Space records, the opening of the launcher and the restoration/restart cycle were checked.
- `debtap`: generates `.MTREE` with UID/GID zero, includes `.INSTALL` only when
exists, interrupts in generation error and saves the final file with zero numerical ownership. Delete `namcap-*` and `pkgbuildinstallations*` package, mtree and size calculation. DEB and RPM of test were converted, installed, checked by `pacman -Qkk` (zero files changed) and removed.
- `update-indexes.sh`: wrapper to run Debtap installed with IPv4,
connection/time limits, returns, verified TLS and HTTPS URLs of Debian/Ubuntu indexes. Checks that all required indexes are not empty after command. Do not change `/usr/bin/debtap`.

After installing the AUR Debtap package, update the indexes:

```bash
sudo bash contributions/target-implementation-fixes/update-indexes.sh
```

The interface test has reached the button **Install** with `SHELL=fish` and `TERM` absent, without clicking the button. RPM with scriptlet has been refused. This does not demonstrate universal compatibility of external packages. Parsec has not been installed in this implementation; its binary is not part of the kit.

The completed corrected copies and their diffs are in this folder. George Savvidis Debtap Code, GPL-2.0 or later, preserved license. The contents of the bases continue depending on the external servers and the upstream heuristic.
