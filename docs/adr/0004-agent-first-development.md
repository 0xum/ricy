# ADR-0004 — Agent-first development

Status: Accepted

## Context

O projeto acumulou kits, variantes cumulativas e registros de sessões. Inferir intenção somente pelo código tende a perpetuar caminhos históricos e a apresentar planos como capacidades já prontas.

## Decision

Usar AGENTS.md como mapa conciso e constituição única; CLAUDE.md apenas o referencia. Autoridade: invariantes, ADRs, arquitetura/componentes, regras locais, implementação. Skills oferecem procedimentos progressivos; validar e registrar evidência.

## Consequences

Agentes carregam contexto por componente, procuram abstrações existentes, documentam conflitos e relatam limites dos testes. Mudança significativa registra Model/Agent, Date, Purpose e Validation performed no changelog.

## Constraints

Nenhuma autorização automática para criar arquitetura. Novo caminho exige proposta, impacto e aprovação explícita antes de implementar; autorizações já dadas no pedido são respeitadas. Não criar burocracia para edições compatíveis nem poluir código com assinaturas.

Referências: [INVARIANTS](../INVARIANTS.md), [ARCHITECTURE](../ARCHITECTURE.md).
