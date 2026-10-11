# Clique para restaurar/minimizar e botão do meio para fechar

Comportamento atual dos ícones de aplicativos na taskbar KDE/KWin:

- Clique esquerdo restaura e dá foco à janela minimizada.
- Se a janela está visível e em foco, o clique esquerdo a minimiza.
- Se a janela está visível atrás de outra, o clique a traz para frente.
- Ícone fixado sem janela em execução inicia o aplicativo.
- Botão do meio solicita fechar uma janela; preserva os diálogos de salvar.
- Botão direito mantém o menu Noctalia; arraste mantém a ordenação dos fixados.

Nos ícones agrupados, o clique prioriza a janela ativa do aplicativo para
minimizar. Sem janela ativa no grupo, preserva a seleção/ciclo existente para
restaurar ou focar uma janela. Não acrescenta prévias ou seleção de grupos
idênticas às do Windows. O botão do meio fecha a janela ativa/representante,
sem encerrar todas as janelas. Ícone sem janela aberta ignora esse botão.

O usuário esclareceu que “abrir minimizadas” significava restaurar pelo ícone
e confirmou essa implementação com “Passou”. Depois solicitou também
minimizar a janela aberta pelo ícone. O binding de middle-click já existia.
A restauração anterior foi validada pelo usuário; a alternância nova tem os
testes abaixo e aguarda confirmação da interação física na sessão.

## Implementação

O adaptador KDE usa `window.minimized = false` antes de ativar/restaurar.
Somente os cliques esquerdos na taskbar passam `toggleMinimize = true`.
O script consulta o estado atual no KWin: minimiza apenas a janela em foco,
não minimizada e minimizável. Busca, dock, atalhos de navegação e outras
chamadas de ativação continuam apenas restaurando/focando. Em outros
compositores, esse método preserva a ativação original; a alternância
implementada nesta variante é específica de KDE/KWin.

Com UUID disponível, a seleção usa exclusivamente a identidade exata.
Class/caption é fallback apenas sem UUID; UUID obsoleto não aciona outra
janela com título igual. O fechamento chama `closeWindow()` e remove o
fallback anterior que apenas minimizava. Isso também beneficia o menu Close.

Ícones menores/hover, menus, junções, tray, volume, network, relógio e
control-center preservam suas implementações anteriores.

## Reproduzir

Noctalia 5.2.1, commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. O patch completo inclui todas as
correções anteriores. Este é o compilador de referência da variante atual.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/taskbar-app-actions"
bash compilar.sh
python ../notification-continuity/ativar.py
```

Dependências: BUILDING.md upstream e contribuição notificacoes-continuidade.
O script aceita fonte limpa ou exatamente este patch. Para migrar de uma
variante anterior, preserve o cache num caminho ainda inexistente e compile
em fonte limpa, conforme taskbar-menu-composition/README.md. Ajuste os caminhos
se XDG_CACHE_HOME estiver configurado. O ativador preserva aplicativos e cria
backup de binário/drop-in; `/usr/bin/noctalia` permanece intacto. Reveja e
recompile ao atualizar Noctalia; o blur mantém sua versão KWin própria.

## Verificação e retorno

Compilação, reprodução pelo script, validação do perfil e git diff --check
passaram. O diff adicional à variante app-icon-interactions afeta os widgets
TaskbarWidget, CompositorPlatform e KwinActiveWindow, cada um com seu header;
os demais blocos do patch anterior são preservados.

Dezessete testes executam os scripts JS reais extraídos da fonte em QJSEngine:
restauração e fechamento por UUID/class-caption, títulos duplicados, UUID
obsoleto, exclusão de janelas não normais, ausência do fallback de minimizar
no fechamento, alternância da janela ativa/minimizada, foco da janela visível
inativa, janela não minimizável, ativação comum sem minimizar e ponteiro.

Após preparar a fonte, repita os testes isolados com Python/PyQt6:

```bash
python validar-acoes.py
# Ou fonte em outro local:
python validar-acoes.py --fonte /caminho/para/noctalia
```

Também foi usada uma janela Qt descartável na sessão real: minimizada,
restaurada/focada, minimizada novamente, restaurada novamente, mantida visível
por uma ativação comum e fechada por UUID. A sequência verifica os estados
diretamente no KWin, sem depender do estado Qt do cliente para minimização.
Scripts/objeto DBus de teste foram
removidos. Nenhuma janela com trabalho do usuário foi fechada. Essa verificação
exercita o adaptador; não simula fisicamente o clique no ícone, nem cobre todos
os aplicativos/grupos. Confira a alternância pelo ícone e o botão do meio
numa janela sem trabalho.

Para retornar à variante anterior, use o backup impresso na ativação:

```bash
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Código upstream MIT, licença incluída. Kit sem binários, capturas, clipboard,
contas, estado privado ou backups da sessão.

## Variante atual: indicador e animações

O usuário confirmou a alternância desta variante. A contribuição posterior
app-indicator-animations preserva as ações e acrescenta bolinha por estado,
transição e efeito KWin. Para reconstruir o estado completo atual, use
../app-indicator-animations/compilar.sh e aplicar-animacoes.py. Este compilador
anterior permanece histórico e recusa cache com diff diferente.
