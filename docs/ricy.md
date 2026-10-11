# Ricy — reprodução do KDE Plasma com Noctalia no CachyOS

> **Organização em 11/10/2026:** projeto em `$HOME/Projects/ricy`; kit ativo em `$HOME/Projects/ricy/ricy-kit`; scripts `iniciar.sh`, `voltar.sh` e `alternar.sh` na raiz do projeto. Documentação e kit transportável em `docs/`; arquivo original em `archives/ricy.zip`. Os caminhos antigos no registro abaixo são históricos. O lock atual é `$HOME/.local/state/ricy/documentacao.lock`.


> **Estado vigente neste destino (10/10/2026):** Noctalia permanente no login, kit ativo em `$HOME/ricy-kit`, aparência completa e SDDM selecionado para o próximo reinício. Use `REINSTALAR.md` e a contribuição final deste registro. Os trechos anteriores sobre modo de teste são históricos.

> **Referência dos próximos ajustes visuais:** consulte [IDENTIDADE-VISUAL.md](IDENTIDADE-VISUAL.md). O guia e os tokens capturam a linguagem do Noctalia para harmonizar outros componentes, com distinção entre aparência já aplicada e trabalho futuro.

Registro de 8 de outubro de 2026. Documento do estado final desta sessão, com explicação das decisões e roteiro de migração. O kit de archives fica em `~/ricy-kit`, ao lado deste documento. **Transfira o documento e o kit juntos.**

## Instruções para os demais chats desta sessão

Este arquivo é o registro compartilhado das mudanças feitas neste CachyOS. Cada chat deve documentar as alterações que efetivamente realizou, para que outro agente ou usuário consiga reproduzi-las em outra instalação. O kit complementar está em `/home/delta/ricy-kit`.

Para ampliar a aparência do sistema, leia primeiro `IDENTIDADE-VISUAL.md` e
`ricy-kit/contributions/noctalia-visual-identity/tokens.json`. Use a linguagem
visual ali registrada como referência para os próximos componentes; preserve
os comportamentos aprovados e registre as adaptações realmente aplicadas.

### Como contribuir

1. Leia o documento antes de escrever e confira seus próprios archives, comandos e configurações atuais. Não apresente intenção, tentativa abandonada ou hipótese como mudança aplicada.
2. Preserve o conteúdo existente. Adicione sua contribuição ao final, sob `## Contribuição — <tema> — <data e hora>`. Identifique o chat pelo título, se conhecido; caso contrário, use uma descrição do trabalho, sem inventar um identificador.
3. Explique o objetivo, o estado anterior e o resultado final. Separe alterações concluídas, tentativas descartadas e trabalho pendente. Registre também mudanças de outros temas além do Noctalia.
4. Inclua caminhos, pacotes e versões observadas, configurações finais, comandos em ordem de execução, dependências, serviços, autostart e efeitos sobre o restante do sistema. Explique como testar e como desfazer cada alteração.
5. Distingua os caminhos desta máquina dos caminhos portáveis. Use `$HOME` nos comandos destinados à outra instalação. IDs de desktop, monitor, usuário, atalhos e backups precisam ser capturados no destino, não reutilizados cegamente.
6. Se depender de scripts, temas ou archives binários, copie somente os materiais necessários para `/home/delta/ricy-kit/contributions/<tema>/` e descreva como instalá-los. Preserve a licença dos archives de terceiros. Não mova os archives ativos nem altere serviços para preparar a documentação.
7. Não sobrescreva archives de outro chat no kit. Não inclua senhas, tokens, chaves, histórico de clipboard, conversas privadas ou backups pessoais completos. Informe a localização de backups existentes e forneça um procedimento para gerar novos no destino.
8. Se sua alteração substitui uma configuração documentada, registre explicitamente o que foi substituído e qual é o estado final. Corrija apenas o trecho necessário com evidência; não reescreva o relato de outro chat por suposição.
9. Registre os testes realmente executados e suas limitações. Se não houver evidência suficiente no contexto disponível, indique a lacuna; não invente comandos ou resultados. A migração documentada não significa que já foi testada em outro computador.
10. Ao terminar, informe o tópico acrescentado e os archives incluídos no kit. Não execute novamente as mudanças no sistema: esta contribuição é de documentação.

### Evitar conflito entre chats

Prepare sua seção em um arquivo temporário e acrescente-a sem regravar todo o documento. Use o mesmo bloqueio para qualquer escrita no registro:

```bash
# Substitua pelo caminho real do arquivo com sua contribuição pronta:
contribuicao="/tmp/ricy-contribuicao-TEMA.md"
flock "$HOME/.ricy-documentacao.lock" bash -c 'cat -- "$1" >> "$2"' _ "$contribuicao" "$HOME/ricy.md"
```

O bloqueio coordena apenas os chats que seguirem esta instrução. Para uma correção pontual, releia o arquivo dentro do bloqueio antes de gravar. Use subpastas distintas no kit. Se incluir novos archives, atualize `SHA256SUMS` sob o mesmo bloqueio, mantendo as entradas existentes; verifique os hashes antes de considerar os materiais prontos. O preparador de migração muda os caminhos dos `.desktop`, portanto seus hashes devem ser conferidos antes de executar a preparação.

### Estrutura sugerida da contribuição

```markdown
## Contribuição — TEMA — DATA E HORA

Chat/trabalho: ...
Objetivo e resultado final: ...

### Mudanças aplicadas
- Arquivo/serviço/pacote: estado anterior, mudança e motivo.

### Reproduzir em outro CachyOS
Pré-requisitos, versões observadas, backups locais e comandos em ordem.
Configurações finais e materiais em ricy-kit/contributions/TEMA/.

### Verificação
Testes executados, resultados e limitações.

### Restaurar
Comandos e archives necessários; o que a restauração cobre.

### Tentativas descartadas e pendências
Somente quando relevantes para evitar repetir um erro ou assumir algo incompleto.
```

---

## 1. Resultado e escopo

Mantivemos a sessão KDE Plasma/Wayland e o KWin. O Noctalia substitui os painéis, o menu e a busca, enquanto o Plasma continua responsável pelo desktop e wallpaper. O objetivo foi continuidade visual, sobriedade, ícones legíveis e controles acessíveis, sem recompilar nem alterar o código-fonte do Noctalia.

| Elemento | Estado final |
|---|---|
| Taskbar | Inferior, 44 px, zona reservada; janelas maximizadas respeitam sua altura |
| Visibilidade | Sempre visível; auto-hide e smart-auto-hide desligados |
| Aplicativos | Ícones à esquerda, indicador ativo, somente workspace atual, sem títulos |
| Tray | À direita; gaveta com 3 colunas e ícones de 24 px |
| Rede e volume | Somente ícones; sem SSID e sem porcentagem |
| Busca | Super, Super+Espaço e digitação no desktop; topo central, encaixada na borda |
| Apoio da busca | Barra superior vazia de 10 px, sem reserva de espaço; só aparece com busca por atalho/adaptador |
| Ponteiro no topo | Não revela a barra de apoio |
| Área de transferência | Super+V abre/fecha histórico do Noctalia no centro |
| Cores | Paleta KDE/Catppuccin Mocha com acento Mauve |
| Blur | KWin no fundo escuro da barra e painéis compatíveis, opacidade 0,70 |
| Menus Qt/KDE | Variante Kvantum KDE-Noctalia, compacta, arredondada, opaca |
| Wallpaper | Preservado pelo Plasma; wallpaper do Noctalia desativado |

A solicitação inicial de barra adaptativa foi testada, mas o estado aprovado mantém a barra inferior fixa com área reservada. Não descrever este estado como ocultação inteligente. O botão launcher da barra ainda pode usar sua própria âncora inferior; a abertura no topo é garantida pelos atalhos e pelo adaptador de digitação.

## 2. Ambiente de referência

Versões observadas neste computador: `noctalia 5.2.1-1.1`, `plasma-desktop 6.7.5-1.1`, `kwin 6.7.5-3.1`, `kvantum 1.1.8-1.1`, `python-gobject 3.58.0-1`, `qt6-tools 6.12.0-1.1`. São versões de referência, não uma promessa de compatibilidade com versões futuras. O Noctalia usado aqui é o binário do pacote CachyOS; configurações de versões antigas baseadas em QML não devem ser misturadas com este TOML.

O pacote `qt6-tools` fornece `qdbus6`; `glib2` fornece `gdbus`; Python com PyGObject fornece `Gio` e `GLib`. `wl-clipboard` é opcional para o método do adaptador que lê o texto já copiado; o histórico normal é do próprio Noctalia. Noto Sans é a fonte do Noctalia; JetBrainsMono Nerd Font de 10 pt era a fonte do KDE, Papirus-Dark o tema de ícones e Breeze a decoração das janelas. Esses três últimos eram a base visual existente, não mudanças necessárias à integração.

## 3. Instalação e preparação no novo CachyOS

Use uma sessão KDE Plasma **Wayland**. Copie `ricy-kit` para a home do usuário de destino. Não copie o backup de restauração da máquina antiga, IDs de monitores, IDs de desktops ou os JSON de atalhos antigos para o destino. O kit entregue não inclui esses archives pessoais.

Instale os componentes disponíveis nos repositórios do seu CachyOS:

```bash
sudo pacman -Syu
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts papirus-icon-theme
# Opcional para displayWithClipboardContents:
sudo pacman -S --needed wl-clipboard
```

Se o repositório não oferecer `noctalia`, resolva a disponibilidade do pacote correspondente à versão documentada antes de continuar. Não substitua automaticamente por outra implementação da shell.

Prepare o kit **antes de alterar o estilo ou iniciar o teste**:

```bash
cd "$HOME/ricy-kit"
python preparar-ambiente.py
```

O preparador cria um backup do DESTINO, registra hashes, gera a restauração do wallpaper com IDs locais, copia o perfil isolado, guarda o estilo anterior e recalcula `Exec=` dos atalhos para o usuário atual. Ele se recusa a sobrescrever um backup já existente. Após começar o teste, use `iniciar-teste.sh` para repeti-lo.

Se o wallpaper do destino já é o desejado, ele será preservado. Para reproduzir a imagem deste computador, escolha previamente no Plasma `/usr/share/wallpapers/cachyos-wallpapers/limine-splash.png`, caso essa imagem exista na instalação. O desktop inicial também tinha uma referência antiga a `north.png`; ela não deve ser aplicada indiscriminadamente a todos os monitores.

## 4. Cores, estilo KDE e menus

A paleta do Noctalia foi extraída das cores ativas do KDE. Principais valores:

| Papel | Cor |
|---|---|
| Fundo escuro | `#181825` |
| Texto | `#cdd6f4` |
| Cards/menus | `#313244` |
| Texto secundário | `#a6adc8` |
| Acento | `#cba6f7` |
| Seleção/hover | `#977dba`, texto preto |
| Contorno | `#46485c` |
| Sucesso | `#a6e3a1` |
| Erro | `#f38ba8` |

O kit contém `KDE-Noctalia.colors`, exportado somente dos grupos de cores efetivamente ativos, e a variante Kvantum completa. Assim não é necessário importar todo o `kdeglobals` antigo com preferências pessoais.

```bash
mkdir -p "$HOME/.local/share/color-schemes" "$HOME/.config/Kvantum"
cp "$HOME/ricy-kit/outputs/kde-outlines/KDE-Noctalia.colors" "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
cp -a "$HOME/ricy-kit/outputs/kde-outlines/KDE-Noctalia" "$HOME/.config/Kvantum/"
printf '[General]\ntheme=KDE-Noctalia\n' > "$HOME/.config/Kvantum/kvantum.kvconfig"
kwriteconfig6 --file kdeglobals --group KDE --key widgetStyle kvantum
```

Reabra os aplicativos Qt para atualizar o estilo; uma nova sessão também aplica a alteração. A variante parte de [Catppuccin Kvantum](https://github.com/catppuccin/kvantum), com licença MIT incluída. Modificamos o SVG de `menu-normal` para cantos de 12 px, fundo `#313244` e borda `#46485c`; `menuitem-normal` ganhou cantos de 6 px e preenchimento `#977dba`. No `.kvconfig`, margens verticais de texto são zero, moldura vertical dos itens 4 px, laterais 6 px, margem lateral do texto 2 px, altura mínima 24 e separador 5 px. `popup_blurring=false`, `reduce_menu_opacity=0` e `shadowless_popup=true` evitam o retângulo de blur fora dos cantos.

A fonte dos menus foi mantida/restaurada para 10 pt. Se quiser a mesma fonte, instale JetBrainsMono Nerd Font e selecione-a no KDE; não force uma fonte ausente. Os menus Qt renderizados pelo aplicativo e os menus próprios do Noctalia são componentes distintos. O Kvantum ajusta os primeiros; não reduz por si só menus desenhados internamente pelo Noctalia.

O script `gerar-variante-kvantum.py` registra como a variante foi construída. Para regenerá-la, coloque o checkout Catppuccin em `work/catppuccin-kvantum`, execute o script na raiz do kit e confira o resultado. Ele também instala a variante local; não é necessário executá-lo para usar os archives prontos.

## 5. Perfil isolado do Noctalia

Estrutura do kit:

```text
~/ricy-kit/
  preparar-ambiente.py
  gerar-variante-kvantum.py
  outputs/noctalia-test/     scripts, TOML, paleta, atalhos e backup do destino
  outputs/kde-outlines/     SVG, Kvantum, paleta KDE e restauração de estilo
  work/noctalia-profile/
    config/noctalia/config.toml
    config/noctalia/palettes/KDE-Atual.json
    state/                   estado isolado gerado no destino
```

`NOCTALIA_CONFIG_HOME` aponta para `work/noctalia-profile/config`; `NOCTALIA_STATE_HOME` aponta para `work/noctalia-profile/state`. Usar o item padrão “Noctalia” do pacote pode abrir outro perfil. Use o script do kit.

A paleta JSON precisa conter também o objeto `terminal`, exigido pelo validador da versão usada, mesmo com templates de terminal desativados.

### Configuração TOML final completa

```toml
[shell]
font_family = "Noto Sans"
setup_wizard_enabled = false
clipboard_enabled = true
screen_time_enabled = false
polkit_agent = false
corner_radius_scale = 1.3

[shell.launcher]
compact = true
sort_by_usage = true
fetch_exchange_rates = false

[bar.default]
position = "bottom"
layer = "top"
thickness = 44
scale = 1.5
font_scale = 0.85
auto_hide = false
smart_auto_hide = false
reserve_space = true
show_on_workspace_switch = false
margin_ends = 0
margin_edge = 0
radius = 6
radius_top_left = 6
radius_top_right = 6
radius_bottom_left = 0
radius_bottom_right = 0
concave_edge_corners = false
background_opacity = 0.70
compositor_blur = true
start = ["launcher", "taskbar"]
center = []
end = ["tray", "volume", "network", "clock", "control-center"]

[widget.taskbar]
scale = 0.666667
icon_scale = 1.725
item_spacing = 6
only_active_workspace = true
show_all_outputs = false
show_active_indicator = true
show_window_title = false

[wallpaper]
enabled = false

[backdrop]
enabled = false

[desktop_widgets]
enabled = false

[dock]
enabled = false

[lockscreen]
enabled = false

[osd]
enabled = false

[weather]
enabled = false

[theme]
mode = "dark"
source = "custom"
custom_palette = "KDE-Atual"
builtin = "Noctalia"

[theme.templates]
enable_builtin_templates = false
enable_community_templates = false
builtin_ids = []
community_ids = []

[widget.network]
show_label = false

[widget.volume]
show_label = false

[shell.panel]
clipboard_placement = "floating"
clipboard_position = "center"
launcher_placement = "attached"
launcher_position = "auto"
open_near_click_launcher = false
transparency_mode = "solid"
control_center_placement = "attached"
control_center_position = "auto"
open_near_click_control_center = true

[widget.tray]
drawer = true
drawer_columns = 3
drawer_item_size = 24
detached_panel = false

[bar]
order = ["search_edge", "default"]

[bar.search_edge]
position = "top"
enabled = true
thickness = 10
auto_hide = false
smart_auto_hide = false
reserve_space = false
show_on_workspace_switch = false
layer = "overlay"
background_opacity = 0.70
compositor_blur = true
margin_ends = 0
margin_edge = 0
padding = 0
radius = 0
radius_top_left = 0
radius_top_right = 0
radius_bottom_left = 0
radius_bottom_right = 0
concave_edge_corners = false
shadow = false
start = []
center = []
end = []
```

## 6. Explicação dos ajustes e problemas resolvidos

**Barra sobre as janelas:** ativamos `reserve_space=true` e mantivemos `layer="top"` na barra principal. A camada overlay anterior a colocava acima de overlays como captura de tela; a zona reservada faz o KWin descontar 44 px de janelas maximizadas. A faixa superior de apoio é overlay para o launcher, mas não reserva espaço.

**Ícones e menu de contexto dos apps:** escala global da barra 1,5 melhorou legibilidade, mas também ampliou o menu de contexto. `widget.taskbar.scale=0.666667` compensa a escala do menu, e `icon_scale=1.725` mantém os ícones por volta de 28 px. `corner_radius_scale=1.3` deixou o retângulo da seleção arredondado. A largura mínima ficou aproximadamente 240 px; o menu pode crescer conforme o texto.

**Tray e textos excessivos:** `network.show_label=false` oculta SSID; `volume.show_label=false` oculta a porcentagem. A gaveta do tray usa três colunas e ícones de 24 px, oferecendo uma apresentação mais compacta para os itens. Não prometemos uniformidade de menus de aplicativos que usam renderização própria.

**Continuidade da central:** `control_center_placement="attached"`, posição `auto` e `open_near_click_control_center=true` fazem a central seguir a barra/âncora de abertura e desenhar a união nativa.

**Blur só no fundo escuro:** `background_opacity=0.70`, `compositor_blur=true` e `shell.panel.transparency_mode="solid"`. O KWin aplica blur atrás da superfície; não é desfoque do texto. Cards e botões permanecem opacos. Os menus de contexto da taskbar usam opacidade interna fixa e não expõem o mesmo blur nativo nesta versão. Decidimos não modificar/recompilar o Noctalia para mudar isso.

Configuração do KWin utilizada:

```bash
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
```

Neste ambiente o protocolo Wayland de efeitos de fundo estava disponível. Se o blur não aparecer no destino, confira primeiro o efeito do KWin e o suporte entre compositor e versão do Noctalia; não suponha que apenas transparência equivale a blur.

**Digitação no desktop:** só trocar o atalho de busca não intercepta a ação do Plasma. Paramamos `plasma-krunner.service` e um adaptador assume `org.kde.krunner` no D-Bus da sessão. Ele atende `/App` (`org.kde.krunner.App`) e `/org/kde/krunner` (`org.freedesktop.Application`). A segunda interface, especialmente `ActivateAction("Query", ...)`, foi necessária para o Plasma 6.7. As consultas são encaminhadas para `noctalia msg panel-open launcher <texto>`; não são gravadas em log pelo adaptador. O adaptador está ligado ao ciclo de vida do serviço do teste.

**Super sozinha:** uma tentativa com `kwinrc/ModifierOnlyShortcuts` não funcionou neste Plasma. Usamos KGlobalAccel e transferimos Meta da ação `plasmashell / activate application launcher` para `codex-noctalia-menu.desktop / _launch`. `setForeignShortcut` é necessário para alterar uma ação pertencente a outro componente. Os códigos Qt usados são Meta `16777250`, Meta+Espaço `268435488` e Meta+V `268435542`. No atalho novo de clipboard registramos a ação e usamos também `setShortcut` antes de `setForeignShortcut`. Os JSON originais são criados no destino antes de transferir os atalhos.

**Busca no topo e união visual:** o modo floating/top_center deixava o aspecto de uma janela solta. Mudamos para attached/auto e criamos a barra vazia `search_edge` como primeira barra na ordem. Ela fornece a âncora superior sem deslocar as janelas. Inicialmente usava auto-hide e reaparecia ao tocar o topo com o ponteiro. A solução final desativa auto-hide, oculta a barra por `bar-hide search_edge`, mostra-a antes de abrir a busca e volta a ocultá-la após o fechamento. Assim a superfície oculta não recebe entrada do ponteiro. O wrapper espera 250 ms pela revelação antes da abertura; o adaptador verifica o estado a cada 250 ms para recolher a barra após Escape, clique externo ou abertura de app.

**Área de transferência:** `clipboard_enabled=true` e o atalho Super+V chama `panel-toggle clipboard`. O painel é floating/center. O histórico começa a ser retido a partir da ativação; não importamos o histórico antigo do Klipper. O atalho original do Plasma é guardado para restauração.

## 7. Iniciar, testar e retornar

Depois da preparação e dos ajustes visuais:

```bash
cd "$HOME/ricy-kit"
./outputs/noctalia-test/iniciar-teste.sh
```

O script valida o TOML, inicia `noctalia-teste.service` via systemd do usuário, aguarda IPC disponível, oculta o apoio superior, instala os itens do menu, restaura wallpaper e só então remove os painéis Plasma do layout de teste. O processo plasmashell continua ativo. Em seguida inicia o adaptador e configura os atalhos. O backup permite recuperar os painéis removidos.

Verifique:

1. As janelas maximizadas param acima da barra inferior.
2. Ícones e tray estão legíveis; Wi-Fi e volume não exibem texto.
3. Super e Super+Espaço abrem a busca no topo com união visual.
4. Ao focar o desktop e digitar, a consulta vai ao Noctalia.
5. Fechar a busca recolhe a faixa de apoio; passar o ponteiro no topo não a revela.
6. Super+V abre o histórico; copie um texto novo para verificar o registro.
7. A central continua ligada à barra inferior e o wallpaper foi preservado.

Diagnóstico:

```bash
systemctl --user status noctalia-teste.service noctalia-busca-desktop.service
noctalia msg status
journalctl --user -u noctalia-teste.service -u noctalia-busca-desktop.service -n 80 --no-pager
```

Para recarregar depois de editar o perfil efetivo:

```bash
noctalia msg config-reload
# Um reload pode recriar a barra superior; mantenha-a oculta quando a busca estiver fechada:
noctalia msg bar-hide search_edge
```

`outputs/noctalia-test/config.toml` é a cópia distribuída; o serviço lê `work/noctalia-profile/config/noctalia/config.toml`. Ao fazer ajustes permanentes, atualize ambos.

Para voltar aos painéis e atalhos Plasma:

```bash
"$HOME/ricy-kit/outputs/noctalia-test/voltar-ao-plasma.sh"
```

A restauração rápida repõe apenas `plasma-org.kde.plasma.desktop-appletsrc` e `plasmashellrc` do backup local, encerra o adaptador/Noctalia, reativa KRunner e restaura os atalhos. Ela não desfaz automaticamente paleta, fontes, blur ou Kvantum. Para restaurar o estilo de aplicativos:

```bash
"$HOME/ricy-kit/outputs/kde-outlines/restaurar-estilo-kde.sh"
```

Esse segundo script restaura widgetStyle, fonte de menu e seleção Kvantum guardados no destino. Para desfazer também a paleta e o blur, recupere seletivamente `kdeglobals` e `kwinrc` do backup, considerando quaisquer mudanças posteriores; não importe configuração completa de outra máquina.

O teste usa serviços transitórios, não uma instalação persistente no login. Existe um item de autostart de recuperação: no próximo login, se a marca `teste-ativo` existir e o serviço estiver inativo, restaura o Plasma. Para reproduzir exatamente o teste, não habilite simultaneamente o autostart padrão do Noctalia. Uma configuração definitiva de login permanece fora do que fizemos.

## 8. Arquivos de integração — conteúdo para auditoria e recriação

Os archives abaixo acompanham o kit. Os `.desktop` devem apontar para a pasta real do destino; `preparar-ambiente.py` faz essa adaptação. Os backups, marcadores e históricos de atalhos não são incluídos no kit porque devem ser gerados localmente.

### preparar-ambiente.py

```python
#!/usr/bin/env python3
"""Prepare o kit no computador de destino ANTES de iniciar o teste."""
from pathlib import Path
import tarfile, shutil, json, configparser, re, hashlib
kit=Path(__file__).resolve().parent
home=Path.home(); base=kit/'outputs/noctalia-test'; style=kit/'outputs/kde-outlines'
backup=base/'plasma-antes.tar.gz'
if backup.exists():
    raise SystemExit('Backup já existe. Use iniciar-teste.sh para repetir; não substitua seu backup original.')
paths=['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc','.config/plasmarc','.config/kdeglobals','.config/kwinrc','.config/kwinoutputconfig.json','.config/kglobalshortcutsrc','.config/kscreenlockerrc','.config/klipperrc','.config/kcminputrc','.config/gtk-3.0/settings.ini','.config/gtk-4.0/settings.ini','.config/autostart','.config/noctalia','.local/state/noctalia','.config/Kvantum']
manifest={}
with tarfile.open(backup,'w:gz') as archive:
    for rel in paths:
        p=home/rel
        if p.exists():
            archive.add(p,arcname=rel)
            manifest[rel]='directory' if p.is_dir() else hashlib.sha256(p.read_bytes()).hexdigest()
        else: manifest[rel]=None
backup.chmod(0o600)
(base/'backup-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
shutil.copy2(backup,style/'kde-antes-contornos.tar.gz')
# A restauração do wallpaper é gerada com os IDs e imagens DO DESTINO.
cfg=configparser.ConfigParser(interpolation=None,strict=False);cfg.optionxform=str
cfg.read(home/'.config/plasma-org.kde.plasma.desktop-appletsrc')
lines=[]
for section in cfg.sections():
    match=re.fullmatch(r'Containments\]\[(\d+)\]\[Wallpaper\]\[org.kde.image\]\[General',section)
    if match and 'Image' in cfg[section]:
        i=int(match[1]); image=json.dumps(cfg[section]['Image'])
        lines.append(f'var d=desktopById({i}); if(d){{d.currentConfigGroup=["Wallpaper","org.kde.image","General"];d.writeConfig("Image",{image});}}')
(base/'restaurar-wallpaper.js').write_text('\n'.join(lines)+'\n')
# Captura o estilo anterior antes de aplicar a variante local.
kg=configparser.ConfigParser(interpolation=None,strict=False);kg.optionxform=str;kg.read(home/'.config/kdeglobals')
(style/'menuFont-antes.txt').write_text(kg.get('General','menuFont',fallback=''))
(style/'widgetStyle-antes.txt').write_text(kg.get('KDE','widgetStyle',fallback=''))
kv=home/'.config/Kvantum/kvantum.kvconfig'
if kv.exists():shutil.copy2(kv,style/'kvantum-config-antes')
else:(style/'kvantum-ausente-antes').touch()
profile=kit/'work/noctalia-profile/config/noctalia';(profile/'palettes').mkdir(parents=True,exist_ok=True)
shutil.copy2(base/'config.toml',profile/'config.toml')
shutil.copy2(base/'KDE-Atual.json',profile/'palettes/KDE-Atual.json')
(kit/'work/noctalia-profile/state').mkdir(parents=True,exist_ok=True)
for name,script in [('menu','abrir-menu.sh'),('clipboard','abrir-clipboard.sh'),('voltar','voltar-ao-plasma.sh'),('recuperar','recuperar-no-login.sh')]:
    p=base/f'codex-noctalia-{name}.desktop'
    p.write_text(re.sub(r'^Exec=.*$',f'Exec="{base/script}"',p.read_text(),flags=re.M))
print('Kit preparado em',kit)
print('Backup do destino:',backup)
```

### outputs/noctalia-test/KDE-Atual.json

```json
{
  "dark": {
    "mPrimary": "#cba6f7",
    "mOnPrimary": "#11111b",
    "mSecondary": "#cba6f7",
    "mOnSecondary": "#11111b",
    "mTertiary": "#a6e3a1",
    "mOnTertiary": "#11111b",
    "mError": "#f38ba8",
    "mOnError": "#11111b",
    "mSurface": "#181825",
    "mOnSurface": "#cdd6f4",
    "mSurfaceVariant": "#313244",
    "mOnSurfaceVariant": "#a6adc8",
    "mOutline": "#46485c",
    "mShadow": "#000000",
    "mHover": "#977dba",
    "mOnHover": "#000000",
    "terminal": {
      "background": "#181825",
      "foreground": "#cdd6f4",
      "cursor": "#cba6f7",
      "cursorText": "#181825",
      "selectionBg": "#977dba",
      "selectionFg": "#000000",
      "normal": {
        "black": "#181825",
        "red": "#f38ba8",
        "green": "#a6e3a1",
        "yellow": "#f9e2af",
        "blue": "#89b4fa",
        "magenta": "#cba6f7",
        "cyan": "#94e2d5",
        "white": "#cdd6f4"
      },
      "bright": {
        "black": "#181825",
        "red": "#f38ba8",
        "green": "#a6e3a1",
        "yellow": "#f9e2af",
        "blue": "#89b4fa",
        "magenta": "#cba6f7",
        "cyan": "#94e2d5",
        "white": "#cdd6f4"
      }
    }
  }
}
```

### outputs/noctalia-test/abrir-menu.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
if ! /usr/bin/noctalia msg status | /usr/bin/python -c 'import json,sys; s=json.load(sys.stdin); sys.exit(0 if s.get("activePanelId")=="launcher" else 1)'; then
 /usr/bin/noctalia msg bar-show search_edge >/dev/null
 sleep 0.25
fi
exec /usr/bin/noctalia msg panel-toggle launcher
```

### outputs/noctalia-test/abrir-clipboard.sh

```bash
#!/usr/bin/env bash
exec /usr/bin/noctalia msg panel-toggle clipboard
```

### outputs/noctalia-test/ativar-busca-noctalia.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 printf 'Inicie o teste Noctalia primeiro.\n' >&2
 exit 1
fi
systemctl --user stop plasma-krunner.service
if ! systemctl --user is-active --quiet noctalia-busca-desktop.service; then
 if ! systemd-run --user --unit=noctalia-busca-desktop --collect --property=Type=dbus --property=BusName=org.kde.krunner --property=BindsTo=noctalia-teste.service --property=After=noctalia-teste.service /usr/bin/python "$base_dir/busca-desktop.py"; then
  systemctl --user start plasma-krunner.service
  exit 1
 fi
fi
```

### outputs/noctalia-test/busca-desktop.py

```python
#!/usr/bin/env python3
"""Adaptador temporário da interface de ativação KRunner para o Noctalia."""
import subprocess
import json
import time
from gi.repository import Gio, GLib

xml = '''<node><interface name="org.kde.krunner.App">
<method name="query"><arg type="s" direction="in"/></method>
<method name="display"/>
<method name="toggleDisplay"/>
<method name="displayWithClipboardContents"/>
<method name="displaySingleRunner"><arg type="s" direction="in"/></method>
<method name="querySingleRunner"><arg type="s" direction="in"/><arg type="s" direction="in"/></method>
</interface></node>'''

def handle(connection, sender, path, interface, method, parameters, invocation):
    values = parameters.unpack()
    term = ''
    if method == 'ActivateAction':
        action, values, platform_data = values
        if action.lower() == 'query' and values:
            term = str(values[0])
    elif method == 'query':
        term = values[0]
    elif method == 'querySingleRunner':
        term = values[1]
    elif method == 'displayWithClipboardContents':
        try:
            term = subprocess.run(['wl-paste', '--no-newline'], capture_output=True, text=True, check=True, timeout=2).stdout
        except (OSError, subprocess.SubprocessError):
            pass
    args = ['/usr/bin/noctalia', 'msg', 'panel-toggle' if method == 'toggleDisplay' else 'panel-open', 'launcher']
    if term:
        args.append(term)
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        if status.get('activePanelId') != 'launcher':
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-show', 'search_edge'], capture_output=True, check=True, timeout=2)
            time.sleep(0.25)
        subprocess.run(args, capture_output=True, check=True, timeout=5)
        invocation.return_value(GLib.Variant('()', ()))
    except (OSError, subprocess.SubprocessError):
        invocation.return_dbus_error('org.kde.krunner.NoctaliaUnavailable', 'Noctalia não está disponível')

freedesktop_xml = '<node><interface name="org.freedesktop.Application"><method name="ActivateAction"><arg type="s" direction="in"/><arg type="av" direction="in"/><arg type="a{sv}" direction="in"/></method><method name="Activate"><arg type="a{sv}" direction="in"/></method></interface></node>'
connection = Gio.bus_get_sync(Gio.BusType.SESSION, None)
info = Gio.DBusNodeInfo.new_for_xml(xml)
registration = connection.register_object('/App', info.interfaces[0], handle, None, None)
freedesktop_info = Gio.DBusNodeInfo.new_for_xml(freedesktop_xml)
freedesktop_registration = connection.register_object('/org/kde/krunner', freedesktop_info.interfaces[0], handle, None, None)
result = connection.call_sync('org.freedesktop.DBus', '/org/freedesktop/DBus', 'org.freedesktop.DBus', 'RequestName', GLib.Variant('(su)', ('org.kde.krunner', 4)), GLib.VariantType.new('(u)'), Gio.DBusCallFlags.NONE, 5000, None).unpack()[0]
if result != 1:
    raise SystemExit('O nome D-Bus do KRunner já está em uso')
# A barra de apoio não reage ao ponteiro: só os comandos de abertura a mostram.
# Ao fechar a busca (Escape, clique externo ou escolha de app), recolhemos a barra.
search_was_open = False

def sync_search_edge():
    global search_was_open
    try:
        status = json.loads(subprocess.run(['/usr/bin/noctalia', 'msg', 'status'], capture_output=True, check=True, timeout=2).stdout)
        search_open = status.get('activePanelId') == 'launcher'
        if search_was_open and not search_open:
            subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, check=True, timeout=2)
        search_was_open = search_open
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return True

subprocess.run(['/usr/bin/noctalia', 'msg', 'bar-hide', 'search_edge'], capture_output=True, timeout=2)
GLib.timeout_add(250, sync_search_edge)
GLib.MainLoop().run()
```

### outputs/noctalia-test/configurar-super.py

```python
#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'super-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=16777250
mine=['codex-noctalia-menu.desktop','_launch','Menu Noctalia (teste)','Menu Noctalia (teste)']
if not saved.exists():
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 old=[]
 for e in entries:
  if e[2]==mine[0]:continue
  old.append({'id':[e[2],e[0],e[3],e[1]],'keys':list(e[6])})
 saved.write_text(json.dumps(old,indent=2)+'\n')
original=json.loads(saved.read_text())
restore=len(sys.argv)>1 and sys.argv[1]=='restore'
if restore:
 call('setForeignShortcut','(asai)',(mine,[268435488]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setForeignShortcut','(asai)',(mine,[meta,268435488]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Não foi possível registrar Super para o Noctalia')
print('Atalho Super restaurado.' if restore else 'Super e Super+Espaço registrados para o Noctalia.')
```

### outputs/noctalia-test/configurar-clipboard.py

```python
#!/usr/bin/env python3
import json,sys
from pathlib import Path
from gi.repository import Gio,GLib
base=Path(__file__).resolve().parent
saved=base/'clipboard-atalho-original.json'
bus=Gio.bus_get_sync(Gio.BusType.SESSION,None)
def call(method,signature,args):
 return bus.call_sync('org.kde.kglobalaccel','/kglobalaccel','org.kde.KGlobalAccel',method,GLib.Variant(signature,args),None,Gio.DBusCallFlags.NONE,5000,None).unpack()
meta=268435542
mine=['codex-noctalia-clipboard.desktop','_launch','Área de transferência Noctalia (teste)','Área de transferência Noctalia (teste)']
call('doRegister','(as)',(mine,))
if not saved.exists():
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 old=[]
 for e in entries:
  if e[2]==mine[0]:continue
  old.append({'id':[e[2],e[0],e[3],e[1]],'keys':list(e[6])})
 saved.write_text(json.dumps(old,indent=2)+'\n')
original=json.loads(saved.read_text())
restore=len(sys.argv)>1 and sys.argv[1]=='restore'
if restore:
 call('setForeignShortcut','(asai)',(mine,[]))
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],entry['keys']))
else:
 for entry in original:
  call('setForeignShortcut','(asai)',(entry['id'],[k for k in entry['keys'] if k!=meta]))
 call('setShortcut','(asaiu)',(mine,[meta],2))
 call('setForeignShortcut','(asai)',(mine,[meta]))
 entries=call('getGlobalShortcutsByKey','(i)',(meta,))[0]
 if not any(e[2]==mine[0] for e in entries):raise SystemExit('Não foi possível registrar Super+V para o Noctalia')
print('Super+V restaurado.' if restore else 'Super+V registrado para o Noctalia.')
```

### outputs/noctalia-test/iniciar-teste.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
workspace_dir="$(dirname "$(dirname "$base_dir")")"
export NOCTALIA_CONFIG_HOME="$workspace_dir/work/noctalia-profile/config"
export NOCTALIA_STATE_HOME="$workspace_dir/work/noctalia-profile/state"
noctalia config validate
if ! systemctl --user is-active --quiet noctalia-teste.service; then
 systemctl --user reset-failed noctalia-teste.service 2>/dev/null || true
 systemd-run --user --unit=noctalia-test --collect --setenv="NOCTALIA_CONFIG_HOME=$NOCTALIA_CONFIG_HOME" --setenv="NOCTALIA_STATE_HOME=$NOCTALIA_STATE_HOME" /usr/bin/noctalia
fi
ready=false
for i in {1..30}; do
 if noctalia msg status >/dev/null 2>&1; then ready=true; break; fi
 sleep 0.3
done
if [ "$ready" != true ]; then
 systemctl --user stop noctalia-teste.service || true
 printf 'Noctalia não iniciou; os painéis do Plasma foram preservados.\n' >&2
 exit 1
fi
noctalia msg bar-hide search_edge >/dev/null
mkdir -p "$HOME/.local/share/applications" "$HOME/.config/autostart"
cp "$base_dir/codex-noctalia-menu.desktop" "$base_dir/codex-noctalia-voltar.desktop" "$base_dir/codex-noctalia-clipboard.desktop" "$HOME/.local/share/applications/"
cp "$base_dir/codex-noctalia-recuperar.desktop" "$HOME/.config/autostart/"
kbuildsycoca6 --noincremental >/dev/null 2>&1
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.doRegister '["codex-noctalia-menu.desktop", "_launch", "Menu Noctalia (teste)", "Menu Noctalia (teste)"]' >/dev/null
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.setShortcut '["codex-noctalia-menu.desktop", "_launch", "Menu Noctalia (teste)", "Menu Noctalia (teste)"]' '[268435488]' 2 >/dev/null
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "$(cat "$base_dir/restaurar-wallpaper.js")"
touch "$base_dir/teste-ativo"
qdbus6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'panels().forEach(p => p.remove()); print("Painéis do Plasma recolhidos para o teste.")'
"$base_dir/ativar-busca-noctalia.sh"
python "$base_dir/configurar-super.py"
python "$base_dir/configurar-clipboard.py"
printf 'Teste iniciado. Para voltar, execute voltar-ao-plasma.sh nesta pasta.\n'
```

### outputs/noctalia-test/voltar-ao-plasma.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python "$base_dir/configurar-super.py" restore
python "$base_dir/configurar-clipboard.py" restore
systemctl --user stop noctalia-busca-desktop.service 2>/dev/null || true
systemctl --user start plasma-krunner.service
systemctl --user stop noctalia-teste.service 2>/dev/null || true
systemctl --user stop plasma-plasmashell.service
python - "$base_dir" <<'PY'
import sys,tarfile,os
from pathlib import Path
base=Path(sys.argv[1]); home=Path.home()
with tarfile.open(base/'plasma-antes.tar.gz') as t:
 for rel in ['.config/plasma-org.kde.plasma.desktop-appletsrc','.config/plasmashellrc']:
  data=t.extractfile(rel).read(); dest=home/rel
  tmp=dest.with_name(dest.name+'.noctalia-restore'); tmp.write_bytes(data); os.replace(tmp,dest)
PY
systemctl --user start plasma-plasmashell.service
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.unregister codex-noctalia-menu.desktop _launch >/dev/null 2>&1 || true
gdbus call --session --dest org.kde.kglobalaccel --object-path /kglobalaccel --method org.kde.KGlobalAccel.unregister codex-noctalia-clipboard.desktop _launch >/dev/null 2>&1 || true
rm -f "$HOME/.local/share/applications/codex-noctalia-clipboard.desktop" "$HOME/.local/share/applications/codex-noctalia-menu.desktop" "$HOME/.local/share/applications/codex-noctalia-voltar.desktop" "$HOME/.config/autostart/codex-noctalia-recuperar.desktop"
kbuildsycoca6 --noincremental >/dev/null 2>&1
rm -f "$base_dir/teste-ativo"
printf 'Painéis originais do Plasma restaurados.\n'
```

### outputs/noctalia-test/recuperar-no-login.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$base_dir/teste-ativo" ] && ! systemctl --user is-active --quiet noctalia-teste.service; then
 "$base_dir/voltar-ao-plasma.sh"
fi
```

### outputs/noctalia-test/codex-noctalia-menu.desktop

```ini
[Desktop Entry]
Type=Application
Name=Menu Noctalia (teste)
Exec="/home/delta/ricy-kit/outputs/noctalia-test/abrir-menu.sh"
Icon=noctalia
Categories=Utility;
X-KDE-Shortcuts=Meta+Space
```

### outputs/noctalia-test/codex-noctalia-clipboard.desktop

```ini
[Desktop Entry]
Type=Application
Name=Área de transferência Noctalia (teste)
Exec="/home/delta/ricy-kit/outputs/noctalia-test/abrir-clipboard.sh"
Icon=edit-paste
Categories=Utility;
X-KDE-Shortcuts=Meta+V
```

### outputs/noctalia-test/codex-noctalia-voltar.desktop

```ini
[Desktop Entry]
Type=Application
Name=Voltar ao Plasma
Exec="/home/delta/ricy-kit/outputs/noctalia-test/voltar-ao-plasma.sh"
Icon=noctalia
Categories=Utility;
```

### outputs/noctalia-test/codex-noctalia-recuperar.desktop

```ini
[Desktop Entry]
Type=Application
Name=Restaurar Plasma após teste Noctalia
Exec="/home/delta/ricy-kit/outputs/noctalia-test/recuperar-no-login.sh"
OnlyShowIn=KDE;
X-KDE-autostart-phase=2
```

## 9. Origens e registro histórico

Código consultado para confirmar comportamentos: [Noctalia](https://github.com/noctalia-dev/noctalia), [Kvantum](https://github.com/tsujan/Kvantum), [Catppuccin Kvantum](https://github.com/catppuccin/kvantum), além das interfaces do Plasma/KWin locais. A documentação aqui registra o que foi observado e configurado nesta sessão; os links são as origens dos projetos, não uma verificação da versão mais recente da web.

Neste computador, os archives ativos originais estão em `/home/delta/Documents/Codex/2026-10-08/no-x20/outputs/noctalia-test` e o perfil ativo em `work/noctalia-profile` da mesma pasta. Os archives do kit são uma cópia de migração: criá-los não moveu nem reconfigurou a sessão atual.

Etapas percorridas: teste com backup → preservação do wallpaper e Plasma ativo → correção de camada/zona exclusiva → aumento de ícones → paleta KDE → compactação e arredondamento de menus → ocultação de SSID/volume → central attached → blur do fundo → menus Qt/Kvantum → tray com gaveta → substituição da busca do desktop → correção da tecla Super pelo KGlobalAccel → busca no topo com continuidade → apoio sem reação ao ponteiro → Super+V.

Os testes intermediários de busca central e floating/top_center foram substituídos pelo arranjo attached descrito aqui. A opacidade final é 0,70, não 0,80. Não modificamos profundamente a shell nem recompilamos o Noctalia. A indisponibilidade inicial dos controles motivou preservar o Plasma ativo e uma barra principal fixa acessível; não depende de encerrar o ambiente desktop inteiro.

## 10. Integridade e transporte

O arquivo `ricy-kit/SHA256SUMS` identifica os archives distribuídos. Confira antes de preparar no destino:

```bash
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
```

Após executar o preparador alguns `.desktop` mudam de caminho, então seus hashes deixam de corresponder ao pacote original. Para transporte, copie a pasta inteira `ricy-kit` e este `ricy.md`; SVG, licença, scripts e TOML devem viajar juntos. O SVG Kvantum completo fica no kit para evitar uma reprodução parcial apenas por descrição.

## Contribuição — Integração Noctalia/KDE e menus compactos — 2026-10-08 17:19 (America/Sao_Paulo)

Chat/trabalho: teste reversível do Noctalia sobre KDE Plasma, continuidade visual e ajustes dos menus Qt/Kvantum. Título do chat não confirmado. Esta contribuição complementa o roteiro anterior com a conferência dos archives ativos, a correção da atualização do estilo em memória e materiais portáveis separados. Não houve reaplicação de mudanças durante esta etapa de documentação.

### Objetivo, mudanças aplicadas e estado conferido

O KDE inicialmente usava seu menu, taskbar e busca, com paleta Catppuccin Mocha Mauve, fonte JetBrainsMono Nerd Font de 10 pt e decoração Breeze. A solicitação foi experimentar Noctalia com controles acessíveis, wallpaper preservado e possibilidade de voltar, depois aproximar o formato e a compactação dos menus KDE do Noctalia.

1. **Noctalia e reversão:** pacote `noctalia 5.2.1-1.1`, perfil isolado sob `work/noctalia-profile`, scripts em `outputs/noctalia-test`, unidade transitória `noctalia-teste.service`. Os painéis Plasma foram removidos do layout do teste após o Noctalia estar pronto; plasmashell permanece ativo. Backup inicial, manifesto e retorno ao Plasma foram preparados. O autostart instalado é de **recuperação**, não de inicialização automática do Noctalia. Não houve recompilação ou alteração de código do Noctalia.
2. **Área útil:** barra inferior de 44 px, camada top, `reserve_space=true`; as tentativas anteriores com overlay e ocultação inteligente foram substituídas. Estado final sempre visível, sem auto-hide ou smart-auto-hide. Escala 1,5, font_scale 0,85; taskbar scale 0,666667, icon_scale 1,725, item_spacing 6. Esses valores compensam a ampliação dos menus enquanto mantêm os ícones legíveis.
3. **Tray, painéis e cores:** rede/volume sem textos (`show_label=false`); gaveta do tray 3 colunas/24 px; central attached/auto perto da âncora. Paleta customizada `KDE-Atual.json` com terminal obrigatório no formato da versão usada. Fundo da barra 0,70 com compositor_blur; cards/painéis sólidos. KWin: blurEnabled true, BlurStrength 5, NoiseStrength 2. Wallpaper permanece sob Plasma, com recursos de wallpaper/backdrop/dock/lockscreen/osd/templates do Noctalia desligados nesta integração.
4. **Busca:** implementado adaptador Python/Gio para `org.kde.krunner`, tanto `/App` quanto `/org/kde/krunner`. Atender `ActivateAction("Query", …)` foi necessário após o usuário relatar que digitar não abria a busca. O teste deste trabalho foi inicialmente floating/center. **Isso foi substituído no estado atual conferido** por launcher attached/auto e apoio superior `search_edge` de 10 px sem reserva de espaço, além de wrappers Super/Super+Espaço e clipboard Super+V. Essa evolução já está descrita no corpo anterior de ricy.md; as cópias desta contribuição refletem os archives atuais, não atribuem uma execução nova durante esta documentação.
5. **KDE/Kvantum:** instalado `kvantum 1.1.8-1.1` via `pkexec pacman -S --needed --noconfirm kvantum`. Criada variante local Catppuccin MIT, instalada em `$HOME/.config/Kvantum/KDE-Noctalia`, selecionada em `kvantum.kvconfig`; `kdeglobals/KDE/widgetStyle=kvantum`. Antes, a chave direta não existia e Breeze era herdado de kdedefaults. A configuração Kvantum anterior selecionava `Catppuccin-Mocha-Mauve-Glass`; ela foi guardada. Não alteramos a decoração externa Breeze, nem as fontes gerais do KDE.
6. **Geometria e fonte finais dos menus:** SVG completo com canto externo 12 px, fundo #313244, contorno #46485c e seleção #977dba; SVG da seleção com raio 6 px. Moldura vertical dos itens 4 px/lateral 6 px, margem de texto vertical 0/lateral 2 px, min_height 24, separador 5. `spread_menuitems=false`, `shadowless_popup=true`, `menu_shadow_depth=0`, `popup_blurring=false`, `reduce_window_opacity=0`, `reduce_menu_opacity=0`. Fonte dos menus restaurada a 10 pt. O teste nativo produziu linhas de 26 px; min_height não é uma garantia de altura real de 24 px.
7. **Atualização efetiva nos aplicativos:** o usuário relatou que a compactação parecia voltar e os cantos ainda tinham um retângulo. Confirmamos que o Dolphin estava aberto desde antes dos últimos ajustes. O código da integração Plasma/Qt só chama `setStyle` se o nome muda; simplesmente emitir StyleChanged com Kvantum já ativo não força reler o tema. Efetuamos a alternância temporária Breeze → Kvantum com sinal `/KGlobalSettings`, `org.kde.KGlobalSettings.notifyChange(2,0)`. Para fontes, o sinal correto é `/KDEPlatformTheme`, `org.kde.KDEPlatformTheme.refreshFonts()`. O envio anterior de notifyChange(0,0) era de paleta, não de fonte. O script portável `recarregar-estilo.py` registra a sequência corrigida, com flush do D-Bus e intervalo de 0,5 s.

Conferência ao documentar: `noctalia-teste.service`, `noctalia-busca-desktop.service` e `plasma-plasmashell.service` ativos; `plasma-krunner.service` inativo; nome `org.kde.krunner` pertence ao processo Python do adaptador; `panels().length=0`. O perfil TOML ativo coincide byte a byte com a cópia em outputs; SVG/kvconfig ativos coincidem com a variante de outputs. `menuFont` é JetBrainsMono Nerd Font, 10 pt; widgetStyle Kvantum; tema KDE-Noctalia. Desktop entries menu/clipboard/voltar presentes em `.local/share/applications`; recuperação presente em `.config/autostart`.

Pacotes conferidos: Plasma Desktop 6.7.5-1.1, KWin 6.7.5-3.1, python-gobject 3.58.0-1, qt6-tools 6.12.0-1.1, python-pyqt6 6.11.0-4, noto-fonts 1:2026.10.01-1. `pacman -Q papirus-icon-theme` não encontrou esse nome de pacote; Papirus-Dark é uma preferência visual previamente existente, não uma instalação comprovada deste chat nem dependência do roteiro. Qt 5 e interfaces próprias de aplicativos não estão cobertos pelo estilo Qt 6 instalado.

### Materiais e reprodução em outro CachyOS

Pasta independente: `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/`. Seu `README.md` contém a sequência completa. Não execute esta cópia e a cópia da raiz do kit ao mesmo tempo: compartilham unidades e IDs de shortcuts.

Arquivos incluídos: `preparar-destino.py`, `aplicar-estilo.sh`, `recarregar-estilo.py`, `restaurar-estilo-e-blur.py`, `verificar-menu-nativo.py`, README; em `outputs/kde-outlines/`, esquema público de cores, SVG/kvconfig completos e licença MIT; em `outputs/noctalia-test/`, TOML/paleta e scripts de início/volta/recuperação, ativação da busca, adaptador D-Bus, wrappers de abertura, configuração de atalhos e quatro modelos `.desktop`.

Os `.desktop` distribuídos usam placeholders e são recalculados no destino. O preparador captura layout, wallpaper, fonte, estilo, blur e Kvantum **do destino**, gera backup 0600 e recusa sobrescrevê-lo. IDs de desktop são obtidos localmente. Arquivos de atalhos originais são criados ao ativar e protegidos em 0600. Não incluímos backups pessoais, sentinela ativa, estado/clipboard do Noctalia, fotos, conversas, SSID, caches Python ou capturas reais do desktop.

Sequência resumida, após copiar documento e kit e conferir `sha256sum -c SHA256SUMS` na raiz:

```bash
sudo pacman -S --needed noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python preparar-destino.py
./aplicar-estilo.sh
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/iniciar-teste.sh
```

`python-pyqt6` é opcional para o teste nativo; `wl-clipboard` é opcional para o método query que usa texto já copiado. O kit preserva a família de fonte do usuário do destino e ajusta menuFont a 10 pt; não impõe uma família ausente. Aplicar `KDE-Noctalia.colors` via plasma-apply-colorscheme é opção de migração explicada no README, **não** mudança aplicada ao KDE neste chat: a paleta já existia. O TOML atual completo está na cópia, evitando reconstruir somente a partir dos valores resumidos.

### Verificação realmente executada e limites

- Durante a configuração: validação da paleta/TOML e IPC, conferência das zonas reservadas; preservação/retorno do Plasma testados no ciclo inicial; chamadas D-Bus Query verificadas; acompanhamento visual do usuário confirmou tamanho de ícones, paleta e formato arredondado. O usuário também relatou falhas, portanto não tratamos todo ajuste intermediário como aprovado.
- Menus: prévias Qt offscreen mostraram seleção/contorno e permitiram corrigir lacunas no SVG. A primeira prévia forçava WA_TranslucentBackground; ela **não** comprovava o comportamento automático dos aplicativos.
- Teste posterior em sessão Wayland: novo QMenu **sem forçar** esse atributo, estilo kvantum, transparência ativada pelo estilo, fonte 10 pt, cinco linhas de 26 px, alfa do canto 0. Também foi conferido alfa 0 nos quatro cantos/255 no centro da prévia. Isso comprova pixels transparentes do widget de teste, não a composição final em todos os programas.
- Após o último relato de cantos preenchidos/escala antiga: atualização correta de fontes e alternância real Breeze/Kvantum executadas nos aplicativos abertos. Captura posterior mostrava desktop/apps, mas o menu de contexto não estava aberto. **Não houve confirmação visual final do usuário do menu Dolphin após essa recarga.** Assim, o trecho anterior que associa popup_blurring=false a evitar o retângulo deve ser lido como configuração/hipótese técnica aplicada, não como prova final de resolução universal.
- Nesta documentação: comparação dos archives ativos e serviços sem mudar configuração; validação estática de todos os scripts Python/Bash, TOML e JSON. Preparador executado apenas em cópia descartável com HOME fictícia: verificou backup 0600, wallpaper/IDs locais, `.desktop` portável e recusa de segunda preparação. Não executamos os novos scripts de aplicação/reversão na sessão real. Migração para outro CachyOS não foi testada.

### Desfazer e backups existentes

Nesta máquina, os backups pessoais permanecem em `/home/delta/Documents/Codex/2026-10-08/no-x20/outputs/noctalia-test/plasma-antes.tar.gz` e `outputs/kde-outlines/kde-antes-contornos.tar.gz` da mesma pasta; não foram transportados para a contribuição. `menuFont-antes.txt` e `kvantum-config-antes` são os valores históricos locais. Os scripts locais originais são específicos deste estado de origem.

No destino preparado com esta contribuição:

```bash
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
./outputs/noctalia-test/voltar-ao-plasma.sh
python restaurar-estilo-e-blur.py
```

A primeira operação restaura painéis/plasmashellrc capturados e os atalhos locais, reinicia KRunner e remove os launchers/autostart do teste. A segunda restaura apenas as chaves de fonte, widgetStyle e blur e a configuração/tema Kvantum anterior. Se já usava Kvantum, recarrega o estilo restaurado. Não remove os pacotes. O esquema opcional de cores exige selecionar o esquema anterior ou restaurar kdeglobals do backup local (procedimento no README, com a ressalva de substituir preferências posteriores). O histórico produzido durante o teste no destino não é apagado automaticamente.

### Tentativas descartadas e pendências

- Smart-hide/overlay iniciais comprometeram acesso/posição da barra; substituídos por barra principal fixa top com reserva. Não encerrar a sessão Plasma inteira para executar a integração.
- Menus de taskbar gigantes foram compensados com escala local; menus do tray, colocados na gaveta. Não modificar código do Noctalia para blur no contexto, conforme pedido explícito do usuário.
- Aumento do menuFont 10 → 11 pt foi interpretação incorreta do pedido e foi revertido. A compactação envolve fonte **e** padding do tema.
- Primeiros SVGs com borda em stroke deixaram falhas de recorte nos cantos; substituídos por preenchimentos com limites exatos. Ativos do kit contêm a variante corrigida.
- Desativar popup blur sozinho não demonstrou resolver o relato; foi necessário investigar o cache do estilo e o sinal de fontes. Mantemos como pendência a confirmação final sobre menus reais e a validação no computador de destino.
- Busca central inicial não é o estado atual: cópia atual attached/top com search_edge já documentada acima. Nenhuma mudança adicional do perfil foi aplicada só para documentar.

Origem e licença: Catppuccin Kvantum MIT, checkout consultado `71105d224fef95dd023691303477ce3eea487457`. Código de investigação: Kvantum `110aff8b97a221531ef55acc4faeacfd719cdfea`; Plasma Integration `46eddde9d38cf907786e567dd4a942140bb1f797`. São revisões consultadas, não identificação comprovada do código exato dos pacotes instalados. Ativos prontos permitem reproduzir sem compilação.

## Contribuição — Instalador DEB/RPM no Dolphin — 2026-10-08 17:31 (America/Sao_Paulo)

Chat/trabalho: suporte a DEB/RPM no CachyOS, integração de duplo clique com Dolphin e correções da conversão do Parsec. Título do chat não confirmado. Esta etapa apenas documentou, conferiu o estado e preparou materiais; não reinstalou pacotes, alterou associações ativas ou corrigiu pendências do sistema.

### Objetivo, estado anterior e mudanças aplicadas

O pedido era abrir pacotes `.deb` e `.rpm` no Dolphin e instalar no próprio CachyOS. Inicialmente havia pacman e bsdtar; dpkg/rpm/debtap não estavam disponíveis, e ambos os tipos de arquivo abriam com `org.kde.ark.desktop`. A primeira resposta instalou só ferramentas de terminal, o que não atendia ao fluxo gráfico esperado. Depois da correção do escopo, o usuário escolheu instalação no próprio CachyOS quando compatível, sem ambiente Ubuntu/Fedora.

1. **Pacotes instalados por este trabalho, confirmados no pacman.log:** `dpkg 1.23.11-1.1`, `rpm-tools 6.0.1-2.2`; dependências `nettle3 3.10.2-2.1`, `rpm-sequoia 1.10.3-1.1`; `namcap 3.6.0-3` com `python-boolean.py 5.0-2`, `python-license-expression 30.4.4-2`, `python-pyelftools 0.33-1`; `debtap 3.6.3-1` construído do AUR; `python-pyqt6 6.11.0-4`, `python-pyqt6-sip 13.13.0-1.1` para a interface. `binutils 2.47-2`, `fakeroot 1:1.37.2-3.1`, `pkgfile 26-1.1`, Git e base-devel já existiam; não atribuir sua instalação a este chat. O checkout AUR preservado tem revisão `d7c54a59fa0e3ac99a13f5db594de172aca0b1f4`; fontes e debtap.install passaram na verificação SHA-512 de makepkg.
2. **Bases do conversor:** inicialização com privilégios em `/var/cache/pkgfile` e `/var/cache/debtap`. A primeira tentativa demorou no servidor Ubuntu, foi encerrada e repetida com wrapper curl IPv4, timeout de conexão 15 s e total 180 s. Os índices Debian/Ubuntu, lista AUR, virtual packages e extended-base-packages-list foram criados; sincronização reportou sucesso. Isso não tornou dpkg/rpm instaladores nativos do CachyOS. O upstream ainda usa HTTP/`curl -k`, registrado como limitação.
3. **Aplicativo local:** `/home/delta/.local/share/cachyos-package-installer/backend.py`, `installer.py`, `normalize_control.py` e cópia executável `debtap`; README local. PyQt6 abre uma janela, converte automaticamente se receber arquivo, confere metadados e transação via `pacman -Qip`/`pacman -Up`; só então oferece **Instalar**. Esse botão executa `pkexec /usr/bin/pacman -U --noconfirm`, exibindo autenticação Polkit. Conversão não usa root, dpkg -i, rpm -i, --nodeps ou --overwrite. `conversion.lock` serializa as conversões desta aplicação; archives intermediários/output ficam em `/home/delta/.cache/cachyos-package-installer/conversion-*`, log em `last-conversion.log`. Caches de testes permanecem na origem; não foram transportados.
4. **Dolphin e MIME:** criada entrada de aplicativo `/home/delta/.local/share/applications/cachyos-local-package-installer.desktop` (ID `cachyos-local-package-installer.desktop`) e serviço executável `/home/delta/.local/share/kio/servicemenus/cachyos-install-package.desktop` com ação **Instalar no CachyOS…**. O `Exec` ativo é `/usr/bin/python /home/delta/.local/share/cachyos-package-installer/installer.py %f`. Defaults em `.config/mimeapps.list`: `application/vnd.debian.binary-package`, seu alias `application/x-debian-package` e `application/x-rpm` apontam ao novo aplicativo. Outros defaults foram preservados. Caches desktop/KDE atualizados. Não foram criados autostart, serviços, daemons, regras Polkit nem mudanças no shell de login/Fish.
5. **Correções efetivamente aplicadas à cópia local do Debtap, sem alterar `/usr/bin/debtap`:** reconhece bases pkgfile terminadas em `.files`; tamanho de payload sem assumir diretórios com 4096 bytes no Btrfs; fakeroot com Bash explícito, heredoc sem expansão prematura, `bash -e` e erro se tar/zstd falham; `.INSTALL` só é empacotado se existe. `backend.py` define `LC_ALL=C`, `SHELL=/usr/bin/bash`, `TERM=dumb`. `normalize_control.py` normaliza CRLF e desdobra campos de dependências. Loop numérico evita `cut: invalid decreasing range`. O normalizador resolve bibliotecas comuns pela ABI exata em `/usr/lib` e seus provedores pacman/pkgfile, incluindo alternativas e limites de versão >=/>> com vercmp; demais nomes continuam sujeitos à heurística do Debtap. Isso corrigiu a escolha errada de loongarch64 cross compiler/Proton observada na conversão do Parsec. Não é um resolvedor universal de dependências.
6. **RPM:** consulta cabeçalho com rpmdb temporária do usuário, captura payload binário de rpm2archive, extração tarfile com filtro data, gera DEB intermediário e converte pelo Debtap. RPMs com scripts de instalação/gatilhos, arquitetura incompatível ou dependências sem mapeamento viável são recusados com explicação. A rpmdb temporária evita tentar criar lock em `/var/lib/rpm`; captura binária evita interpretar gzip como texto. Scriptlets RPM não são ignorados nem executados diretamente.
7. **Parsec, estado posterior confirmado:** `parsec 150-1` instalado em 12:36:53, junto de `ffmpeg4.4 4.4.8-5.1` e `libmfx 23.2.2-6`, conforme pacman.log e banco atual. O chat preparou e reabriu a janela para conclusão pelo usuário; a documentação confirma que a instalação aconteceu posteriormente, não afirma que executamos uma nova instalação agora. Arquivos incluem `/usr/bin/parsecd`, `/usr/share/applications/parsecd.desktop`, ícone e biblioteca `/usr/share/parsec/skel/parsecd-150-104a.so`. Depends On atual: alsa-lib, curl, ffmpeg4.4, glibc>=2.17, libgcc>=3.0, libglvnd, libjpeg-turbo, libpng, libsm, libstdc++>=5.2, libx11, libxcursor, libxi, openssl e systemd-libs. Optional: libxrandr. O DEB original corresponde ao SHA-256 `c8a4407713d72dcb1c59f082977e81e1b9e8ffd679d0666882cde4c8a0821dd2`; não copiamos esse binário para o kit.

### Materiais e reprodução em outro CachyOS

Pasta independente: `$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer/`. O README contém procedimento completo, comandos de dependências/AUR, atualização de índices, configuração final, diagnóstico e reversão. Copiamos só os scripts necessários, dois modelos `.desktop.in`, licença GPL-2.0 do Debtap, patch contra Debtap 3.6.3 e versões observadas. Não há backups pessoais, mimeapps.list da origem, logs, credenciais, Parsec binário ou caches no kit.

A cópia portável mantém backend/GUI/normalizador byte a byte com os ativos. A única adaptação do Debtap para o kit troca o caminho absoluto do normalizador por caminho relativo ao script. Os modelos desktop usam `@INSTALLER@`, calculado e escapado pelo preparador no destino; não dependem de `/home/delta`. O script `instalar-integracao.py` faz backups do DESTINO antes de substituir integração/MIME, em diretório 0700 e manifesto 0600 sob `$HOME/.local/state/cachyos-package-installer-backups/<data-hora>/`. Captura a existência/ausência dos alvos, archives MIME, defaults e lista local de pacotes, sem reutilizar o backup original deste computador. Cada execução gera nova pasta.

Sequência resumida, **para executar em outro computador**, em Bash:

```bash
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
umask 077
backup_pacotes=$(mktemp -d "$HOME/ricy-pacotes-antes-XXXXXXXX")
pacman -Q > "$backup_pacotes/pacotes.txt"
pacman -Qqe > "$backup_pacotes/explicitos.txt"
sudo pacman -Syu
sudo pacman -S --needed dpkg rpm-tools binutils fakeroot pkgfile namcap python-pyqt6 desktop-file-utils git base-devel
build_debtap=$(mktemp -d "$HOME/debtap-build-XXXXXXXX")
git clone https://aur.archlinux.org/debtap.git "$build_debtap/debtap"
cd "$build_debtap/debtap"
cat PKGBUILD debtap.install
makepkg --verifysource
makepkg -si
sudo bash -c 'curl() { /usr/bin/curl -4 --connect-timeout 15 --max-time 180 "$@"; }; export -f curl; /usr/bin/debtap -u'
cd "$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer"
python instalar-integracao.py
```

Pré-requisitos de execução incluem KDE/Dolphin/Polkit, Python/PyQt6, pacman, Bash, binutils, libarchive/bsdtar, fakeroot, pkgfile, namcap, zstd, curl, gawk/grep/sed/coreutils/tar/gzip e desktop-file-utils. Estado de referência: Python 3.14.7-2, libarchive 3.8.9-1.1, Polkit 127-3.1, zstd 1.5.7-2, Dolphin 26.08.1-1.1, desktop-file-utils 0.28-1.1. A lista completa observada está no kit. Índices descompactados ocuparam cerca de 1,1 GiB nesta máquina; não é um limite fixo. AUR e bases podem mudar; a migração não foi executada em outro CachyOS.

### Verificação realizada e limites

- Testes anteriores: sintaxe Python/Bash; desktop-file-validate; janela Qt offscreen com capturas; DEB/RPM mínimos chegaram a pacotes Arch sem instalar as fixtures; RPM com scriptlet foi recusado com mensagem explicativa. As primeiras fixtures não cobriram Fish/CRLF/Parsec.
- Após falha relatada pelo usuário: conversão repetida com o mesmo DEB do Parsec; comparação de hash com o arquivo original; GUI offscreen sob `SHELL=/usr/bin/fish` e TERM removido chegou a **Instalar**, sem avisos tput/cut e sem dependências loongarch/Proton. Pacman -Up resolveu apenas libmfx/ffmpeg4.4/parsec que faltavam. Não houve comprovação de login/streaming ou funcionamento completo do Parsec neste chat.
- Ao documentar: pacman -Q/Qi/Ql e log confirmaram versões e instalação; gio mime confirmou os defaults; conferidos scripts e entradas ativas. Sintaxe AST Python e bash -n dos materiais portáveis passou; cópias comparadas e ausência de caminhos de usuário da origem verificada. Não executamos aplicação/restauração, GUI, conversão ou instalação novamente durante esta documentação.
- **Pendência nova da conferência:** `pacman -Qkk parsec` relatou diferenças de UID/GID em todas as 15 entradas, sem outros avisos nessa execução. `stat` de `/usr/bin/parsecd` e da biblioteca instalada mostrou root:root com modos 755/644, respectivamente; isso não comprova consistência do manifesto `.MTREE`. O fluxo atual não normaliza explicitamente ownership em tar/mtree. Não corrigimos por proibição de reaplicar mudanças nesta etapa. Kit preserva a implementação atual e destaca necessidade de auditar metadados de UID/GID antes de ampliar o uso.

### Restaurar e backups

Backup histórico local de MIME desta máquina: `/home/delta/.local/share/cachyos-package-installer/mimeapps.list.before`. Não foi copiado para o kit, pois contém defaults pessoais. Restaurar esse arquivo completo pode sobrescrever associações alteradas depois; prefira revisar as três entradas. Arquivos de investigação e fontes permanecem em `/home/delta/.cache/package-support`; índices permanecem em `/var/cache/debtap` e `/var/cache/pkgfile`. Transações criaram snapshots Snapper (17–26 durante ferramentas/interface, 27–28 ao instalar Parsec, segundo saídas); não comprovamos sua disponibilidade atual nem incluímos snapshots no kit.

No destino preparado, feche o instalador depois de concluir a operação e execute:

```bash
cd "$HOME/ricy-kit/contributions/dolphin-deb-rpm-installer"
python restaurar-integracao.py "$HOME/.local/state/cachyos-package-installer-backups/<data-hora>"
```

Restaura archives completos/ausências dos alvos e atualiza caches KDE. Exige confirmação porque pode substituir mudanças posteriores nesses archives; para restauração seletiva, revise o backup. Não remove pacotes, apps instalados, cache nem backup. Sem backup, se Ark existe, `xdg-mime default org.kde.ark.desktop <tipo-MIME>` para os três tipos devolve a abertura no Ark, mas não recria automaticamente preferências anteriores diferentes.

Parsec é removível por `sudo pacman -R parsec`. Para remover ferramentas, compare lista anterior/atual, confira dependentes e revise a transação; não remova automaticamente Python/Qt ou ferramentas que já existiam. `sudo pacman -Rns dpkg rpm-tools debtap namcap` só se esses pacotes foram acrescentados e não forem necessários a outros trabalhos. PyQt6 já é citado por outro tema deste documento: sua remoção pode afetá-lo. Cache do usuário pode ser apagado depois de fechar a janela, perdendo output/log; a remoção do pacote Debtap não apaga `/var/cache/debtap`. Índices pkgfile são compartilhados, não apague indiscriminadamente. Apps convertidos e dependências instaladas exigem reversão separada pelo pacman.

### Tentativas descartadas e pendências restantes

Discover/PackageKit, Alien e rpmtoarch foram consultados, não instalados nem usados como solução final. A tentativa de atualizar sem IPv4/timeout foi substituída pela sincronização bem-sucedida. RPM sem rpmdb temporária produziu erro de lock; rpm2archive interpretado como texto produziu bytes gzip: ambos corrigidos. Primeira conversão Parsec sob Fish falhou na compressão e emitiu mensagem enganosa de permissão; corrigido Bash explícito. CRLF/campos dobrados geraram arquitetura inválida e dependências incompletas; corrigidos. A conversão seguinte sugeriu cross compiler/Proton, nunca instalados por essa tentativa; substituídos pelos provedores nativos antes da instalação final.

Não prometer compatibilidade universal ou instalação de qualquer RPM. RPMs com scripts precisam de adaptação; alguns DEBs também exigem ajustes específicos. A checagem pacman -Up não testa funcionamento do app, bibliotecas carregadas dinamicamente nem substitui verificação final de conflitos. Os programas convertidos não recebem atualizações automáticas da distribuição de origem. Permanecem pendentes a divergência UID/GID de metadados, teste em outro computador e validação funcional completa dos aplicativos.

Origem de terceiro: Debtap https://github.com/helixarch/debtap, copyright George Savvidis, GPL-2.0 (ou posterior no cabeçalho), licença preservada. AUR https://aur.archlinux.org/packages/debtap. O patch e fontes prontos permitem auditar as mudanças locais sem depender de uma descrição parcial.

## Contribuição — Implementação no destino e validação — 2026-10-08 19:10 (America/Sao_Paulo)

Trabalho: execução da migração autorizada pelo usuário a partir de `/home/delta/ricy/ricy.md`. Esta etapa implementou a configuração; a restrição histórica das etapas anteriores a somente documentação não corresponde ao pedido atual. Os relatos anteriores foram preservados. A cópia ativa desta instalação fica em `/home/delta/ricy-kit/contributions/`, e o kit transportável permanece em `/home/delta/ricy/ricy-kit/`. Os antigos caminhos sob Documents/Codex referem-se à origem do documento, não ao perfil ativo desta implementação.

### Estado anterior e resultado

O destino já executava CachyOS/KDE Plasma Wayland, com dois painéis Plasma e KRunner ativo. Noctalia, Debtap, dpkg, rpm-tools, namcap e PyQt6 estavam ausentes; Kvantum estava instalado. A cópia original do kit passou em todos os hashes de SHA256SUMS antes de qualquer preparação. O kit foi copiado para `$HOME/ricy-kit`, preservando o original. Utilizamos a contribuição `noctalia-kde-integration-and-menus`, que acrescenta backups de chaves de estilo/blur; a variante antiga na raiz do kit não foi ativada.

Resultado: Noctalia e adaptador D-Bus ativos, plasmashell ativo para desktop/wallpaper, KRunner inativo e painéis Plasma recolhidos. Barras inferiores nos dois monitores, 44 px, exclusive_zone=44, camada top, sempre visíveis. Perfil e paleta do kit validados com Noctalia 5.2.1. Launcher por wrappers e Query D-Bus; clipboard central; Kvantum KDE-Noctalia, menuFont 10 pt preservando a família JetBrainsMono Nerd Font existente; esquema KDE-Noctalia aplicado; blur KWin ativado com força 5 e ruído 2. O wallpaper local já apontava para limine-splash.png e foi preservado. O tema de ícones observado no destino é Breeze-Dark; Papirus da origem não foi imposto como dependência da integração.

Dolphin: associação dos três MIME ao instalador e ação de contexto aplicadas com backup do destino. Conversão como usuário comum, instalação via botão/pkexec/pacman; bases pkgfile/Debtap inicializadas. A implementação mantém o caráter de teste reversível do roteiro: o autostart é de recuperação, e o Noctalia não inicia automaticamente após novo login. Foram criados `/home/delta/ricy/iniciar.sh`, `/home/delta/ricy/voltar.sh` e `/home/delta/ricy/IMPLEMENTADO.md` para uso local.

### Pacotes e sequência executada

A atualização completa do roteiro terminou com 190 pacotes atualizados e 15 adicionados. A lista anterior e a lista final estão no diretório privado `/home/delta/ricy/execucao-2026-10-08/`, junto aos logs. Foram adicionados debtap, dpkg, ministream, namcap, nettle3, noctalia, pyalpm, python-boolean.py, python-license-expression, python-pyelftools, python-pyqt6, python-pyqt6-sip, rpm-sequoia, rpm-tools e sdbus-cpp. Alguns são dependências/adições da atualização, não componentes escolhidos isoladamente. O sistema recomendou reiniciar devido à atualização de componentes de base/kernel; a sessão foi mantida.

Versões finais conferidas: noctalia 5.2.1-1.1; Plasma Desktop 6.7.5-1.1; Plasma Workspace 6.7.5-3.1; KWin 6.7.5-3.1; Kvantum 1.1.8-1.1; python-gobject 3.58.0-1; qt6-tools 6.12.0-1.1; glib2 2.90.1-1.1; noto-fonts 1:2026.10.01-1; dpkg 1.23.11-1.1; rpm-tools 6.0.1-2.2; debtap 3.6.3-1; namcap 3.6.0-3; python-pyqt6 6.11.0-4.

Sequência aplicada, resumida com caminhos portáveis (a execução local foi em Bash, usando os scripts presentes no kit):

```bash
# Registre pacotes e confira hashes antes de instalar/preparar.
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
sudo pacman -Syu --needed --noconfirm noctalia kvantum python python-gobject qt6-tools glib2 noto-fonts python-pyqt6 wl-clipboard dpkg rpm-tools binutils fakeroot pkgfile namcap desktop-file-utils git base-devel
cd contributions/noctalia-kde-integration-and-menus
python preparar-destino.py
./aplicar-estilo.sh
mkdir -p "$HOME/.local/share/color-schemes"
cp outputs/kde-outlines/KDE-Noctalia.colors "$HOME/.local/share/color-schemes/"
plasma-apply-colorscheme KDE-Noctalia
kwriteconfig6 --file kwinrc --group Plugins --key blurEnabled true
kwriteconfig6 --file kwinrc --group Effect-blur --key BlurStrength 5
kwriteconfig6 --file kwinrc --group Effect-blur --key NoiseStrength 2
qdbus6 org.kde.KWin /KWin org.kde.KWin.reconfigure
./outputs/noctalia-test/iniciar-teste.sh
```

O checkout AUR Debtap foi lido, fontes verificadas por SHA-512, construído com `makepkg` e instalado por `pacman -U`. Foram preservados checkout, pacote e logs em `execucao-2026-10-08/debtap-aur/` (materiais locais, não adicionados ao kit portátil). Os índices foram sincronizados com wrapper de curl IPv4, retries, tempo de conexão 15 s/total 180 s, HTTPS e verificação TLS; todos os índices necessários foram conferidos como não vazios. Depois, `python instalar-integracao.py` da contribuição Dolphin instalou a integração como o usuário do desktop.

### Correções necessárias durante a implantação

1. O primeiro início registrou a shell/adaptador e removeu os painéis, mas falhou ao registrar Super. `setForeignShortcut` sozinho não criou o registro neste destino. Acrescentamos `doRegister` e `setShortcut` antes de `setForeignShortcut` em `configurar-super.py`. Super/Super+Espaço passaram a constar no KGlobalAccel; o novo ciclo completo de início terminou sem erro. O JSON original local foi conservado.
2. Corrigimos a pendência UID/GID do conversor: `.MTREE` usa UID/GID zero, o tar final usa owner/group numéricos zero, `.INSTALL` só entra quando existe e erro na geração do mtree interrompe a conversão. Esta alteração foi feita na cópia local e na cópia ativa de contribuição, mantendo `/usr/bin/debtap` original para os índices.
3. As fixtures sem dependências expuseram `namcap-checks`, `namcap-dependencies` e `namcap-libraries` incluídos no pacote final. Excluímos `namcap-*` e `pkgbuildinstallations*` tanto do tar quanto do mtree e do cálculo de tamanho. A nova conversão não contém esses intermediários.
4. O wrapper de atualização elimina `-k`, converte URLs HTTP dos índices Debian/Ubuntu para HTTPS e valida os archives de índices após o comando. A atualização concluída não depende da senha ficar em arquivo; nenhum segredo foi acrescentado ao kit.

Os archives históricos distribuídos de outros chats foram preservados. A nova pasta `ricy-kit/contributions/target-implementation-fixes/` contém os dois archives corrigidos, seus diffs, manifesto de hashes, aplicador idempotente, wrapper de índices, README e licença Debtap. Para outra migração, execute `aplicar-correcoes.py` **depois da conferência SHA256SUMS e antes da preparação/instalação**. O aplicador aceita somente o arquivo original conhecido ou a versão corrigida; modificações desconhecidas exigem revisão do patch. As correções foram reproduzidas em cópia descartável e comparadas byte a byte com o ativo.

### Verificação executada

- `noctalia config validate` aprovou TOML/paleta. Logs registraram reserva inferior de 44 px nos dois monitores e apoio superior sem reserva. KWin confirmou efeito blur carregado.
- Serviços de Noctalia, adaptador e plasmashell ativos; KRunner inativo; `panels().length=0`. Registros KGlobalAccel conferidos para Meta, Meta+Espaço e Meta+V. Os wrappers abriram launcher/clipboard; chamada `org.freedesktop.Application.ActivateAction("Query", …)` abriu launcher pelo adaptador.
- Restauração real com `voltar-ao-plasma.sh`: os dois painéis Plasma voltaram. Reinício pelo script corrigido: painéis recolhidos, atalhos configurados e teste ativo. Os IDs/wallpaper conferidos antes/depois permaneceram os do destino.
- Menu Qt nativo novamente testado sem forçar translucência: Kvantum, fonte 10 pt, cinco linhas 26 px, atributo de translucência ativo e alfa zero no canto. Houve inspeção de captura da sessão, depois removida; não foi registrada confirmação visual do usuário dos menus Dolphin. Não afirmar resolução universal dos menus próprios de aplicativos.
- DEB e RPM mínimos gerados localmente, convertidos e validados por pacman, arquivo/mtree com UID/GID zero e ausência dos intermediários. Foram instalados temporariamente e `pacman -Qkk` relatou, para cada um, 4 archives e 0 alterados. Ambos removidos ao terminar; não permanecem pacotes de teste instalados.
- RPM contendo scriptlet foi recusado com explicação. GUI offscreen executada com SHELL=fish/TERM ausente chegou ao botão Instalar, sem clicar nesse botão. A transação de teste foi feita diretamente pelo pacman com privilégios; não foi testada autenticação interativa Polkit.
- Defaults dos três MIME conferidos. O `.desktop` de aplicativo passou no desktop-file-validate com dica de categoria. Esse validador não aceita Type=Service de menus KDE; sua saída no servicemenu não é prova de erro, pois a estrutura segue a documentação KDE (https://develop.kde.org/docs/apps/dolphin/service-menus/).
- Sintaxe de scripts Python/Bash do kit corrigido aprovada. Aplicador de correções testado duas vezes na mesma cópia descartável. Hashes do kit de transporte conferidos após acrescentar os novos arquivos.

### Backups e desfazer

Backups privados locais desta implementação: `plasma-antes.tar.gz`, `backup-manifest.json` e JSON dos atalhos em `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/`; `kde-antes-contornos.tar.gz` e `estado-antes.json` em `outputs/kde-outlines/`. Os archives de backup/atalhos conferidos têm modo 0600. Não transportar esses archives para outro computador.

```bash
# Layout e atalhos originais; mantém cores/estilo:
"$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/voltar-ao-plasma.sh"
# Chaves de estilo/fonte/blur e Kvantum anteriores:
python "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/restaurar-estilo-e-blur.py"
```

Para cores, selecione o esquema anterior no KDE ou restaure seletivamente kdeglobals do backup local conforme README, considerando preferências posteriores.

Backup da integração Dolphin nesta implementação: `$HOME/.local/state/cachyos-package-installer-backups/20261008-190438-261237/`. Feche a janela e use o restaurador da contribuição com essa pasta. A data/hora é própria deste destino: em outra instalação use o caminho emitido pelo instalador. Não remove pacotes/ferramentas, bases ou programas externos instalados.

### Limitações e estado pendente

A instalação e migração foram efetivamente executadas neste destino, ao contrário da fase histórica apenas documental. As fixtures validam o fluxo e a correção de metadados; não comprovam compatibilidade de qualquer DEB/RPM. Parsec não acompanha o kit e não foi instalado/reinstalado nesta etapa, nem seus metadados históricos foram alterados. Testes de login/streaming permanecem fora do resultado verificado. O aviso Bluetooth do Noctalia aponta ausência de BlueZ ativo no destino; não foi alterado serviço de Bluetooth para a integração. O reinício recomendado pelo atualizador e a conferência visual pelo usuário permanecem pendentes. Após novo login, executar `iniciar.sh` retoma o teste Noctalia.

## Contribuição — Início automático do Noctalia no KDE — 2026-10-08 19:40 (America/Sao_Paulo)

Objetivo: após reiniciar, o usuário relatou que entrou novamente no Plasma e solicitou que o Noctalia viesse por padrão. A implementação anterior seguia o modo de teste do documento e tinha somente recuperação no login. **O estado final de início manual descrito anteriormente foi substituído pelo início automático descrito nesta contribuição.** Plasma/KWin continuam responsáveis pela sessão, desktop e wallpaper.

### Mudanças aplicadas

- Instalada e habilitada `$HOME/.config/systemd/user/ricy-noctalia-integracao.service`, WantedBy=plasma-workspace.target, depois de plasmashell. Uma unidade oneshot aguarda prontidão real de Plasma/KGlobalAccel, inicia a integração e permanece ativa. Em erro durante sua execução, o wrapper restaura o Plasma. Usa Wants para plasmashell, permitindo que o rollback reinicie plasmashell sem cancelar a própria recuperação.
- `$HOME/.config/systemd/user/noctalia-teste.service` passou de transitória a permanente. Usa `/usr/bin/noctalia`, o mesmo NOCTALIA_CONFIG_HOME/NOCTALIA_STATE_HOME do perfil isolado sob `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/`, Restart=on-failure/RestartSec=2, PartOf=graphical-session.target e Wants=noctalia-busca-desktop.service.
- `$HOME/.config/systemd/user/noctalia-busca-desktop.service` é permanente, com Requires/BindsTo/After da shell e PartOf da shell/sessão. Usa Type=exec, sem BusName no systemd; Python assume `org.kde.krunner` como antes. Declarar permanentemente o mesmo BusName da unidade nativa KRunner causou conflito entre unidades; essa tentativa foi corrigida. A ativação compara o PID do dono D-Bus com o MainPID do adaptador antes de declarar sucesso.
- Scripts ativos de início e ativação da busca detectam as unidades permanentes e usam `systemctl start` em vez de criar unidades transitórias. KRunner é parado antes da shell iniciar seu adaptador.
- `recuperar-no-login.sh` não restaura os painéis enquanto a integração automática estiver habilitada. O início automático faz sua própria recuperação. `voltar-ao-plasma.sh` desabilita/para a integração automática antes de restaurar painéis e atalhos; uma recuperação interna evita interromper a própria unidade.
- `configurar-super.py` aguarda até dois segundos pela criação efetiva da ação no KGlobalAccel. A primeira criação após novo login chegou a falhar na conferência imediata; a espera/repetição do registro foi aplicada. Backups originais dos atalhos permanecem intactos.
- `$HOME/ricy/iniciar.sh` habilita e reinicia a integração automática. `$HOME/ricy/voltar.sh` mantém o retorno ao Plasma, agora também para os próximos logins. O guia IMPLEMENTADO.md foi atualizado. `noctalia-plasma.service`, preexistente e desabilitada, não foi habilitada; assim não abre outro perfil.

### Reprodução e materiais

Pasta nova, independente: `ricy-kit/contributions/noctalia-autostart/`. Inclui instalador Python, três modelos de unidade systemd, wrapper automático, cinco scripts atualizados e README. Os archives históricos dos demais chats no kit de transporte foram preservados; o instalador aplica estas atualizações à contribuição preparada no destino.

Depois de conferir SHA256SUMS, aplicar `target-implementation-fixes` e preparar a contribuição `noctalia-kde-integration-and-menus`:

```bash
cd "$HOME/ricy-kit"
python contributions/noctalia-autostart/instalar-inicio-automatico.py
```

O instalador deve ser executado pelo usuário do desktop, sem sudo, em Plasma Wayland. Captura os archives anteriores em `$HOME/.local/state/ricy-inicio-automatico-backups/<data-hora>/`, gera caminhos locais nas unidades, atualiza scripts, valida unidades e habilita/inicia a integração. A execução final teve backup em `20261008-193935-356538`; a primeira execução gerou outro backup anterior, preservado nessa mesma raiz. Cada destino deve usar seu próprio caminho emitido. Não foram refeitos os backups de layout/estilo nem instalados pacotes adicionais nesta etapa.

### Testes e resultado final

- Sintaxe Python/Bash e `systemd-analyze --user verify` das três unidades aprovados.
- Integração habilitada, com symlink real em `plasma-workspace.target.wants`. ExecStart final terminou com 0/SUCCESS. Shell, adaptador e plasmashell ativos; painéis Plasma recolhidos; perfil isolado preservado.
- Volta explícita ao Plasma desabilitou o início automático e restaurou os dois painéis. Novo início reativou a preferência e os atalhos sem pré-registro manual.
- Reiniciar a shell reiniciou o adaptador; o PID proprietário de `org.kde.krunner` coincidiu com MainPID do adaptador. ActivateAction Query abriu o launcher.
- A recuperação antiga de login foi executada com início automático habilitado e preservou a integração.
- Configuração TOML inválida foi introduzida temporariamente: a unidade falhou e restaurou os dois painéis/KRunner. O conteúdo original foi reposto em finally e a integração iniciou novamente com sucesso. Log local em `execucao-2026-10-08/inicio-automatico-recuperacao.log`.
- Uma cópia intermediária perdeu a permissão de execução do wrapper ao ser sincronizada; modos dos scripts foram corrigidos para 0755. O instalador final e o ciclo completo foram executados depois da correção.

Não foi executada outra reinicialização completa pelo agente após estas mudanças. Foram testados os mesmos serviços de início e sua habilitação no target KDE. O estado final já está ativo na sessão atual e configurado para os próximos logins.

### Desfazer

Use a entrada **Voltar ao Plasma**, `$HOME/ricy/voltar.sh`, ou o `voltar-ao-plasma.sh` da contribuição ativa. Isso desabilita o início automático e restaura os painéis/atalhos locais, mantendo as cores e estilo. As unidades permanentes podem permanecer instaladas e inativas; `iniciar.sh` reativa a preferência. Para retornar também aos scripts/unidades anteriores à implantação persistente, revise os archives no backup privado emitido pelo instalador, considerando alterações posteriores. Os restauradores de estilo/blur e da integração Dolphin continuam separados e válidos.


## Contribuição — Bloqueio com o visual da tela de login (08/10/2026, 19:51)

Após a implementação, o usuário pediu que a tela de bloqueio tivesse o visual
da tela de iniciar sessão e esclareceu que a mudança se restringia ao bloqueio.
Foi acrescentada `contributions/login-matched-lock-screen/` ao kit, sem alterar o SDDM.
O tema de login local é `mocha-limine`, com fundo Limine e fonte JetBrainsMono.
O bloqueio usa esse mesmo wallpaper e os componentes visuais Breeze nativos:
relógio, usuário e formulário. O formulário aparece já na abertura e aguarda
um minuto de inatividade, como o login; mídia e botão de revelar senha ficam
ocultos. Os botões de sessão continuam próprios para uma sessão já aberta.

No Plasma 6.7 o bloqueio vem do pacote de shell `org.kde.plasma.desktop`.
O aplicador gera um pacote local do mesmo ID, adaptando apenas apresentação
e tempo de exibição no QML nativo; os demais componentes apontam para o KDE
instalado. Autenticação/PAM, sincronização de senha, biometria e erros continuam
na implementação do KDE. O aplicador valida os trechos antes de escrever e
recusa um shell local pré-existente sem seu marcador. Depois de atualizar o
Plasma, reaplicá-lo regenera os archives a partir do KDE novo.

Verificação: prévia `kscreenlocker_greet --testing`, carregamento local
confirmado no journal em ambos os monitores e conferência visual da captura.
O formulário permaneceu visível após 15 segundos, sem os controles de mídia.
Restauração do estado anterior foi executada, seguida de nova aplicação.
Não foi feito bloqueio real nem teste de senha nesta etapa. Backups e capturas
ficam privados no destino, fora do kit. Os serviços Noctalia permanecem ativos
e o início automático no login está habilitado.


## Correção — Inicialização do desbloqueio (08/10/2026)

Após o teste visual da contribuição de bloqueio, o usuário relatou que
o desbloqueio não processava a senha, embora o SDDM autenticasse.
A adaptação havia alterado o estado inicial de `uiVisible` de `false` para
`true`, impedindo a transição cujo handler inicia a autenticação nativa.
O aplicador foi corrigido para manter o estado inicial do KDE e tornar
a interface visível depois da montagem via `Qt.callLater`. A aparência e
a apresentação inicial do formulário continuam como no login.

Verificação funcional: a cópia da versão anterior reproduziu o problema,
sem início de autenticação e com timeout. A versão corrigida foi exercitada
em cópia temporária usando o formulário original (`passwordBox` e
`startLogin`) até o autenticador real `kde`, com PAM result code 0 / Success
e encerramento do greeter. Passaram os modos imediato e com tolerância de
1200 ms em `--testing` e renderização offscreen, sem bloquear a sessão real.
A senha passou por descritor em memória e não foi salva no kit ou nos logs.
Cópia ativa, contribuição portátil, README e hashes foram atualizados.


## Contribuição — Login, bloqueio, cursor e kit de reinstalação — 2026-10-09 23:39 (America/Sao_Paulo)

Trabalho: captura das configurações efetivas solicitada pelo usuário para
reutilizar a aparência na próxima instalação. Foram exportados assets e
preferências; os novos instaladores não foram aplicados ao sistema de origem.
O novo roteiro consolidado está em `REINSTALAR.md`, ao lado deste registro.

### Estado visual capturado

- **Login SDDM:** `/etc/sddm.conf.d/95-mocha-limine.conf` seleciona
  `mocha-limine`, CursorTheme Bibata-Modern-Classic, CursorSize 16 e Font
  JetBrainsMono Nerd Font. `theme.conf` define showlogo hidden, showClock true,
  type image, color #1e1e2e, fontSize 10 e fundo Limine. O QML local usa
  formulário imediato, timeout 60000 ms e recorte proporcional da imagem.
- **Cores do login:** leitura privilegiada, somente visual, de
  `/var/lib/sddm/.config/kdeglobals`; ColorScheme CatppuccinMochaMauve,
  widgetStyle Breeze, Icons breeze-dark e fonte JetBrainsMono Nerd Font 10 pt.
  Os grupos Colors/ColorEffects foram exportados em `greeter-preferencias.json`.
  A seleção do login é #cba6f7, distinta da seleção #977dba do KDE-Noctalia.
- **Bloqueio:** kscreenlockerrc confirma Limine, FillMode 2, relógio sempre
  visível, sem mídia. O QML ativo conserva uiVisible false e a transição
  Qt.callLater corrigida; o formulário tem 60 s. Reutilizamos a contribuição
  `login-matched-lock-screen`, gerada a partir do KDE do destino, sem copiar a shell
  local desta máquina. Não houve novo bloqueio/teste de senha nesta captura.
- **Cursor:** kcminputrc Mouse cursorTheme Bibata-Modern-Classic/cursorSize 16;
  GTK 3/4 e environment.d/20-cursor.conf confirmam o mesmo. As cópias local e
  do sistema do Bibata 2.0.6 foram comparadas arquivo a arquivo e são idênticas.
- **Demais preferências:** fontes JetBrainsMono Nerd Font 10 pt em KDE, WM e
  GTK; ícones Breeze Dark herdados dos kdedefaults; tema Plasma mocha-blur;
  splash Catppuccin-Mocha-Mauve; decoração efetiva Breeze sem borda,
  BorderSizeAuto false, NoPlugin false; Qt/Kvantum KDE-Noctalia; GTK
  adw-gtk3-dark, som Ocean; fontconfig com antialiasing e hintslight; blur 5/2.
  Os defaults antigos do tema global que citam outro cursor/Aurorae não foram
  tratados como valores efetivos. A aplicação usa overrides seletivos.
- **Extensões opcionais:** fontes de adaptivepanelwidth, smoothwindowgeometry
  e windowsarrows incluídos; flags e atalhos selecionados capturados. O módulo
  nativo de windowsarrows é recompilado no destino antes de aplicar. Não foi
  transportado o .so desta máquina nem archives de testes/backups das fontes.

### Materiais incluídos e reprodução

Nova pasta portátil:
`ricy-kit/contributions/login-lock-cursor-appearance/`, contendo README,
preferencias.json, greeter-preferencias.json, preferencias-kwin.json,
sistema.py, usuario.py, comum.py, aplicar-wallpaper.sh, versões e licenças.
Assets: QML/metadata/logo SDDM, Bibata completo, wallpaper Limine, quatro faces
Regular/Bold/Italic/BoldItalic JetBrainsMono Nerd Font com OFL, temas locais
Plasma/splash, fontconfig e fontes das extensões KWin. Kvantum e cores KDE
reutilizam os archives já existentes da contribuição Noctalia. GTK/ícones/sons
vêm dos pacotes do novo destino.

Siga `REINSTALAR.md`: hashes do kit original; dependências; aplicar correções;
instalar assets/preferências visuais; escolher wallpaper; preparar integração
Noctalia; instalar início automático; gerar bloqueio; extensões/instalador
Dolphin opcionais; nova sessão e conferência. Todas as contas, IDs e caminhos
locais de instalação/backups são resolvidos no destino. O wallpaper transportado
é o público Limine do pacote local, não uma foto pessoal.

### Backups e desfazer no destino

Os instaladores criam backups privados novos em
`/var/lib/ricy-appearance-backups/DATA-HORA/` (sistema) e
`$HOME/.local/state/ricy-appearance-backups/DATA-HORA/` (usuário), com manifesto,
existências anteriores e archives/temas afetados. O backup de sistema registra
UID/GID anteriores; a aplicação resolve a conta sddm do destino. Para desfazer:

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python usuario.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python sistema.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

O bloqueio mantém seu próprio restaurador/backup. Reverta execuções múltiplas
na ordem inversa. As restaurações repõem archives integrais e podem substituir
edições posteriores; não removem pacotes. O script opcional de wallpaper altera
a imagem dos desktops locais sem guardar layout; escolha a imagem anterior
pelo Plasma se quiser desfazer essa escolha.

### Verificação e limites

Scripts Python/Bash e dados JSON foram validados. Aplicação/restauração foram
exercitadas em raiz/home descartáveis, com valores anteriores, ausência de
assets e outras chaves preservadas, incluindo GTK com chave duplicada.
Geração/restauração do bloqueio em HOME descartável confirmou uiVisible false,
Qt.callLater e timeout 60000 ms. O módulo nativo de setas foi recompilado em
pasta temporária contra o KWin instalado. O kit/arquivo de transporte possui
verificação SHA256 atualizada.

Não foram modificadas as configurações ativas do KDE/SDDM/Noctalia nesta etapa,
nem reiniciado SDDM ou realizada uma nova instalação completa. A leitura
privilegiada exportou só preferências visuais, sem dados de login, senha/PAM,
lista de usuários ou avatar. Não foram copiados backups pessoais, IDs de
monitores, históricos ou estado Noctalia. Drivers/dispositivos e versões
futuras de KDE/Noctalia exigem configuração/verificação no destino.


## Correção de escopo — Cursor animado do Konsole — 2026-10-09 23:45 (America/Sao_Paulo)

O usuário esclareceu que o cursor solicitado era o cursor de texto animado
do Konsole. A captura anterior de Bibata corresponde ao ponteiro do mouse,
que permanece como preferência adicional; ela não atendia sozinha ao pedido.

O perfil padrão atual em `~/.config/konsolerc` é `PlasmaBlur.profile`. O arquivo
`~/.local/share/konsole/PlasmaBlur.profile` contém:

```ini
[Terminal Features]
AnimatingCursorEnabled=true
```

O Konsole 26.08.2-1.1 instalado reconhece essa propriedade nativamente, conforme
`/usr/bin/konsole --list-profile-properties`. A definição também foi conferida
no código oficial da versão:
https://github.com/KDE/konsole/blob/v26.08.2/src/profile/Profile.cpp .
Não é um tema de ponteiro nem exige modificar o executável Konsole.

A contribuição nova `ricy-kit/contributions/konsole-animated-cursor/` contém
perfil/paleta completos, wrapper Qt/Kvantum, entrada de aplicativo, aplicador
com backup/restauração e README. Foram capturados JetBrainsMono Nerd Font
10 pt, paleta Catppuccin Mocha, Opacity 0.85, Blur true, MenuBar Disabled e
DefaultProfile PlasmaBlur.profile. BlinkingCursorEnabled, CursorShape e cores
específicas do cursor não estão definidos no perfil local: permanecem os
valores herdados de FALLBACK, sem inventar novas opções.

O aplicador confere o suporte de animação no destino antes de escrever,
mescla somente DefaultProfile/MenuBar em konsolerc e guarda archives
anteriores/ausências sob `$HOME/.local/state/ricy-konsole-backups/DATA-HORA/`.
Não transporta backups, histórico de terminal, SSH, comandos, diretório
inicial ou nomes de usuário da origem. O shell é o do usuário do destino.

```bash
sudo pacman -S --needed konsole kvantum ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit/contributions/konsole-animated-cursor"
python aplicar.py
# Para desfazer, use o backup impresso no destino:
python aplicar.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
```

O guia REINSTALAR.md foi corrigido para aplicar também esta contribuição.
Aplicação/restauração foram testadas em HOME descartável, preservando outras
chaves e restaurando archives anteriores/removendo ausentes. Sintaxe Python,
wrapper Bash e entrada desktop foram validados. Perfil/paleta distribuídos
coincidem com os archives ativos; suporte nativo foi conferido sem abrir uma
nova janela de terminal. Não houve alteração da configuração ativa nem teste
visual novo da animação. Hashes e pacote portátil foram atualizados.

## Contribuição — Estado permanente, aparência completa e SDDM no destino — 2026-10-10 18:04 (America/Sao_Paulo)

Trabalho: validação do pacote atualizado de 09/10 e conclusão da implementação solicitada. O usuário substituiu o pacote anterior e escolheu explicitamente SDDM. Este estado substitui o modo de teste/manual das seções históricas. O roteiro de referência agora é `REINSTALAR.md`; os relatos de outros destinos foram preservados.

### Validação e recuperação do kit

- O kit recém-extraído em `/home/delta/Documents/ricy/ricy-kit` passou integralmente em SHA256SUMS antes das alterações. Sintaxe dos Python/Bash e conteúdo dos JSON conferidos. A versão atual inclui início automático, aparência completa, bloqueio corrigido e cursor animado do Konsole, ausentes no pacote anterior.
- A troca do diretório havia levado o kit ativo, seus backups e seu perfil à lixeira. Foram recuperados da pasta local `$HOME/.local/share/Trash/files/ricy/`, sem mover nem apagar a cópia da lixeira. O backup original de layout recuperado foi comparado por SHA256 e é idêntico ao anterior, modo 0600.
- A instalação ativa agora fica em **`$HOME/ricy-kit`**. Documento e kit de transporte permanecem em `$HOME/Documents/ricy`. Perfil/estado privado, backups e `.desktop` calculados pertencem apenas ao kit ativo. Não transporte a pasta ativa inteira como um kit limpo. O registro da primeira implantação foi preservado em `$HOME/.local/state/ricy-implementacao/ricy-registro-primeira-implantacao.md`.
- Aplicadas as correções finais de `target-implementation-fixes` ao kit ativo, antes dos instaladores. Atualizada a cópia local do instalador Dolphin: metadados com UID/GID zero e exclusão de `namcap-*`/`pkgbuildinstallations*`. Índices sincronizados pelo wrapper HTTPS/TLS da versão atualizada.

### Estado aplicado

| Componente | Estado neste destino |
|---|---|
| Noctalia | Permanente no login KDE Wayland; integração habilitada em plasma-workspace.target |
| Shell/adaptador | Unidades em `.config/systemd/user`, reinício em falha e vínculo à sessão; Type=exec sem disputa por BusName |
| Desktop | Plasma/KWin mantidos; painéis substituídos pelas barras inferiores Noctalia, 44 px e reserva de espaço |
| Busca e clipboard | Meta/Meta+Espaço e Meta+V, busca superior com apoio oculto fora da abertura |
| Paleta/menus | KDE-Noctalia, Kvantum KDE-Noctalia, blur KWin 5/2 |
| Fontes | JetBrainsMono Nerd Font 10 pt em KDE/GTK/WM; quatro faces do kit instaladas no sistema |
| Ícones | Breeze Dark (`breeze-dark`), conforme a captura final; substitui Papirus-Dark usado na primeira implantação |
| Aparência Plasma | mocha-blur; pacote global e splash Catppuccin-Mocha-Mauve, com overrides seletivos |
| Janelas | Breeze sem bordas; WindowsArrows compilado contra KWin local; setas Super registradas; smoothwindowgeometry carregado |
| Wallpaper | Limine em ambos os desktops locais, `/usr/local/share/ricy/limine-splash.png`, FillMode 2; wallpaper do Noctalia desativado |
| Ponteiro | Bibata Modern Classic, tamanho 16, em KDE/GTK, SDDM, environment.d e ambiente do systemd do usuário |
| Konsole | PlasmaBlur.profile padrão, cursor de texto animado, fonte JetBrainsMono 10 pt, paleta Catppuccin, opacidade 0,85 e blur |
| Login | SDDM instalado/selecionado, mocha-limine, cores/fonte/cursor do kit; passa a controlar o login após reiniciar o computador |
| Bloqueio | KDE nativo adaptado: Limine, relógio, formulário imediato/60 s, mídia/revelação de senha ocultos; uiVisible false + Qt.callLater preservados |

Os nomes históricos `noctalia-teste.service`, `iniciar-teste.sh` e `outputs/noctalia-test/` foram mantidos para compatibilidade entre scripts; **não indicam modo de teste**. A unidade agora é permanente. Nomes das entradas de menu e mensagens de início deixaram de exibir “teste”. A recuperação antiga não devolve os painéis enquanto o início automático estiver habilitado. O retorno explícito ao Plasma continua disponível e desabilita a preferência para os próximos logins.

### Sequência realizada e ajustes do destino

1. Kit copiado para `$HOME/ricy-kit`; perfil, estado e backups originais recuperados; caminhos dos quatro `.desktop` recalculados. Não foi executado novamente `preparar-destino.py`, preservando o backup original.
2. Aplicado `contributions/target-implementation-fixes/aplicar-correcoes.py`.
3. Instalados via pacman `sddm 0.21.0-8` e `adw-gtk-theme 6.5-1`, com dependências Xorg. Os demais componentes já estavam instalados. Snapshots Snapper 15/16 foram criados pela transação.
4. Executado `sistema.py` como root e `usuario.py --extensoes-kwin` como usuário. O módulo WindowsArrows foi compilado com os headers/Qt/KWin deste destino; nenhum binário antigo foi importado. Aplicados wallpaper, `konsole-animated-cursor/aplicar.py` e `login-matched-lock-screen/aplicar.py`.
5. Atualizado apenas o script local de preservação do wallpaper com os IDs locais e a imagem Limine escolhida; o backup original de layout não foi modificado.
6. Executado `noctalia-autostart/instalar-inicio-automatico.py`. A migração parou as unidades transitórias, instalou as permanentes, validou-as e habilitou/iniciou a integração. Perfil efetivo: `$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/config/noctalia/config.toml`.
7. Antes de selecionar o SDDM, capturada a preferência anterior do gerenciador de login. Executados `systemctl disable plasmalogin.service` e `systemctl enable sddm.service`, **sem --now**. O link display-manager.service aponta ao SDDM. O processo Plasma Login Manager da sessão atual foi preservado; a troca precisa de reinício do computador.
8. Reinstalada a integração Dolphin a partir do kit corrigido e executado o wrapper de índices atualizado. Nova fixture passou sem instalar pacotes de teste.
9. `adaptivepanelwidth` foi instalado pela opção de extensões, mas desativado neste destino: procurava painéis Plasma ausentes e emitia “panel update failed: missing”. WindowsArrows e smoothwindowgeometry foram mantidos; o efeito maximize concorrente foi descarregado. Flags/atalhos foram aplicados também à instância ativa via KWin/KGlobalAccel.
10. Prévia do SDDM revelou referência `config.logo` indefinida mesmo com logo oculto. Acrescentado `logo=default-logo.svg` ao theme.conf instalado e às duas cópias do asset no kit. O logo permanece oculto. Rótulos/mensagens da integração permanente foram corrigidos nos modelos e scripts ativos.

Para reproduzir em outro destino, use a sequência do `REINSTALAR.md`, preparando backups novos nesse computador. A recuperação a partir da lixeira foi específica desta instalação e não deve ser copiada como etapa de migração.

### Verificação executada e limites

- `systemd-analyze --user verify` das três unidades passou. Integração habilitada, symlink no target KDE, `Result=success`, `ExecMainStatus=0`; shell/adaptador/Plasma ativos. FragmentPath da shell aponta ao arquivo permanente da home. Reinício da integração terminou com sucesso.
- PID proprietário de `org.kde.krunner` coincide com MainPID do adaptador; consulta Query abre busca após a migração. Atalhos Meta/Meta+Espaço/Meta+V mantidos; Super+setas registrado no script KWin. Painéis Plasma: zero. As duas imagens de desktop apontam ao Limine instalado.
- Bibata 16 aplicado pela ferramenta KDE; ambiente do systemd atualizado. Fontconfig resolve JetBrainsMono Nerd Font instalada. Menu Qt: Kvantum, JetBrainsMono 10 pt, cinco linhas 26 px e alfa zero no canto.
- `konsole --list-profile-properties` reconhece AnimatingCursorEnabled; perfil padrão e propriedade true conferidos. O Konsole já aberto não foi encerrado, para preservar o trabalho em andamento; novas janelas carregam o perfil. Não houve teste visual específico da animação.
- Prévia do bloqueio com `kscreenlocker_greet --testing --shell org.kde.plasma.desktop` carregou o QML local: journal confirmou a mensagem Ricy nas duas saídas. A prévia foi encerrada por timeout; GetActive da sessão permaneceu false. Estado inicial false, Qt.callLater e 60000 ms conferidos. Não foi fornecida senha, nem testado desbloqueio real; o teste funcional PAM da origem continua sendo evidência histórica, não teste novo neste destino.
- Prévia SDDM offscreen/software executada como a conta sddm: tema/QML foram carregados e uma view foi criada. Avisos de socket/backend gráficos são da prévia sem daemon/tela real; a referência indefinida do logo foi corrigida. Conta sddm tem ownership do seu kdeglobals privado. Não houve login/autenticação real pelo SDDM nem reinício do computador nesta etapa.
- Fixture DEB com o conversor final passou em pacman, UID/GID zero e ausência dos intermediários namcap no tar/mtree; não foi instalada. Os testes anteriores de RPM/recusa de scriptlets não foram repetidos.

### Backups e reversão

Backups novos deste destino:

- Sistema/SDDM/assets: `/var/lib/ricy-appearance-backups/20261010-175757-266724/`.
- Aparência e extensões do usuário: `$HOME/.local/state/ricy-appearance-backups/20261010-175814-614754/`.
- Konsole: `$HOME/.local/state/ricy-konsole-backups/20261010-175817-074216/`.
- Bloqueio: `$HOME/.local/state/ricy-lockscreen-backups/20261010-175817-144082/`.
- Início automático/scripts: `$HOME/.local/state/ricy-inicio-automatico-backups/20261010-175834-898747/`.
- Seleção do gerenciador de login: `/var/lib/ricy-display-manager-backups/20261010-xxc6JxxS/`.
- Integração Dolphin atualizada: `$HOME/.local/state/cachyos-package-installer-backups/20261010-175846-254383/`; backup inicial anterior também preservado.

Para voltar aos painéis/atalhos e desabilitar Noctalia no próximo login:

```bash
"$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/voltar-ao-plasma.sh"
```

Para reativar Noctalia:

```bash
systemctl --user enable ricy-noctalia-integracao.service
systemctl --user restart ricy-noctalia-integracao.service
```

Bloqueio, Konsole, aparência e assets de sistema têm os restauradores e backups acima, conforme `REINSTALAR.md`. Restauração integral de um arquivo pode substituir mudanças posteriores. Para devolver Plasma Login Manager no próximo reinício, use `sudo systemctl disable sddm.service` seguido de `sudo systemctl enable plasmalogin.service`, sem --now dentro da sessão atual. Os pacotes continuam instalados. O wallpaper anterior era o padrão north; pode ser selecionado novamente pelo Plasma.


## Contribuição — Cedilha no teclado US internacional — 2026-10-10 18:09 (America/Sao_Paulo)

Após o usuário validar a implementação visual, relatou ausência da cedilha
no Konsole e no Brave. A sessão confirmou um único layout ativo: English
(US, alt. intl.), `us(alt-intl)`, herdado da configuração do sistema.
Não havia `$HOME/.XCompose` nem configuração de layout em kxkbrc. A sessão
Plasma/Konsole usa LANG=en_US.UTF-8. A tabela de composição inglesa foi
reproduzida localmente: dead_acute+c/C produzia ć/Ć.

Aplicado `$HOME/.XCompose`, incluindo a tabela da locale (`include "%L"`)
e sobrescrevendo somente dead_acute+c/C para ç/Ç. O layout físico e o idioma
não foram alterados. Backup de ausência:
`$HOME/.local/state/ricy-teclado-backups/20261010-180848-912053/`.
Não foram encerrados os aplicativos do usuário; processos abertos podem
manter a tabela anterior e precisam ser fechados completamente/reabertos.

Adicionada `contributions/keyboard-cedilla/` aos kits ativo e de transporte,
com aplicador idempotente, preservação de regras existentes e instruções de
reversão. REINSTALAR.md agora inclui o passo 3a. Os archives compactados
originais não foram regenerados; esta correção está nos diretórios atualizados.

Validação: libxkbcommon confirmou ç/Ç em en_US.UTF-8, C.UTF-8 e pt_BR.UTF-8;
á, ã, ê, apóstrofo e dead_cedilla+c permaneceram corretos. Gtk.IMContextSimple
confirmou ç/Ç, á e ã em janela offscreen, sem enviar teclas às janelas do usuário.
Sintaxe do aplicador e segunda execução sem mudanças conferidas. A digitação
física nas janelas existentes do Konsole/Brave depende do recarregamento pelo
usuário e não foi apresentada como teste realizado. A conta separada do SDDM
e o console virtual não foram alterados por este ajuste de usuário.

## Contribuição — Cedilha no Brave por XWayland — 2026-10-10 18:14 (America/Sao_Paulo)

O usuário confirmou ç no Konsole após a contribuição anterior, mas o Brave
continuou produzindo ć. A primeira correção não cobria a rota nativa Wayland
do Chromium. Brave local: 155.1.97.56. O código upstream WaylandInputMethodContext
usa CharacterComposer para eventos não consumidos pelo IME, com tabela própria.

Configurado `$HOME/.config/brave-flags.conf` com `--ozone-platform=x11`.
O launcher `/usr/bin/brave` do pacote lê esse arquivo. Apenas o navegador
usa XWayland; a sessão KDE permanece Wayland. Não foram alterados .XCompose,
layout, idioma, flags de sandbox nem perfil pessoal. Backup de ausência:
`$HOME/.local/state/ricy-teclado-backups/20261010-181356-714082/`.
O Brave deve ser completamente reaberto para carregar a opção. Em telas
HiDPI, a mudança de backend pode alterar escala/renderização.

Adicionado aplicador idempotente `contributions/keyboard-cedilla/aplicar-brave.py`
a ambos os kits. README, roteiro de reinstalação e SHA256SUMS atualizados.
Os archives compactados históricos continuam sem esta atualização.

Teste funcional: instância Brave com perfil temporário em servidor XWayland
aninhado separado, campo HTML local e entrada por XTest somente nesse display.
A opção X11 sozinha (sem forçar GTK, sem variáveis de IM) produziu `ççÇ`.
A primeira rodada com GTK explícito também passou; essas opções extras não
foram incluídas na configuração definitiva. As instâncias isoladas foram
encerradas; logs/perfis de teste permanecem em /tmp/ricy-brave-validation-*.
Segunda execução do aplicador não alterou o arquivo. Não foi enviada entrada
às janelas do usuário nem usado seu perfil no teste.

## Contribuição — Driver USB AIC8800 para Wi-Fi e Bluetooth — 2026-10-10 18:25 (America/Sao_Paulo)

Solicitação do usuário: instalar o driver do adaptador Wi-Fi/Bluetooth AIC8800.
Identificação local antes da instalação: USB `a69c:8800` (AIC Wlan), porta
1-14, sem driver/interface de rede. Kernel ativo 7.2.9-2-cachyos com Clang;
LTS 6.18.55-2-cachyos-lts também instalado, compilado com GCC. Ambos tinham
headers correspondentes. Secure Boot estava desativado. Ethernet existente
foi preservada; nenhuma rede/senha foi configurada.

Instalados `dkms 3.4.3-1` e pacote local
`aic8800-usb-dkms-ricy 5.0.20260123.9-3`. Fonte primária Radxa:
https://github.com/radxa-pkg/aic8800, commit
`d13d07963cd15d731e2895e8288a04cca6152ac9`, arquivo de origem verificado por
SHA256. A preparação normaliza CRLF e aplica a série de patches upstream,
incluindo compatibilidade dos kernels novos e uso de BlueZ. Foram empacotados
somente os drivers/firmware USB; nenhuma biblioteca Android foi instalada.

Módulos: `aic_load_fw`, `aic8800_fdrv`, `aic_btusb`. Firmware:
`/usr/lib/firmware/aic8800_fw/USB`. DKMS escolhe Clang/GCC lendo a configuração
de cada kernel e recompila nas atualizações com headers disponíveis. A primeira
compilação DKMS do LTS usava Clang fixo e falhou; corrigida a seleção por kernel.
Ambos passaram após a correção. A versão final registra o driver Bluetooth
antes de carregar o firmware e dá prioridade a aic_btusb quando btusb é
solicitado. Foi removida a referência circular entre aic_load_fw e
aic8800_fdrv: o último já tem dependência nativa do primeiro. btusb não foi
bloqueado globalmente.

Após a carga do firmware, o dispositivo passou a `a69c:8801`, com duas
interfaces Wireless ligadas a aic_btusb e uma Vendor Specific ligada a
aic8800_fdrv. NetworkManager reconheceu wlan0 e p2p-dev-wlan0. RFKill sem
bloqueios. Buscas encontraram 9–13 redes Wi-Fi. BlueZ criou hci0,
Powered=yes; descoberta Bluetooth iniciou sem erro e foi encerrada após o
teste. Não surgiram dispositivos anunciados nessa janela de busca. Serviço
bluetooth já estava habilitado antes; foi iniciado e está ativo.

Verificação final: DKMS instalado para 7.2.9-2-cachyos e
6.18.55-2-cachyos-lts; vermagic correto nos dois. Teste funcional realizado
somente no kernel ativo 7.2; não houve boot no LTS, conexão Wi-Fi ou pareamento.
O driver upstream emite avisos de compilação/debug, preservados nos logs; os
builds terminaram com sucesso. As transações pacman geraram snapshots Snapper
pelo hook já existente e reconstruíram os initramfs por Limine/mkinitcpio.
Não houve reinício do computador nem interrupção da Ethernet.

Reprodução: `contributions/driver-aic8800/README.md` no kit ativo e de transporte,
com PKGBUILD, dkms.conf, build.sh e configuração modprobe. REINSTALAR.md ganhou
passo opcional 6a. SHA256SUMS atualizado/verificado nas duas cópias. Os archives
compactados históricos não foram regenerados. Fontes baixadas e compilações
ficam no cache local, sem credenciais. Logs e inventário anterior:
`$HOME/.local/state/ricy-aic8800/`.

Reversão: `sudo pacman -R aic8800-usb-dkms-ricy`; DKMS remove módulos em disco.
Reconecte o adaptador ou reinicie para encerrar módulos ainda carregados.
DKMS/BlueZ podem ser mantidos para outros dispositivos; o estado anterior do
serviço Bluetooth era habilitado e inativo.

## Contribuição — Busca junto à lupa da barra — 2026-10-10 18:34 (America/Sao_Paulo)

O usuário pediu que Search Applications aberto pela lupa apareça no canto,
seguindo o comportamento do controle Noctalia à direita. Ativado
`shell.panel.open_near_click_launcher = true`. O launcher permanece attached/auto:
o clique na lupa posiciona a busca junto ao widget, no lado esquerdo da barra.
A opção equivalente do control-center já estava true. Os wrappers de teclado
e a barra superior search_edge foram preservados.

Atualizados o perfil ativo e os config.toml de outputs da contribuição
noctalia-kde-integration-and-menus nos kits ativo e de transporte. Backup:
`$HOME/.local/state/ricy-busca-backups/20261010-183355-074732/`.
Executados `noctalia config validate` (válido) e `noctalia msg config-reload`
(ok). Exportação efetiva confirmou true, attached e auto. A shell permaneceu
ativa com o mesmo PID 1218, sem reiniciar nem encerrar aplicativos filhos.
O painel já aberto pode exigir fechar/reabrir pela lupa para reposicionar;
não houve clique automatizado nem captura visual da nova geometria.
REINSTALAR.md e hashes dos config.toml foram atualizados.

Referência: [configuração oficial de painéis Noctalia](https://github.com/noctalia-dev/noctalia/blob/main/docs/user/configuration/shell.mdx).

## Contribuição — Barra superior compacta e arredondada da busca — 2026-10-10 18:37 (America/Sao_Paulo)

Após validar a abertura junto à lupa, o usuário pediu uma barra superior
mais estreita e arredondada para a busca aberta por Super/digitação.
Alterado somente `[bar.search_edge]`: thickness 16, margin_ends 640,
margin_edge 8, radius e os quatro raios 8. Permanecem opacity 0,70,
blur, sem sombra, sem reserva de espaço e sem auto-hide. A revelação e
ocultação continuam sob o adaptador/wrapper existentes. A lupa inferior
continua com open_near_click_launcher=true.

Os dois monitores atuais têm largura lógica 1920; a barra resultante mede
640 px, centralizada, cerca de 40 px além do launcher de 560 px por lado.
O topo fica a 8 px da borda. Em outras resoluções, recalcule margin_ends
como `(largura lógica - largura desejada) / 2`; para escalas/resoluções
distintas, use overrides por monitor. Isso foi registrado em REINSTALAR.md.

Atualizados o perfil ativo e os dois templates de config.toml. Backup:
`$HOME/.local/state/ricy-busca-backups/20261010-183630-034925/`.
Validação Noctalia passou e config-reload retornou ok; shell permaneceu
no PID 1218. Busca reaberta pela interface D-Bus usada pelos atalhos.
Captura visual conferiu largura reduzida, união com o painel e cantos
arredondados. O painel de verificação foi fechado ao concluir. Capturas
locais temporárias não foram incluídas no kit. Manifestos SHA256 atualizados.

## Contribuição — Barra da busca apenas no monitor ativo — 2026-10-10 18:40 (America/Sao_Paulo)

O usuário validou o visual compacto, mas a barra aparecia nas duas telas
enquanto o launcher abria em uma. O adaptador agora consulta
`org.kde.KWin.activeOutputName`, a mesma referência usada pelo Noctalia/KDE
para resolver o monitor da abertura. Antes de revelar o launcher, recolhe
a barra search_edge em todas as telas e executa `bar-show search_edge NOME`
para somente o conector ativo. Ao fechar a busca, recolhe a barra como antes.

`abrir-menu.sh` agora chama toggleDisplay do mesmo adaptador D-Bus; isso
unifica Super/Super+Espaço e a digitação sem duplicar a escolha de monitor.
Nenhum nome DP/HDMI foi fixado nos scripts. Mantidos a barra de 640 px,
arredondamento, comportamento da lupa inferior e abertura junto ao clique.
Falhas de consulta/comando devolvem erro D-Bus e tentam recolher a barra.

Backups dos dois scripts anteriores:
`$HOME/.local/state/ricy-busca-backups/20261010-183834-044045/`.
Atualizadas as cópias ativa/de transporte, REINSTALAR.md e SHA256SUMS.
Reiniciado somente noctalia-busca-desktop.service, preservando a shell e
seus aplicativos filhos; MainPID da shell continuou 1218.

Verificação: Python/Bash válidos. Abertura por display D-Bus no DP-1
confirmada visualmente com a barra somente nessa tela. Abertura pelo wrapper
de Super no HDMI-A-1 também conferida: barra e launcher apenas na tela
correta. O foco foi alternado pelas ações KWin Switch to Screen para o teste,
aguardando sua aplicação; ao concluir, painel fechado e foco devolvido a DP-1.
Não houve clique automatizado na lupa nem alteração de geometria das janelas.

## Contribuição — Notificações contínuas com a taskbar — 2026-10-10 18:55 (America/Sao_Paulo)

Trabalho: notificações no canto inferior direito com barra de tempo e união
visual com a taskbar. Após a prévia, o usuário pediu explicitamente retirar
o recorte arredondado da borda inferior direita. O resultado aplicado mantém
os outros três cantos arredondados e faz essa borda alcançar a taskbar.

No perfil ativo em
`$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus/work/noctalia-profile/config/noctalia/config.toml`
e nos templates `outputs/noctalia-test/config.toml` dos dois kits,
`[notification]` passou a position="bottom_right", follow_focused_output=true,
background_opacity=0.70, border=false, offset_x=0 e offset_y=0. A notificação
segue o monitor ativo e a mesma transparência da taskbar. A barra de progresso
Mauve e a expiração já são nativas do Noctalia; não foi criado outro daemon.
Notificações persistentes mantêm o comportamento nativo.

O Noctalia 5.2.1 não oferece preferência de raio individual para esse cartão.
Aplicado patch em `src/shell/notification/notification_toast.cpp` para usar
raio zero somente no canto inferior direito quando bottom_right e offset_y=0.
Fundo e região de blur usam os mesmos quatro raios. Este estado substitui a
premissa histórica de usar apenas configurações sem recompilar o Noctalia:
agora há uma adaptação local pequena sobre o commit v5.2.1
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`.

Instalados neste destino meson 1.12.1-2, ninja 1.13.2-3.1,
wayland-protocols 1.49-1, nlohmann-json 3.12.0-2 e stb (20260415), além da
dependência python-tqdm 4.70.1-1. A instalação pelos repositórios foi concluída
com autenticação local; os hooks criaram snapshots Snapper 41/42.
Compilação release Meson/C++23 e Ninja concluída sem erros. Fontes/build em
`$HOME/.cache/ricy-noctalia-src-5.2.1/`, fora dos materiais portáteis.

O binário selecionado pela shell é `$HOME/.local/lib/ricy-noctalia/noctalia`,
por `~/.config/systemd/user/noctalia-teste.service.d/50-notificacoes-ricy.conf`.
`/usr/bin/noctalia` e o pacote original permanecem instalados. O prefixo /usr
da compilação serve para localizar os assets existentes; não foi executado
meson install. A shell e o adaptador foram reiniciados com KillMode=process
temporário para preservar os aplicativos lançados pelo menu, incluindo o
Codex usado neste trabalho; o override temporário foi removido e a unidade
voltou a KillMode=control-group. Shell e adaptador estão ativos.

Materiais incluídos nos kits ativo e de transporte:
`contributions/notification-continuity/README.md`, `compilar.sh`, `ativar.py`,
`notificacao-canto-direito.patch` e licença MIT upstream. `REINSTALAR.md`
ganhou o passo 4a. Para reproduzir, siga o README: prepare primeiro a integração
permanente, instale as dependências, execute `bash compilar.sh` e
`python ativar.py`. O compilador exige versão/commit compatíveis e recusa
alterações de fonte desconhecidas. O executável local não acompanha sozinho
atualizações do pacote: revise/rebaseie e recompile o patch ao trocar de versão,
ou restaure a seleção original antes de usar assets de outro Noctalia.

Verificação executada: sintaxe Python/Bash, git diff --check, compilação nativa
e nova execução do compilador sobre o build existente passaram. Capturas da
notificação no HDMI-A-1 confirmaram a união do canto inferior direito e a barra
de tempo menor entre o início e o meio. Teste D-Bus com prazo de 8000 ms recebeu
NotificationClosed com reason=1 aos 8,0 segundos; captura posterior confirmou
seu desaparecimento. O teste visual e de expiração foi nesta instalação,
não em outro computador. A pausa ao passar o ponteiro foi conferida no código
nativo, sem teste de interação separado.

Backups locais, não incluídos no kit:
`$HOME/.local/state/ricy-notificacoes-backups/20261010-184413-289100/config.toml`
contém a configuração anterior; a ativação guardou seu estado em
`20261010-185312-672533/manifest.json` no mesmo diretório-base. Para desfazer
a seleção do binário use `python ativar.py --restaurar CAMINHO_DO_BACKUP`
conforme o README. Para desfazer as preferências, restaure o config.toml
anterior ou ajuste somente `[notification]`; a restauração do binário não
remove pacotes nem essas preferências.

SHA256SUMS atualizado e verificado nas duas cópias preservando suas entradas.
Arquivos ZIP/tar históricos não foram regenerados. Nenhum histórico de
clipboard, estado privado ou captura de tela foi incluído nos materiais.

## Contribuição — Junção curva do canto inferior esquerdo da notificação — 2026-10-10 18:59 (America/Sao_Paulo)

O usuário corrigiu o resultado anterior: retirar somente o raio inferior
direito não resolvia a conexão visual, pois o canto inferior esquerdo ainda
se arredondava para dentro do cartão. A variante local foi ajustada novamente:
agora esse canto se abre para fora com uma curva côncava, seguindo a geometria
nativa dos painéis encaixados, e encontra a borda superior da taskbar.
O canto inferior direito continua reto; os dois superiores ficam arredondados.
Esta contribuição substitui a descrição anterior de manter três cantos
arredondados. As preferências de posição, monitor, opacidade e prazo continuam
as documentadas na contribuição anterior.

O patch em `src/shell/notification/notification_toast.cpp` agora reserva uma
extensão à esquerda na superfície e na área de recorte da animação, preservando
a largura do conteúdo e o alinhamento à direita. Fundo e blur usam
CornerShape::Concave no canto inferior esquerdo e o mesmo inset lateral.
A geometria especial se aplica somente em bottom_right com offset_x=0 e
offset_y=0; outras posições/afastamentos mantêm o formato nativo. Não foi
alterado o funcionamento do daemon nem da contagem de tempo.

Compilação incremental Ninja concluída sem erros e git diff --check passou.
Executado novamente `python ativar.py`; a shell usa o binário local corrigido.
Backup dessa troca em
`$HOME/.local/state/ricy-notificacoes-backups/20261010-185903-989917/`.
Este backup restaura a variante anterior, com somente o canto direito reto;
o backup da primeira ativação restaura a seleção do pacote original.
A troca usou o override temporário de preservação de aplicativos; ao final,
shell e adaptador ativos e KillMode=control-group restabelecido.

Captura visual no DP-1 confirmou a extensão curva à esquerda até a taskbar,
com o cartão alinhado à borda direita. Repetido o teste D-Bus de 8000 ms:
NotificationClosed reason=1 aos 8,0 segundos, com progresso menor na captura
intermediária e ausência do cartão na captura posterior. Não houve novo teste
de hover, de outras posições ou de instalação em outra máquina.

Atualizados o patch e o README em
`contributions/notification-continuity/` nas cópias ativa e de transporte,
o passo 4a de REINSTALAR.md e os dois SHA256SUMS (423 entradas verificadas).
Para reproduzir/reverter, permanecem os comandos dos scripts e as cautelas
de atualização de versão descritos no README. Capturas e backups permanecem
locais; os archives compactados históricos não foram alterados.

## Contribuição — Continuidade do blur entre barras e painéis — 2026-10-10 19:20 (America/Sao_Paulo)

Corrigida a continuidade do fundo desfocado entre taskbar, notificações,
busca junto à lupa, menu do Noctalia e apoio superior da busca por Super ou
digitação. Igualar opacidade e cantos não eliminava a emenda: o blur nativo
amostrava um retângulo diferente para cada superfície.

Foi compilado o efeito separado `ricyblur`, baseado no código oficial do
KWin 6.7.5, commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.
Enquanto um painel ou aviso Noctalia está visível, as suas superfícies usam
o mesmo fundo filtrado por monitor, recortado pelas formas de cada janela.
A cópia do fundo é feita antes de desenhar o Noctalia, sem incluir a própria
barra. O recorte OpenGL é preservado na composição final e não limita a cópia
ou o filtro compartilhado. Outros aplicativos seguem o algoritmo nativo.
Também aplicado `panel_overlap = 0` em `[bar.default]` e `[bar.search_edge]`,
no perfil ativo e nos dois templates públicos, removendo a faixa de um pixel
com transparência duplicada na junção. A geometria de cantos e notificações,
a opacidade 0,70, a barra compacta e a escolha de monitor continuam preservadas.

O novo plugin foi instalado em
`/usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so`, mantendo os archives
originais do KWin. O helper `$HOME/.local/lib/ricy-blur/iniciar.py` e a unidade
`ricy-blur-continuidade.service`, habilitada na sessão gráfica, selecionam o
efeito somente em KWin 6.7.5 quando suportado. O blur nativo permanece
habilitado na configuração e é mantido/recarregado se a variante não puder
ser usada. O compositor e a shell principal não foram reiniciados nesta troca.

Materiais públicos em `contributions/blur-continuity/`: README, licença
GPL-2.0-or-later, patch e scripts `compilar.py`, `integrar.py`, `iniciar.py`.
O compilador fixa versão e commit, recusa alterações desconhecidas na fonte
e recompila no destino; não distribuímos o binário desta máquina. Foram
usados os headers oficiais Vulkan 1.4.363 no cache, commit
`6802bb4733b63ed5efd3adb308a6c885ef180ea1`, sem instalar novos pacotes neste
trabalho. O roteiro de reinstalação usa o pacote vulkan-headers do destino.
Consulte o README e o passo 4b de REINSTALAR.md para reproduzir ou voltar ao
blur nativo; versões futuras do KWin exigem revisão/recompilação do patch.

Verificação executada: compilação final reproduzida pelo script do kit,
patch sem erros de whitespace e sintaxe Python conferida. Teste visual em
KWin/Noctalia isolados com fundo de faixas coloridas verificou a continuidade
entre menu encaixado e barra; a sessão de teste foi encerrada ao terminar.
Na sessão principal, efeito ricyblur carregado, unidade ativa/habilitada e
configuração Noctalia validada/recarregada; aberta a busca superior e
verificado seu apoio no monitor correspondente. O usuário confirmou:
“Visualmente já passou”. Não houve novo teste de hover ou de expiração da
notificação nesta contribuição; os testes de prazo estão no registro anterior.
O journal do compositor principal não registrou erros de framebuffer desde
a aplicação da variante final.

Limites: escalas diferentes, reinstalação em outra máquina e consumo com
vídeo/animações não foram medidos. Com painel/aviso aberto, frames alterados
repintam o monitor para evitar reutilizar pixels contendo a barra; isso pode
aumentar o custo de composição. Não há laço de repintura contínuo quando a
cena está parada, nem gravação do fundo em disco pelo efeito.

Backups privados em `$HOME/.local/state/ricy-blur-backups/`: integrador
`20261010-191516/` e perfil anterior em `20261010-191527/config.toml`.
Restaurar o blur nativo não reverte panel_overlap; use o backup ou ajuste
somente essa preferência. As cópias ativa e portátil foram sincronizadas,
com todos os hashes conferidos e as entradas anteriores preservadas
(429 archives em cada SHA256SUMS). Capturas, caches, perfis/clipboard e backups
não foram incluídos. Os ZIP/tar históricos continuam como retratos anteriores;
para transportar esta correção, copie a pasta pública atualizada com este
registro e o roteiro.

## Contribuição — Wallpaper no cartão Home da sessão real — 2026-10-10 19:24 (America/Sao_Paulo)

O usuário apontou que a sessão real não mostrava wallpaper no menu. O teste
isolado tinha o serviço de wallpaper Noctalia ativo; na sessão principal ele
está desativado porque o Plasma gerencia o desktop. Sem superfície/texture de
wallpaper do Noctalia, HomeTab recebia currentPath vazio e mostrava cor sólida.

A variante local Noctalia 5.2.1 agora consulta getDefaultWallpaperPath no cartão
Home quando currentPath está vazio e o wallpaper Noctalia está desativado.
A imagem é carregada pelo thumbnail nativo, mantendo o Plasma responsável pelo
desktop. A alteração está em src/shell/control_center/tabs/home_tab.cpp,
incluída no patch composto de contributions/notification-continuity;
a geometria das notificações e o efeito ricyblur permanecem aplicados.
O cartão exibe a imagem; o restante do menu continua translúcido com blur do
conteúdo atrás dele, sem aplicar wallpaper artificial ao painel inteiro.

Adicionado sincronizar-wallpaper.py: lê a imagem estática pela API do Plasma,
valida existência e igualdade entre desktops e registra o caminho via IPC
wallpaper-set. Nesta máquina, ambos usam
/usr/local/share/ricy/limine-splash.png. Não habilitamos [wallpaper] no Noctalia.
O sincronizador não acompanha futuras mudanças automaticamente: execute-o
novamente após mudar o fundo no Plasma. Fundos diferentes/animados exigem outra
integração e são recusados sem alteração de preferências pelo script.

Verificação: Ninja compilou o binário; compilar.sh aceitou o patch composto;
git diff --check e sintaxe Python/Bash passaram. Ativação com preservação de
aplicativos concluída, KillMode=control-group restabelecido e ricyblur ainda
carregado. Aberto control-center home na sessão principal; captura confirmou
a imagem Limine no cartão, comparada ao arquivo do desktop. Menu fechado ao
fim. Não foi feito novo teste de notificações ou migração para outra máquina.

Backup do binário anterior em
$HOME/.local/state/ricy-notificacoes-backups/20261010-192258-920118/;
restaura o executável anterior com notificações corrigidas e cartão sólido.
O primeiro sincronizador apontou o backup para config/settings.toml em vez
de state/settings.toml: 20261010-192254-917307 NÃO contém backup do estado
original e seu manifest foi marcado como inválido para restauração.
Corrigido o caminho no script distribuído. Backup válido em
$HOME/.local/state/ricy-menu-wallpaper-backups/20261010-192326-080532/ guarda
o estado já sincronizado, antes da segunda execução idempotente; não deve
ser apresentado como cópia anterior à primeira alteração. O caminho padrão
Noctalia observado antes era /usr/share/noctalia/assets/noctalia-wallpaper.png.

Patch, README e sincronizador atualizados nas duas cópias do kit; passo 4a de
REINSTALAR.md atualizado e 430 hashes conferidos em cada manifesto, preservando
as entradas anteriores. Nenhuma captura, imagem pessoal, estado ou backup foi
incluído; os compactados históricos permanecem inalterados.

## Contribuição — Datas em inglês, clima e eventos em Cosmópolis/SP — 2026-10-10 19:28 (America/Sao_Paulo)

Atendido o pedido de datas em inglês mantendo Cosmópolis/SP-BR como localização.
O processo Noctalia herdava LC_TIME=pt_BR.UTF-8, apesar da interface em inglês.
Aplicado shell.lang="en" e drop-in 60-ricy-idioma-localizacao.conf com
LC_TIME=en_US.UTF-8, TZ=America/Sao_Paulo e UnsetEnvironment=LC_ALL.
A locale global, unidades regionais e composição do teclado não foram alteradas.

Localização fixa: auto_locate=false e address="Cosmopolis, Sao Paulo, Brazil".
O endereço completo foi validado na API usada pelo Noctalia: latitude -22.64583,
longitude -47.19611, nome Cosmópolis, Brazil. Consultar somente Cosmópolis
retornou uma cidade homônima nos EUA; esse resultado não foi aplicado.
Clima habilitado em unidades métricas e calendário/eventos habilitado.
O usuário escolheu apenas habilitar eventos por enquanto: nenhuma conta ou
fonte de eventos/feriados foi acrescentada. O calendário usa o fuso da sessão;
a localização por si só não fornece eventos pessoais ou feriados.

Nova contribuição contributions/noctalia-language-and-localization com aplicar.py e
README. O aplicador ajusta as mesmas chaves no perfil e no settings.toml, pois
havia um override privado auto_locate=true; preserva outras preferências e
contas. Instala o drop-in e usa o helper existente de preservação de aplicativos
para reiniciar shell/adaptador. Não foi alterado o executável local nesta etapa.
Templates públicos das duas cópias também atualizados; aplicar.py é necessário
para instalar LC_TIME/TZ na unidade e corrigir overrides do destino.

Verificação executada: Noctalia config validate passou; ambiente do processo
confirmou LC_TIME=en_US.UTF-8 e TZ=America/Sao_Paulo sem LC_ALL.
Calendário na sessão real exibiu Saturday e October; cartão de eventos habilitado
sem contas conectadas. Cache nativo confirmou localização brasileira e previsão
com timezone America/Sao_Paulo, offset -10800 e sete dias disponíveis.
Comparação TOML com o backup confirmou que as preferências não relacionadas
foram preservadas. ricyblur permaneceu carregado; KillMode padrão restabelecido.
Não foram testadas sincronização de conta ou instalação em outra máquina.

Backup privado anterior em
$HOME/.local/state/ricy-idioma-localizacao-backups/20261010-192713-914138/.
O manifest indica presença anterior de config/settings/drop-in. Consulte o
README para reversão e preservação de alterações posteriores; dados privados
e capturas não foram incluídos no kit. Registro, passo 4c de REINSTALAR.md e
ambas as cópias sincronizados, com 432 hashes conferidos em cada manifesto.
Os compactados históricos permanecem inalterados.

## Contribuição — Identidade visual Noctalia como referência do sistema — 2026-10-10 19:35 (America/Sao_Paulo)

O usuário pediu registrar a identidade visual do Noctalia e incorporá-la ao
Ricy para orientar a adequação de outras partes do sistema. Criado
IDENTIDADE-VISUAL.md como guia vigente, com vínculo no início deste registro
e no roteiro de reinstalação. Os próximos ajustes visuais devem consultar
essa referência e documentar adaptações e resultados no componente real.
Esta contribuição registra a base aprovada; não aplica novos temas ao sistema.

A referência captura paleta KDE-Atual/Catppuccin Mocha com acento Mauve,
fundo #181825, cartões #313244, texto #cdd6f4/#a6adc8, contornos #46485c,
hover #977dba e cores semânticas. Define materiais com fill alpha 0,70 para
barras, notificações e painéis que herdam a barra, preservando texto legível
e cartões sólidos. Diferencia painéis desanexados no modo solid, de alpha 1,
e menus Kvantum opacos: não foi generalizada transparência para todo o sistema.

Registrados cantos e junções vigentes: taskbar 44 px com superiores 6 px e
inferiores retos; apoio superior 640 × 16 px, raio 8 px e margem superior 8 px;
notificação com canto inferior esquerdo côncavo para fora e direito reto;
bar.panel_overlap=0 e fundo compartilhado ricyblur por monitor. Fonte shell
Noto Sans; KDE/GTK JetBrainsMono Nerd Font 10, com distinção entre pontos e
pixels lógicos. Raios, espaçamentos, paddings e durações nativos foram extraídos
das constantes do código 5.2.1 e marcados como referência, não medição de todos
os componentes. A escala de cantos 1,3 é distinta dos raios explícitos da barra.

Materiais públicos em contributions/noctalia-visual-identity:
README.md (guia), tokens.json (valores/papéis estruturados, não executável) e
referencia.svg (prancha vetorial própria, sem dados pessoais). O README foi
publicado também em Documents/ricy/IDENTIDADE-VISUAL.md para acesso direto.
A prancha ilustra cores, cartões, fonte e junção com alpha em uma forma comum;
não é uma captura real nem simula o filtro OpenGL. Os archives permitem que
outros agentes usem os mesmos parâmetros nos próximos trabalhos.

Validação executada: paleta ativa e template público comparados byte a byte;
conferidos overrides visuais pertinentes sem copiar settings privado; lidos
Style, regras de transparência/radius no código e preferências KDE, Kvantum,
GTK e Plasma atuais. JSON e SVG analisados; cores do JSON conferidas contra
a paleta; SVG renderizado e inspecionado visualmente. Efeito ricyblur confirmado
carregado. Nenhum aplicativo, serviço ou preferência foi alterado/reiniciado.

O guia diferencia referência atual e trabalho futuro: Qt/KDE tem parte da
integração ativa; GTK e aplicativos de terceiros não são declarados totalmente
harmonizados; login/bloqueio têm registro próprio e não foram revalidados aqui.
Datas inglesas, fuso São Paulo e região Cosmópolis permanecem preservados.
Aplicar a linguagem a novas áreas exigirá mudanças e validação próprias; esta
contribuição não apresenta essas adaptações como concluídas. Reversão aqui é
somente documental, preservando o histórico; futuros ajustes devem guardar
seus backups e registrar reversão por componente.

Sincronizados os três materiais nas cópias ativa e portátil. SHA256SUMS de
ambas preserva as 432 entradas anteriores e acrescenta três (435 verificadas).
Os documentos fora do kit não fazem parte desse manifesto, conforme estrutura
existente. Não incluídos capturas, clipboard, perfis, backups ou fonte/build
completa; compactados históricos não foram modificados. Para transportar,
copie também IDENTIDADE-VISUAL.md junto a ricy.md, REINSTALAR.md e kit atual.

## Contribuição — Menu da aplicação como composição Noctalia — 2026-10-10 19:44 (America/Sao_Paulo)

O usuário pediu que as opções do botão direito num aplicativo da taskbar
aparecessem na composição Noctalia, como o tray. O popup XDG independente foi
substituído por um Panel nativo encaixado, id ricy:taskbar-menu, gerenciado pelo
mesmo PanelManager da gaveta do tray. A abertura usa o callback da barra com
âncora no centro do ícone, mantendo barra/monitor de origem. Herda opacidade,
blur, junção e animação nativos. Não foram alterados menus internos de apps.

A lista e seus handlers originais foram preservados: Pin/Unpin, ações do
desktop entry, Close e Close All, conforme a aplicação/janelas disponíveis.
Callbacks usam weak guard de vida do widget; ativação/abertura adiada até o
fim do evento. Incluídas setas e Enter/Espaço para navegar/ativar; Escape e
clique externo ficam a cargo do PanelManager. Removido o popup próprio e sua
interceptação de eventos na taskbar.

O usuário viu a primeira composição e apontou que a altura gerava rolagem.
Identificado padding duplicado: PanelManager já descontava a margem nativa.
Corrigido layout e removida ScrollView; altura calculada por todas as entradas,
separadores e padding, sem limite de 12 linhas. Largura calculada pelo texto
mais largo, mínimo de conteúdo 240 px à escala 1, acrescida da margem nativa.
Isso substitui o popup de largura mínima fixa e a primeira composição rolável.

Nova contribuição contributions/taskbar-menu-composition com README,
compilar.sh, patch composto noctalia-ricy.patch e licença MIT. O patch aplica
sobre o commit Noctalia 5.2.1 conhecido e mantém as correções anteriores de
notificação e wallpaper do Home. O compilador deste diretório é a referência
para reconstruir o estado completo atual; o anterior recusa esse cache com
mudanças diferentes. O README orienta preservar a fonte anterior e usar cache
limpo ao migrar de variante, sem sobrescrever alterações desconhecidas.
Atualizados o passo 4a, o guia de identidade/tokens e a nota da contribuição
anterior para apontar ao compilador composto.

Verificação executada: compilação final Ninja pelo script da contribuição,
git diff --check, bash -n e Noctalia config validate passaram. SHA do executável
ativo corresponde ao build final: 8fa83842d58d1d1ceedd791defb9a82169f7cfa96ac1065f94ed14a861d24a26.
Shell/adaptador ativos, KillMode=control-group restabelecido e ricyblur carregado.
A captura enviada pelo usuário comprovou a composição inicial, ainda com
scroll. Não foi registrada confirmação visual do ajuste final sem scroll,
teste das ações em aplicativo descartável, listas muito extensas, barras
laterais/superiores ou migração para outra máquina. A tentativa de automatizar
um clique não abriu o menu alvo; nenhum resultado dessa tentativa foi usado
como validação. O dispositivo de entrada e script temporários foram encerrados.

Backups privados em $HOME/.local/state/ricy-notificacoes-backups/:
20261010-193948-522126 restaura a variante anterior com popup e correções
anteriores; 20261010-194151-517805 restaura a primeira composição com scroll.
Use ativar.py --restaurar conforme README, preservando aplicativos.
A troca não modifica preferências de idioma, wallpaper ou clima.

Sincronizados quatro archives públicos nas cópias ativa e portátil; ambos os
manifestos preservam entradas anteriores e têm 439 hashes conferidos.
Capturas, dispositivos/scripts de teste, binários e estado privado não foram
incluídos. Os compactados históricos permanecem inalterados.

## Contribuição — Opções do tray na composição Noctalia e retorno à gaveta — 2026-10-10 19:56 (America/Sao_Paulo)

O usuário pediu a mesma composição do menu da aplicação para as opções dos
itens do tray. Substituído o popup independente por Panel nativo encaixado
ricy:tray-menu, preservando DBusMenu como fonte das opções e das ações.
Mantém Pin/Unpin, separadores, entradas desabilitadas, checkmarks, rádio e
submenus. Herda opacidade da barra, blur compartilhado, desenho de junção,
animação, monitor/barra e fechamento externo do PanelManager. Itens que não
expõem DBusMenu continuam apresentando o menu do próprio aplicativo.

A largura acompanha o maior texto (mínimo de conteúdo 240 px à escala 1).
A altura considera todas as entradas e margens nativas, sem padding duplicado
nem limite artificial de linhas. ScrollView só apresenta rolagem se a lista
exceder a área disponível. Submenus navegam dentro da mesma composição, com
linha de retorno e esquerda/Escape para subir um nível. Na raiz Escape fecha.
Eventos opened/closed, atualizações e carregamento sob demanda continuam
ligados ao provedor; retry limitado a 300/900/2000 ms. Ações adiadas verificam
a linha atual e a geração/vida do menu antes de atuar. Remover o item fecha o
menu. Uma consulta de retângulo público no PanelManager traduz o clique na
gaveta para coordenadas do monitor antes de abrir o menu substituto.

O usuário confirmou: “Passou e ficou bom”, pedindo uma setinha entre menu e
tray para retornar à gaveta. Adicionado botão Ghost nativo na base do menu,
chevron-down na barra inferior; 32 px e intervalo 4 px à escala 1. Permite
voltar diretamente à gaveta no mesmo monitor/barra/âncora, inclusive a partir
de submenus. O botão participa do Tab/Enter nativo. O usuário confirmou
“Passou” depois da ativação da setinha: ambas as etapas passaram visualmente.

Nova contribuição contributions/tray-menu-composition com README, compilador,
patch completo e licença MIT. O patch corresponde ao commit Noctalia 5.2.1
6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 e inclui as mudanças anteriores de
notificações, wallpaper do Home e menu da taskbar. Este é o compilador de
referência para reproduzir a variante atual. Compiladores/patches anteriores
permanecem históricos e recusam cache com alterações diferentes; preserve
a fonte anterior e use cache limpo ao migrar, conforme o README.
Atualizados reinstalação, identidade visual e tokens, notas das contribuições
anteriores, kit ativo e cópia portátil. Preferências de idioma/clima e contas
não foram alteradas.

Verificações: compilação final Ninja pelo script da contribuição, git diff
--check, bash -n e validação do perfil passaram. Executável ativo e build
coincidem, SHA256 cf9ee62d8a0cb359a9a2775eb4ccc5d90d08c3d45833967cc0fd1c8c56b95ada. Shell/adaptador ativos, KillMode=control-group
restabelecido e efeito ricyblur carregado. Confirmação visual do usuário
registrada para menu e setinha. Não foi registrado teste completo de ações,
submenus, listas extensas, barras laterais/superiores ou outra máquina.
Um provedor DBus temporário foi registrado e removido; a tentativa de clicar
nele automaticamente não abriu seu menu e não foi usada como validação.
Dispositivos de entrada, script KWin e preferências do dispositivo temporário
foram removidos. Nenhuma ação real de atualização/fechamento foi disparada
como teste.

Backups privados em $HOME/.local/state/ricy-notificacoes-backups/:
20261010-195150-527306 restaura a variante anterior com menu da taskbar;
20261010-195539-054921 restaura a composição do tray sem a setinha.
O ativador/restaurador anterior continua responsável pela troca segura de
binário/drop-in, preservando aplicativos e o pacote /usr/bin/noctalia.

Ambos os manifestos preservam entradas anteriores e têm 443 hashes
conferidos. Sem binários, contas, estado privado, capturas ou material do
clipboard no kit. Compactados históricos permanecem inalterados.

## Ajuste — Alinhamento do menu e retorno à gaveta do tray — 2026-10-10 20:01 (America/Sao_Paulo)

O usuário apontou que a gaveta mudava de posição ao retornar pelo botão inferior
do menu; queria as setas na mesma posição horizontal. A referência anterior
era a posição do clique no item (com conversão de coordenadas da superfície).
Alterado TrayMenu::toggleForItem: ao abrir pela gaveta, a referência é o centro
real do retângulo da gaveta em coordenadas do monitor, independente do item
clicado. Menu, seus submenus/redimensionamentos e retorno usam essa referência.

No layout da setinha, a coordenada horizontal é projetada a partir desse eixo
fixo para o conteúdo do painel, descontando a posição real e o padding nativo.
Isso preserva o alinhamento também quando um menu mais largo precisa ser
limitado pela borda do monitor: a seta acompanha o eixo da gaveta, não o centro
do menu deslocado. O botão permanece dentro do corpo do painel. Não foram
alterados ações, aparência, duração, monitor ou fonte das opções.

Compilação final Ninja/script de reprodução, git diff --check, bash -n e
config validate passaram. Conferidos 45 cenários geométricos de gavetas/menus
com larguras distintas e posições centrais/próximas das bordas: centro do
retorno e seta mantêm o eixo, tolerância de meio pixel pelo arredondamento.
Esses cálculos não substituem um teste gráfico automatizado. O usuário confirmou
“Passou” depois da ativação: alinhamento validado visualmente na sessão real.
Binário ativo corresponde ao build, SHA256 ad70b2ffdb54dcedef8a23bb9b27cf5a0b9230cc29fed26bfbcf577e2a0ee0c0. Shell/adaptador ativos,
KillMode=control-group e ricyblur carregado. Não foram ampliados testes de ações,
listas extensas, barras laterais ou outras máquinas.

Backup privado anterior à troca:
$HOME/.local/state/ricy-notificacoes-backups/20261010-200022-501476.
Pode ser restaurado pelo ativador existente; retorna à composição com setinha
antes da correção de alinhamento, preservando aplicativos. Atualizado o patch
composto de tray-menu-composition, README, tokens/identidade e reinstalação.
Kit ativo e portátil sincronizados, 443 hashes conferidos em cada manifesto;
entradas anteriores preservadas. Nenhuma captura, binário ou estado privado
foi incluído; compactados históricos permanecem inalterados.

## Contribuição — Ícones menores e hover para apps e busca — 2026-10-10 20:07 (America/Sao_Paulo)

Pedido do usuário: reduzir um pouco os ícones das aplicações e animá-los no
hover, incluindo search, sem atingir tray/opções, volume, hora, network ou
botão do Noctalia. Implementado somente em TaskbarWidget e LauncherWidget:
o desenho fica em escala 0,88 no repouso e cresce até 1,0 no hover, retornando
a 0,88 ao sair. Entrada/saída 140 ms, EaseOutCubic, com AnimationManager nativo
e respeito às preferências de movimento/velocidade. A inversão do hover cancela
a animação anterior e continua do progresso atual.

Transformados apenas nós Image/Glyph do ícone, sem mudar medida de layout ou
área de clique. Mantidos espaçamento, títulos, indicadores, badges e interação
original (ativar, alternar, fechar, menu e drag). Inclui imagens, fallback de
apps e glyph/imagem da lupa. O destaque de fundo já existente dos tiles de apps
acompanha a transição de 140 ms; outros elementos da taskbar mantêm seu hover
anterior. Volume, relógio, network, tray, menus do tray e control-center não
receberam alteração. Não foram modificadas cores, fontes ou preferências
privadas. Aplicação no código garante reprodução da variante, sem depender
de um ajuste manual do perfil ativo.

Nova contribuição contributions/app-icon-interactions: README, compilar.sh,
patch completo noctalia-ricy.patch e licença MIT. O patch do Noctalia 5.2.1
6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 mantém correções anteriores de
notificações, wallpaper do Home, menu da taskbar e menu/retorno/alinhamento do
tray. Este compilador é a referência atual; os anteriores permanecem históricos
e recusam cache com diff diferente. Preserve a fonte anterior e use cache
limpo ao migrar, conforme README. Atualizados reinstalação, guia visual e tokens,
com exclusões explícitas do efeito. Nenhum binário foi colocado no kit.

Verificações: compilação final Ninja/script de reprodução, git diff --check,
bash -n e config validate passaram. Comparados os blocos do patch completo
com a variante anterior: mudanças adicionais restritas aos dois widgets;
todos os demais blocos anteriores permanecem iguais. Binário ativo e build
coincidem, SHA256 b30d5efc4461d0eea3e82c2001d05bbc32fe79fc3e5770eee152ce1af4b694fb. Shell/adaptador ativos, KillMode=control-group
restabelecido e ricyblur carregado. Não registrada confirmação visual do usuário
neste ajuste, nem testes de clique/arraste, hover rápido, movimento desabilitado,
escalas variadas ou outra máquina. A verificação de escopo/compilação não
substitui esses testes visuais e de interação.

Backup privado antes da troca:
$HOME/.local/state/ricy-notificacoes-backups/20261010-200612-039983.
Restaurável pelo ativador anterior, retorna à variante com alinhamento do tray
sem redução/zoom dos ícones, preservando aplicativos. Kit ativo e portátil
sincronizados: 447 hashes conferidos em cada manifesto, entradas anteriores
preservadas. Sem clipboard, capturas, contas, estado privado ou backups no kit;
compactados históricos permanecem inalterados.

## Contribuição — Ações dos ícones: restaurar, minimizar e fechar — 2026-10-10 20:18 (America/Sao_Paulo)

O usuário esclareceu que “abrir minimizadas” significa restaurar a janela pelo
ícone e confirmou a implementação anterior com “Passou”. Essa variante
restaurava explicitamente no KDE/KWin, preservava o middle-click existente
para solicitar fechamento e selecionava a identidade exata por UUID para
não ativar/fechar outra janela de mesmo título. A confirmação é desse estado
anterior, cujo binário era SHA256
1b32307c4bfd041a0eb62f329ff4cab57a70f511798380d8d94ec5e5e9ecaa79.

Novo pedido: comportamento do Windows, restaurando minimizadas e minimizando
abertas pelo ícone. Implementado clique esquerdo: janela minimizada restaura
e recebe foco; janela visível em foco minimiza, se minimizável; janela visível
inativa vem para frente. Aplicativo fixado sem janela continua iniciando.
Nos grupos, a janela ativa é priorizada para minimizar; sem ativa no grupo,
a seleção/ciclo existente escolhe a janela para restaurar/focar. Não reproduz
prévias ou seletor de grupos do Windows. Middle-click solicita fechar uma
janela ativa/representante, preservando diálogos de salvar; sem janela ignora.
Clique direito e drag mantêm menus/ordenação anteriores.

Somente o clique esquerdo da taskbar envia toggleMinimize; o script lê o estado
atual no KWin, sem confiar em flags antigas do tile. Ativação por busca, dock,
atalhos e outros chamadores restaura/foca, sem minimizar. Implementação da
alternância específica KDE/KWin; outros compositores mantêm ativação original.
UUID exato com fallback class/caption apenas sem UUID; UUID obsoleto não
aciona outra janela. Close chama closeWindow e não usa minimizar como fallback.

Nova contribuição contributions/taskbar-app-actions com README, compilar.sh,
patch completo noctalia-ricy.patch, LICENSE e validar-acoes.py. Referência
atual para compilar Noctalia 5.2.1, commit
6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4. Corrigidos TaskbarWidget,
CompositorPlatform e KwinActiveWindow, com seus headers; comparados os blocos
com app-icon-interactions, todos os outros blocos anteriores são iguais.
Preservados ícones/hover, notificações/wallpaper, menus, junções e tray.
Atualizados reinstalação, guia e tokens de interação, aviso na variante anterior.

Verificações: 17 testes executam JS real extraído da fonte em QJSEngine,
incluindo identidade/títulos iguais, UUID obsoleto, restauração, alternância,
janela inativa/não minimizável, ativação comum e fechamento. Na sessão real,
janela Qt descartável foi minimizada e scripts corrigidos restauraram/focaram,
minimizaram, restauraram novamente e preservaram visibilidade na ativação
comum; depois solicitaram fechamento por UUID. Estados de minimização/foco
conferidos diretamente no KWin, pois estado Qt do cliente não acompanha de
forma confiável minimização externa. A sequência síncrona verifica o adaptador,
sem simular cliques físicos ou cobrir todos os aplicativos/grupos. Tentativas
iniciais com consultas Qt/timers tiveram medições inconsistentes; a verificação
final por estado do KWin passou. Nenhuma janela com trabalho foi fechada;
scripts e objeto DBus temporários removidos. A alternância nova ainda não
recebeu confirmação do usuário. Compilação/script de reprodução, bash -n,
git diff --check, aplicação reversa do patch e config validate passaram.

Binário ativo/build coincidem, SHA256 fcfc99017bc29cdf3c93742dfc5463ea62c01e07662666baebbeb610da7a08a6.
Shell/adaptador ativos, KillMode=control-group restabelecido, ricyblur carregado.
Backup privado antes desta troca:
$HOME/.local/state/ricy-notificacoes-backups/20261010-201748-372725;
retorna à variante restaurar/fechar aprovada, preservando aplicativos.
Backup privado da implantação anterior:
$HOME/.local/state/ricy-notificacoes-backups/20261010-201242-075546;
retorna à variante de ícones/hover sem as correções de ações.

Kit ativo e portátil sincronizados: 452 hashes conferidos em cada manifesto,
447 entradas anteriores preservadas e cinco novas adicionadas. Sem binários,
clipboard, capturas, contas, estado privado, bytecode Python ou backups no kit.
Compactados históricos permanecem inalterados.

## Contribuição — Bolinha roxa por estado e animações das ações — 2026-10-10 20:28 (America/Sao_Paulo)

Usuário confirmou “Está funcionando” para a variante restaurar/minimizar pelo
ícone e fechar com middle-click. Pediu que a bolinha roxa reagisse e acrescentar
animações. Implementados quatro estados no indicador: ativa opacidade/escala
1/1; aberta inativa 0,55/0,82; minimizada 0,28/0,65; fixada sem janela 0/0,55.
Transição 160 ms EaseOutCubic, AnimationManager nativo, respeitando preferências
da shell. Parte do valor visual atual e preserva snapshots por identidade
entre reconstruções; isso permite apagar o indicador de um fixado fechado.
Ícone não fixado desaparece ao fechar a última janela. Mesma regra na linha
quando títulos estão visíveis. Layout, área de clique e hover preservados;
resumo de pontos de workspaces mantém sua composição. Sem mudanças no tray,
volume, relógio, network ou control-center.

Adaptador KDE conecta minimizedChanged, serializa sexto campo de minimização
por UUID e inclui mudanças de estado no callback. Estado chega ao modelo;
janela minimizada não pode permanecer ativa por foco retido da shell. Seleção
ativa prioriza UUID, sem acender duplicatas de título. Fixados agrupados só
ficam minimizados se todas as janelas estiverem; representante de grupo de
workspace prioriza ativa/visível. WaylandToplevels preserva minimized em wlr.

Efeito local ricywindowactions deriva do Squash KDE GPL-2.0-or-later. Minimiza
com compressão, deslocamento e fade; restaura em sentido inverso; base 240 ms,
InCubic/OutCubic, com reversão rápida e cleanup do blur. O Squash nativo não
animava quando Noctalia não publicava iconGeometry. Novo fallback usa destino
18×18 no mesmo monitor, eixo horizontal do centro da janela e 22 px acima da
borda inferior (taskbar 44 px). É destino aproximado, não o ícone exato; se
iconGeometry existir, ela é preferida. Apenas janelas normais da taskbar,
respeitando efeitos de tela cheia. Se a barra mudar de posição/altura, revisar
fallback. Nenhum protocolo Plasma de geometria de ícone foi acrescentado.

Scale nativo para abrir/fechar: base 180 ms, escala 0,92 e fade; diálogos também
podem receber o Scale conforme implementação KDE. Squash, Magic Lamp e Fade
desativados para evitar sobreposição; Smooth Window Geometry e ricyblur mantidos.
Velocidade KDE AnimationDurationFactor=0,25 preservada: tempos reais de referência
aproximadamente 60/45 ms para minimizar/fechar. As preferências de movimento
Noctalia e KWin são independentes; AnimationManager e animationTime respeitam
as respectivas preferências. Sem reiniciar compositor nem terminar aplicativos.

Nova referência de compilação contributions/app-indicator-animations inclui
patch completo Noctalia 5.2.1 no commit
6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4 e efeito testado em KWin 6.7.5.
Dez archives públicos: README, compilador, patch, licença MIT, dois validadores,
aplicador, licença GPL e dois assets do efeito. Comparação dos blocos confirma
mudanças adicionais somente em TaskbarWidget, KwinActiveWindow e WaylandToplevels
com respectivos headers. Outros blocos, menus, notificações, wallpaper e
correções das ações anteriores preservados. Atualizados reinstalação, guia
visual e tokens; aviso na contribuição anterior aponta para esta variante.

Verificações: 17 testes JS das ações e 15 de sinais/serialização/animações
passaram; compilação final/reprodução, bash -n, config validate, git diff
--check e aplicação reversa do patch passaram. Compilação ampla apresentou
avisos -Wmaybe-uninitialized preexistentes em config_service.cpp, sem mudanças
nesse arquivo. Janela Qt descartável real confirmou restaurar/minimizar/restaurar,
ativação comum sem minimizar e fechamento; ricywindowactions e Scale apareceram
ativos durante as transições. A velocidade 0,25 fez uma consulta inicial após
65 ms perder as animações; observação dentro de 60 ms passou. Capturas privadas
confirmaram o indicador ativo→minimizado. Não houve simulação física do clique,
validação de todos os grupos/apps, escalas ou reversões rápidas reais; este
ajuste ainda não recebeu confirmação visual do usuário. Scripts e DBus de teste
removidos. Nenhuma janela com trabalho foi fechada.

Shell/adaptador ativos, KillMode=control-group restabelecido; ricyblur,
ricywindowactions e Scale carregados. Binário ativo/build coincidem,
SHA256 ac14659d1461da4cb5c86b2b38dfb1757c2526b875f5a729d939cd670bfb28a2.
Backup da shell: $HOME/.local/state/ricy-notificacoes-backups/20261010-202443-366945,
retorna ao comportamento das ações aprovado antes deste indicador.
Backup do efeito/chaves: $HOME/.local/state/ricy-indicador-animacoes-backups/20261010-202354-251513.
Reversão completa requer restaurar ambos conforme README. Backup das chaves
limitado às modificadas, sem distribuir estado privado no kit.

Kit ativo/portátil sincronizados: 462 hashes conferidos por manifesto,
452 entradas anteriores preservadas e dez novas adicionadas. Créditos e
licenças do KDE preservados. Nenhum binário, screenshot, clipboard, conta,
bytecode, estado privado ou backup no kit. Compactados históricos inalterados.

## Contribuição — Animações dos ícones, correção do fundo e reorganização — 2026-10-10 20:46 (America/Sao_Paulo)

Usuário pediu pulso/bounce por estado e relatou fundo preto na primeira
implementação. Slot Box foi substituído por Node sem pintura, mantendo área
de clique e hover independente. Capturas privadas antes/depois confirmaram
remoção. Ícones recebem ações finitas: abrir 420 ms (bounce/pulso), restaurar
360 ms (bounce), foco 260 ms (pulso), minimizar 220 ms (compressão para barra),
segundo plano 200 ms (redução/esmaecimento), fixado fechado 240 ms (contração).
Não fixado removido dissolve em 220 ms, escala 1→0,72, sem hit-test/layout,
com verificação de saída da janela e guardas de vida útil. Movimento/velocidade
nativos respeitados, sem loops em repouso, sem animação inicial de todos os
apps, retomando progresso em reconstruções e interrupções. Capturas verificam
bounce/compressão; não há captura conclusiva do fantasma ao fechar. Janela Qt
real descartável confirmou estados/efeitos; nenhum trabalho do usuário fechado.

Pedido seguinte: clicar/arrastar para reorganizar aplicativos. Estendido
mecanismo upstream restrito a fixados para todos os tiles da faixa plana,
sem alterar fixação. Ícone acompanha cursor, spacer transparente marca alvo,
vizinhos cedem espaço. Limiar nativo evita confundir clique com arraste; segurar
sem mover preserva clique. Release de gesto consumido suprime ação da janela.
Middle-click/contexto preservados. Busca/tray/controles ficam fora da faixa;
agrupamento por workspace mantém layout original. Eixo horizontal/vertical
conforme orientação, pitch real considera título/escala/espaçamento.

ConfigService grava widget.taskbar.app_order em settings.toml privado, após
despachar o evento. Chaves app+ocorrência não contêm títulos/UUIDs. Instâncias
retêm chave durante atualizações, novas podem reutilizar slot livre; entre
reinícios não há identidade de documento específico em janelas do mesmo app.
Lista preserva apps fechados/filtrados e acrescenta novos sem preferência ao
final. Widget compartilhado aplica ordem em seus monitores. Guardas de geração
invalidam commit em modelo alterado; cancelamento restaura fluxo; soltura
aguarda recarga na posição final. Preferência privada não copiada para kit.

Usuário confirmou “Passou” após ativação da reordenação. Ordem real com dois
slots distintos encontrada e config validate passou após o arraste. Captura
privada mostra a ordem alterada e ausência do fundo preto. Não houve simulação
física automatizada; validação visual veio do usuário. Barras verticais,
outras escalas e alterações de modelo durante arraste real não foram
validadas visualmente. Testes: 22 de ordem (incluindo 24 permutações), 11
contra objetos nativos TaskbarWidget/ConfigService em perfil temporário,
20 de motion, 17 JS das ações e 15 do indicador/efeito passaram. Teste nativo
confirmou apps não fixados, movimento, cancelamento, geração inválida,
supressão de clique, escrita sem pin e schema/definição decodificando ordem
em nova instância; não se conectou ao compositor. Patch sobre fonte limpa,
17 archives idênticos, compilação/reprodução, bash -n e git diff --check
passaram. Nova etapa muda só TaskbarWidget, definição e taskbar_order.h;
patch inclui integralmente os ajustes anteriores, incluindo header de motion.

Contribuições públicas: app-icon-states (12 archives) registra a etapa
anterior; app-icon-reordering (16 archives) é a referência cumulativa atual.
Reinstalação, identidade e tokens atualizados. Binário ativo/build coincidem,
SHA256 da29814a36e2091d3889c1abce94ea046bb89aa27c4df66efb36d3cc18e87d4f. Shell/adaptador ativos, KillMode=control-group restabelecido;
ricyblur, ricywindowactions e Scale carregados. Sem alteração dos efeitos
KWin nesta etapa. Backup para desfazer apenas arraste:
$HOME/.local/state/ricy-notificacoes-backups/20261010-204423-864447,
retorna às animações com fundo corrigido. Para antes das animações dos ícones,
use 20261010-203450-476691; 203558-299413 é intermediário com Box preto.

Kit ativo e portátil sincronizados, 490 hashes por manifesto: 462 entradas
anteriores preservadas, 12 da etapa de estados e 16 da reordenação adicionadas.
Sem binários, capturas, clipboard, contas, preferências locais, bytecode ou
backups públicos. Compactados históricos preservados. Licenças MIT e GPL e
créditos upstream mantidos.

## Contribuição — Fade e expansão das janelas — 2026-10-10 21:00 (America/Sao_Paulo)

Usuário forneceu referência Slick Window Arrangement:
https://windhawk.net/mods/slick-window-arrangement
Perguntado o escopo, confirmou “Abrir/restaurar e fechar/minimizar”.
Consultadas fontes primárias Windhawk e KDE Scale/Squash. O mod fornecido
implementa sliding/snapping de movimentação; nenhum código Windows foi
copiado. Aplicado o fade + expansão solicitado usando API nativa KWin.

Abrir/restaurar: escala 0,85→1 e opacidade 0→1, OutCubic. Fechar/minimizar:
1→0,85 e opacidade 1→0, InCubic. Centro da própria janela, sem translação para
ícone ou monitor, sem modificar geometria real. Duração base 320 ms; global
KDE AnimationDurationFactor=0,25 preservado, referência aproximada 80 ms.
Ricywindowactions passa de compressão/deslocamento para Scale+Opacity;
Scale nativo abre/fecha com mesmos valores e preserva seus filtros/diálogos.

Reversões usam redirect e, se necessário, cancelamento antes do novo sentido.
IDs de trilhas acompanhados para liberar blur somente quando ambas acabam;
IDs antigos/estranhos ignorados. Fechar durante ação cancela transição local;
blur do Scale de fechamento já ativo não é limpo prematuramente. Filtros
mantidos para janelas normais da taskbar/efeitos de tela cheia. Fade, Squash
e Magic Lamp desativados para evitar duplicação. Smooth Window Geometry,
ricyblur, binário Noctalia, arraste/ordem/hover/pulso/bounce/indicador e painéis
preservados. Não houve mudança em maximização ou movimentação de janelas.

Nova contribuição window-fade-expand, sete archives: README, aplicador,
validador, licença GPL e três assets (metadata, JS, schema XML). Aplicador
salva pacote e dez chaves alteradas, preserva demais chaves de kwinrc,
reconfigura/recarrega efeitos sem reiniciar KWin/Noctalia nem fechar apps;
restaura automaticamente o backup se ativação falhar. Backup desta sessão:
$HOME/.local/state/ricy-fade-expand-backups/20261010-205749-431612.
Reversão em README; estado/backup local não distribuído. Instalador anterior
app-icon-reordering permanece histórico para efeitos; reinstalação atual
combina seu compilador Noctalia com aplicar-animacoes.py da nova contribuição.

28 cenários JS/config/pacote passaram. Janela Qt descartável real confirmou
abrir, restaurar/minimizar/restaurar, minimizar/restaurar em sequência rápida,
ativação comum sem minimizar e fechar; Scale ativo na entrada/saída e efeito
local nas ações. Pacote/chaves conferidos; ricywindowactions, Scale e ricyblur
carregados, shell/adaptador ativos. Consulta ao journal não trouxe erros de
script. Testes/objeto DBus removidos, nenhuma janela com trabalho fechada.
Não há medição quadro a quadro de escala/opacidade nem validação de todos
os apps/diálogos/monitores/escalas; ainda sem confirmação visual do usuário.

Reinstalação, identidade, tokens e avisos da contribuição anterior atualizados.
Kit ativo/portátil sincronizados: 497 hashes por manifesto, 490 anteriores
preservados e sete novos adicionados. Créditos/licença GPL preservados.
Sem binários, screenshots, clipboard, contas, preferências privadas, bytecode
ou backups públicos; compactados históricos preservados.


## Contribuição — Dolphin com identidade Noctalia — 2026-10-10 21:07 (America/Sao_Paulo)

Pedido: aproximar a aparência do Dolphin da referência Noctalia. Criada
variante exclusiva Kvantum Ricy-Dolphin, derivada de KDE-Noctalia/Catppuccin
MIT: superfície #181825, texto #cdd6f4/#a6adc8, contorno #46485c e acento Mauve.
Folha Qt com Noto Sans 10 pt, toolbuttons/campos/abas com raio 8 px, hover em
#313244 e seleção #977dba. Fontes de archives nos três modos configuradas em
dolphinrc (UseSystemFont=false/ViewFont=Noto Sans). Ícones e comportamento de
archives preservados. Fonte global KDE, Noctalia, MIME e decoração intactos.

Tema atribuído somente ao executável dolphin via Kvantum/Applications. Wrapper
$HOME/.local/bin/ricy-dolphin injeta -stylesheet. Entrada local de aplicativo,
serviço D-Bus FileManager1 e drop-in de plasma-dolphin.service usam o wrapper.
Nenhum arquivo de sistema substituído; daemon não reiniciado. QSS aplicado por
D-Bus aos processos existentes sem fechar janelas. Janelas antigas podem exigir
reabertura para carregar a variante e fontes de arquivos. Execução direta de
/usr/bin/dolphin não injeta a folha; o launcher normal e wrapper a carregam.

Inspecionadas capturas antes/depois de janela nova, com fonte proporcional e
controles arredondados. Sintaxe Python, XML SVG, atribuição, fontes, caminho
QSS ativo, desktop-file-validate e systemd-analyze --user verify conferidos.
Dolphin 26.08.2-1.1, Kvantum 1.1.8-1.1. Somente janelas de conferência do agente
foram fechadas; janela Home existente preservada. Uma asserção inicial esperava
QSS literal no D-Bus, mas Qt retorna file:////CAMINHO quando carrega -stylesheet;
conferidos o caminho e a igualdade do arquivo instalado. Não comprovados todos
os diálogos/ações, novas sessões, todos os monitores ou migração. Ainda sem
confirmação visual do usuário. Superfícies opacas para leitura; não estendido
blur compartilhado da shell. Decoração conserva fonte KDE.

Material portátil: contributions/dolphin-noctalia-identity/aplicar.py,
dolphin.qss, README.md e licença MIT. Aplicador gera backup privado e oferece
--restaurar BACKUP. Neste trabalho foram duas aplicações: desfazer em ordem
inversa 20261010-210632-242640 e 20261010-210604-287127, sob
$HOME/.local/state/ricy-dolphin-backups. Restaurador repõe archives inteiros e
ausências; reabra Dolphin. Alterações posteriores nesses archives podem ser
substituídas. Kits ativo/portátil sincronizados e hashes novos conferidos,
preservando entradas anteriores. Backups/capturas/estado não publicados.
Compactados históricos preservados.


## Contribuição — Dolphin: blur, cantos e chips — 2026-10-10 21:33 (America/Sao_Paulo)

Chat de harmonização Dolphin/Noctalia. O usuário rejeitou a primeira versão
opaca/quadrada; esta contribuição substitui esse estado final, preservando
seu registro histórico. Fundo agora #181825 alfa 178/255 (~0,70), cartão
translúcido de archives #313244 alfa 40/255, raio 12, contorno #46485c. Um
plugin Qt genérico privado, ativado por -plugin ricydolphinui no launcher,
marca DolphinMainWindow WA_TranslucentBackground antes da criação da superfície.
Kvantum Ricy-Dolphin ativa translucent_windows/blurring, reduce_window_opacity=30
para a superfície, Base/AlternateBase transparentes e transparent_dolphin_view.
Textos/ícones ficam nítidos; ricyblur fornece blur nativo aos apps externos,
sem extensão do fundo compartilhado Noctalia. Nenhum reinício do compositor.

Efeito próprio ricydolphinrounding, instalado com Polkit em
/usr/lib/qt6/plugins/kwin/effects/plugins/ricydolphinrounding.so, atribui raio
nativo Window::setBorderRadius(16) só a normais/diálogos dolphin/org.kde.dolphin.
Maximização parcial/completa, fullscreen e tiling usam zero. Guarda/restaura
raios originais e acompanha mudanças por sinais. Não adiciona shader nem
passes próprios; usa recorte e blur nativos KWin 6.7.5. Breeze mantém título
sólido e fonte KDE. Protótipos ricydolphincorners/ricydolphinshape descarregados,
chaves apagadas e bibliotecas removidas. Somente efeito final instalado.

A pedido posterior, hover lateral virou chip pelo conteúdo e todas as linhas
de detalhes receberam fundos arredondados. Usuário aprovou, depois pediu
incluir ícones e ajustar header. Estado final: lateral envolve ícone + nome;
linhas #313244 alfa 90, raio até 10, insets 3/2; hover/seleção #977dba com
alfa 95/170/195 e foco sólido #cba6f7 cobrindo ícone e linha. Header único
#313244 alfa 155, contorno #46485c alfa 150, Noto Sans 10 pt e seta nativa.
QProxyStyle sobre Kvantum troca primitivas; wrapper preserva delegate KIO para
seções, dispositivos, capacidade e tooltips. QGraphicsEffect desenha fundos
antes de drawSource nativo. Sem interceptar mouse/teclado ou mudar arquivos.
Chips de linha usadas em itens >140 px de largura e <=64 px de altura;
miniaturas grandes mantêm seu conteúdo. QSS sozinho não corrige fillRect da
zebra; paleta transparente e backing por item resolvem esse desenho próprio.

Compilação Qt e instalação do helper verificadas; capturas novas mostraram
chips, seleção com ícone, foco sólido arredondado e header com seta. Captura
do desktop mostrou blur composto. Captura RGBA anterior mediu alfa 178 no
fundo (antes 255). Status nativo confirmou raio16; cliente Qt descartável
confirmou normal16, maximizado0 e restaurado16. Sem crashes observados nos
logs de teste. ricyblur/ricydolphinrounding carregados e Noctalia/adaptador
ativos. Usuário aprovou chips antes da inclusão de ícones/header; esta revisão
final ainda sem confirmação visual dele. Não testados todos os diálogos,
transferências, drag/drop, reordenação/resize de colunas, monitores/escalas,
folders gigantes ou desempenho; reinstalação em outro PC não foi testada.

Fontes/compiladores/README/licença MIT próprios na nova contribuição
contributions/dolphin-blur-cantos. Atualizados aplicar.py, QSS e README de
dolphin-noctalia-identity; adicionado lancar.py. Qt6 Widgets/headers, g++ e
pkg-config bastam para helper. Efeito exige headers/dependências KWin 6.7.5;
compilar.py recusa outra versão. Reusados headers Vulkan oficiais do cache
Ricy. Nenhum .so, screenshot, cache, backup ou dado privado incluído no kit.
Fontes externas de cantos consultadas, sem reutilizar código. Créditos do
tema Catppuccin/MIT preservados. Serviços/desktop mantêm wrapper; daemon não
reiniciado nem janelas fechadas automaticamente pelo aplicador. Instâncias
antigas precisam reabrir para plugin/tema, QSS aplicado ao vivo por D-Bus;
script trata corrida quando usuário fecha uma instância durante aplicação.

Reproduzir/restaurar pelos READMEs e passo 8a atualizado de REINSTALAR.md.
Backup de cantos: ~/.local/state/ricy-dolphin-corners-backups/20261010-211849-253315.
Backup antes das chips: ~/.local/state/ricy-dolphin-backups/20261010-212842-374549;
reversão em ordem inversa 213035-906999, 212959-440141, 212842-374549 (prefixo
20261010-) retorna à revisão de blur anterior. Para estado anterior ao blur,
continue 211713-181764, 211458-875287 e 211018-558522. Restaurador de cantos
preserva chaves/raios sem substituir kwinrc inteiro; não remove biblioteca.
Backups são privados, use os novos nomes emitidos no destino.

Registro acrescentado sob flock compartilhado. Identidade e tokens atualizados,
kits ativo e portátil sincronizados; manifestos preservam entradas existentes,
recalculam só materiais editados e incluem archives novos. Compactados antigos
preservados. Esta seção supersede a afirmação anterior de superfícies opacas.


## Contribuição — Alternância Plasma/Noctalia sem restaurar configurações antigas — 2026-10-10 22:49 (America/Sao_Paulo)

Trabalho: alternância concisa entre as duas shells, preservando o Ricy. O usuário
relatou ausência de retorno simples ao Noctalia e mudança inesperada do wallpaper
ao usar o retorno ao Plasma. Este estado substitui o fluxo de troca das
contribuições noctalia-autostart e integração/KDE anteriores; os registros
históricos e o backup original foram preservados.

### Causa conferida e resultado aplicado

O retorno antigo sobrescrevia plasma-org.kde.plasma.desktop-appletsrc e
plasmashellrc inteiros a partir de plasma-antes.tar.gz. O layout restaurado tinha
um grupo de wallpaper antigo north; os desktops vivos 43/44 ficaram sem Image
configurada. A entrada antiga também executava restaurar-wallpaper.js, com IDs e
imagem fixos capturados antes. Os wrappers $HOME/ricy/iniciar.sh e voltar.sh
citados no histórico não existiam mais no destino. No início deste trabalho,
Plasma estava ativo, Noctalia/adaptador/integrador inativos e preferência no
login desabilitada; havia um painel vivo (23, monitor 0).

Instalada contributions/plasma-noctalia-switching com sete archives públicos.
Comandos em $HOME/.local/bin: ricy noctalia, ricy plasma, ricy alternar (também
a ação de ricy sem argumento), ricy status, voltar-ao-noctalia, voltar-ao-plasma.
Entradas persistentes no menu: Voltar ao Noctalia, Voltar ao Plasma, Alternar
Plasma e Noctalia. Recriados $HOME/ricy/iniciar.sh, voltar.sh e alternar.sh.
As duas ações explícitas mudam também a preferência de login.

O instalador substituiu iniciar-teste.sh e voltar-ao-plasma.sh em três locais
do kit ativo (outputs histórico, integração/KDE e modelos inicio-automatico) por
wrappers que encaminham à nova implementação. No kit público esses scripts
históricos continuam originais; o novo instalador os substitui no destino.
Unidades, drop-ins e nomes de perfil continuaram existentes.

Antes de recolher painéis, plasmashell é parado/iniciado brevemente para
sincronizar KConfig e capturar todos os grupos dos painéis e sua geometria.
O retorno repõe somente esses grupos; conserva desktops, wallpaper, widgets
e grupos gerais atuais. Inclui tray externo e remapeia IDs quando entram em
conflito com desktops/widgets posteriores; nesta máquina o applet aninhado
43 foi remapeado para 47 no primeiro retorno. Retorno com painéis já existentes
é inócuo. Snapshot sem painéis não substitui um snapshot válido.

Super, Super+Espaço e Super+V são capturados a cada ciclo, transferidos para
Noctalia e restaurados para suas ações anteriores. Shell/adaptador devem estar
prontos antes da remoção dos painéis. Erro nessa etapa tenta recuperar Plasma;
o comando também desabilita a preferência Noctalia se a unidade falhar.
Os locks de comando e integração serializam chamadas; o login segue usando
ricy-noctalia-integracao.service. Cada comando dispara um worker em uma unidade
transitória separada, para sobreviver ao encerramento da shell chamadora.
Assim o retorno também pode concluir quando iniciado pelo menu do Noctalia.

Recuperado uma única vez o Limine previamente escolhido,
/usr/local/share/ricy/limine-splash.png, FillMode 2, nos desktops vivos pelos
IDs obtidos localmente. O estado privado do Noctalia e o registro anterior
confirmavam essa imagem. As trocas seguintes não impõem wallpaper algum.
Desktop e aparência geral são compartilhados; Noctalia segue integrado ao
KDE/KWin. Não é troca de compositor/sessão nem restauração dos temas antigos.

### Reproduzir e desfazer

Após preparar integração/KDE e instalar noctalia-autostart:

```bash
python "$HOME/ricy-kit/contributions/plasma-noctalia-switching/instalar.py"
"$HOME/.local/bin/ricy" noctalia
# Para voltar ou alternar:
"$HOME/.local/bin/ricy" plasma
"$HOME/.local/bin/ricy" alternar
```

Requer Python/PyGObject, qdbus6, flock, systemctl e kbuildsycoca6 na sessão
Plasma Wayland já preparada. Não usa sudo nem reinstala pacotes. Perfil
continua em contributions/noctalia-kde-integration-and-menus/work/noctalia-profile;
o serviço mantém o executável personalizado $HOME/.local/lib/ricy-noctalia/noctalia.
Sem alteração de binário, patches, cores, Dolphin, efeitos, login ou bloqueio.
REINSTALAR.md atualizado com o instalador e os comandos nos dois sentidos.
Reaplique o instalador se reinstalar posteriormente os scripts antigos.

Backup privado emitido nesta máquina:
$HOME/.local/state/ricy-alternancia/backups/20261010-224512-267960.
Guarda wrappers anteriores, ausências e os archives Plasma anteriores à
recuperação do wallpaper. Snapshots de painéis/atalhos e marcadores ficam
em $HOME/.local/state/ricy-alternancia. Não são materiais de migração.
O README contém restaurar-instalacao.py: execute primeiro ricy plasma, depois
passe o backup para restaurar wrappers/entradas e estado anteriores; o
restaurador preserva o desktop atual. Não desfaz o wallpaper nem aparência.
O backup completo original continua disponível, mas restaurá-lo integralmente
reintroduz a perda das preferências posteriores.

### Verificação e limites

Dois ciclos reais Plasma→Noctalia→Plasma concluídos, mais um terceiro retorno
iniciado por um chamador descartável vinculado à shell e entrada final no
Noctalia. O chamador foi encerrado com a shell; o worker separado continuou
e repôs painel/KRunner com sucesso. Isso simula a dependência de ciclo de vida
do comando aberto pela shell; não houve clique visual no menu neste teste. Testados ricy alternar, aliases, status e chamadas repetidas em ambos
os ambientes. O segundo retorno teve grupos completos de painéis/geometria
idênticos ao último snapshot; um painel Plasma foi conservado. Wallpaper
Limine presente nos dois monitores em ambos os sentidos. Shell/adaptador e
integração ativos ao final, zero painéis Plasma, preferência Noctalia habilitada;
KRunner ativo quando Plasma selecionado. Atalhos originais conferidos no D-Bus
no retorno. Oito hashes de binário, TOML, drop-ins, kdeglobals, kwinrc, dolphinrc
e seleção Kvantum permaneceram idênticos; PIDs dos apps acompanhados preservados.

verificar.py passou: preservação de wallpaper/desktops/widgets/views, IDs e
referências em conflito, tray externo, comentários, idempotência e recusa de
backup vazio. Sintaxe Python/Bash, desktop-file-validate e systemd-analyze
--user verify passaram. Um erro inicial na fixture usou expectativa de ID
inconsistente com seus próprios applets; corrigida a fixture, suíte final passou.
Não houve reinício completo/login novo, medição visual de todas as geometrias
ou injeção real de falha durante remoção/recuperação. Não testado em outro PC.

Materiais públicos copiados explicitamente, sem perfil/clipboard, backups,
binários, screenshots ou bytecode. Ambos os manifestos agora têm 518 entradas
conferidas; 511 existentes preservadas, sete materiais novos, hashes dos seis
wrappers atualizados apenas no kit ativo. Compactados históricos preservados.
Registro acrescentado sob o bloqueio compartilhado de documentação.


## Contribuição — Posição do hover do header Dolphin — 2026-10-11 (America/Sao_Paulo)

A pedido do usuário, corrigida a posição da chip de hover nas colunas do
cabeçalho: inicia 8 px antes do retângulo nativo da coluna, inset vertical
3 px e interseção com o header inteiro recuado 5/3 px. Evita encostar o texto
na borda e extrapolar a cápsula nas colunas largas/roladas. HeaderChip fornece
bounds temporários ao QProxyStyle durante drawSource, sem alterar eventos,
labels, seta ou geometria das colunas. ui.cpp recompilado/instalado pelo
aplicar.py; backup 20261011-083312-062208 em ~/.local/state/ricy-dolphin-backups.
Restaurar com aplicar.py --restaurar BACKUP, depois reabrir Dolphin.
Teste de desenho Qt offscreen passou: padding antes do label, inset superior/
inferior e recorte do overflow. Nova janela de Dolphin aberta para conferência;
instâncias antigas precisam reabrir para código novo. Não testados todos os
monitores, escalas, RTL ou scroll horizontal reais. README e ui.cpp sincronizados
no kit ativo/portátil; hashes atualizados preservando demais entradas.


## Contribuição — Hover Size/Modified Dolphin — 2026-10-11 (America/Sao_Paulo)

Hover inclui o retângulo nativo da seta de ordenação com margem 6 px.
Última coluna identificada pela pintura do padding End (section-1), ou posição
End da própria coluna; seu hover alcança a borda interna direita do header.
Name mantém os insets anteriores. Sem usar strings traduzidas das colunas.
Teste Qt offscreen passou para identificação da última coluna, preenchimento
até a margem direita, limites externos/verticais e inclusão da seta.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084408-791214.
Reverter com aplicar.py --restaurar BACKUP e reabrir Dolphin.

Helper recompilado/instalado; fontes/README sincronizados nos dois kits e
hashes conferidos. Instâncias existentes precisam reabrir para novo código.
Sem confirmação visual do usuário nesta revisão.


## Contribuição — Size somente texto no hover — 2026-10-11 (America/Sao_Paulo)

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


## Contribuição — Size: largura da coluna sem seta — 2026-10-11 (America/Sao_Paulo)

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


## Contribuição — Padding interno de Size — 2026-10-11 (America/Sao_Paulo)

Chip mantém a largura da coluna e o limite que exclui a seta anterior.
Agora o label de colunas intermediárias é recuado para garantir 8 px internos
no início/fim, sem deslocar a chip sobre a seta. Name e Modified preservados.
Helper recompilado/instalado. Teste de pintura Qt offscreen passou para
preenchimento da largura, reserva da seta e primeiro pixel do texto pelo
menos 8 px após a borda da chip. Nova janela pelo launcher aberta.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084751-069063; restaurar
com aplicar.py --restaurar BACKUP e reabrir. Sem aprovação visual final.


## Contribuição — Name: espaço à direita da seta — 2026-10-11 (America/Sao_Paulo)

Usuário aprovou padding de Size. Hover da primeira coluna Name agora estende
a borda direita em 6 px, mantendo recorte no header comum. Size e Modified
preservados. Helper recompilado/instalado. Teste offscreen verificou extensão
finita à direita e manteve checks de Size, padding e última coluna.
Backup ~/.local/state/ricy-dolphin-backups/20261011-084856-807309; restaurar
com aplicar.py --restaurar BACKUP e reabrir. Sem aprovação final de Name.


## Contribuição — Espaçamento uniforme do header Dolphin — 2026-10-11 (America/Sao_Paulo)

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


## Contribuição — Padding lateral da sidebar Dolphin — 2026-10-11 (America/Sao_Paulo)

KFilePlacesView recebe padding-left/right 8 px na folha Qt. Recuo do viewport
move juntos títulos, ícones, chips e barras de capacidade, sem deslocar só
o desenho do delegate. Aplicador criou backup privado
~/.local/state/ricy-dolphin-backups/20261011-085235-777886. Captura de janela
nova confirmou títulos/ícones/chip recuados; sidebar não encosta na esquerda.
QSS aplicado também a instâncias existentes, sem fechá-las. Fonte/helpers
e espaçamento do header preservados. Reverter: aplicar.py --restaurar BACKUP
e reabrir Dolphin. Não testados scrollbars/drag-drop em todas as larguras.


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
