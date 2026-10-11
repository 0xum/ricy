# Ícones menores e animação de hover para aplicativos e busca

Na barra, os ícones dos aplicativos e a lupa de busca ficam 12% menores em
repouso. Ao passar o mouse, crescem suavemente até o tamanho visual anterior;
ao sair, retornam ao tamanho reduzido. Entrada e saída duram 140 ms, com
EaseOutCubic, respeitando a configuração de movimento/velocidade do Noctalia.
Reentrar durante a animação continua a partir do progresso atual.

O efeito transforma somente o desenho do ícone: área de clique, espaçamento,
layout da barra, títulos e indicadores permanecem fixos. Aplica-se a imagens,
ícones de fallback dos aplicativos e à imagem/glyph do launcher de busca.
Não modifica tray ou seus menus, volume, relógio, network, control-center/
botão do Noctalia, nem o efeito dos rótulos/badges de workspaces.
O destaque de fundo já existente dos apps acompanha o hover de 140 ms.

Implementação em TaskbarWidget e LauncherWidget. Constantes de escala em ambos
os archives devem ser mantidas coerentes: kAppIconRestScale=0.88 e
kAppIconHoverDurationMs=140. Usa AnimationManager nativo e cancela a animação
anterior ao mudar o destino; os owners da cena cancelam animações ao destruir
os nós. Transformações marcam apenas repintura, sem recalcular o layout.

## Reproduzir

Noctalia 5.2.1, commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. O patch completo preserva também
notificações, wallpaper Home, menu da taskbar, menu/retorno do tray e seu
alinhamento horizontal. Este é o compilador de referência da variante atual.

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/app-icon-interactions"
bash compilar.sh
python ../notification-continuity/ativar.py
```

O compilador aceita fonte limpa ou exatamente este patch. Para migrar de uma
variante anterior, preserve seu cache num caminho ainda inexistente e compile
em fonte limpa, conforme taskbar-menu-composition/README.md. Ajuste o caminho
se XDG_CACHE_HOME estiver configurado. Dependências: BUILDING.md upstream e
contribuição notificacoes-continuidade. O ativador preserva aplicativos, cria
backup de binário/drop-in e não substitui `/usr/bin/noctalia`.
Reveja e recompile ao atualizar o Noctalia; o blur compartilhado continua
vinculado à contribuição blur-continuity para o KWin instalado.

## Validação e restauração

Compilação, reprodução pelo script, validação do perfil e git diff --check
passaram. O patch foi comparado ao anterior: somente os archives dos widgets
de taskbar e launcher mudaram; correções anteriores e demais widgets foram
preservados. A confirmação visual e testes de clicar/arrastar aplicativos,
hover rápido, diferentes escalas e movimento desabilitado ainda não foram
registrados nesta revisão.

Passe o mouse sobre apps e lupa para conferir redução e ampliação suave,
sem mover a barra. Verifique também clicar, alternar janelas e arrastar um app
fixado. Compare tray, volume, relógio, network e control-center com o estado
anterior. Para restaurar, use o backup impresso pelo ativador:

```bash
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Código upstream MIT, licença incluída. Sem binários, capturas, clipboard,
contas, backups ou estado privado no kit.

## Variante atual: ações dos ícones

A variante posterior mantém estes ícones/hover e acrescenta restaurar/minimizar
pelo clique esquerdo no KDE/KWin, com fechamento exato pelo botão do meio.
Para reconstruir o estado completo atual, use ../taskbar-app-actions/compilar.sh.
Este compilador anterior permanece histórico e recusa cache com diff diferente.
