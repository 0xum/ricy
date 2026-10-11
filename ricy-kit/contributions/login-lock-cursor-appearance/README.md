# Login, bloqueio, cursor e aparência — captura de 09/10/2026

Esta contribuição exporta a aparência efetiva deste computador para outra
instalação CachyOS/KDE Plasma Wayland. O guia consolidado está em
`REINSTALAR.md`, junto de `ricy.md`. Nenhum destes instaladores foi aplicado à
sessão de origem durante a exportação.

## Configurações incluídas

| Componente | Estado capturado |
|---|---|
| Tela de iniciar sessão | SDDM, tema local `mocha-limine`, baseado no Breeze Qt 6 |
| Fundo do login | `limine-splash.png`, imagem incluída no kit, preenchimento com recorte proporcional |
| Login: relógio/formulário | Relógio ligado, formulário imediato, ocultação após 60 s de inatividade, logo oculto |
| Login: cores | Grupos `Colors:*`/`ColorEffects:*` da conta SDDM: Catppuccin Mocha Mauve; seleção `#cba6f7` |
| Login: fonte/ícones/estilo | JetBrainsMono Nerd Font 10 pt; Breeze Dark; widgetStyle Breeze |
| Ponteiro do mouse (extra) | Bibata Modern Classic 2.0.6, tamanho 16, KDE/GTK/SDDM e XCURSOR |
| Bloqueio | Fundo Limine, relógio sempre visível, formulário imediato/60 s, mídia e revelar senha ocultos |
| Autenticação do bloqueio | Adaptação existente preserva `uiVisible: false` e usa `Qt.callLater` após a montagem |
| Fontes KDE | JetBrainsMono Nerd Font 10 pt: geral, mono, menus, barras, menores e títulos |
| Ícones KDE/GTK | `breeze-dark`, preferência efetiva herdada dos defaults KDE |
| Aplicativos Qt | Kvantum `KDE-Noctalia`, paleta `KDE-Noctalia` já distribuída no kit |
| Aparência Plasma | Tema local `mocha-blur`; pacote global `Catppuccin-Mocha-Mauve` e seu splash |
| Decoração de janelas | Breeze, BorderSize None, BorderSizeAuto false, NoPlugin false |
| Aplicativos GTK | `adw-gtk3-dark`, preferência escura, fonte/cursor/ícones acima, som `ocean`, DPI 96 |
| Fontconfig | Hinting ligado, hintslight e antialiasing; arquivo visual capturado |
| Blur KWin | Ativo, força 5, ruído 2 |
| Extensões opcionais | adaptivepanelwidth, smoothwindowgeometry e windowsarrows, fontes e atalhos selecionados incluídos |

`preferencias.json` contém somente chaves de aparência da conta do desktop.
`greeter-preferencias.json` contém os grupos visuais realmente lidos de
`/var/lib/sddm/.config/kdeglobals` por leitura privilegiada. A paleta do login é
diferente da paleta KDE-Noctalia dos aplicativos; ambas foram preservadas.
`preferencias-kwin.json` contém apenas os atalhos necessários às setas.

O cursor solicitado pelo usuário é o cursor de texto animado do Konsole.
Seu perfil/paleta e aplicador ficam na contribuição irmã
`konsole-animated-cursor/`, incluída no guia de reinstalação. Bibata é uma
preferência adicional do ponteiro do mouse, capturada nesta contribuição.

Assets incluídos: QML/metadata do login, Bibata completo, wallpaper Limine,
quatro faces JetBrainsMono Nerd Font (Regular/Bold/Italic/BoldItalic), temas
locais Plasma/splash e fontes das extensões KWin. Kvantum e esquema KDE são
reutilizados da contribuição `noctalia-kde-integration-and-menus` do mesmo kit.
GTK, ícones Breeze, componentes Qt/KDE e sons Ocean vêm dos pacotes do destino.

Não foram transportados avatar pessoal, senha, histórico de usuário do SDDM,
PAM, autologin com nome de usuário, IDs de monitores/desktops, aceleração
específica do mouse, backups da origem, caches ou histórico de clipboard.
As pastas de sessões personalizadas de SDDM desta máquina não são importadas:
selecione a sessão Plasma Wayland oferecida pela nova instalação.

## Instalar no destino

Use o roteiro consolidado de `REINSTALAR.md`. Para apenas esta contribuição,
instale primeiro as dependências do KDE/GTK em uma sessão Plasma Wayland:

```bash
sudo pacman -S --needed sddm plasma-workspace breeze breeze-icons kvantum qt6-5compat qt6-svg python fontconfig adw-gtk-theme ocean-sound-theme
cd "$HOME/Projects/ricy/ricy-kit/contributions/login-lock-cursor-appearance"
sudo python sistema.py
python usuario.py
python ../login-matched-lock-screen/aplicar.py
```

`sistema.py` instala o tema SDDM/cursor/fonte/wallpaper e mescla as preferências
visuais em `/etc/sddm.conf`, `/etc/sddm.conf.d/95-mocha-limine.conf` e na conta
SDDM. Resolve UID/GID de `sddm` no destino, sem importar IDs numéricos desta
máquina. O fundo passa a `/usr/local/share/ricy/limine-splash.png` e a fonte a
`/usr/local/share/fonts/ricy/`. Não reinicia o gerenciador de login.

`usuario.py`, executado sem sudo, guarda os archives afetados antes de
instalar os temas e mesclar as chaves KDE/GTK. Define cursor em kcminputrc,
GTK 2/3/4, environment.d e herança de cursor em icons/default. Mantém outras
chaves dos archives existentes. Não aplica os defaults completos do tema
global: os defaults antigos ainda citam Aurorae/outro cursor, mas o estado
efetivo capturado usa Breeze e Bibata. Se aplicar posteriormente um tema
global pelo KDE, execute novamente `usuario.py` para voltar a este estado.

O bloqueio é instalado pelo aplicador existente. Ele lê o tema de login
instalado, gera o QML a partir do KDE do destino e interrompe antes de escrever
se os trechos esperados mudarem. Reaplique depois de atualizar o Plasma. Não
copie a pasta de shell local gerada nesta máquina para outra versão do KDE.

Faça uma nova sessão para carregar cursor, fonte, splash, ícones e estilo.
Não use `systemctl restart sddm` de dentro de uma sessão que deseja preservar.

## Extensões de janelas (opcional)

Para levar também os efeitos e o comportamento das setas Super atuais:

```bash
sudo pacman -S --needed gcc pkgconf qt6-base qt6-declarative kwin kconfig
python usuario.py --extensoes-kwin
```

O script recompila windowsarrows em uma pasta temporária, usando headers e
bibliotecas do destino, antes de alterar as preferências. Não distribui o
`.so` antigo. Também instala adaptivepanelwidth/smoothwindowgeometry, aplica
seus flags e desabilita o efeito maximize concorrente. Define Super+setas
para o script e libera as mesmas combinações do quick tile nativo. Preserva
maximizar Super+PgUp, minimizar Super+PgDown e restaurar Super+Backspace.
Faça nova sessão para carregar o módulo e os atalhos. Mudanças da API/ABI
KWin podem exigir adaptação; o código-fonte está incluído.

## Wallpaper do desktop (opcional)

O Noctalia continua deixando o wallpaper a cargo do Plasma. Para escolher
Limine nos desktops da nova instalação, antes de preparar a integração:

```bash
bash aplicar-wallpaper.sh
```

O script enumera os desktops locais pela API Plasma. Ele muda a imagem nos
desktops presentes; o wallpaper anterior pode ser escolhido novamente pelas
Configurações do Sistema. Não cria um backup próprio do layout. Se preferir
preservar a imagem da nova instalação, não execute este passo. A integração
Noctalia deve ser preparada depois dessa escolha para registrar a imagem
correta em seu script local de preservação do wallpaper.

## Desfazer no destino

Use os caminhos de backup impressos pelos instaladores; cada execução gera
um backup novo. Se aplicou as extensões em uma execução posterior, desfaça
primeiro essa execução, depois a execução anterior da aparência:

```bash
python ../login-matched-lock-screen/restaurar.py "$HOME/.local/state/ricy-lockscreen-backups/DATA-HORA"
python usuario.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python sistema.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

Os restauradores repõem os archives/temas afetados e removem os que antes
não existiam. A restauração é integral para cada arquivo guardado e pode
substituir edições posteriores nesses arquivos. No backup de sistema, UID/GID
originais também são guardados. Pacotes instalados não são removidos.
Os backups são privados, com pasta 0700; mantenha-os na instalação que os gerou.

## Verificação e limites

Foram conferidas configurações locais efetivas, equivalência das cópias
Bibata de usuário/sistema e dependências do tema. Aplicação e restauração dos
scripts foram exercitadas em raízes/home descartáveis, incluindo paleta do
greeter, preservação de outras chaves, GTK com chave duplicada, existência e
ausência prévias. A geração/restauração do bloqueio foi exercitada em HOME
descartável; `uiVisible: false`, Qt.callLater e 60 s foram conferidos.
O módulo windowsarrows foi recompilado em pasta temporária com o KWin local.

Não houve reaplicação visual na sessão real, reinício SDDM, novo bloqueio ou
teste de senha nesta exportação. O teste PAM anterior permanece descrito em
ricy.md. Uma instalação nova completa e o comportamento das extensões em
outra versão não foram testados. Os números em `versoes-observadas.txt` são
referências de captura, não garantia de compatibilidade futura.

Licenças/avisos originais foram mantidos. Bibata: GPL-3.0, fonte upstream
https://github.com/ful1e5/Bibata_Cursor/tree/v2.0.6 ; Catppuccin KDE: MIT,
https://github.com/catppuccin/kde ; QML Breeze/tema Plasma: avisos KDE LGPL;
metadata SDDM declara CC-BY-SA. Textos complementares ficam em `licenses/`.
As fontes incluem OFL. Wallpaper Limine foi copiado do pacote local
cachyos-wallpapers; mantenha sua atribuição ao transportar este backup pessoal.
