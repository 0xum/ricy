# ADR-0009 — Nonpurging Ricy Files trash mutation

Status: **Superseded** — closed2026-10-11 by [ADR-0011](0011-dolphin-as-ricy-file-manager.md).

Approval evidence: the user approved the bounded native send-to-trash adapter,
required Freedesktop semantics, no purging/replacement, collision-safe names,
symlink/mount/permission/error/cancellation tests and safe-only rollback. The
user authorized finalizing milestone 08 and proceeding sequentially to 09 and 10.
KIO retains its other approved responsibilities; no new filesystem framework or
default/FileManager1/Dolphin/Plasma/session integration change is authorized.


> Historical record only. The separate application was explored and a prototype
> was produced, then retired before taking on file operations, Trash, devices
> and FileManager1. The user chose Dolphin to reduce infrastructure scope.
> Earlier approvals/proposals below no longer authorize implementation.

## Context

[ADR-0008](0008-ricy-files-technical-architecture.md) is Accepted. Its assessment
selected reuse of the KIO trash worker. Milestone 08's explicit destructive-safety
investigation found that KIO 6.30 `adaptTrashSize()` reads `ktrashrc` and may
permanently delete existing trash entries under time/size cleanup policies.
An ordinary trash request can affect unrelated data even without a Files Delete
or Empty Trash action. No inspected public per-job flag disables that policy.
Evidence: [pinned KIO source](https://github.com/KDE/kio/blob/v6.30.0/src/kioworkers/trash/trashimpl.cpp#L1160).

Qt's existing `QFile::moveToTrash` avoids those KIO policies, but the inspected
Qt 6.12 implementation reserves metadata exclusively then uses replace-capable
payload `renameat`. It can replace an orphan payload lacking matching metadata.
Its hardlink path also does not check source unlink success before returning
true, and metadata short writes need reconciliation. It cannot be represented
as an unconditional no-replace backend merely by adding a preflight check.
Evidence: [pinned Qt source](https://github.com/qt/qtbase/blob/v6.12.0/src/corelib/io/qfilesystemengine_unix.cpp#L1515),
[documented volume limits](https://doc.qt.io/qt-6/qfile.html#moveToTrash).

No user cleanup settings or trash contents were inspected or changed. These are
source-level capabilities, not evidence of this user's policy or data loss.
[FILES-MVP](../history/ricy-files/FILES-MVP.md) requires nonpurging, nonreplacement and explicit
partial/uncertain outcomes. ADR-0007 remains Proposed; it supplies no accepted
session/default contract or authorization for a new worker topology.

## Decision

Use one bounded Ricy-owned native Freedesktop trash mutation adapter inside
the existing OperationsService. Retain Qt Quick/C++, KIO directory/trash listing
and appropriate jobs, Solid devices, module ownership and central tokens from
ADR-0008. Do not add a daemon, IPC, patched worker, global setting or private trash
format. This increases Ricy's filesystem/backend responsibility and is not
silently treated as already approved by selecting KIO in milestone 07.

The adapter must use [Freedesktop Trash storage](https://specifications.freedesktop.org/trash/1.0/)
and this commit protocol:

1. Validate source entry/held parent, protected targets and mount identity without
   following a source symlink leaf. Choose a writable same-mount home or per-volume
   standard trash location. Check ownership, permissions, sticky-bit policy and
   no-symlink directory traversal using held descriptors. Unsupported subvolume,
   mount or capability fails; no copy/delete fallback.
   Home trash is `$XDG_DATA_HOME/Trash` when a same-mount move is supported. For
   other volumes, use a validated sticky shared `<topdir>/.Trash/<uid>` when
   available, otherwise a validated `<topdir>/.Trash-<uid>`, following the standard
   ownership/permission rules. Never choose an arbitrary private fallback path.
2. Choose one candidate basename for paired `files/` payload and `info/` metadata.
   Reserve `.trashinfo` with exclusive no-follow creation; reject both metadata
   and payload conflicts. Write the exact percent-encoded original path and
   deletion time completely, handling interrupted/short writes and checking
   file/directory flush errors before payload commit. Check close/after-commit
   reconciliation errors too; they cannot retroactively turn a commit into no-op.
   Keep descriptor/identity ownership of this reservation.
   Metadata is UTF-8 ASCII syntax: `[Trash Info]`, `Path=` and `DeletionDate=`
   lines. Percent-encode original native path bytes; home-trash Path is absolute,
   per-volume Path is relative to the mount top directory without `..` traversal.
   Preserve a symlink leaf's lexical path. Use local `YYYY-MM-DDThh:mm:ss` deletion
   time; do not alter the user's clock/time zone or silently canonicalize a link.
3. Honor cancellation before commit. Move the source entry to the held payload
   directory with `renameat2(RENAME_NOREPLACE)`. A late payload/orphan collision
   must fail without replacing it; choose another candidate only after safe
   cleanup of this job's own reservation. Unsupported/EXDEV means failure.
4. Reconcile source absence, committed payload identity and original-path metadata.
   Report success only with established evidence. Metadata/flush/reconciliation
   anomalies after commit produce Partial/Indeterminate, preserve the payload and
   stop the batch; never delete it to repair metadata or automatically undo a
   committed move. Do not promise a two-file atomic transaction/crash rollback.
5. On failure, reconcile first. Remove the verified metadata reservation only
   after establishing that payload commit did not occur; an ambiguous commit
   error is not a precommit failure. Report any cleanup failure/residual. Never delete an existing
   payload or an ambiguous metadata record. No age/size policy or free-space
   cleanup runs; insufficient capacity fails visibly.

Native source rename still is not an atomic compare-and-rename of an expected
source inode. Held parents/revalidation mitigate detected namespace changes;
there is no malicious same-user sandbox guarantee. Destination no-replace and
nonpurging are requirements to verify, not claims of implemented behavior.

Run preparation/commit on an app-owned worker; cancellation occurs before the
commit and between items. Do not kill a thread during a filesystem primitive or
invent mid-commit cancellation, byte progress or rollback. Do not call KIO trash,
Qt trash or permanent delete as fallback. No restore/delete/empty action is added.
Mutation stays unavailable until this ADR is accepted AND disposable storage,
collision, link, permission, partial-error and cancellation tests pass.

## Options

| Option | Benefit | Cost / limit |
|---|---|---|
| A — Bounded native standard-trash adapter, recommended | Explicit nonpurging policy and atomic destination no-replace; existing Linux/C++ process, no settings/helper topology change | Ricy owns location validation, paired metadata protocol, permissions and residual handling; requires careful implementation/review/integration tests |
| B — Existing Qt trash plus checks | Existing dependency and avoids KIO cleanup policy | Checks cannot close replace-capable payload commit or establish every return-value outcome; does not meet the unconditional no-replace contract |
| C — Proven isolated/patched KIO worker | Could preserve more KIO operation behavior | No proven per-job isolation; worker/config/service lifecycle and any patch are additional unapproved decisions; purge/rename semantics still need proof |
| D — Keep trash mutation unavailable | No Files-induced purge while pending | Does not satisfy required MVP Move to Trash; milestone 08/10 remain incomplete |

## Consequences

The exception introduces a small Ricy-owned native mutation capability alongside
KIO inside the already accepted OperationsService. This is additional backend
ownership, not a new general recursive-copy engine. KIO remains the principal
listing/launch/file-service dependency. The MVP Trash view stays read-only.
Storage interoperability needs disposable tests; restore/default/session policy
remains outside this decision. Qt/KDE retain their code/licenses; no upstream
source is copied into the project by this proposal.

## Constraints

Approval permits bounded implementation after the milestone 09 gate. Do not rewrite
`ktrashrc`, XDG locations, MIME/FileManager1 defaults, Dolphin, Plasma Recovery or
private state. No old-entry purge, privilege escalation, deletion fallback,
nonstandard trash format, new daemon/IPC or wholesale filesystem backend.
Approval is permission for bounded implementation and validation, not proof of
race behavior, storage correctness, crash durability or universal volume support.

## Original approval gate — resolved for option A

ARCHITECTURE DECISION REQUIRED

**Problem:** the selected KIO trash path can purge existing contents; the available
Qt substitute still has a replace-capable payload commit. Neither matches the
required nonpurging/no-replace safety contract unchanged.

**Evidence:** pinned KIO 6.30 and Qt 6.12 source reviewed independently; no runtime
mutation or personal-state inspection occurred.

**Options:** A — native standard-trash adapter; B — Qt plus checks; C — separately
approved worker isolation/patch; D — keep mutation disabled and the gate pending.

**Recommended:** A with the bounded commit protocol and mandatory disposable tests.

**Impact:** additional internal trash-backend ownership/testing; accepted
Qt Quick/KIO/Solid boundaries retained, no new daemon/default/session change and
no new dependency for Plasma/Dolphin Recovery.

References: [INVARIANTS](../INVARIANTS.md), [RECOVERY](../RECOVERY.md),
[technical architecture](../history/ricy-files/FILES-TECHNICAL-ARCHITECTURE.md),
[architecture-change](../../.agents/skills/architecture-change/SKILL.md).
