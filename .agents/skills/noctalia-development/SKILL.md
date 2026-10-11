---
name: noctalia-development
description: Alterar patches, APIs, comportamento do perfil ou integração Noctalia/KWin do Ricy; ajustes apenas de valores visuais existentes seguem DESIGN-SYSTEM e regras locais.
---

# noctalia-development

1. Siga as regras locais da shell. Consulte [COMPONENTS](../../../docs/COMPONENTS.md)
   ao localizar ownership/contratos; [ARCHITECTURE](../../../docs/ARCHITECTURE.md)
   se mudar responsabilidades/coexistência. Noctalia é a shell principal.
2. Identifique a variante cumulativa atual e confirme versão/commit/patch real.
   Não aplique em sequência patches completos históricos. Ricy pode ter patches
   próprios, claramente distinguíveis do upstream e acompanhados de licença.
3. Verifique APIs na fonte da versão compatível; não presumir API de outra
   implementação/release chamada Noctalia. Build atual fixa Noctalia 5.2.1.
4. Workspaces não fazem parte do produto. Não acrescentar UI, ações ou gestos.
   Registre resíduos existentes sem confundir objetos internos KWin com a UX.
5. Respeite KWin como gerenciador de janelas; use integrações existentes. Visual
   exige DESIGN-SYSTEM; use [visual-development](../visual-development/SKILL.md)
   para estados/interações, materiais ou adaptações entre componentes.
6. Se afetar crash, prontidão, aplicativos filhos, atalhos ou retorno Plasma,
   leia RECOVERY e os invariantes/ADRs pertinentes. Preserve /usr/bin/noctalia,
   snapshots e ativador/reversão. Não reinicie a shell para validar documentação.
7. Rode checks apropriados conforme [DEVELOPMENT](../../../docs/DEVELOPMENT.md),
   documente versão, evidência e limitações de integração/visual/recovery.
