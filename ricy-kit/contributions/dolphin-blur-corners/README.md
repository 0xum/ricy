# Dolphin: transparência com Qt e cantos nativos KWin

Atualização da contribuição dolphin-identidade-noctalia. A primeira versão
opaca foi rejeitada pelo usuário. A aparência atual usa fundo #181825 com
alfa 178/255 (~0,70) e blur de compositor. A área de archives tem contorno
#46485c, raio 12 px e preenchimento leve #313244 (40/255), permitindo que o
blur continue visível. Textos/ícones não recebem opacidade de janela.

Dois componentes pequenos e independentes:

- ui.cpp: plugin Qt genérico carregado somente pelo argumento -plugin do
  launcher Dolphin. Antes de criar a superfície da DolphinMainWindow, ativa
  WA_TranslucentBackground. Permite aplicar a folha Qt desde a abertura sem
  impedir o canal alfa. Também instala um QProxyStyle de Kvantum para chips:
  hover/seleção da lateral envolve ícone + nome, com largura pelo conteúdo;
  seleção/foco da lista acompanha toda a chip, incluindo ícones. O delegate
  nativo continua responsável por texto, cabeçalhos de seção, ações de volumes,
  barras de capacidade, tooltips e drag/drop. Um QGraphicsEffect por item
  desenha fundo #313244 (90/255), raio até 10 px, margem horizontal 3 px e
  vertical 2 px; drawSource mantém conteúdo nativo. Aplicado a itens com largura
  >140 e altura <=64 px, cobrindo linhas de detalhes/compactas sem colocar um
  fundo em miniaturas grandes. AlternateBase/Base transparentes removem zebra
  retangular. Um efeito no header desenha a cápsula comum #313244 (155/255),
  contorno #46485c (150/255) e fonte Noto Sans 10 pt. O estilo mantém labels e
  seta de ordenação nativos, com hover arredondado por coluna. Não intercepta
  cliques, seleção, expansão, ordenação ou geometria das colunas.
- corners.cpp: efeito ricydolphinrounding para KWin 6.7.5. Atribui BorderRadius
  nativo 16 somente a janelas normais/diálogos de classe dolphin/org.kde.dolphin.
  Fullscreen, maximização parcial/completa e tiling recebem raio zero.
  Observa mudanças da decoração e do estado; descarregar restaura raios anteriores.
  Usa o renderizador e o recorte de blur nativos. Não adiciona shaders, passes
  de pintura, polling ou animações. isActive=false porque atua por eventos.

O ricyblur existente fornece o blur nativo para aplicativos externos à shell;
seu fundo compartilhado continua restrito ao Noctalia. Não foi modificado o
ricyblur, nem reiniciado KWin ou Noctalia. Breeze ainda desenha título e botões,
com título sólido e a fonte KDE; não foi criada uma decoração nova.

## Reproduzir

Use o KDE-Noctalia/Kvantum instalado pelo roteiro. Para compilar o helper Qt:
Qt6 Widgets/headers, pkg-config e g++ (qt6-base/base-devel no CachyOS).
O aplicar.py da contribuição irmã executa compilar-ui.py, instala a biblioteca
no diretório privado do Dolphin e atualiza o launcher. O kit contém fontes,
sem .so pré-compilado.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-noctalia-identity"
python aplicar.py
```

Para os cantos externos, headers KWin 6.7.5/KF6/Qt6/KDecoration3, Vulkan,
libepoxy/libdrm/Wayland e ferramentas de compilação (dependências do blur Ricy):

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-blur-corners"
python compilar.py
# O caminho segue XDG_CACHE_HOME, se definido:
sudo install -D -m 0755 "$HOME/.cache/ricy-dolphin-corners-build-6.7.5/ricydolphinrounding.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricydolphinrounding.so
python ativar-cantos.py
```

O compilador recusa KWin de outra versão. Revise/recompile ao atualizar KWin;
não copie o binário antigo. Se vulkan-headers estiver ausente, pode indicar a
pasta include compatível em RICY_VULKAN_HEADERS. Esta sessão reutilizou os
headers oficiais Vulkan já documentados no cache Ricy. Instalação do plugin
foi autenticada por Polkit. O Qt helper é instalado sem sudo.

Use o launcher normal. Processos Dolphin já existentes podem não ter um canal
alfa e precisam ser totalmente fechados/reabertos para carregar o helper e o
tema. Aplicador aplica a folha nas instâncias abertas sem fechá-las; não pode
prometer transparência retroativa em superfícies criadas opacas. Não interrompe
transferências nem reinicia o daemon automaticamente. Caminhos diretos de
/usr/bin/dolphin não injetam o helper/QSS; use ~/.local/bin/ricy-dolphin.

## Verificar / restaurar

```bash
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.isEffectLoaded ricydolphinrounding
qdbus6 org.kde.KWin /RicyDolphinRounding org.ricy.DolphinRounding.status
python ativar-cantos.py --restaurar "$HOME/.local/state/ricy-dolphin-corners-backups/DATA-HORA"
```

Status é somente leitura: classe, tipo, maximização/tiling e raio, sem nomes de
archives ou títulos. O restaurador repõe presença/ausência da chave em kwinrc
e estado de carregamento. Descarrega o efeito e devolve os raios nativos.
Não remove a biblioteca em disco; após descarregar, pode removê-la com sudo rm
no caminho instalado. Para reverter a aparência, use aplicar.py --restaurar
da contribuição irmã, depois reabra Dolphin. Reversões sucessivas devem ser
feitas em ordem inversa. Não substitui integralmente kwinrc.

Backup final dos cantos nesta sessão:
~/.local/state/ricy-dolphin-corners-backups/20261010-211849-253315.
Backup antes da nova aparência com blur:
~/.local/state/ricy-dolphin-backups/20261010-211018-558522.
Para voltar ao estado anterior às chips, reverta em ordem inversa os backups
20261010-213035-906999, 20261010-212959-440141 e 20261010-212842-374549.
Depois, para retornar ao estado anterior ao blur, reverta 20261010-211713-181764,
20261010-211458-875287 e 20261010-211018-558522.
O README da contribuição irmã registra os backups da primeira versão opaca.

## Evidência e limites

Compilação nativa de ambos os componentes concluída. Nova janela pelo helper
mostrou alfa 178 no fundo em captura RGBA; versão QSS anterior mostrava alfa
255. Capturas do desktop verificaram blur atrás do Dolphin com texto e ícones
nítidos, área de archives arredondada e translúcida. Capturas individuais de
janela não mostram o fundo composto e não bastam para verificar blur.

Status nativo confirmou raio 16 em todas as janelas Dolphin normais observadas.
Cliente Qt descartável com app-id Dolphin confirmou normal=16, maximizado=0 e
restaurado=16. Foi fechado ao terminar; não processou arquivos. Não mede frames,
nem testa todos os diálogos, monitores/escalas, tiling visual ou nova instalação.
O usuário aprovou as chips iniciais e pediu que também envolvessem os ícones
e que o header fosse ajustado. Esta revisão final foi inspecionada em capturas: 
header arredondado com seta, linhas arredondadas, seleção e foco sólidos
arredondados. A inclusão do ícone lateral está implementada no retângulo de
pintura, sem confirmação visual final do usuário. Não testados todos os casos
de renomear, drag/drop, reordenar/redimensionar colunas, transferências ou
diretórios muito grandes; não há medição de custo de QGraphicsEffect. Leitura de geometria
confirma a configuração nativa, sem alegar uma medição pixel a pixel dos cantos.

A primeira tentativa de atualizar QSS encontrou uma instância encerrada entre
listagem e comando D-Bus. Configuração já estava aplicada; o script final trata
essa corrida sem interromper a atualização das demais instâncias. Protótipos
ricydolphincorners/ricydolphinshape foram descarregados/desabilitados e suas bibliotecas removidas; o efeito
final usa outro nome para evitar reutilização do código carregado pelo Qt.
Não há reinício do compositor. Fontes de um efeito externo de cantos foram
consultadas no cache, mas nenhum código desse projeto foi usado.

Fontes primárias consultadas: KDE KWin v6.7.5 Window::setBorderRadius,
WindowItem::updateBorderRadius, ItemRendererOpenGL e efeito Blur; Kvantum
Style::setSurfaceFormat/Theme-Config; classes de visualização do Dolphin.
Implementação própria sob MIT. Créditos do tema base permanecem no kit irmão.


## Ajuste do hover do header — 11/10/2026

Hover deslocado 8 px para antes do início nativo da coluna, com inset vertical
3 px e recorte no backing comum (5 px horizontais/3 px verticais). Resolve
texto encostado no início e overflow visual nas colunas largas/roladas.
HeaderChip fornece os limites durante drawSource; labels e ordenação nativos
permanecem. Helper recompilado e instalado sem reiniciar janelas existentes.
Teste Qt offscreen do desenho confirmou padding antes do texto, inset superior
e inferior e recorte do overflow. Sem validação visual de todos os hovers na
janela real; nova janela aberta pelo launcher para conferência.
Backup: ~/.local/state/ricy-dolphin-backups/20261011-083312-062208.
Reversão: aplicar.py --restaurar BACKUP e reabrir Dolphin.


## Hover Size/Modified — 11/10/2026

Hover inclui o retângulo nativo da seta de ordenação com margem 6 px.
Última coluna identificada pela pintura do padding End (section-1), ou posição
End da própria coluna; seu hover alcança a borda interna direita do header.
Name mantém os insets anteriores. Sem usar strings traduzidas das colunas.
Teste Qt offscreen passou para identificação da última coluna, preenchimento
até a margem direita, limites externos/verticais e inclusão da seta.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084408-791214.
Reverter com aplicar.py --restaurar BACKUP e reabrir Dolphin.


## Correção: Size somente texto — 11/10/2026

Pedido esclarecido: Size deve ter chip curta somente em volta do texto, sem
incluir seta. Substitui a regra de inclusão da seta da revisão anterior.
Colunas intermediárias usam SE_HeaderLabel, alinhamento/direção nativos e
largura do texto elidido + 8 px de padding de cada lado. Name e extensão da
última coluna Modified preservados. Seta continua desenhada nativamente.
Helper recompilado/instalado; teste offscreen conferiu chip menor que coluna,
texto dentro e ausência de preenchimento junto à seta. Última coluna continua
preenchendo até a margem direita. Sem confirmação visual final do usuário.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084526-161433.
Restaurar com aplicar.py --restaurar BACKUP e reabrir Dolphin.


## Size: largura da coluna sem seta — 11/10/2026

Correção do pedido: chip ocupa a largura da coluna Size, não só o texto.
Colunas intermediárias usam o rect nativo com inset 3 px em cada lado, sem
o deslocamento negativo que engolia a seta da coluna anterior. Quando a
própria coluna tem seta de ordenação, esse espaço é excluído com margem 4 px.
Name e Modified preservados. Substitui a regra de largura pelo texto.
Compilação/instalação e teste offscreen passaram: início dentro da coluna,
preenchimento além do label, área anterior sem hover e reserva da seta.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084620-426269.
Reverter com aplicar.py --restaurar BACKUP e reabrir Dolphin.
Sem confirmação visual final; processos antigos precisam reabrir.


## Padding interno do texto Size — 11/10/2026

Chip mantém a largura da coluna e o limite que exclui a seta anterior.
Agora o label de colunas intermediárias é recuado para garantir 8 px internos
no início/fim, sem deslocar a chip sobre a seta. Name e Modified preservados.
Helper recompilado/instalado. Teste de pintura Qt offscreen passou para
preenchimento da largura, reserva da seta e primeiro pixel do texto pelo
menos 8 px após a borda da chip. Nova janela pelo launcher aberta.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084751-069063; restaurar
com aplicar.py --restaurar BACKUP e reabrir. Sem aprovação visual final.


## Name: espaço à direita da seta — 11/10/2026

Usuário aprovou padding de Size. Hover da primeira coluna Name agora estende
a borda direita em 6 px, mantendo recorte no header comum. Size e Modified
preservados. Helper recompilado/instalado. Teste offscreen verificou extensão
finita à direita e manteve checks de Size, padding e última coluna.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084856-807309; restaurar
com aplicar.py --restaurar BACKUP e reabrir. Sem aprovação final de Name.


## Espaçamento uniforme entre chips do header — 11/10/2026

Usuário aprovou Size e solicitou simetria do espaçamento. Geometria centralizada
em headerChipRect: chips terminam no limite de coluna +3 px; a seguinte inicia
nesse limite +9 px, mantendo 6 px entre elas. Name conserva margem da seta,
última coluna alcança a margem interna direita. Todas usam inset vertical 3 px
e conteúdo com padding mínimo 8 px; labels intermediárias/final recuados,
sem deslocar chip sobre a seta anterior. A seta da própria coluna, quando
necessário, tem área reservada à parte. Não altera largura/hit-test das colunas.
Compilação/instalação e teste Qt offscreen confirmaram 6 px nos dois intervalos,
altura/y iguais, Modified até o fim, texto com padding e Size ocupando largura.
Backup ~/.local/state/ricy-dolphin-backups/20261011-085034-172903; restaurar
com aplicar.py --restaurar BACKUP e reabrir Dolphin. Ainda sem confirmação
visual deste espaçamento; não mede todos os cenários de ordenação/RTL/scroll.


## Contribuição — Sidebar estável, expansão e chips aninhadas — 2026-10-11 (America/Sao_Paulo)

Usuário confirmou que o crash da sidebar parou; aprovou chips acompanhando
a largura visível e o recuo final até aproximadamente o ícone da pasta pai.
Removidos PlacesDelegate/setItemDelegate: não troca mais delegate nativo
KFilePlacesView. ChipStyle consulta índice/texto/ícone via view/model públicos
durante pintura. Preserva conexões e eventos KIO. Core coredumpctl/gdb indicava
tratamento de eventos KIO; não há símbolos de debug suficientes para a linha
exata. Teste nativo KIO QtTest passou 21 cliques/21 sinais urlChanged.

Outra causa de crash nas atualizações: copy2 sobrescrevia o inode da biblioteca
.so mapeada por processos abertos. Instalador agora copia para tempfile no
mesmo diretório e troca por os.replace. Reaplicação preservou processo anterior
315482 vivo, sem corromper a biblioteca carregada. Isto substitui instalação
in-place; verificações visuais anteriores não cobriam esse risco.

Configuração final dolphinrc: DetailsMode/ExpandableFolders=true e
LeftPadding=20; General/ShowSelectionToggle=false/BrowseThroughArchives=true.
Quadrado '+' de .md era seleção por hover, não expansão, e foi desligado.
Chevron 6 px, traço1,5 #a6adc8 só para PE_IndicatorBranch State_Children;
direita/baixo fechado/aberto. Arquivos comuns não têm seta. QStyleSheetStyle
Qt descartava branch com QStyleOption simples; itens gráficos agora usam
ChipStyle diretamente, widgets mantêm QSS. Teste Dolphin real em fixture
privada expandiu pasta via clique, 2→3 linhas, filho indentado e chevron.
Navegação em compactados ativada; modelo nativo expande diretórios em árvore,
não archives compactados. Estes podem ser abertos via KIO quando suportados;
sem seta sem ação funcional. Não testados todos os formatos.

RowChip intersecta bounds do item com viewport visível em coordenadas locais.
Fundo/clip/foco arredondados acompanham largura visível; conteúdo excedente
recortado. sourcePixmap NoPad com contexto mede profundidade pelos slots
nativos de branch. Recorte alcança hover/seleção em cache, foco redesenhado
na chip para manter contorno após recuo. Estado final aprovado: raiz inset3px;
filho acrescenta 20px gutter + profundidade × altura da linha. Na altura22px,
primeiro nível começa ~45px, no ícone da pasta pai; próximos avançam22px.
Substitui tentativa8px por nível rejeitada como pequena. Direita inset3px,
vertical2px/raio até10px; conteúdo/colunas não deslocados. Capturas de viewport
real conferiram expansão, chevron e recuo. Usuário aprovou largura e recuo.

Probe Qt temporário carregado explicitamente e fixture no cache não entram
no kit. Biblioteca de probe e cópia extraída do core removidas ao terminar;
janelas manipuladas pelo usuário preservadas. Não testados RTL, centenas de
níveis, escalas/formatos de arquivo, transferências, drag/drop ou performance.

Backups em ~/.local/state/ricy-dolphin-backups, restaurar em ordem inversa para
voltar antes da sequência: 20261011-090752-444876, 20261011-090705-662420,
20261011-090614-400487, 20261011-090454-088355, 20261011-090310-602007,
20261011-090132-953293, 20261011-085727-916570. Use aplicar.py --restaurar
BACKUP e reabra. Restaurador repõe archives inteiros, podendo substituir
edições posteriores. Não reaplique instalador antigo que sobrescreve .so.
Probe nos backups permanece privado/inativo; launcher só usa ricydolphinui.
Pode excluir libricyprobe.so ao restaurar snapshot com probe.

Fontes/aplicador/READMEs sincronizados nos kits ativo/portátil; hashes conferidos
preservando demais entradas. Não incluídos .so, screenshots, core ou backups.


## Contribuição — Painel e tabs como botões Noctalia; setas aninhadas — 2026-10-11 (America/Sao_Paulo)

Pedido: topbar/sidebar com blur, conteúdo em painel delimitado e tabs com
cores/formato de botões Noctalia. Também preservar ajuste de setas aninhadas
feito antes da ampliação do pedido. Tabs: neutro #313244/#cdd6f4, contorno
#46485c; ativa #cba6f7 com texto #11111b; hover #977dba/texto #000000.
Raio12 px, padding6/14 px e margem3 px (intervalo6 px). Troca as tabs pill
raio14/translúcidas Mauve da tentativa anterior por botões como referência.
QTabBar::close-button reserva right8/12px; toolbuttons do tabbar compactos;
QTabWidget::pane sem borda; helper setDrawBase(false) elimina linha de base.
Ícones e fechamento/reordenação mantêm comportamento nativo.

Root QMainWindow mantém #181825 alfa178/255 (~0,70), sidebar/topbar continuam
transparentes sobre esse fundo, com canal alfa antes de criar a superfície.
Conteúdo fica em painel #181825 alfa96/255 sobre o root, contorno #46485c,
raio12 e margem/padding8. Substitui painel #313244 alfa40; alfa composto medido
em captura de janela ~207/255. Topbar/sidebar mediram178/255. Textos e ícones
não recebem opacidade global. Captura real de Dolphin nova com várias tabs
mostrou botões Mauve/neutros e painel delimitado. No momento desta revisão
blur nativo KWin está carregado (blurEnabled=true/força5), ricyblur não está
carregado nem habilitado. Esse estado foi encontrado na sessão e preservado:
não reativado ricyblur, não reiniciado compositor ou Noctalia. Não confundir
essa observação atual com os estados anteriores documentados nesta contribuição.

Setas de subpastas deslocadas4px para dentro (RTL direção oposta), quando
o branch está além do slot raiz; seta raiz preservada. Geometria/hit-test
nativos de expansão não mudam; deslocamento cabe no slot de expansão.
Recorte de chips filhas e conteúdo acompanha viewport como aprovado.

Compilação/helper instalado conferidos e instalação atômica preservada.
Teste Qt de tabs confirmou ícones definidos preservados, botão de fechar
recuado e base desativada. Fixture usa ícone sintético, não valida todos os
ícones Breeze. Captura do Dolphin real confirmou paleta/layout; não testadas
todas as ações de abas, monitores, RTL ou todos os níveis de pastas. Uma captura
posterior de janela ativa pegou Codex porque o usuário trocou foco; não usada
como evidência do Dolphin. Aprovação visual desta revisão ainda pendente.

Backups privados em ~/.local/state/ricy-dolphin-backups: final
20261011-091610-462637; para voltar ao estado antes desta sequência, restaurar
em ordem inversa também 20261011-091325-096396 e 20261011-091239-713431.
Use aplicar.py --restaurar BACKUP e reabra. Restaurador repõe archives inteiros
e pode substituir edições posteriores. Kits ativo/portátil e tokens locais
sincronizados; hashes preservam demais entradas. Capturas/testes ficam no
cache privado, sem binários/estado/screenshots no kit.


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
