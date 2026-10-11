---
name: architecture-change
description: Avaliar mudanças em fronteiras, contratos, dependências críticas ou invariantes do Ricy; exigir decisão explícita para arquitetura nova.
---

# architecture-change

1. Identifique a mudança solicitada e a autorização já existente no pedido.
2. Leia [ARCHITECTURE](../../../docs/ARCHITECTURE.md),
   [INVARIANTS](../../../docs/INVARIANTS.md) e os [ADRs](../../../docs/adr/README.md) relevantes.
3. Mapeie os componentes afetados em [COMPONENTS](../../../docs/COMPONENTS.md),
   leia regras locais e procure abstrações/convenções existentes.
4. Determine se a mudança modifica arquitetura ou apenas implementa um contrato
   já aprovado. Agentes não possuem autorização automática para criar arquiteturas.
5. Se houver decisão arquitetural nova, registre o bloco abaixo, explique impacto,
   PARE essa parte e solicite aprovação explícita antes de implementar. Continue
   partes independentes seguras. Não peça novamente aprovação já concedida para
   a mesma proposta; a aprovação não se estende a decisões adicionais.
6. Depois da aprovação: implemente incrementalmente, valide os níveis relevantes,
   crie/atualize ADR, componentes, recovery e changelog. Registre limites dos testes.

```text
ARCHITECTURE DECISION REQUIRED
Problem: ...
Evidence: ...
Options: A ... / B ...
Recommended: ...
Impact: componentes, dependências, compatibilidade e recovery
```

Não resolva conflitos docs/código silenciosamente. A estrutura futura por si só
não aprova um novo daemon, protocolo IPC ou migração de caminhos.
