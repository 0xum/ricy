# Dolphin com identidade Noctalia

Variante exclusiva Ricy-Dolphin do Kvantum, derivada do KDE-Noctalia/Catppuccin
MIT instalado. Fundo #181825, texto #cdd6f4, secundário #a6adc8, contorno
#46485c, cartões de controle #313244 e destaque #977dba/#cba6f7.
Fonte Noto Sans 10 pt na interface e nos três modos de arquivos. Controles da
barra, campos e abas têm cantos de 8 px. Menus preservam a variante compacta
KDE-Noctalia existente. Ícones Breeze Dark e operações de archives preservados.

O tema é atribuído somente a dolphin em Kvantum/Applications. O launcher
ricy-dolphin injeta a folha Qt e o helper de transparência. Desktop, serviço
FileManager1 e drop-in plasma-dolphin.service usam o launcher. A versão atual
requer a contribuição irmã dolphin-blur-corners, que contém o compilador Qt.
Fundo 0,70 com blur, área de archives translúcida arredondada de 12 px e cantos
externos nativos de 16 px pelo efeito KWin opcional. A lateral usa chip que
envolve ícone + nome; linhas, hover, seleção/foco e header de archives usam
cápsulas arredondadas, mantendo os desenhos e eventos nativos. Leia seu README para
compilação, evidência, atualização de versões e reversão dos cantos.

Fonte KDE global, operações de archives, MIME e Noctalia preservados. Breeze
mantém título/botões nativos. Processos existentes sem alfa exigem fechar e
reabrir Dolphin para carregar tudo; o aplicador preserva as janelas abertas.
Execução direta de /usr/bin/dolphin não injeta helper/QSS: use o launcher normal
ou ~/.local/bin/ricy-dolphin. Nenhum arquivo de sistema do Dolphin é substituído.

## Reproduzir

Pré-requisitos: Plasma Wayland, Dolphin, Qt/Kvantum, KDE-Noctalia instalado,
Noto Sans, Qt6/headers, g++, pkg-config, Python, qdbus6, kwriteconfig6, kbuildsycoca6 e systemd de usuário.
Referência deste destino: Noctalia 5.2.1, KWin 6.7.5.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-noctalia-identity"
python aplicar.py
```

O aplicador preserva os archives anteriores em backup privado 0700 e atribuições
de outros aplicativos. Aplica QSS via D-Bus aos processos Dolphin abertos sem
fechá-los. Janelas novas pelo launcher carregam também a nova variante; janelas
antigas podem exigir reabertura para atualizar tema/fontes de arquivos.
Não reinicia o daemon nem fecha janelas, evitando interromper transferências.
Reaplicações criam novos backups; reverta na ordem inversa.

## Restaurar

```bash
python aplicar.py --restaurar "$HOME/.local/state/ricy-dolphin-backups/DATA-HORA"
```

Restaura archives inteiros e ausências anteriores; pode substituir edições
posteriores dos mesmos arquivos. Reabra Dolphin para carregar o estado anterior.
Na primeira versão opaca houve duas aplicações: reverta 20261010-210632-242640 e depois
20261010-210604-287127. Não remove pacotes nem altera archives pessoais.

## Verificação realizada

Inspecionadas capturas de uma janela nova antes/depois: fonte proporcional,
sidebar/fundo unificados, controles arredondados. Conferidas atribuição Kvantum,
fontes dos três modos, stylesheet no processo, desktop-file-validate e
systemd-analyze --user verify. XML SVG, sintaxe Python e configuração conferidos.
Apenas janelas de conferência criadas pelo agente foram fechadas. A janela
Home existente foi preservada. Para a validação atual de blur e cantos, consulte dolphin-blur-corners/README.md.
Não testadas transferências, todas as ações,
novas sessões, todos os diálogos/monitores ou outra instalação. Sem confirmação
visual final do usuário para ícones + header. As chips iniciais foram aprovadas. Capturas e backups não são publicados no kit.

Referência primária de temas por aplicativo e opções Kvantum:
https://github.com/tsujan/Kvantum/blob/master/Kvantum/doc/Theme-Config
Fonte ViewFont/UseSystemFont:
https://github.com/KDE/dolphin/blob/master/src/settings/dolphin_detailsmodesettings.kcfg


## Padding lateral da sidebar — 11/10/2026

KFilePlacesView recebe padding-left/right 8 px na folha Qt. Recuo do viewport
move juntos títulos, ícones, chips e barras de capacidade, sem deslocar só
o desenho do delegate. Aplicador criou backup privado
~/.local/state/ricy-dolphin-backups/20261011-085235-777886. Captura de janela
nova confirmou títulos/ícones/chip recuados; sidebar não encosta na esquerda.
QSS aplicado também a instâncias existentes, sem fechá-las. Fonte/helpers
e espaçamento do header preservados. Reverter: aplicar.py --restaurar BACKUP
e reabrir Dolphin. Não testados scrollbars/drag-drop em todas as larguras.


Atualização 11/10/2026: helper instalado por troca atômica, preservando
biblioteca mapeada pelas janelas abertas. Delegate nativo da sidebar preservado.
Pastas expansíveis/navegação em compactados habilitadas; '+' seleção desativado.
Chips recortadas ao viewport com recuo do filho até o ícone do pai.
Evidência, aprovação, limites e backups na seção final do README irmão.


Atualização 11/10/2026: tabs como botões Noctalia (#313244 neutro, #cba6f7
ativo/#11111b texto, #977dba hover), raio12/intervalo6; sidebar/topbar sobre
fundo alfa0,70 e painel de archives #181825 alfa96 com raio12. Setas de
subpastas4px mais para dentro. Estado atual usa blur nativo KWin; referências
anteriores a ricyblur descrevem histórico. Detalhes/evidência/backups no README
dolphin-blur-corners, seção final.


### Revisão — painel opaco e fechar das tabs — 2026-10-11

Área principal usa #313244 sólido (alfa 255), conforme painel Noctalia
referenciado pelo usuário. Sidebar/topbar permanecem sobre #181825 alfa178,
com blur nativo KWin preservado. O helper reposiciona os botões nativos das
tabs antes de pintar, com 12px de recuo externo (inclui margem de 3px);
preserva sinais e ações de fechamento. Subcontrol QSS anterior não deslocava
o botão no Dolphin real. Captura/probe no aplicativo confirmou painel
RGBA(49,50,68,255), shell alfa178 e recuo12 nas três tabs.
Backup final: ~/.local/state/ricy-dolphin-backups/20261011-092428-218159;
anterior nesta sequência: 20261011-092338-169456. Helper usa instalação
atômica; código novo requer janela nova.


### Revisão — sidebar/topbar num painel em L; botões laterais — 2026-10-11

Por solicitação do usuário, sidebar e topbar agora compartilham um único
painel opaco #313244, igual ao painel principal. ShellPanel é um QWidget
filho atrás dos controles: desenha o L inteiro com raio12, margem8 e
gutter8 para a área de archives, sem receber input ou alterar o layout.
Geometria acompanha os containers visíveis (inclusive mais de uma área),
redimensionamento e ocultação do dock; sem sidebar desenha só o painel de
topbar. A margem externa continua sobre a shell translúcida alfa178, com
blur KWin preservado. Esta revisão substitui a transparência interna da
sidebar/topbar registrada anteriormente.

Itens laterais são botões de largura uniforme: neutro #242435, hover
#977dba, selecionado #cba6f7, contorno #46485c, raio8. Ícones nativos24,
spacing1 da lista e recuo vertical2 deixam 6px entre botões. Padding lateral
12; paleta HighlightedText #11111b, preservando desenho nativo do texto
ativo/inativo e ícones. KFilePlacesView mantém seu delegate original,
cliques, atalhos, drop, indicadores de capacidade e ações dos dispositivos.
Tamanho de ícones é gravado pelo KIO em dolphinrc, incluído nos backups.

Verificações: helper compilado/instalado atomicamente; captura no Dolphin
real confirma L contínuo e botões; teste da lateral passou21 cliques/21
navegações sem trocar delegate. Fixture Qt confirma braços conectados,
recorte livre para conteúdo, ausência de captura de mouse, resize e
sidebar ocultada. Não validados todos os layouts RTL ou docks flutuantes.
Backup final: ~/.local/state/ricy-dolphin-backups/20261011-093607-825801.
Antes desta sequência: 20261011-093205-549123, seguido de 093320-666039
e 093439-242103 (mesmo prefixo de data). Para reverter toda a sequência,
restaure na ordem inversa. Código novo requer janela nova.
