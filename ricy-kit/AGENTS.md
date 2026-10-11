# Active kit

Consult [COMPONENTS](../docs/COMPONENTS.md) to locate ownership/boundaries and
[DEVELOPMENT](../docs/DEVELOPMENT.md) to select checks. Follow only the rules below
relevant to the task's files/impact. Do not move outputs, contributions, or
templates without mapping units, wrappers, absolute paths, and backups.

Use [CONTRIBUTION-AUDIT](../docs/CONTRIBUTION-AUDIT.md) for current consumers and
part-level classifications. An active kit contains historical files; the current
source patch is not necessarily the deployed binary. UNKNOWN is not permission
to remove or replace a contribution.

For normal development/build, use the source selection in
[DEVELOPMENT](../docs/DEVELOPMENT.md#historical-reproduction). Historical builders
require deliberate opt-in and an isolated source; do not bypass guards or run
transport copies to rebuild the current installation. Notification enable/restore,
switching wrappers, and backups remain current consumers even beside old patches.

- Noctalia shell/profile/patch: [shell rules](../shell/AGENTS.md).
- Effects/blur/ABI: [compositor rules](../compositor/AGENTS.md).
- Search, shortcuts, Dolphin, and KDE: [integrations](../integrations/AGENTS.md).
- Tokens/themes/QSS: [themes](../themes/AGENTS.md).
- Switching/panels: [recovery](../recovery/AGENTS.md).
- Destination preparation/applicators: [installer](../installer/AGENTS.md).

Cumulative Noctalia variants do not form a sequence of patches to apply together.
The active kit's profile, work, backups, and state are not publication material.
SHA256SUMS is historical: do not regenerate it merely to hide installation changes.
New AGENTS files are development metadata, outside the original manifest.
