# ADR-0003 — Ricy Files

Status: Accepted

## Context

O futuro desktop precisa de um gerenciador alinhado à identidade e às interações Ricy. Dolphin já é usado e personalizado, e sua remoção antes de existir substituto deixaria uma lacuna funcional.

## Decision

Adotar RICY-005: reservar apps/file-manager/ para Ricy Files; ele será o padrão da futura sessão Ricy. Dolphin permanece disponível para Plasma Recovery.

## Consequences

Separar a futura aplicação das adaptações Dolphin existentes. Toolkit, contratos e cronograma de Files permanecem UNKNOWN até proposta aprovada.

## Constraints

Não implementar Files ou Settings agora, não mudar associações MIME/FileManager1 nem remover Dolphin. Não reutilizar sem análise wrappers globais que afetariam recovery.

Referências: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
