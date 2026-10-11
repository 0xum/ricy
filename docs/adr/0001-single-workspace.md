# ADR-0001 — Single Workspace

Status: Accepted

## Context

O produto quer uma experiência direta de aplicativos e janelas; a organização herdada do compositor por desktops não deve ditar o modelo mental do Ricy.

## Decision

Adotar RICY-001: um único espaço de trabalho na experiência Ricy, sem indicadores, switchers, ações move-to-workspace, gestos ou navegação multi-desktop.

## Consequences

Novos componentes não podem depender de múltiplos desktops. A exposição legada precisa de auditoria separada; preservar APIs KWin necessárias ao funcionamento não implica expô-las.

## Constraints

Não refatorar upstream indiscriminadamente, não tratar toda ocorrência de `workspace` como violação e não quebrar Plasma Recovery. A conformidade runtime ainda é UNKNOWN.

Referências: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
