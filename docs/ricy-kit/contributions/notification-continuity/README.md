# Notificações contínuas com a taskbar

Preferências distribuídas no config.toml da integração Noctalia:

```toml
[notification]
position = "bottom_right"
follow_focused_output = true
background_opacity = 0.70
border = false
offset_x = 0
offset_y = 0
```

As notificações aparecem no monitor ativo, junto à taskbar inferior e à borda
direita, com a mesma transparência. O Noctalia 5.2.1 já desenha uma barra de
tempo que diminui até expirar; ao passar o ponteiro, a contagem pausa.
Avisos persistentes sem prazo não ganham um prazo artificial.

O cartão nativo deixa um recorte arredondado na junção com a taskbar.
`notificacao-canto-direito.patch` mantém o canto inferior direito reto e abre
o canto inferior esquerdo para fora, com uma curva côncava que encontra a barra.
Os dois cantos superiores permanecem arredondados. Isso se aplica quando a
posição é bottom_right com offset_x=0 e offset_y=0. A superfície reserva espaço
à esquerda sem reduzir o conteúdo nem afastar o cartão da borda direita.
Desenho, recorte da animação e região de blur seguem essa geometria, sem alterar
a lógica do daemon ou da contagem regressiva.

## Reproduzir

Primeiro prepare e instale a integração permanente Noctalia deste kit.
Esta contribuição foi feita para Noctalia **5.2.1**, commit upstream
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. O script recusa outras versões;
revise/rebaseie o patch antes de migrar para outro Noctalia.

No CachyOS/Arch, confira as dependências do BUILDING.md upstream. Neste destino
foi necessário acrescentar apenas:

```bash
sudo pacman -S --needed meson ninja wayland-protocols nlohmann-json stb
cd "$HOME/ricy-kit/contributions/notification-continuity"
bash compilar.sh
python ativar.py
```

A compilação usa prefixo /usr apenas para encontrar os assets do pacote; não
executa `meson install` e não substitui `/usr/bin/noctalia`. O executável local
fica em `$HOME/.local/lib/ricy-noctalia/noctalia`, selecionado por um drop-in
da unidade noctalia-teste.service. O CLI original continua enviando IPC para
a mesma shell. O código-fonte/build ficam no cache do usuário, fora do kit.

`ativar.py` guarda binário/drop-in anteriores, recarrega a unidade e reinicia
a shell/adaptador. Durante essa troca aplica temporariamente KillMode=process
para preservar os aplicativos lançados pelo menu; remove esse override logo
após a troca. A configuração permanente de encerramento da unidade é mantida.

Atualizar o pacote Noctalia não atualiza automaticamente o executável local.
Ao atualizar a versão, revise o patch e recompile, ou restaure o pacote original
antes de adotar assets/configuração da versão nova.

## Restaurar

```bash
python ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Use o backup impresso pelo ativador (contém manifest.json), que restaura a
seleção anterior da shell e seu binário local, se existia. Isso não reverte
as preferências visuais no config.toml; para isso restaure o backup de
configuração ou ajuste apenas `[notification]`. O aplicador não remove pacotes.

Código upstream sob licença MIT, incluída em LICENSE.
Referências: [notificações](https://docs.noctalia.dev/noctalia/services/notifications/)
e [compilação da versão](https://github.com/noctalia-dev/noctalia/blob/v5.2.1/BUILDING.md).

## Wallpaper do cartão Home com desktop Plasma

A variante local também permite que o cartão Home use o caminho configurado
quando `[wallpaper] enabled = false`. O Noctalia continua sem desenhar o fundo
do desktop; a miniatura do cartão é carregada independentemente pelo serviço
nativo de thumbnails. A opacidade e o blur dos painéis permanecem os mesmos.

Após compilar/ativar, registre a imagem dos desktops Plasma:

```bash
python sincronizar-wallpaper.py
```

O script usa a API do Plasma e só prossegue quando todos os desktops usam a
mesma imagem estática local. Guarda settings.toml da integração em backup
privado e usa o IPC wallpaper-set do Noctalia para registrar essa mesma imagem
(a API também sincroniza a seleção com o Plasma). Fundos diferentes, animados
ou archives ausentes são recusados antes de alterar preferências. Não copia
imagens pessoais para o kit. Execute novamente se mudar o wallpaper no Plasma;
esta contribuição não instala um monitor automático de mudanças.

A imagem é do cartão Home; o restante do menu mantém o fundo translúcido com
blur da cena atrás dele. O wallpaper não é desenhado sobre o painel inteiro.
Restaurar o binário pelo ativador também restaura o comportamento anterior do
cartão; settings.toml e wallpaper do Plasma são preferências separadas. Revise
um backup de settings antes de restaurá-lo, pois contém outras preferências.

## Variante composta atual

Para reproduzir também o menu da taskbar como painel Noctalia encaixado e
sem rolagem, use ../taskbar-menu-composition/compilar.sh e seu patch completo.
Este compilador anterior permanece como referência da variante de
notificações/Home; ele recusa corretamente um cache com mudanças diferentes.
O ativador/restaurador desta pasta continua sendo usado pela variante nova.

## Atualização: menus do tray

O estado atual inclui também as opções dos itens do tray como painel Noctalia
e setinha para retornar à gaveta. Para reconstruir todas as mudanças, use
../tray-menu-composition/compilar.sh e seu patch completo. Este compilador
anterior permanece como referência histórica e recusa cache diferente.
