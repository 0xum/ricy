# Janelas: fade e expansão

Referência visual fornecida pelo usuário:
[Slick Window Arrangement](https://windhawk.net/mods/slick-window-arrangement).
Escopo confirmado: abrir/restaurar e fechar/minimizar janelas.

| Ação | Escala | Opacidade | Curva |
|---|---|---|---|
| Abrir ou restaurar | 0,85 → 1,00 | 0 → 1 | OutCubic |
| Fechar ou minimizar | 1,00 → 0,85 | 1 → 0 | InCubic |

Duração base **320 ms**, com centro da própria janela como referência. A
transformação é visual: posição e tamanho real não mudam. Não requer geometria
de ícone e não desloca a janela para a taskbar ou outro monitor. Preferência
global do KDE preservada: AnimationDurationFactor=0,25 na sessão registrada
resulta em duração de referência aproximada **80 ms**. animationTime aplica
as preferências KDE, inclusive redução de movimento; não altera kdeglobals.

Minimizar/restaurar usa a nova variante do efeito local ricywindowactions,
com Scale e Opacity, mantendo a reversão por redirect nativo. Se a reversão
falhar, cancela antes de iniciar o novo sentido. Eventos repetidos não empilham
animações. Blur permanece até ambas as trilhas terminarem; IDs antigos ou de
outros efeitos são ignorados. Fechar durante uma transição cancela as trilhas
de minimizar/restaurar, preservando o blur do Scale nativo caso ele já tenha
iniciado o fechamento.

Abrir/fechar usa **Scale nativo KDE**, agora configurado com 320 ms e escala
0,85. Pode também animar diálogos conforme os filtros nativos do KDE. Fechar
ocorre quando o aplicativo aceita a solicitação, incluindo confirmação de
salvar. Minimizar/restaurar segue apenas janelas normais que aparecem na
barra; painéis, popups e efeitos de tela cheia mantêm seus filtros. Fade,
Squash e Magic Lamp ficam desativados para evitar efeitos duplicados.

Noctalia permanece com o binário aprovado da contribuição
icones-apps-reordenacao. Arraste, ordem salva, animações/hover dos ícones,
indicador roxo e composições da shell mantidos. ricyblur e
smoothwindowgeometry permanecem carregados. Maximizar, redimensionar e mover
janelas não receberam ajustes nesta etapa.

## Aplicar e reverter

Execute como usuário da sessão, sem sudo:

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/window-fade-expand"
python validar.py
python aplicar-animacoes.py
```

Instalador salva cópia do pacote anterior e somente as dez chaves alteradas
em ~/.local/state/ricy-fade-expand-backups/DATA-HORA. Instala o pacote local em
~/.local/share/kwin/effects/ricywindowactions e configura kwinrc. Recarrega
apenas os efeitos e reconfigura o KWin, sem reiniciar compositor ou shell,
e preserva aplicativos abertos. Se a ativação falhar, restaura o backup.
Não requer recompilar o Noctalia.

Para voltar ao comportamento anterior desta sessão:

```bash
python aplicar-animacoes.py --restaurar "$HOME/.local/state/ricy-fade-expand-backups/20261010-205749-431612"
```

Em outra máquina, use o caminho de backup impresso pelo instalador. Reversão
restaura pacote, chaves presentes/ausentes e configuração do Scale. Backups e
preferências privadas não fazem parte do kit. Ao reproduzir a sessão atual,
use o compilador app-icon-reordering para Noctalia e este instalador para
as animações das janelas.

## Verificação e referências

28 cenários executam o JS real em QJSEngine: fade/escala, geometria intacta,
velocidade, limites de configuração, reversão e fallback, eventos repetidos,
blur por ID de trilha, fechamento em curso, filtros e instalação coordenada.
Uma janela Qt descartável na sessão real confirmou abertura com Scale,
restaurar/minimizar/restaurar, sequência rápida minimizar/restaurar, ativação
comum sem minimizar e fechamento com Scale. ricywindowactions esteve ativo
nas ações de minimizar/restaurar. Pacote instalado coincide com o do kit,
configuração foi conferida e os efeitos ricywindowactions/Scale/ricyblur
continuam carregados. Não apareceram erros do script no journal consultado.
Scripts/DBus de teste removidos; nenhuma janela com trabalho foi fechada.

Não mede frame a frame a escala/opacidade na sessão nem valida todos os
aplicativos, diálogos, monitores ou escalas. Valores e reversão são cobertos
pelo JS isolado; a janela real valida integração e estados. Este ajuste ainda
não recebeu confirmação visual do usuário.

A [fonte do Slick Window Arrangement](https://github.com/ramensoftware/windhawk-mods/blob/main/mods/slick-window-arrangement.wh.cpp)
descreve sliding e snapping durante movimentação. O efeito solicitado aqui
foi implementado com a API nativa do KWin; nenhum código Windows foi copiado.
Referências primárias KDE:
[Scale](https://github.com/KDE/kwin/blob/v6.7.5/src/plugins/scale/package/contents/code/main.js)
e [Squash](https://github.com/KDE/kwin/blob/v6.7.5/src/plugins/squash/package/contents/code/main.js).
Efeito local deriva da estrutura reversível KDE, mantendo crédito de Vlad
Zahorodnii e licença GPL-2.0-or-later no código e arquivo de licença. Compatível
com a sessão KWin 6.7.5; reveja ao atualizar o compositor. Kit sem binários,
contas, screenshots, clipboard, bytecode ou preferências privadas.
