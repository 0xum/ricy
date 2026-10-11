---
name: documentation
description: Criar documentação Ricy, atualizar arquitetura/ADRs ou fontes de verdade e registrar mudanças significativas; não usar apenas para corrigir typo, comentário ou redação local sem alterar decisões.
---

# documentation

1. Leia [AGENTS](../../../AGENTS.md), procure equivalente antes de criar arquivo.
   Prefira consolidar ou apontar para a fonte mantida, preservando histórico.
2. Descreva why, what, constraints, ownership, dependencies e recovery implications.
   Use KNOWN com caminho/evidência; INFERRED com justificativa; PLANNED para
   destino aprovado; UNKNOWN quando faltar prova. Não narrar cada linha de código.
3. Separe intenção normativa e funcionamento observado; registre conflitos sem
   corrigi-los silenciosamente. ADRs explicam o porquê, não duplicam manual técnico.
4. Use links relativos válidos e fontes progressivas; não copie registros privados
   para documentação pública. Preserve caminhos e licenças históricas.
5. Atualize [CHANGELOG](../../../docs/CHANGELOG.md) em mudanças significativas com
   Model/Agent, Date, Purpose, Validation performed. Não assine arquivos de código.
6. Execute `./scripts/verify architecture`, revise links e relate limitações.
   Mudança significativa de arquitetura passa por
   [architecture-change](../architecture-change/SKILL.md).
