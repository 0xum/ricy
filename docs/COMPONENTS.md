# Components

KNOWN means presence and responsibility verified in the cited files; not Runtime certification in this task. All destinations are PLANNED. Ownership indicates maintenance, preserving upstream licenses. Each current link leads to local README.

The root `ricy-kit/` is active; `docs/ricy-kit/` preserves the transport variant. Read [kit rules](../ricy-kit/AGENTS.md) before editing. Replicas are not interchangeable sources. Noctalia patch cycle is cumulative: the most recent registered reference is app-icon-reordering, with window-fade-expand for windows.

| Current component/location | Responsibility | Future destination | Dependencies | Status / ownership | Impact on recovery |
|---|---|---|---|---|---|
|  [noctalia-kde-integration-and-menus](../ricy-kit/contributions/noctalia-kde-integration-and-menus/README.md)  | Qt search, profile, shortcuts and menus adapter |  `integrations/kde/ + services/ + themes/`  | Noctalia, PyGObject, D-Bus, KGlobalAccel, Kvantum | KNOWN / RICY-OWNED + derivative assets | High: shortcuts, wallpaper and shared style |
|  [noctalia-autostart](../ricy-kit/contributions/noctalia-autostart/README.md)  | Shell units, search and integration in login |  `services/ + installer/`  | user systemd, Plasma, integration | KNOWN / RICY-OWNED | High: start only after readiness; Plasma return |
|  [plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md)  | Ricy command, snapshots and panel restoration |  `recovery/plasma/ + integrations/kde/`  | systemd, Python/PyGObject, qdbus6, flock, KGlobalAccel | KNOWN / RICY-OWNED | Critical: current return path |
|  [notification-continuity](../ricy-kit/contributions/notification-continuity/README.md)  | Local binary notification patch and activator |  `shell/noctalia/`  | Pinned Noctalia, integration, blur | KNOWN / PATCHES + RICY-OWNED | Preserve /usr/bin/noctalia, backup and apps |
|  [taskbar-menu-composition](../ricy-kit/contributions/taskbar-menu-composition/README.md)  | Fitted app menu; cumulative historical variant |  `shell/noctalia/`  | Noctalia and previous patches | KNOWN / PATCHES | Shell crash risk; maintain activator/reversion |
|  [tray-menu-composition](../ricy-kit/contributions/tray-menu-composition/README.md)  | DBusMenu Menus Fitted; Historical Variation |  `shell/noctalia/`  | Noctalia, DBusMenu | KNOWN / PATCHES | Actions belong to the applications; do not change without validation |
|  [app-icon-interactions](../ricy-kit/contributions/app-icon-interactions/README.md)  | Hover/Icon scale; historical variant |  `shell/noctalia/`  | Noctalia Style | KNOWN / PATCHES | Do not change hit area or session control |
|  [taskbar-app-actions](../ricy-kit/contributions/taskbar-app-actions/README.md)  | Focus/minimization/closing by UUID; historical |  `shell/noctalia/ + integrations/kde/`  | KWin and Noctalia API | KNOWN / PATCHES | Tests should not close user work |
|  [app-indicator-animations](../ricy-kit/contributions/app-indicator-animations/README.md)  | Indicators and previous window animation |  `shell/noctalia/ + compositor/kwin/`  | Noctalia and KWin | KNOWN / PATCHES + KDE derivative | Previous variant; do not apply on the current |
|  [app-icon-states](../ricy-kit/contributions/app-icon-states/README.md)  | Icon movement by action; history |  `shell/noctalia/`  | Noctalia, KDE effects | KNOWN / PATCHES | Do not replace current cumulative variant by accident |
|  [app-icon-reordering](../ricy-kit/contributions/app-icon-reordering/README.md)  | Cumulative reference variant: ordering/icons/actions |  `shell/noctalia/`  | Pinned Noctalia 5.2.1, Meson/Ninja/C++, KWin | KNOWN / PATCHES | Rebuild and separate activation; preserve rollback |
|  [window-fade-expand](../ricy-kit/contributions/window-fade-expand/README.md)  | Current animation ricywindowactions and Scale |  `compositor/kwin/`  | KWin script API, PyQt6 for testing | KNOWN / RICY-OWNED derivative KDE | Change shared effects with Plasma |
|  [blur-continuity](../ricy-kit/contributions/blur-continuity/README.md)  | ricyblur derived from upstream blur |  `compositor/kwin/`  | KWin 6.7.5/headers, Qt/KF6, C++ | KNOWN / PATCHES | Critical ABI; do not replace compositor |
|  [dolphin-noctalia-identity](../ricy-kit/contributions/dolphin-noctalia-identity/README.md)  | Theme/QSS and Launcher Dolphin, FileManager1 |  `integrations/kde/ + themes/`  | Dolphin, Kvantum, helper Qt | KNOWN / RICY-OWNED + derived themes | High: access to files in recovery |
|  [dolphin-blur-corners](../ricy-kit/contributions/dolphin-blur-corners/README.md)  | Helper Qt and Dolphin Corner Effect |  `integrations/kde/ + compositor/kwin/`  | Qt, Kvantum, ABI KWin | KNOWN / RICY-OWNED + KDE derivative | Incompatible plugin may affect Dolphin |
|  [dolphin-deb-rpm-installer](../ricy-kit/contributions/dolphin-deb-rpm-installer/README.md)  | Local DEB/RPM integration with conversion and UI |  `integrations/kde/ + installer/`  | Dolphin, PyQt6, debtap, pkexec/pacman | KNOWN / RICY-OWNED + upstream dependencies | Do not run installation to test docs |
|  [target-implementation-fixes](../ricy-kit/contributions/target-implementation-fixes/README.md)  | Versioned corrections for preparation of destination |  `installer/`  | Kit Scripts, debtap | KNOWN / PATCHES + RICY-OWNED | Apply only after checking destination kit |
|  [login-lock-cursor-appearance](../ricy-kit/contributions/login-lock-cursor-appearance/README.md)  | Assets and applicators for SDDM/Plasma/Qt/GTK |  `themes/ + integrations/kde/`  | SDDM, Plasma, Kvantum, fonts and themes | KNOWN / UPSTREAM assets + RICY-OWNED | High: login/blocking and global settings |
|  [login-matched-lock-screen](../ricy-kit/contributions/login-matched-lock-screen/README.md)  | Log-in lock adaptation |  `themes/ + integrations/kde/`  | KDE/Breeze installed, SDDM | KNOWN / PATCHES / derivative assets | High: keep usable unlocking |
|  [konsole-animated-cursor](../ricy-kit/contributions/konsole-animated-cursor/README.md)  | Terminal profile and palette |  `themes/ + integrations/kde/`  | Konsole, Kvantum | KNOWN / RICY-OWNED configuration | Terminal should remain available for diagnosis |
|  [keyboard-cedilla](../ricy-kit/contributions/keyboard-cedilla/README.md)  | XCompose composition and Brave adaptation |  `integrations/`  | Layout/XCompose, optional Brave | KNOWN / RICY-OWNED | Preserve text entry and preferences |
|  [noctalia-language-and-localization](../ricy-kit/contributions/noctalia-language-and-localization/README.md)  | Shell language/region/weather |  `shell/noctalia/ + integrations/`  | Noctalia, locale, systemd units | KNOWN / RICY-OWNED | Do not globalize installation preferences |
|  [noctalia-visual-identity](../ricy-kit/contributions/noctalia-visual-identity/README.md)  | Tokens and board of existing identity |  `themes/tokens/`  | Config/palette/Style Noctalia and visual contributions | KNOWN / RICY-OWNED reference | No installation; visual differences need to be recorded |
|  [driver-aic8800](../ricy-kit/contributions/driver-aic8800/README.md)  | USB Wi-Fi/Bluetooth Driver and DKMS package |  `integrations/hardware/`  | Kernel/headers, DKMS, Radxa source fixed | KNOWN / UPSTREAM + patches + Ricy packaging | Risk of losing network; hardware dependency, not every session |

## Entry points and cross-cutting components

| Current component/location | Responsibility | Destination | Dependencies | Status | Recovery |
|---|---|---|---|---|---|
|  [Root wrappers](../start.sh), [come back](../return.sh), [switch](../switch.sh)  | Entry points for this installation | core/ (to be evaluated) | Absolute path of the kit | KNOWN / RICY-OWNED | Do not move without revising callers |
|  [prepare-environment.py](../ricy-kit/prepare-environment.py), outputs/ | Preparation and seeds/templates; you can create private backups | installer/ + integrations/ | Python and destination settings | KNOWN / RICY-OWNED | Do not execute on active kit to validate structure |
|  [generate-kvantum-variant.py](../ricy-kit/generate-kvantum-variant.py)  | Qt style variant | themes/ | Kvantum/existing theme | KNOWN | Shared style with recovery |
|  [Transport kit](ricy-kit/AGENTS.md) and archives/ | Reproduction/historical | installer/ and historical file after audit | Manifests, scripts and licenses | KNOWN: presence; UNKNOWN: full secure publication | Do not copy active installation status |
| KWin / Plasma / Dolphin | Compositor, shared desktop, and files | compositor/kwin/ + recovery/plasma/ | System Packages | KNOWN: code dependency; external upstream | Unremovable |
|  [Ricy Files](../apps/file-manager/README.md)  | Future Ricy Standard Manager | apps/file-manager/ | UNKNOWN: toolkit/contracts | PLANNED / RICY-OWNED | Dolphin remains available |
|  [Core](../core/AGENTS.md) / [Services](../services/AGENTS.md)  | Future common limits; current services are in the contributions | core/ + services/ | UNKNOWN: new contracts | PLANNED | Do not create new daemon/IPC by assumption |

Read it. [migration](MIGRATION-PLAN.md) before relocating any component. Read
[RECOVERY](RECOVERY.md) for operations that affect session, login or files.
