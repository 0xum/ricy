# Continuidade do blur entre superfícies Noctalia

O KWin 6.7.5 calcula o blur usando uma textura limitada ao retângulo de cada
janela. Nas barras, painéis e notificações isso pode deixar uma emenda, mesmo
quando cor e transparência são iguais.

Esta contribuição compila um efeito separado, `ricyblur`, a partir do blur
oficial do KWin 6.7.5, commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.
As superfícies com resourceClass `noctalia` usam uma referência comum do fundo
por monitor enquanto há um painel/aviso visível. O mesmo resultado é recortado
pela forma de cada superfície. A amostragem não inclui o próprio Noctalia;
o recorte OpenGL da janela não limita a cópia ou o filtro do fundo compartilhado.
Outros aplicativos mantêm a lógica nativa de blur.

O fundo é reconstituído antes da primeira superfície Noctalia em cada frame
necessário, e o filtro é calculado uma vez por monitor. Enquanto um painel/aviso
está aberto, os frames com alterações repintam todo o monitor para evitar
reutilizar pixels que já contêm a barra. Isso pode aumentar o custo de composição
com vídeo/animações; não é criado um laço de repintura contínuo quando tudo está
parado. Não são feitas capturas de tela nem gravado conteúdo do fundo em disco.

Também aplicado `panel_overlap = 0` em `[bar.default]` e `[bar.search_edge]`:
remove a faixa de um pixel com duas camadas de transparência na junção.
A posição, os cantos, a opacidade 0,70 e a escolha de monitor permanecem como
nas contribuições de busca/notificações. A geometria das notificações ainda
depende da variante local do Noctalia em `../notification-continuity/`.

## Reproduzir no CachyOS/Arch

Prepare primeiro a integração Noctalia e sua geometria de notificações.
O ABI de plugins KWin exige a mesma versão do compositor. O compilador recusa
versão diferente de 6.7.5; revise/rebaseie o patch ao atualizar.

```bash
sudo pacman -S --needed base-devel git vulkan-headers kwin kconfig kcoreaddons kdecoration qt6-base qt6-declarative kwindowsystem libepoxy libdrm wayland
cd "$HOME/Projects/ricy/ricy-kit/contributions/blur-continuity"
python compilar.py
sudo install -D -m 0755 "$HOME/.cache/ricy-blur-build-6.7.5/ricyblur.so" /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so
python integrar.py
noctalia msg config-reload
```

Se XDG_CACHE_HOME estiver definido, use seu diretório no comando install.
Neste destino não foi preciso instalar mais pacotes: foram usados headers
oficiais Vulkan 1.4.363 no cache, commit
`6802bb4733b63ed5efd3adb308a6c885ef180ea1`, por RICY_VULKAN_HEADERS apontando
para sua pasta include. Numa reinstalação, o pacote vulkan-headers é suficiente.

O efeito não substitui o binário, as bibliotecas ou o plugin nativo do KWin.
`integrar.py` instala o seletor em `$HOME/.local/lib/ricy-blur/iniciar.py` e
habilita `ricy-blur-continuidade.service` na sessão gráfica. Não reinicia o
compositor ou a shell nem encerra aplicativos. O script seleciona a variante
somente em KWin 6.7.5 e quando ela é suportada; se não puder carregá-la, mantém
ou recarrega o blur nativo. O nativo permanece habilitado na configuração;
ricyblur não é habilitado como plugin automático do KWin.

As preferências `panel_overlap` vêm dos templates do kit; numa instalação já
ativa, ajuste também seu config.toml antes de recarregar. Faça backup antes.

## Verificar e restaurar

```bash
systemctl --user status ricy-blur-continuidade.service
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.isEffectLoaded ricyblur
```

Para voltar ao efeito nativo:

```bash
systemctl --user disable --now ricy-blur-continuidade.service
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.unloadEffect ricyblur
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.loadEffect blur
noctalia msg config-reload
```

O arquivo do plugin pode permanecer instalado e desativado. Remova-o, se
desejado, com `sudo rm -- /usr/lib/qt6/plugins/kwin/effects/plugins/ricyblur.so`.
O integrador guarda helper/unidade anteriores em
`$HOME/.local/state/ricy-blur-backups/`. A restauração do efeito não reverte
panel_overlap; restaure o backup do config.toml ou ajuste só essa preferência.

Teste visual feito primeiro em uma sessão KWin/Noctalia isolada, com faixas
coloridas, menu e notificação; depois aplicado na sessão principal. O usuário
validou visualmente durante o trabalho. A migração para outro computador e
escalas diferentes não foi testada. Código upstream GPL-2.0-or-later, licença
incluída em LICENSE.

Fontes: [blur oficial da versão](https://github.com/KDE/kwin/tree/v6.7.5/src/plugins/blur)
e [regras do ABI de efeitos](https://github.com/KDE/kwin/blob/v6.7.5/src/effect/effect.h).
