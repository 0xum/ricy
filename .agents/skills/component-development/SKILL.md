---
name: component-development
description: Adicionar componente Ricy já aprovado, migrar componente ou alterar ownership, fronteiras, responsabilidades, dependências significativas ou contratos entre componentes; não usar para correção interna localizada.
---

# component-development

1. Localize o componente em [COMPONENTS](../../../docs/COMPONENTS.md).
2. Siga AGENTS aplicáveis e ADRs do contrato afetado. Em contribuições legadas,
   use `ricy-kit/AGENTS.md`; destino planejado não transfere ownership atual.
3. Mapeie chamadores e dependências afetados, incluindo a cópia de transporte.
   Procure contrato/abstração equivalente antes de criar outro.
4. Faça alteração mínima compatível. Preserve caminhos usados por unidades,
   instaladores e backups. Separe UPSTREAM, PATCHES e RICY-OWNED.
5. Execute validação do componente e integração quando aplicável; considere
   [RECOVERY](../../../docs/RECOVERY.md) para mudanças na sessão ou em Dolphin.
6. Documente mudanças relevantes, conflitos e limites; use
   [DEVELOPMENT](../../../docs/DEVELOPMENT.md) para checks e changelog.

Se precisar alterar fronteiras/contratos, use
[architecture-change](../architecture-change/SKILL.md) antes de implementar.
