# Closed Ricy Files exploration

Status: HISTORICAL, closed 2026-10-11 by explicit user direction and
[ADR-0011](../../adr/0011-dolphin-as-ricy-file-manager.md).

The project explored a separate Qt Quick/C++ file manager and produced a local
browser prototype. It was stopped before assuming file operations, Trash,
devices, FileManager1 and other critical infrastructure responsibilities.
Dolphin is the chosen file manager; no own application or Dolphin fork is planned.

The active checkout had24 tracked files under apps/file-manager at commit
`0fe09c224c62a076c533ad7df464c80a04e64aef`. Code, QML, packaging, CMake, tests
and the exclusive isolated runner are removed from the working state. No local
build directory existed inside that tree. The code was absent from main and
was not merged into it for cleanup. Git history remains unchanged.

`codex/ricy-files-mvp` preserves the exact prototype; the separate browser/UI
branches and worktrees remain unmerged historical work, outside the active
product. They are not continuation targets. No other chat's checkout or private
state was removed. No runtime service/default or installed Dolphin file changed.

- [Prototype record](PROTOTYPE-README.md) — historical commands, not active builds.
- [Integration assessment](FILES-INTEGRATION.md).
- [Technical assessment](FILES-TECHNICAL-ARCHITECTURE.md).
- [MVP and 07–10 gates](FILES-MVP.md) — retired.
- [Build vs Adapt assessment](FILES-BUILD-VS-ADAPT.md) — proposal not accepted.
- [Current Dolphin baseline](../../DOLPHIN-BASELINE.md).
