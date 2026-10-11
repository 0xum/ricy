# Integração Noctalia/KDE e menus compactos

Esta pasta é uma contribuição independente ao ricy-kit. As cópias registram o estado conferido em 08/10/2026. Não execute os dois kits de integração simultaneamente: ambos usam `noctalia-teste.service`, `noctalia-busca-desktop.service` e IDs `codex-noctalia-*.desktop`.

## Preparar no DESTINO

Use uma sessão CachyOS KDE Plasma Wayland com painéis Plasma e wallpaper já escolhidos. Copie esta pasta para `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus`. Confira primeiro o SHA256SUMS da raiz. Não traga backups, estado do Noctalia, IDs de monitor ou atalhos originais da máquina de origem.

Dependências de execução observadas: Noctalia 5.2.1-1.1, Kvantum 1.1.8-1.1, Plasma 6.7.5, KWin 6.7.5-3.1, python-gobject 3.58.0-1, qt6-tools 6.12.0-1.1, Python, glib2, coreutils, util-linux, bash. Qt 6 PyQt6 6.11.0-4 é necessário apenas para o teste opcional de menu. A fonte do Noctalia é Noto Sans; no destino preserve sua fonte KDE. JetBrainsMono Nerd Font, Papirus-Dark e Catppuccin já eram escolhas da origem, não dependências obrigatórias destes scripts.

```bash
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts
# Opcionais, conforme o teste/método usado:
sudo pacman -S --needed python-pyqt6 wl-clipboard
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python preparar-destino.py
```

O preparador só cria archives do kit: backup privado local dos archives pertinentes, manifesto, estado anterior das chaves, restauração do wallpaper com IDs DO DESTINO, perfil isolado e `.desktop` com caminhos recalculados. Não inicia serviços nem aplica o estilo. Recusa sobrescrever o backup original. Os backups podem conter preferências pessoais: mantenha-os no destino, não os redistribua. `config.toml` e `KDE-Atual.json` não contêm identificação de rede, usuário, archives recentes nem estado de clipboard.

## Aplicar estilo e blur, depois iniciar Noctalia

```bash
./aplicar-estilo.sh
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/iniciar-teste.sh
```

`aplicar-estilo.sh` instala os ativos completos Kvantum KDE-Noctalia, seleciona o estilo e define menuFont 10 pt preservando a família do destino. Não modifica a decoração Breeze ou o tamanho geral das fontes. Ao editar um tema já selecionado, `python recarregar-estilo.py` alterna temporariamente para Breeze e retorna a Kvantum, além de emitir o sinal real de atualização de fontes. Isso é necessário porque a integração Qt/KDE ignora a troca de estilo se o nome continua igual.

A paleta pública está em `outputs/kde-outlines/KDE-Noctalia.colors`. Se o destino ainda não usa essas cores e quiser adotá-las, use opcionalmente:

```bash
mkdir -p "$HOME/.local/share/color-schemes"
cp outputs/kde-outlines/KDE-Noctalia.colors "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
```

Essa aplicação de esquema não foi feita neste chat: o KDE da origem já usava Catppuccin Mocha Mauve. É uma opção de migração, independente da instalação do estilo.

O início retira os painéis Plasma somente após o IPC do Noctalia estar pronto. O plasmashell permanece ativo para desktop/wallpaper. O adaptador substitui KRunner no D-Bus e registra Super/Super+Espaço e Super+V; os atalhos originais são capturados localmente. A recuperação de login restaura os painéis se o teste não está ativo. O kit não inicia automaticamente o Noctalia após login. O script conserva a lógica de integração atual; não é um instalador genérico para sessões sem os serviços Plasma esperados.

## Estado final esperado

- Barra inferior top, 44 px, área reservada, escala 1,5, sem auto-hide/smart-auto-hide, fundo 0,70 com blur. Ícones taskbar aproximadamente 28 px: scale 0,666667, icon_scale 1,725, espaçamento 6.
- Sem SSID nem percentual de volume; tray com gaveta 3 colunas, ícones 24 px. Central attached/auto e cards opacos.
- Paleta escura #181825, cards #313244, texto #cdd6f4, acento #cba6f7, hover #977dba, contornos #46485c. Objeto terminal também incluído no JSON para passar o validador.
- Busca atual attached/auto no topo através de apoio `search_edge` 10 px sem reserva; abertura/ocultação controlada pelos wrappers e adaptador. O teste anterior floating/center foi substituído. Clipboard floating/center ativo na cópia atual.
- Menus Qt: cantos externos 12 px; SVG de seleção com raio 6 px, moldura vertical 4 px e lateral 6 px; margem de texto vertical 0/lateral 2; altura mínima 24 px; separadores 5 px; `spread_menuitems=false`, `shadowless_popup=true`, `popup_blurring=false`, opacidades reduzidas 0. A altura real depende da fonte/ícones; teste nativo desta máquina produziu linhas de 26 px.

## Verificar

```bash
export NOCTALIA_CONFIG_HOME="$PWD/work/noctalia-profile/config"
export NOCTALIA_STATE_HOME="$PWD/work/noctalia-profile/state"
noctalia config validate
systemctl --user is-active noctalia-teste.service noctalia-busca-desktop.service plasma-plasmashell.service
noctalia msg status
kreadconfig6 --file kdeglobals --group KDE --key widgetStyle
kreadconfig6 --file kdeglobals --group General --key menuFont
python verificar-menu-nativo.py
```

O último comando abre um pequeno menu Qt sem forçar WA_TranslucentBackground e o fecha em 1 s. Imprime estilo, fonte, altura de linhas e alfa do canto; alfa 0 significa pixel transparente. Teste o resultado real sobre uma janela e no Dolphin, pois alfa de uma captura do próprio widget não comprova a composição visual de todos os aplicativos. A confirmação visual final do usuário sobre o problema dos cantos ainda estava pendente no fechamento deste registro.

Confira também: janelas maximizadas respeitam barra; menus e ícones têm tamanho aceitável; tray/gaveta; Super e digitar no desktop; Esc recolhe busca/apoio; Super+V; wallpaper preservado. Estes testes devem ser repetidos no destino. Não foi feita migração real para outro computador.

## Desfazer no DESTINO

```bash
./outputs/noctalia-test/voltar-ao-plasma.sh
python restaurar-estilo-e-blur.py
```

A primeira restauração usa o backup local de layout/plasmashellrc, recupera os atalhos locais, inicia KRunner e retira os launchers/recuperação do teste. A segunda restaura as chaves de fonte, estilo e blur capturadas e o tema/configuração Kvantum anterior. Mantém os pacotes instalados. Reabra aplicativos para garantir atualização. Não executa restauração cega do KDE inteiro.

Se aplicou opcionalmente o esquema de cores, restaure as cores escolhendo o esquema anterior no KDE. Para uma restauração exata do kdeglobals capturado (inclui outras preferências e substitui mudanças posteriores), extraia somente esse arquivo do backup local:

```bash
tar -xzf outputs/kde-outlines/kde-antes-contornos.tar.gz -C "$HOME" .config/kdeglobals
```

Faça nova sessão para refletir essa restauração completa. A reversão não apaga histórico gerado posteriormente no perfil isolado; isso é dado pessoal do destino, a ser administrado por seu usuário.

## Conteúdo e origem

Scripts de preparação/aplicação/restauração foram adaptados para o destino nesta contribuição e verificados estaticamente; não foram executados contra esta sessão. Os scripts `outputs/noctalia-test/` são cópias da integração ativa conferida, incluindo a evolução para busca superior/clipboard já descrita na parte principal de ricy.md. Não representam execução de novas mudanças ao documentar.

Tema Catppuccin MIT incluído em `outputs/kde-outlines/KDE-Noctalia/LICENSE`. Checkout consultado: catppuccin/kvantum 71105d224fef95dd023691303477ce3eea487457. Código consultado de tsujan/Kvantum 110aff8b97a221531ef55acc4faeacfd719cdfea e plasma/plasma-integration 46eddde9d38cf907786e567dd4a942140bb1f797: são revisões de investigação, não comprovação de que correspondem exatamente ao pacote instalado. Os archives prontos do tema são suficientes para instalar; não é necessário compilar nem baixar esses checkouts.

Origens: https://github.com/catppuccin/kvantum ; https://github.com/tsujan/Kvantum ; https://invent.kde.org/plasma/plasma-integration ; https://github.com/noctalia-dev/noctalia .
