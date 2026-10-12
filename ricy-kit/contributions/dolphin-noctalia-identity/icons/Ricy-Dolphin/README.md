# Ricy Dolphin chrome overlay

Only selected action names are provided. Native KDE/Breeze supplies folders,
files, MIME, thumbnails/previews, applications, Places, storage/device state,
mount/unmount and MTP assets. No content directory or copied Breeze payload is
included. The theme inherits breeze-dark, breeze and hicolor; it is hidden from
normal theme selection and the helper chooses it only within Dolphin.

## Mapping and provenance

The installed Noctalia5.2.1 GlyphRegistry resolves named Tabler glyphs from its
font/JSON resources. Its `close` alias resolves to `x`, and `add` to `plus`;
these aliases are not KDE icon names. Application icons use separate XDG
providers. Noctalia's other state/own assets are not copied into this overlay.
Exact font-outline equality with the SVG release is UNKNOWN; naming, source,
semantic meaning and Tabler outline language are established.

All SVGs come from Tabler v3.35.0, commit
`147130cd0e67a9cfc70538f8b3a14a48a695d90b`, licensed MIT by Paweł Kuna.
[provenance.json](provenance.json) records each pinned upstream URL and source/
adapted SHA-256; [LICENSE](LICENSE) retains the complete upstream notice.
Only KDE filenames and ColorScheme-Text CSS were adapted. Original24x24 geometry,
2px stroke, round caps/joins and transparent fill remain. KDE's native icon engine
handles palette/modes and native control sizes; SVG boxes do not change hit areas.

| Dolphin action | Current KDE name | Noctalia/Tabler equivalent | Source / fallback |
|---|---|---|---|
| Back | go-previous | arrow-left | Pinned Tabler SVG / Breeze |
| Forward | go-next | arrow-right | Pinned Tabler SVG / Breeze |
| Up | go-up | arrow-up | Pinned Tabler SVG / Breeze |
| Refresh | view-refresh | refresh | Pinned Tabler SVG / Breeze |
| Search | edit-find | search | Pinned Tabler SVG / Breeze |
| Hamburger menu | application-menu | menu-2 | Pinned Tabler SVG / Breeze |
| Split / open in split | view-split-left-right | layout-columns | Pinned Tabler SVG / Breeze |
| Close Tab menu action | document-close | close alias → x | Pinned Tabler SVG / Breeze |
| Native close actions | dialog-close | close alias → x | Pinned Tabler SVG / Breeze |
| New Tab / open in new tab | tab-new | add alias → plus | Pinned Tabler SVG / Breeze |
| Icons mode | view-list-icons | layout-grid | Pinned Tabler SVG / Breeze |
| Compact mode | view-list-details | columns-3 | Pinned Tabler SVG / Breeze |
| Details mode / view settings | view-list-tree | list-details | Pinned Tabler SVG / Breeze |
| Tab's native close control | Qt/Kvantum standard close glyph | Existing geometric x | Native style retained; its layout/signals are unchanged |
| Breadcrumb/dropdowns | Qt primitive/helper chevrons and QSS menu arrow | Existing geometric chevrons | Native/scoped paint retained; no icon-name substitution |
| Tab overflow arrows | Qt/Kvantum arrow primitives | Existing arrows | Native RTL/overflow behavior retained |
| Home/Recent/Trash/Devices | Native Places/Solid names and state assets | No replacement | KDE providers retained |

Names shared by equivalent native menu actions intentionally share the same
meaning. Other names fall through the inherited native themes. No semantic
mapping is invented for unrelated actions. Existing Qt/Kvantum primitive glyphs
remain rather than replacing an already approved small-control geometry.

## Scoping and fallback

The existing Qt helper is already filtered to applicationName=dolphin. At startup
it checks the optional native KIconTheme's validity, then uses the process-local
KIconTheme override and reconfigures the existing KIconLoader. KDE documents that
[API](https://api.kde.org/kicontheme.html) for precise theme expectations; its
historical forceThemeForTests name does not write configuration. The override
persists across native loader reconfiguration in that process only. The helper
links Dolphin's existing KF6IconThemes library; headers are build prerequisites.
No global settings, dolphinrc theme key, wrapper/default or shell dependency is
introduced. The rejected dolphinrc selection did not provide a sufficient
missing-theme fallback and was undone before final validation.

Absent/invalid overlay → keep current native system theme (breeze-dark on the
validated desktop). Missing individual names → native inherited theme. A Qt
helper failure still has the preexisting manual upstream fallback; this pass
does not claim independent failure Recovery or repair the existing shutdown139.

Install only this phase with `python3 -B ricy-kit/contributions/dolphin-noctalia-identity/apply-icons.py`.
The full existing identity applicator also backs up/installs this overlay for
explicit later reproduction. Neither installer selects a global theme. Use the
printed manifest with the existing `apply.py --restaurar BACKUP`, then reopen
Dolphin. Existing processes retain their mapped helper/loaded theme.

Offline check: `python3 -B ricy-kit/contributions/dolphin-noctalia-identity/validate-icons.py`.
See [live phase evidence and limits](../../../../../docs/DOLPHIN-BASELINE.md#identity--motion-pass--phase-2-iconography--2026-10-11).
