# Continuity of the blur between Noctalia surfaces

The KWin 6.7.5 calculates the blur using a texture limited to the rectangle of each window. In bars, panels and notifications this can leave an amendment even when color and transparency are equal.

This contribution compiles a separate effect, `ricyblur`, from the official KWin blurch 6.7.5, commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`. Surfaces with resourceClass `noctalia` use a common background reference per monitor while there is a visible dashboard/warning. The same result is cut by the shape of each surface. Sampling does not include Noctalia itself; OpenGL window clipping does not limit the copy or filter of the shared background. Other applications maintain native blur logic.

The background is reconstituted before the first Noctalia surface in each required frame, and the filter is calculated once per monitor. While a panel/warning is open, frames with changes repaint the entire monitor to avoid reuse of pixels that already contain the bar. This can increase the cost of composition with video/animations; no continuous repainting loop is created when everything is stopped. No screenshots or recorded content of the disk background are made.

Also applied `panel_overlap = 0` ed `[bar.default]` and `[bar.search_edge]`: removes the range of a pixel with two layers of transparency at the junction. The position, corners, opacity 0,70 and the choice of monitor remain as in the search/notification contributions. The geometry of notifications still depends on the local variant of Noctalia in `../notification-continuity/`.

## Play in CachyOS/Arch

First prepare the Noctalia integration and its notification geometry. KWin plugin ABI requires the same version of the compositor. The compiler refuses different version of 6.7.5; Review/rebase the patch when updating.

```bash
sudo pacman -S --needed base-devel git vulkan-headers kwin kconfig kcoreaddons kdecoration qt6-base qt6-declarative kwindowsystem libepoxy libdrm wayland
cd "$HOME/ricy-kit/contributions/blur-continuity"
python build.py
sudo install -D -m 0755 "$HOME/.cache/ricy-blur-build-6.7.5/ricyblur.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so
python integrate.py
noctalia msg config-reload
```

If XDG_CACHE_HOME is set, use your directory in the install command. In this destination no more packages needed to be installed: official Vulkan headers were used 1.4.363 cache, commit `6802bb4733b63ed5efd3adb308a6c885ef180ea1`, by RICY_VULKAN_HEadERS pointing to your folder include. In a reset, the vulkan-headers package is sufficient.

The effect does not replace KWin binary, libraries or native plugin. `integrate.py` installs the selector in `$HOME/.local/lib/ricy-blur/start.py` and enables `ricy-blur-continuidade.service` in the graphical session. Do not restart the compositor or shell or close applications. The script selects the variant only in KWin 6.7.5 and when it is supported; if you cannot load it, maintain or reload the native blur. The native remains enabled in the configuration; ricyblur is not enabled as an automatic KWin plugin.

Preferences `panel_overlap` come from the kit templates; in an already active installation, also adjust your config.toml Before reloading. Back up first.

## Check and Restore

```bash
systemctl --user status ricy-blur-continuidade.service
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.isEffectLoaded ricyblur
```

To return to the native effect:

```bash
systemctl --user disable --now ricy-blur-continuidade.service
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.unloadEffect ricyblur
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.loadEffect blur
noctalia msg config-reload
```

The plugin file can remain installed and disabled. Remove it, if desired, with `sudo rm -- /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so`. The integrator guards previous helper/unit in `$HOME/.local/state/ricy-blur-backups/`. Restore effect does not reverse panel_overlap; restore backup of config.toml Or just adjust that preference.

Visual test performed first in a single KWin/Noctalia session, with colored tracks, menu and notification; then applied in the main session. The user visually validated during work. Migration to another computer and different scales has not been tested.2.0-or-later, licence included in LICENSE.

Sources: [Official version blur](https://github.com/KDE/kwin/tree/v6.7.5/src/plugins/blur) and [ABI effect rules](https://github.com/KDE/kwin/blob/v6.7.5/src/effect/effect.h).
