---
name: visual-development
description: Alterar estados/interações visuais, materiais ou adaptar identidade entre componentes Ricy; para ajuste isolado de token existente, DESIGN-SYSTEM e regras locais bastam.
---

# visual-development

1. Leia [DESIGN-SYSTEM](../../../docs/DESIGN-SYSTEM.md) e somente o trecho relevante
   do guia de identidade. Procure tokens e componentes já existentes.
2. Identifique o consumidor real (Style Noctalia, Qt/QSS/Kvantum, KWin ou tema).
   Reutilize papéis e valores existentes, respeitando unidades, escala e toolkit.
3. Proibido: random colors, random radius, random spacing, random animations e
   parallel design systems. Não copiar tokens para estabelecer outra autoridade.
4. Preserve geometria, legibilidade, ícones de aplicativos, redução de movimento,
   hit areas e identidade Ricy. Não generalize o blur de Noctalia para outros apps.
5. Quando houver ferramenta capaz, verifique antes/depois em normal, hover, foco,
   seleção e desabilitado, escalas/monitores relevantes e junções de blur.
   Sem acesso visual, declare NOT RUN e o limite; parse não prova aparência.
6. Atualize referência só quando a mudança correspondente estiver validada;
   registre recovery se afetar Plasma/Dolphin. Valores novos exigem justificativa
   no sistema central, não uma convenção paralela escondida no componente.
