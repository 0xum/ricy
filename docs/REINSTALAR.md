# Ricy — roteiro para a próxima instalação

Preparado em 09/10/2026 para reproduzir a configuração capturada de CachyOS,
KDE Plasma Wayland e Noctalia. Este é o ponto de entrada da reinstalação;
`ricy.md` preserva o histórico e `ricy-kit/` contém os scripts e assets.

A referência para manter e ampliar a aparência está em `IDENTIDADE-VISUAL.md`,
com tokens e prancha em `ricy-kit/contributions/noctalia-visual-identity/`.
Consulte-a antes de adequar outros componentes e transporte o guia com o kit.

O pacote `ricy-reinstalacao-2026-10-09.tar.gz` reúne este guia, o registro e
todo o kit portátil. `ricy.zip` oferece o mesmo conteúdo em formato ZIP.
Guarde um desses archives em outro disco, pendrive ou armazenamento remoto
antes de formatar. O arquivo não contém os logs/backups privados da origem.

Os compactados de 09/10 são retratos daquela data. Para transportar as
contribuições posteriores, copie também a pasta pública `ricy-kit/`, o
`ricy.md` e este roteiro atualizados.

## 1. Extrair e conferir

Na nova instalação CachyOS, entre em KDE Plasma Wayland como seu novo usuário.
Extraia o arquivo em uma pasta de trabalho. Exemplo em Bash:

```bash
mkdir -p "$HOME/ricy-importacao"
unzip /caminho/ricy.zip -d "$HOME/ricy-importacao"
# Se estiver usando o tar.gz, substitua o comando unzip por:
# tar -xzf /caminho/ricy-reinstalacao-2026-10-09.tar.gz -C "$HOME/ricy-importacao"
# Faça esta cópia uma vez, com $HOME/ricy-kit ainda inexistente:
cp -a "$HOME/ricy-importacao/ricy-kit" "$HOME/ricy-kit"
cd "$HOME/ricy-kit"
sha256sum -c SHA256SUMS
```

Use a cópia recém-extraída do kit portátil. Não reutilize a pasta ativa da
instalação anterior com seus backups, marcadores, perfis/clipboard e IDs.
Todos os comandos abaixo que escrevem preferências de usuário são sem sudo;
instalação de pacotes, `sistema.py` e instalação do plugin de blur usam sudo.

## 2. Dependências e correções do kit

```bash
sudo pacman -Syu
sudo pacman -S --needed noctalia kvantum konsole python python-gobject qt6-tools glib2 noto-fonts sddm plasma-workspace breeze breeze-icons qt6-5compat qt6-svg fontconfig adw-gtk-theme ocean-sound-theme
# Para reproduzir também todas as faces da fonte de origem:
sudo pacman -S --needed ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit"
python contributions/target-implementation-fixes/aplicar-correcoes.py
```

Opcional: `wl-clipboard` para a busca que usa texto copiado; `python-pyqt6`
para o instalador DEB/RPM e o teste Qt. Se Noctalia não estiver disponível
nos repositórios do destino, resolva a disponibilidade da implementação
compatível antes de iniciar a integração. O kit foi validado com Noctalia
5.2.1 e Plasma/KWin 6.7.5; confira versões novas antes de aplicar.

Confira os hashes antes de executar o aplicador de correções. Depois dele,
os dois archives corrigidos já não têm os hashes históricos; depois da
preparação os `.desktop` também mudam de caminho. Isso é esperado.

## 3. Login, cursor animado do Konsole, fontes e aparência

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
sudo python sistema.py
python usuario.py
python ../konsole-animated-cursor/aplicar.py
```

Isso instala o login `mocha-limine`, as cores reais da conta SDDM, fundo
Limine, cursor Bibata Modern Classic 16, fontes JetBrainsMono 10 pt, ícones
Breeze Dark, temas Plasma/splash, menus Kvantum KDE-Noctalia e aparência GTK.
O script preserva outras preferências do destino e imprime seu backup.

O cursor solicitado é o cursor de texto do Konsole: o perfil padrão PlasmaBlur
incluído ativa `AnimatingCursorEnabled=true`, fonte JetBrainsMono 10 pt,
paleta Catppuccin, transparência 0,85 e blur. Feche e abra o Konsole para
carregar esse perfil. O aplicador verifica o suporte à animação no destino.
Bibata 16 é uma preferência adicional do ponteiro do mouse.

Se a instalação usa Plasma Login Manager e você quer reproduzir o login
SDDM deste kit, selecione o serviço depois de aplicar `sistema.py`:

```bash
# Confirme primeiro o gerenciador existente:
readlink -f /etc/systemd/system/display-manager.service
# Neste destino, o anterior era plasmalogin.service:
sudo systemctl disable plasmalogin.service
sudo systemctl enable sddm.service
```

Em outro destino, substitua o serviço anterior pelo que estiver instalado.
Esses comandos não usam `--now` e preservam a sessão atual. Reinicie o
computador para a troca ter efeito; sair/entrar na sessão apenas não troca
o processo do gerenciador que já está em execução.

Para também adotar o wallpaper Limine nos desktops do Plasma:

```bash
bash aplicar-wallpaper.sh
```

Esse último passo é opcional. Escolha o wallpaper antes do próximo passo,
pois o preparador Noctalia gera sua preservação com os IDs/imagens do destino.

## 3a. Cedilha no teclado US internacional

Para o teclado US internacional (`us`, variante `alt-intl`) utilizado neste
destino, aplique também a composição de cedilha:

```bash
cd "$HOME/ricy-kit"
python contributions/keyboard-cedilla/aplicar.py
python contributions/keyboard-cedilla/aplicar-brave.py
```

Acento agudo seguido de c/C produz ç/Ç; os demais acentos e o idioma da
interface são preservados. O Brave utiliza XWayland para respeitar essa
composição; o KDE continua em Wayland. Os archives anteriores ficam em backup. Reabra
completamente Konsole e Brave para carregar a regra. Consulte o README da
contribuição para reversão. Se o teclado físico for ABNT2, configure o layout
brasileiro adequado em vez de aplicar este ajuste ao layout US.

## 4. Preparar e iniciar a integração Noctalia

```bash
cd "$HOME/ricy-kit/contributions/noctalia-kde-integration-and-menus"
python preparar-destino.py
cd "$HOME/ricy-kit"
python contributions/noctalia-autostart/instalar-inicio-automatico.py
python contributions/plasma-noctalia-switching/instalar.py
```

O preparador guarda layout/estilo/atalhos locais, cria o perfil isolado e os
launchers. O instalador seguinte habilita Noctalia no login, com recuperação
do Plasma em erro. Plasma/KWin continuam responsáveis pelo desktop e wallpaper.
A barra inferior fica fixa em 44 px; Super/Super+Espaço abrem busca e Super+V
abre clipboard. A lupa da barra abre a busca junto ao clique, no canto
esquerdo, como o controle Noctalia abre junto ao ícone à direita. Use somente
esta contribuição; a variante histórica em
`ricy-kit/outputs/` não deve ser iniciada simultaneamente.

O último instalador adiciona **Voltar ao Noctalia**, **Voltar ao Plasma** e
**Alternar Plasma e Noctalia** no menu e os comandos `ricy noctalia`,
`ricy plasma`, `ricy alternar` e `ricy status` em `$HOME/.local/bin`.
A preferência também vale no próximo login. Salva os painéis Plasma atuais
antes de recolhê-los e restaura só os grupos dos painéis, preservando wallpaper,
desktops, personalizações e perfil Noctalia. Substitui os scripts antigos que
restauravam appletsrc/plasmashellrc inteiros do backup original. Reaplique esse
instalador se reinstalar posteriormente `noctalia-autostart`.

Depois de editar o perfil Noctalia, mantenha sincronizadas as cópias em
`outputs/noctalia-test/config.toml` e
`work/noctalia-profile/config/noctalia/config.toml` desta contribuição.


A busca por Super ou digitação usa uma barra superior centralizada de 640 px,
altura 16 px, cantos de 8 px e distância de 8 px do topo, somente enquanto
aberta, somente no monitor onde a busca aparece. O adaptador consulta o
monitor ativo do KWin antes de mostrar a barra; Super e digitação usam a
mesma abertura. Nos monitores atuais de 1920 px lógicos, `bar.search_edge.margin_ends`
é 640. Em outra resolução, ajuste essa margem para `(largura lógica - 640) / 2`
(arredondada e limitada a zero), usando overrides por monitor se necessário.
A busca mede 560 px com `accessibility.ui_scale = 1`; se alterar a escala,
ajuste também a largura desejada da barra.

## 4a. Composição Noctalia: notificações, wallpaper e menus

O perfil inclui notificações no canto inferior direito do monitor ativo, sem
contorno, com opacidade 0,70 e barra nativa de tempo restante. Para também unir
o cartão à taskbar com uma curva aberta para fora no canto inferior esquerdo
e o canto inferior direito reto, compile a adaptação local do Noctalia 5.2.1:

```bash
sudo pacman -S --needed meson ninja wayland-protocols nlohmann-json stb
cd "$HOME/ricy-kit/contributions/app-icon-reordering"
bash compilar.sh
python ../notification-continuity/ativar.py
python ../window-fade-expand/aplicar-animacoes.py
# Imagem do Plasma no cartão Home, mantendo o desktop no Plasma:
python ../notification-continuity/sincronizar-wallpaper.py
```

A variante composta mais recente inclui menus da taskbar e dos itens do tray
como painéis encaixados, com largura/altura por conteúdo. O menu do tray tem
setinha na base para voltar diretamente à gaveta no mesmo monitor,
preservando o eixo horizontal entre menu, seta e gaveta.
A variante inclui também ícones de apps e busca 12% menores no repouso,
com hover de 140 ms e área de clique estável; os demais controles ficam iguais.
No KDE/KWin, clique no ícone restaura minimizadas, minimiza a janela visível
em foco e traz à frente uma janela visível inativa. O botão do meio solicita
fechar uma janela; os grupos priorizam a ativa, preservando seleção/ciclo quando
não há ativa. Busca e outros chamadores continuam apenas restaurando/focando.
O indicador roxo agora distingue ativa, aberta inativa e minimizada, com
transição de 160 ms. As janelas agora recebem fade e expansão ao abrir/restaurar
(escala 0,85→1) e contração ao fechar/minimizar (1→0,85), centradas na janela.
Duração base 320 ms segue velocidade global KDE (0,25 na sessão, cerca de
80 ms). O novo aplicador window-fade-expand preserva a preferência global,
recarrega os efeitos sem reiniciar o compositor e oferece reversão em backup.
Não exige geometria de ícone ou referência à posição/altura da barra.
Ícones recebem bounce ao abrir/restaurar, pulso ao ganhar foco e resposta
breve ao minimizar/fechar, sem fundo preto. Na faixa plana, clique/arraste
reorganiza todos os apps, sem fixá-los; a ordem é salva no perfil. Busca e
outros controles mantêm posição. Soltar arraste não ativa/minimiza a janela.
Consulte app-icon-reordering/README.md para preservar o cache de uma variante
anterior e recompilar a partir de fonte limpa quando necessário.

O script mantém o pacote original e seleciona o executável local apenas na
unidade da shell. Confira o README para dependências adicionais, reversão e
atualizações: a variante local precisa ser revista/recompilada ao atualizar a
versão do Noctalia. O ativador preserva aplicativos durante a troca da shell.


A mesma variante inclui a imagem no cartão Home mesmo com o serviço de
wallpaper Noctalia desativado. O sincronizador exige desktops Plasma com a
mesma imagem estática local e registra esse caminho; execute-o novamente ao
mudar o fundo. Leia o README se os monitores usam imagens diferentes.

## 4b. Continuidade do blur entre painéis

Para unir visualmente o fundo de notificações, busca, menu e barras, depois
dos passos 4/4a compile o efeito separado para KWin 6.7.5:

```bash
sudo pacman -S --needed base-devel git vulkan-headers kwin kconfig kcoreaddons kdecoration qt6-base qt6-declarative kwindowsystem libepoxy libdrm wayland
cd "$HOME/ricy-kit/contributions/blur-continuity"
python compilar.py
sudo install -D -m 0755 "$HOME/.cache/ricy-blur-build-6.7.5/ricyblur.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so
python integrar.py
noctalia msg config-reload
```

Se XDG_CACHE_HOME estiver definido, ajuste o caminho do plugin no install.
O script seleciona a variante compatível em cada sessão; conserva o blur
nativo quando não puder usá-la. Não reinicia KWin ou aplicativos. O ABI exige
revisar/recompilar o patch ao atualizar KWin; o compilador recusa outra versão.
Os templates incluem `panel_overlap = 0` nas barras default e search_edge;
num perfil já existente, ajuste também essas duas preferências e recarregue.
Consulte `contributions/blur-continuity/README.md` para detalhes e reversão.
O custo de composição pode aumentar enquanto painéis/avisos estão abertos.

## 4c. Datas em inglês, clima e eventos em Cosmópolis/SP

```bash
cd "$HOME/ricy-kit"
python contributions/noctalia-language-and-localization/aplicar.py
```

Exige a locale en_US.UTF-8 gerada no destino. Define datas em inglês somente
no Noctalia e fuso America/Sao_Paulo; localização fixa Cosmópolis, São Paulo,
Brasil, com clima em °C. Habilita calendário/eventos sem conectar contas.
Para eventos pessoais, conecte a fonte posteriormente nas configurações.
O endereço completo evita a cidade homônima nos EUA. Consulte o README da
contribuição para backup/reversão; o aplicador preserva aplicativos ao
reiniciar shell/adaptador e corrige overrides de preferências do destino.

## 5. Tela de bloqueio

```bash
cd "$HOME/ricy-kit/contributions/login-matched-lock-screen"
python aplicar.py
```

A tela de bloqueio usa o fundo do login, relógio e formulário imediato por
60 s, sem mídia/revelar senha. O script mantém o fluxo nativo de autenticação
do KDE e a correção `Qt.callLater`. Se o QML do Plasma do destino tiver mudado,
o script recusa a adaptação; revise-o antes de insistir. Após atualizações
Plasma, reaplique a partir dos novos archives do sistema.

## 6. Efeitos e setas de janelas (opcional)

```bash
sudo pacman -S --needed gcc pkgconf qt6-base qt6-declarative kwin kconfig
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python usuario.py --extensoes-kwin
# A barra do Noctalia substitui os painéis Plasma:
kwriteconfig6 --file kwinrc --group Plugins --key adaptivepanelwidthEnabled false
```

Inclui os efeitos locais e Super+setas que mantêm a mesma janela como alvo
até soltar Super. O módulo nativo é recompilado para o KWin do destino;
nenhuma biblioteca antiga é reutilizada. Esse passo exige API/headers
compatíveis. A recompilação foi verificada com o KWin da captura.

## 6a. Adaptador USB AIC8800 (opcional)

Para o adaptador deste destino (`a69c:8800` antes do firmware,
`a69c:8801` em funcionamento), siga
`ricy-kit/contributions/driver-aic8800/README.md`. O pacote fonte DKMS
fornece Wi-Fi, Bluetooth e firmware, com seleção de compilador para cada
kernel. Use headers compatíveis com os kernels instalados. Não é uma etapa
necessária em máquinas com outro adaptador.

## 7. Instalador DEB/RPM no Dolphin (opcional)

Siga a contribuição `dolphin-deb-rpm-installer/README.md`, incluindo registro
de pacotes do destino e construção revisada de Debtap do AUR. A contribuição
`target-implementation-fixes` já deve ter sido aplicada no passo 2.

Após instalar as dependências e Debtap, use o wrapper corrigido de índices,
em vez do wrapper histórico HTTP/curl -k:

```bash
cd "$HOME/ricy-kit"
sudo bash contributions/target-implementation-fixes/atualizar-indices.sh
cd contributions/dolphin-deb-rpm-installer
python instalar-integracao.py
```

A janela converte como usuário, mostra metadados e oferece Instalar via
Polkit/pacman. RPM com scriptlets é recusado. Compatibilidade de cada app
externo deve ser verificada separadamente; não use --nodeps/--overwrite.

## 8. Conferir e carregar tudo

Se selecionou outro gerenciador de login, reinicie o computador. Caso contrário,
encerre a sessão normalmente e entre novamente em Plasma Wayland. Isso
também permite conferir o login e o início automático Noctalia. Não reinicie
SDDM de dentro de uma sessão que deseja preservar.

```bash
systemctl --user is-enabled ricy-noctalia-integracao.service
systemctl --user is-active noctalia-teste.service noctalia-busca-desktop.service
kreadconfig6 --file kcminputrc --group Mouse --key cursorTheme
kreadconfig6 --file kcminputrc --group Mouse --key cursorSize
kreadconfig6 --file kdeglobals --group General --key font
kreadconfig6 --file kwinrc --group org.kde.kdecoration2 --key library
fc-match 'JetBrainsMono Nerd Font'
```

Confira visualmente login/bloqueio, cursor 16, menus/fontes, wallpaper,
monitores, busca e clipboard. Para uma prévia do bloqueio sem bloquear a
sessão: `/usr/lib/kscreenlocker_greet --testing` e feche a janela ao terminar.
Testes anteriores e suas limitações estão nos READMEs e no registro.

## 8a. Dolphin com identidade Noctalia (opcional)

Após configurar KDE-Noctalia/Kvantum:

```bash
cd "$HOME/ricy-kit/contributions/dolphin-noctalia-identity"
python aplicar.py
```

Requer Qt6 Widgets/headers, g++, pkg-config e Noto Sans. Compila o helper Qt
privado, aplica variante exclusiva, fonte Noto Sans, fundo alfa 0,70 com blur,
chips na lateral (ícone + nome), linhas e header arredondados. Reabra Dolphin
pelo launcher para carregar o helper; processos antigos não o recebem por QSS.

Para cantos externos nativos 16 px, siga a contribuição
ricy-kit/contributions/dolphin-blur-corners/README.md: compilar.py requer headers
KWin 6.7.5 e dependências indicadas, instalação da biblioteca em diretório de
sistema com sudo e ativar-cantos.py. Não reinicie KWin; ao atualizar sua versão,
revise a API e recompile antes de reutilizar o efeito. A transparência da Qt
não aplica opacidade aos textos/ícones. Blur existente ricyblur fornece o fundo.
Reprodução, limites e reversão nos READMEs das duas contribuições; fonte KDE
global e operações de archives preservadas.
Biblioteca atualizada por troca atômica. Delegate nativo da sidebar preservado,
expansão de pastas/navegação em compactados habilitadas e '+' seleção desligado.
Chips acompanham viewport ao reduzir janela; filhos recuam conforme hierarquia.
Leia evidência/limites no final de dolphin-blur-corners/README.md.


## Restaurar no destino

Os caminhos DATA-HORA abaixo são exemplos; use os caminhos impressos na nova
instalação. Não copie os backups da origem. Para voltar ao Plasma:

```bash
"$HOME/.local/bin/ricy" plasma
```

Para reativar Noctalia:

```bash
"$HOME/.local/bin/ricy" noctalia
```

Para desfazer a nova contribuição de aparência:

```bash
cd "$HOME/ricy-kit/contributions/login-lock-cursor-appearance"
python ../login-matched-lock-screen/restaurar.py "$HOME/.local/state/ricy-lockscreen-backups/DATA-HORA"
python ../konsole-animated-cursor/aplicar.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
python usuario.py --restaurar "$HOME/.local/state/ricy-appearance-backups/DATA-HORA"
sudo python sistema.py --restaurar /var/lib/ricy-appearance-backups/DATA-HORA
```

Se aplicou aparência duas vezes (por exemplo, para incluir extensões), use
os backups na ordem inversa das aplicações. A reversão restaura os archives
guardados e pode substituir alterações posteriores nesses mesmos arquivos.
Escolha novamente seu wallpaper anterior pelo Plasma se mudou a imagem.
O restaurador Dolphin é independente e usa o backup emitido por seu instalador.

Este pacote é um backup portátil de configurações e assets de aparência;
não é uma imagem de disco. Drivers, resolução/escala de monitores, conexões de
rede, dispositivos, contas, senhas e dados de aplicativos devem ser configurados
na nova máquina. O histórico contém configurações antigas substituídas;
use a ordem deste guia e as contribuições finais para a reinstalação.
