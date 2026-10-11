# Incremental migration

## Current structure — KNOWN
- Root: README and wrappers with absolute paths to the active kit.
- `ricy-kit/`: contributions, outputs/scripts, demonstrations and installation materials.
- `docs/ricy-kit/`: preserved transportable variant; it is not automatic mirror.
- `docs/ricy.md`, `REINSTALL.md`, `VISUAL-IDENTITY.md`: history and references.
- `archives/ricy.zip`: preserved original file; later local Git selection is
  documented in [GIT-BASELINE](GIT-BASELINE.md).

Sources and dependencies per contribution are in [COMPONENTS](COMPONENTS.md).
[CONTRIBUTION-AUDIT](CONTRIBUTION-AUDIT.md) grounds all 24 contributions, consumers,
part-level roles and cumulative variants. It does not authorize relocation or
removal. The foundation created documentary directories and validators; it did
not relocate runtime.

The later [token-centralization decision](adr/0005-consumable-visual-tokens.md)
implements the canonical JSON source in [themes/tokens](../themes/tokens/README.md).
Only the offline identity board consumes it so far, with exact before/after
bytes. Existing runtime sources and transport snapshots remain in place;
application/toolkit and desktop consumer migrations remain PLANNED.

Grounding gates: current RICY-001 source is not deployed (G-02); blur-continuity
has a failed registered consumer and UNKNOWN disposition (G-03); exact compiled
Dolphin-helper provenance and individual private plugin consumers remain UNKNOWN.
Preserve these limits before selecting migration inputs. MIGRATE tooling and
PLANNED destinations do not imply that a move, activation, or new contract has
been approved. No contribution currently has sufficient evidence for REMOVE.

## Target structure — PLANNED
| Current | Destination expected | Condition before migration |
|---|---|---|
| Patches Noctalia and public profile | shell/noctalia/ | Identify cumulative variant and consumers; do not transport private profile |
| Blur/ricywindowactions/corners | compositor/kwin/ | Preserve version/ABI, licenses, build/install/reversion |
| Theme Tokens and Assets | themes/ and themes/tokens/ | Canonical JSON and offline board consumption implemented; runtime/assets require individual migration while maintaining values and appearance |
| Search/ Shortcuts Adapter/KDE/Dolphin | integrations/kde/ | Map D-Bus, units, desktops and paths in both kits |
| Autostart and integration units | services/ | Preserve order/readiness, names and return policy |
| Alternance and snapshots | recovery/plasma/ | Validate restoration and reduce Ricy dependency without losing panels |
| Preparation/applicators | installer/ | Separate public backup/state materials by allowlist |
| AIC8800 Driver | integrations/hardware/ | Keep optional, pin/licenses and kernel support |
| Common wrappers/helpers | core/ if justified | Find real duplication; do not create framework |
| No current Files application | apps/file-manager/ | New implementation proposal, approved toolkit/contracts |
| Checks of this step | scripts/ | Keep offline; tools/ only for needed tools |

## Safe migrations
Documenting borders, adding rules/links and read-only tests are safe at this stage. Consolidating references can precede movement of sources. Even a seemingly simple change of path requires search for callers. Before each migration: inventory → references → backup → minimum change → appropriate validation → update of affected docs/manifests → clear rollback.

## Risky migrations — not executed
Rename contributions/outputs; unify kits; move profiles/snapshots; change paths recorded in drives, symlinks, desktop entries and wrappers; reorganize cumulative patches; change activators; separate Plasma/Noctalia session; remove Dolphin; exchange login manager. Require own plan and recovery tests. Do not regenerate historical SHA256SUMS to disguise installation divergences.

## Deprecated Concepts — Preserved as History
Names `noctalia-teste.service`/`start-test.sh` do not mean temporary session today. “Transport configuration” remains useful for playback, but no longer defines the whole product. Previous cumulative compilers remain historical. Inherited workspaces do not define future experience. No files have been removed because it appears obsolete.

## Migration order
1. Audit RICY-001 in configs, UI, menus, shortcuts and gestures, distinguishing API KWin
of exposure to the user; propose minimum adjustment without altering fallback.
2. Inventory references and prepare revised public baseline: sources/licenses,
portable path, absence of private data; choose versioning before publishing.
3. Centralize consumption of tokens, one component at a time, with visual comparison.
4. Extract patches/builds and component integrations with path compatibility.
5. Design Plasma Recovery isolation and only then an independent Ricy session.
6. Propose implementation of Ricy Files by keeping Dolphin as recovery.

## Architecture Decisions Required — Only Blocked Future Parts

ARCHITECTURE DECISION REQUIRED

**Problem:** how to separate the future Ricy session without losing wallpaper/desktop and recovery that today depend on plasmashell and Ricy scripts?

**Evidence:**  `plasma-noctalia-switching/integration.py` keeps plasmashell, uses D-Bus/KGlobalAccel and reads Ricy snapshots when restoring. View
[ARCHITECTURE C-002](ARCHITECTURE.md) and [RECOVERY](RECOVERY.md).

**Options:** A. conserve the current integration while specifying and testing an independent route; B. create dedicated sessions and set wallpaper ownership, login and recovery before migrating.

**Recommended:** A in this foundation; draw up comparative proposal before B.

**Impact:** units, login, wallpaper, shortcuts, compositor and return after crash. Runtime separation is PLANNED and is not implemented without explicit approval. The already requested documentary reservation remains valid and independent of this decision.
