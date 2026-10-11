# apps

Dolphin is the Ricy file manager under [ADR-0011](../docs/adr/0011-dolphin-as-ricy-file-manager.md).
The own Ricy Files application, 07–10 roadmap and exclusive infrastructure are
retired; do not recreate apps/file-manager, an own filesystem/Trash backend,
FileManager1 implementation or a Dolphin fork. Other applications require
explicit approval; Settings remains unapproved.

Dolphin adaptations remain in their existing integration/theme contributions,
not a new app. Preserve directory defaults, MIME, FileManager1, wrappers,
installed settings and Plasma Recovery unless a separate task authorizes changes.
Read [COMPONENTS](../docs/COMPONENTS.md), [RECOVERY](../docs/RECOVERY.md), and the
[component-development skill](../.agents/skills/component-development/SKILL.md)
for actual approved component work.
