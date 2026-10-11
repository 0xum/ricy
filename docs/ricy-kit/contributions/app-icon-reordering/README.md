# Reorganizar ícones de aplicativos

O usuário confirmou “Passou” na sessão real. Pressione com o botão esquerdo,
arraste para a posição desejada e solte. O ícone acompanha o cursor; um espaço
indica o destino e os vizinhos mudam de posição. O gesto começa ao ultrapassar
o limiar nativo de arraste; um clique parado continua restaurando/minimizando.
Arraste consumido não dispara abertura, foco ou minimização ao soltar.
Botão direito e middle-click mantêm as ações anteriores.

O mecanismo upstream era limitado à lista de fixados. Agora funciona em toda
a faixa plana de aplicativos, incluindo abertos não fixados e lançadores.
Busca é outro widget e conserva sua posição. Tray, controles e agrupamento
por workspace ficam fora desta reordenação. Faixas horizontais/verticais usam
o eixo correspondente, com destino limitado aos slots existentes. Largura
dos títulos, escala e espaçamento entram no pitch real dos tiles.

A preferência `widget.taskbar.app_order` é gravada pelo ConfigService no
settings.toml do perfil ativo e reaplicada ao montar a barra. Ela ordena os
apps independentemente da fixação; arrastar nunca fixa um aplicativo. A lista
preserva slots de apps fechados ou filtrados em outro monitor/workspace.
Apps novos sem posição salva entram ao final. Monitores usando o mesmo widget
compartilham a preferência. Não se publica o settings.toml privado no kit.

As chaves usam identidade do app e número de ocorrência, sem títulos nem UUIDs
persistidos. Janelas duplicadas mantêm suas chaves durante atualizações;
instâncias novas podem reutilizar um slot livre. Após reiniciar, a ordem das
instâncias de um mesmo app corresponde à ordem natural de descoberta; não
identifica um documento específico entre reinícios. Guardas de geração
impedem salvar índices de um modelo que mudou durante o gesto. Cancelamento
restaura o layout. A gravação é adiada até terminar o evento, protegendo a
InputArea durante recarga; ao soltar, o ícone aguarda no slot de destino.

## Reproduzir a versão atual

```bash
cd "$HOME/ricy-kit/contributions/app-icon-reordering"
bash compilar.sh
python ../notification-continuity/ativar.py
# Necessário ao instalar os efeitos KWin pela primeira vez:
python ../window-fade-expand/aplicar-animacoes.py
```

Fonte Noctalia 5.2.1, commit 6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4.
O patch é cumulativo e inclui notificações, wallpaper, menus, hover,
ações, indicador e animações. Compilador recusa cache com diff diferente;
para outra variante, preserve o cache e recrie a fonte limpa antes de aplicar.
Instalação preserva aplicativos abertos e não reinicia o compositor.
Reveja/recompile ao atualizar Noctalia/KWin; dependências em BUILDING.md
upstream e ../notification-continuity/README.md.

## Verificações

```bash
python validar-ordem.py
# Requer build-ricy pronto; usa objetos realmente compilados do Noctalia:
python validar-arraste-nativo.py
python validar-motion.py
python validar-acoes.py
python validar-indicador.py
```

22 cenários de ordem, incluindo 24 permutações, passaram. 11 cenários nativos
instanciam TaskbarWidget/ConfigService em perfil temporário, sem conectar ao
compositor: permitem apps não fixados, movimentam o tile, cancelam, invalidam
modelo antigo, suprimem clique consumido, gravam e decodificam a ordem em
nova instância. 20 cenários de animação, 17 das ações e 15 do indicador/efeito
passaram. Compilação, reprodução, config validate, bash -n, git diff --check
e aplicação sobre fonte limpa passaram; todos os 17 archives do patch
coincidem com a fonte ativa. Comparado à variante de animações dos ícones,
só TaskbarWidget (.cpp/.h), sua definição e o novo taskbar_order.h mudaram.

Confirmação do usuário após ativar; preferência real com dois slots distintos
foi encontrada e validada. Não houve automação física de arraste: os testes
nativos cobrem a lógica e a validação visual foi feita pelo usuário. Captura
privada confirmou ícones sem fundo preto. Demais escalas, barras verticais e
mudanças de modelo durante um arraste real não foram validadas visualmente.

## Reversão

Backup antes desta ativação:
`$HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447`,
que retorna às animações dos ícones com o fundo preto já corrigido:

```bash
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447"
```

A ordem salva permanece no perfil; removê-la restaura a ordem padrão.
Efeitos KWin não mudaram nesta etapa. Para voltar também aos efeitos anteriores,
use aplicar-animacoes.py --restaurar com o backup das chaves/efeito registrado
na contribuição indicador-apps-animacoes. Para voltar antes das animações dos
ícones, o backup correto é 20261010-203450-476691; 203558-299413 contém a
implementação intermediária com Box preto e não é recomendado.

Noctalia/patch sob MIT (LICENSE). Efeito KDE sob GPL-2.0-or-later, créditos
preservados e licença separada. Kit sem binários, screenshots, clipboard,
contas, preferências privadas, bytecode ou backups.

## Resposta do ícone

Cada mudança real de estado dispara uma animação curta, sem loops:

| Ação | Movimento | Duração base |
|---|---|---:|
| Abrir | Dois saltos amortecidos e pulso leve | 420 ms |
| Restaurar | Dois saltos amortecidos menores | 360 ms |
| Ganhar foco | Pulso sem deslocamento | 260 ms |
| Minimizar | Compressão vertical em direção à barra | 220 ms |
| Perder foco | Redução/esmaecimento discretos | 200 ms |
| Fechar app fixado | Contração/esmaecimento, voltando ao lançador | 240 ms |
| Fechar app não fixado | Dissolver o ícone removido, escala 1→0,72 | 220 ms |

AnimationManager/MotionService nativos respeitam movimento e velocidade da
shell. Estado estável permanece parado; primeira montagem não anima todos
os apps. Reconstruções e interrupções preservam o progresso visual atual.
Hover continua no ícone filho, separado das transformações por estado.
Slot e área de clique ficam estáveis. Deslocamento acompanha a orientação da
barra. Busca mantém apenas seu hover; tray, volume, relógio, network e botão
Noctalia mantêm sua interação anterior.

O slot usa Node sem pintura. A primeira implementação com Box deixou um
retângulo preto atrás do ícone, relatado pelo usuário. Corrigido usando Node;
capturas privadas da sessão confirmaram a remoção. O fantasma de fechamento
é não interativo, ignorado pelo layout e removido com guardas de vida útil.
Só aparece quando a identidade exata da janela saiu do compositor; mudança
de monitor, filtro ou fixação não produz falso fechamento.

20 cenários C++ verificam estados, pulso/bounce, limites, interrupção,
cancelamento por proprietário e movimento desabilitado, usando o header e o
AnimationManager reais. Execute `python validar-motion.py`. Os validadores
anteriores das ações e do indicador continuam incluídos. Uma janela Qt
descartável real confirmou restaurar/minimizar/restaurar/fechar e efeitos
KWin. Capturas verificaram bounce e compressão; não há captura conclusiva do
fantasma de fechamento nem teste de todas as escalas/grupos.

## Bolinha roxa da taskbar

O indicador mantém a cor configurada no Noctalia:

| Estado | Opacidade | Escala visual |
|---|---:|---:|
| Janela ativa | 1,00 | 1,00 |
| Aberta em segundo plano | 0,55 | 0,82 |
| Minimizada | 0,28 | 0,65 |
| Ícone fixado sem janela | 0,00 | 0,55 |

Transição de 160 ms, EaseOutCubic, no AnimationManager nativo, respeitando
movimento/velocidade da shell. A animação parte do valor visual atual ao ser
interrompida. Os valores são preservados quando os tiles são reconstruídos,
permitindo também apagar suavemente o indicador de um app fixado fechado.
Ícone não fixado é removido quando sua última janela fecha. Não muda área de
clique, layout, hover dos ícones nem opções do tray. A opção show_active_indicator
continua sendo respeitada. Quando há títulos visíveis, a linha indicadora usa
os mesmos estados. Os pontos do resumo de workspaces mantêm sua composição.

O script KDE envia agora o estado de minimização de cada UUID e conecta
minimizedChanged. Uma janela minimizada não permanece ativa por foco antigo
retido sobre uma superfície da shell. Seleção ativa prioriza UUID, evitando
acender outra janela de mesmo título. Nos fixados agrupados, o estado minimizado
significa que todas as janelas estão minimizadas; nos grupos de workspace,
a representação prioriza uma janela ativa ou visível. A estrutura ToplevelInfo
também preserva o estado anunciado por wlr, quando disponível.

## Animações no KWin

ricywindowactions deriva do efeito Squash do KDE: comprime/desloca/esmaece
para minimizar e inverte para restaurar, com duração base 240 ms, InCubic/OutCubic.
Reversões rápidas reutilizam a animação; se não for possível, ela é cancelada
antes da nova. Mantém blur forçado durante a transição e o libera ao terminar.

O efeito nativo Squash não anima sem iconGeometry. Noctalia não publica essa
geometria de ícone Plasma. Esta variante usa a geometria quando fornecida;
na ausência dela, usa um destino de 18×18 no mesmo monitor, centrado na
horizontal da janela e a 22 px da borda inferior, referência da taskbar de 44 px.
Esse destino é aproximado: não é a posição exata do ícone. Não desloca a
janela de um monitor para outro. Para barra em outra posição/altura, revise
o destino de fallback. Anima somente janelas normais que aparecem na taskbar;
painéis, busca, tray e efeitos de tela cheia não recebem essa animação.

Abertura/fechamento usam o efeito nativo Scale, duração base 180 ms,
escala 0,92↔1 e fade. Fechamento ocorre após o aplicativo aceitar o pedido,
respeitando diálogos de salvar. Scale também pode animar diálogos conforme
sua implementação nativa. Desativados Squash/Magic Lamp e Fade para evitar
sobreposição com os efeitos escolhidos. Smooth Window Geometry permanece.

animationTime respeita a velocidade global do KDE. Na sessão validada,
AnimationDurationFactor=0,25 reduz 240 ms para cerca de 60 ms e 180 ms para
cerca de 45 ms. A preferência global foi preservada. Noctalia e KWin têm
preferências de movimento independentes; os tempos citados são de referência,
não medidas de latência real. Composições anteriores e ricyblur permanecem.

## Atualização das animações das janelas

O Noctalia continua usando esta fonte/binário. Para o efeito atual de fade e
expansão nas quatro ações, use ../window-fade-expand/aplicar-animacoes.py
após compilar/ativar esta contribuição. O aplicador KWin desta pasta registra
a etapa anterior; a referência abaixo descreve os efeitos daquela etapa.
Leia ../window-fade-expand/README.md para valores atuais e reversão.
