# Design System

## CURRENT — KNOWN
A identidade já existe. O guia detalhado é [IDENTIDADE-VISUAL](IDENTIDADE-VISUAL.md);
os valores estruturados estão em
[tokens.json](../ricy-kit/contributions/noctalia-visual-identity/tokens.json).
Este documento é o ponto de entrada normativo; não cria uma segunda paleta.
A cópia de transporte tem seus próprios tokens históricos: não presumir sincronia.

| Papel | Referência vigente dos tokens |
|---|---|
| Superfície / cartão | `#181825` / `#313244` |
| Texto / secundário | `#cdd6f4` / `#a6adc8` |
| Acento / seleção / contorno | `#cba6f7` / `#977dba` / `#46485c` |
| Vidro encaixado / cartões | Opacidade do fundo 0,70 / 1,00, textos opacos |
| Fonte shell | Noto Sans; 11 / 13 / 14 / 16 / 20 px lógicos antes da escala |
| Espaçamento / padding | 4 / 8 / 12 / 16 px; padding nativo 14 px |
| Radius | 3 / 6 / 9 / 12 px nativos × escala 1,3; barra tem raios próprios |
| Movimento | Nativo 100 / 200 / 400 ms; hover de apps 140 ms; indicador 160 ms |

As variantes Dolphin, KDE e terminal têm adaptações específicas nos tokens e
no guia; não universalizar um raio, fonte ou opacidade de um componente.
Blur depende da implementação do compositor e da classe da janela, não apenas
cor/opacidade. Ícones próprios de aplicativos mantêm a identidade.

KNOWN: configurações TOML, paletas JSON, QSS e instaladores ainda repetem valores.
Os tokens são referência documental, não configuração executável nem gerador.
Referências a workspace badges/groups são legado registrado em C-001; não são
permissão para novas interfaces de workspaces. Detalhes visuais anteriores podem
estar superados por ajustes posteriores do guia; registrar discrepâncias.

## TARGET — PLANNED
[themes/tokens](../themes/tokens/README.md) reserva o endereço central, apontando
para os tokens atuais sem copiar valores. Migrar consumidores um por vez com
comparação antes/depois, versionamento de contratos e rollback. Nenhum gerador
ou formato novo está escolhido. Não criar cores, radius, espaçamentos ou
animações arbitrários, nem um design system paralelo.

Ownership: Ricy mantém os papéis visuais; upstream mantém primitivas dos toolkits.
Dependências: Noctalia Style, KWin/blur, Qt/Kvantum e temas KDE/GTK existentes.
Recovery: adaptações globais podem afetar Plasma/Dolphin; toda mudança visual
nesses pontos deve manter ferramentas utilizáveis e restauração documentada.

Para estados/interações, materiais ou adaptação entre componentes, use
[visual-development](../.agents/skills/visual-development/SKILL.md).
Valide normal, hover, foco, seleção, desabilitado, escala, monitores, movimento
reduzido e junções/blur quando aplicável. Sem captura/interação real, declare
Visual NOT RUN; parse de tokens não comprova aparência.
