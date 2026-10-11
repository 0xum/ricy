# Identidade visual do Ricy — referência Noctalia

Referência vigente capturada em 10/10/2026. Use este guia antes de harmonizar
outras partes do sistema. O Noctalia define a linguagem da shell; KWin é o
compositor da sessão Plasma Wayland. Este documento registra a aparência e
orienta mudanças futuras. Não instala temas nem aplica preferências.

A assinatura visual é escura, azulada e discreta, com destaque Mauve, cartões
arredondados, ícones claros e continuidade entre painéis encaixados e barras.
A profundidade vem da diferença entre superfícies e do blur do fundo.

## Paleta e estados

Paleta ativa: `KDE-Atual`, modo dark, fonte custom. Os valores abaixo foram
conferidos no arquivo ativo e no template público da integração.

| Uso | Cor | Papel Noctalia |
|---|---|---|
| Fundo da shell | `#181825` | mSurface |
| Cartões e controles neutros | `#313244` | mSurfaceVariant |
| Texto e ícones principais | `#cdd6f4` | mOnSurface |
| Texto e ícones secundários | `#a6adc8` | mOnSurfaceVariant |
| Acento Mauve, ativo, progresso normal | `#cba6f7` | mPrimary / mSecondary |
| Texto sobre acento | `#11111b` | mOnPrimary / mOnSecondary |
| Hover e seleção | `#977dba` | mHover |
| Texto sobre hover/seleção | `#000000` | mOnHover |
| Contorno sutil | `#46485c` | mOutline |
| Sucesso | `#a6e3a1` | mTertiary / terminal.green |
| Erro/urgência crítica | `#f38ba8` | mError |
| Aviso | `#f9e2af` | terminal.yellow |
| Informação | `#89b4fa` | terminal.blue |

Use o acento para seleção, ação principal, foco e progresso. Textos extensos
usam a cor principal; legendas usam a secundária. Preserve as cores semânticas
para erro, aviso e sucesso. A seleção KDE atual e o hover nativo usam a cor
mais escura de seleção, enquanto toggles ativos do Noctalia usam Mauve claro.
Essa diferença faz parte da referência capturada.

## Materiais, contornos e blur

| Superfície | Tratamento vigente |
|---|---|
| Taskbar, apoio da busca e painéis que herdam a barra | Fundo `#181825`, opacidade 0,70, blur do compositor |
| Notificações | Fundo 0,70, blur, sem contorno, junto à taskbar |
| Cartões internos | `#313244`, opacidade 1,00, contorno sutil quando habilitado |
| Painéis flutuantes/desanexados | Opacidade 1,00 no modo `shell.panel.transparency_mode=solid` |
| Menus Kvantum | Compactos, opacos, sem sombra de menu nem popup_blurring |

Opacidade 0,70 é a cor de preenchimento da superfície, não a opacidade de
textos, ícones ou da janela inteira. A cor percebida varia com o conteúdo sob
ela. `transparency_mode=solid` mantém os cartões sólidos; um painel encaixado
que herda a barra continua com fundo 0,70. Evite interpretar essa opção como
uma ordem de tornar todos os elementos translúcidos.

O `ricyblur`, derivado do KWin 6.7.5, fornece uma amostragem comum por monitor
para as superfícies Noctalia quando um painel/aviso aparece. As junções usam
`panel_overlap=0` para evitar um pixel com duas camadas de preenchimento.
Mesma cor/opacidade em duas janelas, por si só, não garante blur contínuo.
O efeito trata a classe Noctalia; **não estende automaticamente esse fundo
compartilhado a aplicativos novos ou de terceiros**. A adaptação exige análise
do componente e do compositor. Consulte a contribuição blur-continuidade.

Sombra é dependente do componente: o apoio superior não tem sombra; menus
Kvantum não têm sombra de popup; painéis nativos mantêm suas regras próprias.
Não considerar todas as sombras desligadas como estado vigente.

## Geometria e escala

Os valores são pixels lógicos, não pixels físicos de captura. Base atual:
`accessibility.ui_scale=1`, `shell.corner_radius_scale=1.3`.

| Elemento | Regra vigente |
|---|---|
| Taskbar | Inferior, 44 px, reserva 44 px, sempre visível |
| Cantos da taskbar | Superiores 6 px; inferiores retos |
| Busca pela lupa | Encaixada junto ao clique na barra |
| Controle Noctalia | Encaixado junto ao ícone à direita |
| Busca por Super/digitação | Launcher de 560 px e apoio superior de 640 × 16 px |
| Apoio superior | Cantos 8 px, distância 8 px do topo; somente no monitor da busca |
| Notificação | Canto inferior direito, offsets zero; canto inferior esquerdo côncavo para fora e direito reto |
| Menu da aplicação por botão direito | Painel Noctalia encaixado junto ao ícone; tamanho por conteúdo, sem rolagem |
| Opções de item do tray | Painel Noctalia encaixado; dimensões por conteúdo; setinha e gaveta compartilham o mesmo eixo horizontal ao retornar, no mesmo monitor |
| Clipboard | Painel flutuante no centro |

Raios nativos do Style: 3 / 6 / 9 / 12 px, multiplicados por escala local e
corner_radius_scale; a UI de escala 1 usa 3,9 / 7,8 / 11,7 / 15,6 px.
Barras têm raios explícitos próprios de 6 e 8 px, sem substituir esses valores
pelo raio geral dos cartões. A escala de conteúdo da barra é 1,5 e a escala
de fonte da barra 0,85; são parâmetros diferentes da escala geral da UI.

Espaçamentos nativos: 4 / 8 / 12 / 16 px; padding de cartão/painel de 14 px.
Use essa cadência para novos componentes e adapte o tamanho ao conteúdo.
Os monitores de referência têm 1920 px lógicos de largura. A margem de apoio
640 resulta em largura 640; em outro monitor use `(largura lógica - 640) / 2`,
limitada a zero, e revise o launcher se alterar a escala.

A continuidade é geométrica: bordas em contato têm uma junção única, sem
fresta escura, sobreposição dupla ou canto que recorta a conexão para dentro.
A notificação é uma assimetria intencional; não generalize quatro cantos
arredondados para componentes conectados à barra.

## Tipografia, ícones e movimento

Noctalia: **Noto Sans**. Tamanhos base nativos antes da escala: mini 11,
caption 13, corpo 14, título 16 e cabeçalho 20 px. Não converter esses valores
em pontos sem considerar a implementação/escala do toolkit.

KDE e menus: **JetBrainsMono Nerd Font, 10 pt**; GTK registra a mesma família
e tamanho 10. São preferências atuais, preservadas nesta contribuição.
Para os próximos ajustes, Noto Sans é a referência de UI da shell; a fonte
monoespaçada continua adequada ao terminal e deve ser tratada conscientemente
nos aplicativos. Alterar fontes globais ou de conteúdo exige um ajuste próprio.

Ícones de controles Noctalia usam desenho simples e legível, com destaque de
estado. Tema de ícones do sistema: Breeze Dark; ícones coloridos de aplicativos
mantêm sua identidade. Evite redefinir o ícone de cada aplicativo como Mauve.

Ícones dos aplicativos da taskbar e a lupa de busca usam escala visual **0,88
em repouso e 1,0 no hover**, com transição de **140 ms / EaseOutCubic** para
entrar e sair. Mantêm área de clique, espaçamento e indicadores fixos. O efeito
é restrito a esses ícones: tray/menus, volume, hora, network, botão do Noctalia
e badges de workspaces mantêm o comportamento anterior. A escala do hover
respeita o movimento/velocidade global da shell.

Constantes nativas de animação: 100 / 200 / 400 ms, com velocidade base 1.
São referências de transição, não medidas de latência real. Mantenha o indicador
ativo, o foco e a barra de tempo de notificação legíveis em cada estado.
O temporizador e a pausa por hover permanecem nativos.

## Interação dos aplicativos na taskbar

No KDE/KWin, clique esquerdo restaura/foca a janela minimizada, minimiza a
janela visível em foco e traz à frente a janela visível que está atrás de outra.
Ícone fixado sem janela inicia o aplicativo. Em grupos, prioriza a janela
ativa para minimizar; sem ativa, preserva seleção/ciclo para restaurar/focar.
Botão do meio solicita fechar uma janela, respeitando diálogos de salvar;
clique direito abre o menu composto e arraste ordena os fixados. A seleção
usa UUID exato quando disponível. Busca e outros chamadores de ativação
continuam apenas restaurando/focando. Reproduza com a contribuição
taskbar-app-actions, que preserva a composição e o hover aprovados.

O indicador roxo reage ao estado: **ativa 1/1, aberta inativa 0,55/0,82,
minimizada 0,28/0,65**, em opacidade/escala; sem janela, opacidade zero.
Transição **160 ms / EaseOutCubic**, preservada em reconstruções dos tiles.
Janelas usam **fade e expansão centrados**, escala **0,85→1** ao abrir/restaurar
ou **1→0,85** ao fechar/minimizar, OutCubic/InCubic. Duração base **320 ms**,
seguindo a velocidade KDE; fator global 0,25 preservado corresponde a cerca de
80 ms. Abrir/fechar usa Scale nativo; minimizar/restaurar usa ricywindowactions
com reversão e continuidade de blur por trilha. Geometria real preservada.
Referência atual dos efeitos: **window-fade-expand**; fonte Noctalia:
**app-icon-reordering**.

Ícones de aplicativos também respondem com movimentos finitos por ação:
**abrir 420 ms / bounce; restaurar 360 ms / bounce; foco 260 ms / pulso;
minimizar 220 ms / compressão; segundo plano 200 ms / redução; fechar fixado
240 ms / contração; remover não fixado 220 ms / dissolve**. Tempos base seguem
preferências da shell. Hover permanece separado, sem alterar área de clique;
slots usam Node sem pintura, evitando fundo preto. Nenhum loop em repouso.

Aplicativos podem ser reorganizados com botão esquerdo e arraste na faixa
plana. Um espaço indica o destino; o ícone acompanha o cursor. Ordem salva
no perfil e preservada entre recargas, independentemente da fixação. Gestos
consumidos não ativam/minimizam ao soltar. Busca/tray/controles mantêm posição.
Usuário confirmou o arraste na sessão real. Referência cumulativa atual:
**app-icon-reordering**; detalhes/testes/limitações em seu README.

## Aplicação nas próximas partes do sistema

Use os papéis de cor, a hierarquia entre superfície/cartão, o acento e a
geometria como referência para cada implementação. Registre o que foi aplicado
e o que continua dependente do toolkit; mantenha o layout e comportamentos
já aprovados ao mudar sua aparência.

| Área | Estado observado / direção dos próximos ajustes |
|---|---|
| Shell Noctalia | Referência principal; preservar barra, busca, notificações e continuidade |
| Qt/KDE | KDE-Noctalia + Kvantum KDE-Noctalia ativos; avaliar decoração, diálogos e controles em aplicativos reais |
| GTK | adw-gtk3-dark ativo; harmonização completa de cores e componentes ainda não demonstrada |
| Plasma | mocha-blur ativo; revisar elementos remanescentes por componente |
| Terminal | Preferências próprias Catppuccin/blur/cursor registradas nas contribuições existentes; manter legibilidade monoespaçada |
| Login e bloqueio | Aparência já documentada nas contribuições próprias; não revalidada nesta captura |
| OSD | Noctalia OSD desativado; escolher a implementação a adequar em um ajuste posterior |
| Navegadores/aplicativos de terceiros | Tema e conteúdo dependem de cada app; não presumir que seguir o tema KDE os torna integralmente harmonizados |

Para validar um ajuste, observe estados normal/hover/foco/seleção/desabilitado,
texto e ícones sobre fundos claros/escuros e as junções enquanto o conteúdo
sob o painel muda. Confira abertura/fechamento, monitor ativo e escala. Uma
captura com fundo uniforme não demonstra sozinha a continuidade do blur.

Região preservada: datas/UI Noctalia em inglês, fuso America/Sao_Paulo,
Cosmópolis/SP-BR, clima métrico e eventos habilitados sem conta conectada.
Essas preferências acompanham a referência, sem definir a paleta.

## Arquivos, fontes e uso no Ricy

- `tokens.json`: valores estruturados, papéis e regras para futuros agentes/ferramentas. É referência, não um config.toml substituto.
- `referencia.svg`: prancha vetorial com paleta e uma junção esquemática. Não é uma captura da sessão nem uma reprodução do blur OpenGL.
- `README.md`: este guia, também publicado como `Documents/ricy/IDENTIDADE-VISUAL.md`.

Fontes conferidas: config.toml e KDE-Atual.json da integração ativa/pública;
settings.toml privado apenas para conferir overrides pertinentes, sem copiá-lo;
style.h/style.cpp, config_types.cpp e regras de painel/barra da fonte Noctalia
5.2.1; kdeglobals, Kvantum e preferências GTK/Plasma atuais; contribuições de
notificações, blur, wallpaper e idioma/localização. Os tamanhos nativos são
constantes de código, não medições pixel a pixel de todos os componentes.

Esta contribuição não muda serviços, temas, fontes, configurações ou aplicativos.
Para retirar a referência, remova seu vínculo documental e seus archives do
kit, atualizando o manifesto. Mudanças futuras devem registrar sua própria
reversão e os backups do componente alterado. Preserve o histórico do Ricy.


## Adaptação aplicada ao Dolphin — 10/10/2026

Ricy-Dolphin/Kvantum é exclusivo do aplicativo: Noto Sans 10 pt, superfície
#181825 alfa 178/255, blur existente ricyblur, área de archives #313244 alfa
40/255 com contorno #46485c e raio 12 px. O helper Qt habilita a superfície
translúcida antes de criá-la. Não reduz opacidade dos textos/ícones.

A lateral envolve ícone + nome numa chip de largura pelo conteúdo: destaque
#977dba (alfa 95 hover, 170 seleção, 195 ambos). Linhas têm fundo #313244
alfa 90, raio até 10 px e margens 3 px horizontais/2 px verticais. Hover,
seleção e foco arredondados cobrem também o ícone; foco usa #cba6f7 sólido.
Header tem cápsula comum #313244 alfa 155, contorno #46485c alfa 150 e Noto
Sans, preservando labels/seta nativos. São adaptações aos widgets do Dolphin,
não mudanças de tokens da shell. Breeze mantém título e botões nativos.

Efeito ricydolphinrounding usa o raio nativo KWin 16 px só no Dolphin; raio zero
maximizado/fullscreen/tiling. Recompile ao atualizar KWin 6.7.5. Detalhes e
reversão: contribuições dolphin-noctalia-identity e dolphin-blur-cantos.
Chips iniciais aprovadas pelo usuário; ícones/header ainda sem aprovação final.
