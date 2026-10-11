# Animações dos ícones por estado

O usuário confirmou restaurar/minimizar pelo ícone e fechar com o botão do
meio. Esta variante acrescenta resposta visual aos estados das janelas.


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

## Reproduzir

Fonte Noctalia 5.2.1, commit
6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4; efeito validado no KWin 6.7.5.
Dependências de compilação: BUILDING.md upstream e notificacoes-continuidade.
Aplicador requer Python, kwriteconfig6 e qdbus6 na sessão, sem sudo.

```bash
cd "$HOME/ricy-kit/contributions/app-icon-states"
bash compilar.sh
python ../notification-continuity/ativar.py
python aplicar-animacoes.py
```

O patch completo preserva as contribuições anteriores. O compilador aceita
fonte limpa ou exatamente este diff; ao migrar, preserve o cache anterior e
use fonte limpa conforme taskbar-menu-composition/README.md. Ajuste caminhos
quando XDG_CACHE_HOME estiver definido. Não substitui /usr/bin/noctalia.
O ativador da shell preserva aplicativos durante a troca. O aplicador do efeito
registra backup das chaves que altera e do pacote local anterior, instala em
XDG_DATA_HOME/kwin/effects/ricywindowactions e carrega sem reiniciar KWin.
Reveja/recompile ao atualizar as versões Noctalia/KWin.

## Validação e reversão

Compilação, reprodução, bash -n, validação do perfil, git diff --check e
aplicação reversa do patch passaram. Comparado com taskbar-app-actions:
mudanças adicionais limitadas a TaskbarWidget, KwinActiveWindow e
WaylandToplevels, cada um com fonte/header. Outros blocos preservados.

```bash
# Requer Python/PyQt6; executa JS real extraído da fonte, sem janelas reais.
python validar-acoes.py
python validar-indicador.py
# Fonte alternativa:
python validar-indicador.py --fonte /caminho/para/noctalia
```

17 cenários preservam restauração/minimização/fechamento e identidade exata;
15 verificam sinal de minimização, serialização, foco, fallback de monitor,
reversão e cleanup do blur. Uma janela Qt descartável na sessão real confirmou
estados de restaurar/minimizar/restaurar e fechar, com os efeitos efetivamente
ativos durante as transições. Capturas locais verificaram a mudança do
indicador ativo→minimizado; capturas não são distribuídas. A velocidade global
0,25 exige observar o efeito antes de 60 ms: uma consulta inicial após 65 ms
perdeu a animação; a verificação dentro da transição passou. Scripts/objeto DBus
de teste removidos. Nenhuma janela com trabalho foi fechada. A confirmação do
usuário é da variante anterior; este ajuste ainda aguarda avaliação visual dele.
Não valida todos os grupos, aplicativos, escalas ou movimentos rápidos reais.

Para desfazer, restaure as duas partes usando os backups impressos:

```bash
python aplicar-animacoes.py --restaurar "$HOME/.local/state/ricy-indicador-animacoes-backups/DATA-HORA"
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Noctalia/patch sob MIT (LICENSE). Efeito derivado do KDE Squash sob
GPL-2.0-or-later, com créditos preservados no main.js e licença separada em
LICENSE-KWIN-GPL-2.0-or-later.txt. Kit sem binários, capturas, clipboard,
contas, estado privado, bytecode ou backups.

## Variante posterior: reorganização

A referência completa atual é ../app-icon-reordering: preserva estas
animações, corrige o fundo preto e permite arrastar todos os apps, salvando a
ordem. Seu compilador histórico exige o diff desta variante; para reconstruir
a sessão atual, use ../app-icon-reordering/compilar.sh.
