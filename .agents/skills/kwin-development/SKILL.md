---
name: kwin-development
description: Modificar efeitos, scripts ou patches KWin usados pelo Ricy, com compatibilidade de versão e proteção da sessão Plasma.
---

# kwin-development

1. Leia [INVARIANTS](../../../docs/INVARIANTS.md),
   [RECOVERY](../../../docs/RECOVERY.md) e AGENTS locais; consulte COMPONENTS
   quando ownership, fronteiras ou dependências estiverem em questão.
2. KWin é infraestrutura crítica. Prefira alteração conservadora e localizada;
   nunca substitua o compositor ou enfraqueça mecanismos necessários ao fallback.
3. Confira versão instalada, headers/ABI, commit upstream, patch e licenças.
   O blur do kit fixa 6.7.5; não supor compatibilidade binária em outra versão.
4. Separe patches do upstream e instaladores Ricy. Inspecione aplicação e
   restauração antes de alterar efeito compartilhado com Plasma/Dolphin.
5. Execute teste isolado relevante primeiro; integração real exige ambiente
   adequado e retorno. Não manipule janelas com trabalho para produzir evidência.
6. Preserve Plasma Recovery; documente alterações de efeito, dependências,
   rollback, testes executados e NOT RUN. Se exigir nova arquitetura, siga
   [architecture-change](../architecture-change/SKILL.md).
