# Opções da aplicação em painel Noctalia encaixado

O botão direito num ícone da taskbar usa agora um Panel nativo, registrado como
`ricy:taskbar-menu`, com o mesmo PanelManager da gaveta do tray. O painel abre
junto ao ícone e à barra que recebeu o clique, no monitor correspondente.
Herda fundo/opacidade da barra, desenho de junção, animação, blur e fechamento
externo nativos. Na configuração Ricy isso resulta em fundo 0,70 e continuidade
com a taskbar pelo ricyblur. Não altera menus internos de aplicativos nem menus
de contexto dos itens do tray.

As opções continuam sendo geradas pelo código original: Pin/Unpin quando
houver desktop entry, ações desse entry, Close e Close All quando aplicáveis.
Ações de fechar e fixar mantêm seus handlers originais; callbacks usam o guard
de vida do widget e a ativação é adiada até terminar o evento de entrada.

A largura é calculada pelo texto mais largo, com mínimo de conteúdo 240 px
na escala 1, e padding nativo do painel. A altura usa todas as entradas,
separadores e padding; **não há ScrollView nem limite de 12 linhas**.
O PanelManager já desconta o padding: a implementação não o aplica uma segunda
vez no conteúdo. Setas navegam e Enter/Espaço ativam; Escape/clique externo
seguem o fluxo nativo do painel. O tamanho ainda está sujeito aos limites do
monitor/compositor; listas muito extensas não foram testadas.

## Reproduzir

Compatível com Noctalia 5.2.1, commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. Prepare a integração permanente.
Este patch **composto** inclui também as correções de notificação e wallpaper
Home anteriores, preservando o estado completo da variante local.

```bash
cd "$HOME/ricy-kit/contributions/taskbar-menu-composition"
bash compilar.sh
python ../notification-continuity/ativar.py
```

Dependências: as da contribuição notification-continuity e BUILDING.md
upstream. O script fixa versão/commit e aceita somente uma fonte limpa ou o
mesmo patch composto já aplicado. No cache de uma variante anterior, o script
recusa diferenças; preserve a pasta anterior antes de começar um novo cache:

```bash
# Execute apenas quando o cache ainda contém a variante anterior conhecida.
# Use um nome de backup que ainda não exista; não sobrescreva fonte pessoal.
mv "$HOME/.cache/ricy-noctalia-src-5.2.1" "$HOME/.cache/ricy-noctalia-src-5.2.1-anterior"
bash compilar.sh
```

Com XDG_CACHE_HOME definido, ajuste ambos os caminhos. A instalação local
continua feita pelo ativador existente, com backup de binário/drop-in e
KillMode temporário para preservar aplicativos. `/usr/bin/noctalia` e os assets
do pacote permanecem instalados normalmente. O compilador antigo de
notification-continuity corresponde à variante anterior e não aceita este
cache composto; use o compilador desta contribuição para o estado atual.
Reveja/recompile ao atualizar o Noctalia. Blur compartilhado continua dependendo
da contribuição blur-continuity para a versão KWin correspondente.

## Validar e restaurar

Clique com botão direito em aplicativos na barra de cada monitor; confira
opções aplicáveis, lista inteira sem rolagem, Escape/clique externo e ações em
um aplicativo descartável. Não feche aplicativos com trabalho para testar.
Nesta implementação: compilação final e validação do perfil passaram; shell e
adaptador ativos, KillMode normal restabelecido, ricyblur carregado. O usuário
viu o painel nativo na primeira versão e apontou rolagem; corrigido o padding
duplicado, removida ScrollView e aplicada a variante final. A validação visual
final e a execução de cada ação pelo usuário ainda não foram registradas.

Para voltar à versão anterior, use o backup impresso na ativação:

```bash
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

O backup da primeira troca desta contribuição volta ao menu popup anterior;
o da segunda volta à primeira composição, que ainda apresentava rolagem.
Configuração de idioma, clima e demais preferências são independentes do
binário. Para compilar novamente a versão antiga, preserve o cache composto e
use fonte limpa com o compilador/patch correspondente. Não reutilize um cache
com alterações diferentes sem revisar seu diff.

Código upstream MIT; licença incluída. Os materiais não incluem binário,
clipboard, imagens de aplicativos, backups ou capturas reais da sessão.

## Atualização: menus do tray

O estado atual inclui também as opções dos itens do tray como painel Noctalia
e setinha para retornar à gaveta. Para reconstruir todas as mudanças, use
../tray-menu-composition/compilar.sh e seu patch completo. Este compilador
anterior permanece como referência histórica e recusa cache diferente.
