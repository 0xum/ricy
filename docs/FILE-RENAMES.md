# English file names

Project files use en-US names. This map records the October 11, 2026 rename
in the repository root and both the active and transport kits. Directory names
were already in English. References, Python imports, launchers, and installers
use the new file names.

## Compatibility and recovery

Existing installed systemd unit IDs and private backup/state paths remain
unchanged so recovery can locate existing snapshots. English-named service
templates explicitly map to the existing installed unit IDs. No service was
restarted and no session migration was performed. Five installed unit/launcher
files had absolute references to renamed repository scripts. Those references
were updated after saving private copies under
`$HOME/.local/state/ricy-file-rename-backups/`; systemd configuration was reloaded
without restarting services. Other installations require their own reference
updates or a deliberate reinstall following the contribution's recovery instructions.

Historical SHA256SUMS files retain their original path labels and digests as
provenance. They describe the original snapshot, not the renamed/translated
working tree; use this map to locate current names. Operational correction
manifests use current paths and replacement digests.

## Refreshing already registered launchers

Updating a `.desktop` file and rebuilding the application database with
`kbuildsycoca6 --noincremental` does not refresh a launcher already retained by
KWin's embedded KGlobalAccel. The menu shortcut continued to execute the old
`open-menu.sh` predecessor even though the installed desktop entry was correct.
KGlobalAccel's [service-action component](https://github.com/KDE/kglobalacceld/blob/master/src/kserviceactioncomponent.cpp)
retains the service object used for launching.

For this installation, the menu component was recreated through its D-Bus
`cleanUp` method, followed by `doRegister`. Before cleanup, its active shortcuts
and defaults were captured in a private backup under
`$HOME/.local/state/ricy-launcher-refresh-backups/`. Both were restored and
compared with the snapshot: Super and Super+Space remained active, with
Super+Space as the default. Unregistering only the action did not refresh the
retained service object and was insufficient.

The registered `_launch` action was then invoked through D-Bus. Noctalia
reported `activePanelId=launcher`; no new missing-program error appeared in
the journal. KWin, Noctalia, and the session were not restarted. For another
installation, capture and preserve its own shortcut assignments rather than
applying this installation's values. This verifies menu activation, not full
login or crash recovery.

## Name mapping

The mapping applies wherever the original basename occurred in either kit.

| Original name | Current name |
|---|---|
| `IDENTIDADE-VISUAL.md` | `VISUAL-IDENTITY.md` |
| `KDE-Atual.json` | `KDE-Current.json` |
| `REINSTALAR.md` | `REINSTALL.md` |
| `abrir-clipboard.sh` | `open-clipboard.sh` |
| `abrir-menu.sh` | `open-menu.sh` |
| `alternar.sh` | `switch.sh` |
| `aplicar-animacoes.py` | `apply-animations.py` |
| `aplicar-brave.py` | `apply-brave.py` |
| `aplicar-correcoes.py` | `apply-fixes.py` |
| `aplicar-estilo.sh` | `apply-style.sh` |
| `aplicar-wallpaper.sh` | `apply-wallpaper.sh` |
| `aplicar.py` | `apply.py` |
| `ativar-busca-noctalia.sh` | `enable-noctalia-search.sh` |
| `ativar-cantos.py` | `enable-corners.py` |
| `ativar.py` | `enable.py` |
| `atualizar-indices.sh` | `update-indexes.sh` |
| `blur-continuidade.patch` | `blur-continuity.patch` |
| `busca-desktop.py` | `desktop-search.py` |
| `codex-noctalia-recuperar.desktop` | `codex-noctalia-recover.desktop` |
| `codex-noctalia-voltar.desktop` | `codex-noctalia-return.desktop` |
| `compilar-ui.py` | `build-ui.py` |
| `compilar.py` | `build.py` |
| `compilar.sh` | `build.sh` |
| `comum.py` | `common.py` |
| `configurar-clipboard.py` | `configure-clipboard.py` |
| `configurar-super.py` | `configure-super.py` |
| `configurar-super.py.patch` | `configure-super.py.patch` |
| `debtap-alteracoes.patch` | `debtap-changes.patch` |
| `gerar-variante-kvantum.py` | `generate-kvantum-variant.py` |
| `greeter-preferencias.json` | `greeter-preferences.json` |
| `iniciar-automatico.sh` | `start-automatically.sh` |
| `iniciar-teste.sh` | `start-test.sh` |
| `iniciar.py` | `start.py` |
| `iniciar.sh` | `start.sh` |
| `instalar-inicio-automatico.py` | `install-autostart.py` |
| `instalar-integracao.py` | `install-integration.py` |
| `instalar.py` | `install.py` |
| `integracao.py` | `integration.py` |
| `integrar.py` | `integrate.py` |
| `lancar.py` | `launch.py` |
| `noctalia-busca-desktop.service.in` | `noctalia-desktop-search.service.in` |
| `noctalia-teste.service.in` | `noctalia-test.service.in` |
| `notificacao-canto-direito.patch` | `notification-right-corner.patch` |
| `paineis.py` | `panels.py` |
| `preferencias-kwin.json` | `kwin-preferences.json` |
| `preferencias.json` | `preferences.json` |
| `preparar-ambiente.py` | `prepare-environment.py` |
| `preparar-destino.py` | `prepare-destination.py` |
| `recarregar-estilo.py` | `reload-style.py` |
| `recuperar-no-login.sh` | `recover-at-login.sh` |
| `referencia.svg` | `reference.svg` |
| `restaurar-estilo-e-blur.py` | `restore-style-and-blur.py` |
| `restaurar-estilo-kde.sh` | `restore-kde-style.sh` |
| `restaurar-instalacao.py` | `restore-installation.py` |
| `restaurar-integracao.py` | `restore-integration.py` |
| `restaurar.py` | `restore.py` |
| `ricy-noctalia-integracao.service.in` | `ricy-noctalia-integration.service.in` |
| `sincronizar-wallpaper.py` | `sync-wallpaper.py` |
| `sistema.py` | `system.py` |
| `usuario.py` | `user.py` |
| `validar-acoes.py` | `validate-actions.py` |
| `validar-arraste-nativo.cpp` | `validate-native-drag.cpp` |
| `validar-arraste-nativo.py` | `validate-native-drag.py` |
| `validar-indicador.py` | `validate-indicator.py` |
| `validar-motion.cpp` | `validate-motion.cpp` |
| `validar-motion.py` | `validate-motion.py` |
| `validar-ordem.cpp` | `validate-order.cpp` |
| `validar-ordem.py` | `validate-order.py` |
| `validar.py` | `validate.py` |
| `verificar-menu-nativo.py` | `verify-native-menu.py` |
| `verificar.py` | `verify.py` |
| `versoes-observadas.txt` | `observed-versions.txt` |
| `voltar-ao-plasma.sh` | `return-to-plasma.sh` |
| `voltar.sh` | `return.sh` |
