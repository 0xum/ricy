# ADR-0002 — Plasma Recovery

Status: Accepted

## Context

A shell personalizada e patches podem falhar. O kit atual já depende de Plasma para desktop/wallpaper e usa scripts Ricy para restaurar painéis, portanto ainda existe acoplamento de recuperação.

## Decision

Adotar RICY-004: manter Plasma, Dolphin, System Settings e ferramentas KDE funcionais. Recovery deve ter tão poucas dependências Ricy quanto razoavelmente possível.

## Consequences

Qualquer alteração em login, unidades, atalhos, compositor ou defaults precisa considerar a rota de retorno. O mecanismo atual continua preservado, enquanto uma sessão independente permanece PLANNED.

## Constraints

Não remover pacotes ou desativar mecanismos necessários ao fallback. Testes offline não comprovam login/recovery real; não inventar watchdog ou gerenciador de sessão nesta etapa.

Referências: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
