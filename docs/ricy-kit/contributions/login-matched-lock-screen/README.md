# Lock with login display

Contribution to Plasma 6.7 and local login `mocha-limine`. Uses the wallpaper configured in SDDM, clock, user and password field of the same Breeze components. The form appears immediately and remains visible for a minute as in login. Media controls are disabled and the password field does not display the password reveal button, following the login theme.

```bash
python apply.py
```

The adaptation only copies the KDE lock installed for a local package of the same ID. The other shell components point to the system files. Authentication, password synchronization, biometrics, virtual keyboard, and bug handling continue using native implementation. SDDM is not modified. The script interrupts before writing if there is another local shell or QML has changed. After updating Plasma, reapply to use your new lock.

Private backup stays in `~/.local/state/ricy-lockscreen-backups/`To come back:

```bash
python restore.py /caminho/do/backup/informado
```

Preview without blocking the session: `/usr/lib/kscreenlocker_greet --testing`. In the normal session, the change is worth the next lock. Session buttons remain appropriate for an already open session; there is no disengagement or choice of SDDM session within the lock.

Scripts from this contribution: MIT. Generated QMLs keep their original KDE license notices (GPL-2.0-or-later / LGPL-2.0- or-later).

## Authentication startup correction (08/10/2026)

The field is visible through a transition of `uiVisible` after mounting the QML (`Qt.callLater`), preserving the initial state `false` KDE. Start directly with `true` It prevented the shooting of `onUiVisibleChanged`, which initiates authentication; the form appeared, but the password was not processed.

The regression was reproduced in a temporary copy of the previous version: no login and timeout. The corrected version passed through the native form to the actual PAM (`kde`): result 0 / Success and output of the greeter. The modes were exercised immediately and with tolerance of 1200 ms, in `--testing`, with offscreen rendering, without blocking the session. The password was provided only by a memory descriptor without entering the kit or logs.
