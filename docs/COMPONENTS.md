# Components

The maintained grounding is [CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md): consumers,
dependencies, cumulative lineage, part-level classifications, recovery impact,
and read-only observations for all 24 contributions and shared material.
Classes describe current roles; KNOWN/UNKNOWN describe evidence. Neither a
registered consumer nor a passing static check certifies runtime functionality.
All destinations are PLANNED. Ownership preserves upstream licenses. Each
component link below leads to its local README; consult the audit before acting.

The root `ricy-kit/` owns the active installation; this does not make every file
in it ACTIVE. `docs/ricy-kit/` preserves HISTORICAL transport variants. Read
[kit rules](../ricy-kit/AGENTS.md) before editing; replicas are not interchangeable.
The current source reference is app-icon-reordering, with window-fade-expand for
windows. The deployed Noctalia binary still matches the earlier reordering diff
preserved in the transport copy, not the RICY-001 source revision. Native blur
is loaded; the ricyblur selector is failed. See audit G-02/G-03 for the limits.

| Current component/location | Responsibility | Future destination | Dependencies | Class / ownership | Impact on recovery |
|---|---|---|---|---|---|
|  [noctalia-kde-integration-and-menus](../ricy-kit/contributions/noctalia-kde-integration-and-menus/README.md)  | Qt search, profile, shortcuts and menus adapter |  `integrations/kde/ + services/ + themes/`  | Noctalia, PyGObject, D-Bus, KGlobalAccel, Kvantum | ACTIVE / RICY-OWNED + derivative assets | High: shortcuts, wallpaper and shared style |
|  [noctalia-autostart](../ricy-kit/contributions/noctalia-autostart/README.md)  | Shell units, search and integration in login |  `services/ + installer/`  | user systemd, Plasma, integration | ACTIVE / RICY-OWNED | High: start only after readiness; Plasma return |
|  [plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md)  | Ricy command, snapshots and panel restoration |  `recovery/plasma/ + integrations/kde/`  | systemd, Python/PyGObject, qdbus6, flock, KGlobalAccel | RECOVERY / RICY-OWNED | Critical: current return path |
|  [notification-continuity](../ricy-kit/contributions/notification-continuity/README.md)  | Local binary notification patch and activator |  `shell/noctalia/`  | Pinned Noctalia, integration, compositor blur | ACTIVE (split) / PATCHES + RICY-OWNED | Preserve /usr/bin/noctalia, backup and apps |
|  [taskbar-menu-composition](../ricy-kit/contributions/taskbar-menu-composition/README.md)  | Fitted app menu; cumulative historical variant |  `shell/noctalia/`  | Noctalia and previous patches | HISTORICAL / PATCHES | Shell crash risk; maintain activator/reversion |
|  [tray-menu-composition](../ricy-kit/contributions/tray-menu-composition/README.md)  | DBusMenu Menus Fitted; Historical Variation |  `shell/noctalia/`  | Noctalia, DBusMenu | HISTORICAL / PATCHES | Actions belong to the applications; do not change without validation |
|  [app-icon-interactions](../ricy-kit/contributions/app-icon-interactions/README.md)  | Hover/Icon scale; historical variant |  `shell/noctalia/`  | Noctalia Style | HISTORICAL / PATCHES | Do not change hit area or session control |
|  [taskbar-app-actions](../ricy-kit/contributions/taskbar-app-actions/README.md)  | Focus/minimization/closing by UUID; historical |  `shell/noctalia/ + integrations/kde/`  | KWin and Noctalia API | HISTORICAL / PATCHES | Tests should not close user work |
|  [app-indicator-animations](../ricy-kit/contributions/app-indicator-animations/README.md)  | Indicators and previous window animation |  `shell/noctalia/ + compositor/kwin/`  | Noctalia and KWin | HISTORICAL / PATCHES + KDE derivative | Previous variant; do not apply on the current |
|  [app-icon-states](../ricy-kit/contributions/app-icon-states/README.md)  | Icon movement by action; history |  `shell/noctalia/`  | Noctalia, KDE effects | HISTORICAL / PATCHES | Do not replace current cumulative variant by accident |
|  [app-icon-reordering](../ricy-kit/contributions/app-icon-reordering/README.md)  | Cumulative reference variant: ordering/icons/actions |  `shell/noctalia/`  | Pinned Noctalia 5.2.1, Meson/Ninja/C++, KWin | ACTIVE deployed variant; MIGRATE source revision / PATCHES | Rebuild and separate activation; preserve rollback |
|  [window-fade-expand](../ricy-kit/contributions/window-fade-expand/README.md)  | Current animation ricywindowactions and Scale |  `compositor/kwin/`  | KWin script API, PyQt6 for testing | ACTIVE / RICY-OWNED derivative KDE | Change shared effects with Plasma |
|  [blur-continuity](../ricy-kit/contributions/blur-continuity/README.md)  | ricyblur derived from upstream blur |  `compositor/kwin/`  | KWin 6.7.5/headers, Qt/KF6, C++ | UNKNOWN / PATCHES | Registered unit failed; native blur loaded; preserve ABI/fallback |
|  [dolphin-noctalia-identity](../ricy-kit/contributions/dolphin-noctalia-identity/README.md)  | Theme/QSS and Launcher Dolphin, FileManager1 |  `integrations/kde/ + themes/`  | Dolphin, Kvantum, helper Qt | ACTIVE / RICY-OWNED + derived themes | High: access to files in recovery |
|  [dolphin-blur-corners](../ricy-kit/contributions/dolphin-blur-corners/README.md)  | Helper Qt and Dolphin Corner Effect |  `integrations/kde/ + compositor/kwin/`  | Qt, Kvantum, ABI KWin | ACTIVE (split) / RICY-OWNED + KDE derivative | Incompatible plugin may affect Dolphin |
|  [dolphin-deb-rpm-installer](../ricy-kit/contributions/dolphin-deb-rpm-installer/README.md)  | Local DEB/RPM integration with conversion and UI |  `integrations/kde/ + installer/`  | Dolphin, PyQt6, debtap, pkexec/pacman | ACTIVE / RICY-OWNED + upstream dependencies | Do not run installation to test docs |
|  [target-implementation-fixes](../ricy-kit/contributions/target-implementation-fixes/README.md)  | Versioned corrections for preparation of destination |  `installer/`  | Kit Scripts, debtap | MIGRATE (split) / PATCHES + RICY-OWNED | Apply only after checking destination kit |
|  [login-lock-cursor-appearance](../ricy-kit/contributions/login-lock-cursor-appearance/README.md)  | Assets and applicators for SDDM/Plasma/Qt/GTK |  `themes/ + integrations/kde/`  | SDDM, Plasma, Kvantum, fonts and themes | ACTIVE (split) / UPSTREAM assets + RICY-OWNED | High: login/blocking and global settings |
|  [login-matched-lock-screen](../ricy-kit/contributions/login-matched-lock-screen/README.md)  | Log-in lock adaptation |  `themes/ + integrations/kde/`  | KDE/Breeze installed, SDDM | ACTIVE / PATCHES / derivative assets | High: keep usable unlocking |
|  [konsole-animated-cursor](../ricy-kit/contributions/konsole-animated-cursor/README.md)  | Terminal profile and palette |  `themes/ + integrations/kde/`  | Konsole, Kvantum | ACTIVE / RICY-OWNED configuration | Terminal should remain available for diagnosis |
|  [keyboard-cedilla](../ricy-kit/contributions/keyboard-cedilla/README.md)  | XCompose composition and Brave adaptation |  `integrations/`  | Layout/XCompose, optional Brave | ACTIVE / RICY-OWNED | Preserve text entry and preferences |
|  [noctalia-language-and-localization](../ricy-kit/contributions/noctalia-language-and-localization/README.md)  | Shell language/region/weather |  `shell/noctalia/ + integrations/`  | Noctalia, locale, systemd units | ACTIVE / RICY-OWNED | Do not globalize installation preferences |
|  [noctalia-visual-identity](../ricy-kit/contributions/noctalia-visual-identity/README.md)  | Tokens and board of existing identity |  `themes/tokens/`  | Config/palette/Style Noctalia and visual contributions | ACTIVE reference / RICY-OWNED reference | No installation; visual differences need to be recorded |
|  [driver-aic8800](../ricy-kit/contributions/driver-aic8800/README.md)  | USB Wi-Fi/Bluetooth Driver and DKMS package |  `integrations/hardware/`  | Kernel/headers, DKMS, Radxa source fixed | ACTIVE on this hardware / UPSTREAM + patches + Ricy packaging | Risk of losing network; hardware dependency, not every session |

## Entry points and cross-cutting components

| Current component/location | Responsibility | Destination | Dependencies | Class / evidence | Recovery |
|---|---|---|---|---|---|
|  [Root wrappers](../start.sh), [come back](../return.sh), [switch](../switch.sh)  | Entry points for this installation | core/ (to be evaluated) | Absolute path of the kit | ACTIVE start/switch; RECOVERY return / RICY-OWNED | Do not move without revising callers |
|  [prepare-environment.py](../ricy-kit/prepare-environment.py), outputs/ | Preparation and seeds/templates; you can create private backups | installer/ + integrations/ | Python and destination settings | HISTORICAL root recipe; see audit | Do not execute on active kit to validate structure |
|  [generate-kvantum-variant.py](../ricy-kit/generate-kvantum-variant.py)  | Qt style variant | themes/ | Kvantum/existing theme | HISTORICAL generator; selected theme assets ACTIVE elsewhere | Shared style with recovery |
|  [Transport kit](ricy-kit/AGENTS.md) and archives/ | Reproduction/historical | installer/ and historical file after audit | Manifests, scripts and licenses | HISTORICAL; UNKNOWN publication readiness | Do not copy active installation status |
| KWin / Plasma / Dolphin | Compositor, shared desktop, and files | compositor/kwin/ + recovery/plasma/ | System Packages | ACTIVE infrastructure/desktop; RECOVERY packages/tools | Unremovable |
|  [Ricy Files](../apps/file-manager/README.md)  | Future Ricy Standard Manager | apps/file-manager/ | UNKNOWN: toolkit/contracts | UNKNOWN implementation; PLANNED / RICY-OWNED | Dolphin remains available |
|  [Core](../core/AGENTS.md) / [Services](../services/AGENTS.md)  | Future common limits; current services are in the contributions | core/ + services/ | UNKNOWN: new contracts | UNKNOWN implementation; PLANNED | Do not create new daemon/IPC by assumption |

Classes have part-level overrides in the [audit](CONTRIBUTION-AUDIT.md): notably
notification's historical build/current activator, reordering's deployed/source
variants, and the appearance bundle's three independent KWin extensions.
No contribution is classified REMOVE. UNKNOWN does not authorize deletion.

Read [migration](MIGRATION-PLAN.md) before relocating any component. Read
[RECOVERY](RECOVERY.md) for operations that affect session, login or files.
