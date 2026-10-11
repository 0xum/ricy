# Opções dos itens do tray na composição Noctalia

Menus DBusMenu de itens do tray usam o painel nativo encaixado
`ricy:tray-menu`, com fundo/opacidade da barra, blur contínuo, junção, animação
e fechamento externo do PanelManager. A apresentação substitui o popup
independente; ações e estados continuam fornecidos pelo aplicativo.

Na barra inferior há uma **setinha para baixo na base do menu**, junto à barra.
Ela volta diretamente à gaveta do tray, mantendo monitor, barra e âncora.
A referência horizontal é o centro da gaveta, independente do ícone clicado.
Menu e retorno usam o mesmo eixo; a setinha acompanha esse eixo mesmo quando
um menu mais largo precisa ser deslocado pelo limite do monitor.
O botão usa o estilo Ghost nativo: fundo transparente e destaque ao passar
o mouse. Está presente também dentro de submenus quando a gaveta está habilitada.

Pin/Unpin, separadores, entradas desabilitadas, marcas de seleção e opções de
rádio são preservados. Submenus navegam dentro da mesma composição, com
`← Back`, esquerda/Escape para subir um nível; Escape na raiz e clique externo
fecham. Setas percorrem ações habilitadas; Enter/Espaço ativam, direita entra
em submenu. O botão de retorno também participa da navegação por Tab.
Ações são adiadas até o fim do evento e verificam a linha atual antes do
acionamento. Eventos opened/closed continuam sendo enviados ao provedor.

A largura considera o maior texto e tem mínimo de conteúdo de 240 px à escala
1. A altura inclui todas as linhas, separadores, padding nativo e o botão de
retorno, sem repetir o padding já descontado pelo PanelManager. Não há
rolagem quando a lista cabe no monitor; ScrollView permite acessar listas
maiores que a área disponível. Carregamento sob demanda e atualizações
DBusMenu mantêm o retry limitado e redimensionam a composição conforme as
linhas mudam. Ao remover o item do tray, o menu fecha.

Itens sem DBusMenu continuam entregando seu menu ao próprio aplicativo.
As ações, incluindo atualizar pacotes ou sair, mantêm o significado original.

## Reproduzir

Compatível com Noctalia 5.2.1, commit
`6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`. Este patch composto reúne
notificações, wallpaper do Home, menu da taskbar e menu dos itens do tray.

```bash
cd "$HOME/ricy-kit/contributions/tray-menu-composition"
bash compilar.sh
python ../notification-continuity/ativar.py
```

Dependências: BUILDING.md upstream e contribuição notificacoes-continuidade.
O compilador aceita fonte limpa ou exatamente este patch; não sobrescreve
alterações desconhecidas. Para migrar de variante, preserve o cache anterior
num nome ainda inexistente antes de recompilar em fonte limpa, conforme
taskbar-menu-composition/README.md. Ajuste o caminho se XDG_CACHE_HOME estiver
configurado. O ativador cria backup e preserva os aplicativos durante a troca.
Não substitui `/usr/bin/noctalia`. O blur compartilhado requer a contribuição
blur-continuity correspondente ao KWin instalado.

## Validação e retorno

A compilação e validação do perfil passaram. O usuário confirmou visualmente
a composição do menu do tray e, depois, a setinha de retorno à gaveta.
O usuário também confirmou o ajuste posterior do alinhamento horizontal
entre menu, setinha e gaveta. Conferidos 45 cenários geométricos de larguras
e bordas, além da compilação/validação do perfil.
Testes completos de submenus, estados de seleção, ações de cada aplicativo,
listas extensas e outras posições de barra ainda não foram registrados. Um provedor temporário de teste foi registrado e removido; a
tentativa de automatizar o clique não abriu seu menu, portanto não confirma
as ações nem submenus. Dispositivos e scripts temporários foram encerrados.

Para conferir, abra a gaveta e o menu de um item, clique na setinha inferior
e verifique o retorno à gaveta no mesmo monitor. Confira também Escape,
submenus e uma ação segura antes de usar ações como fechar ou atualizar.

Para restaurar o binário anterior, use o backup impresso pelo ativador:

```bash
python ../notification-continuity/ativar.py --restaurar "$HOME/.local/state/ricy-notificacoes-backups/DATA-HORA"
```

Código upstream MIT; licença incluída. O kit contém apenas código e documentação
públicos; sem binários, capturas, clipboard, contas ou estado privado.

## Variante atual: ícones e hover

A variante posterior mantém este menu/alinhamento e acrescenta ícones de apps
e busca menores, com zoom suave ao passar o mouse. Para reconstruir o estado
completo atual, use ../app-icon-interactions/compilar.sh. Este compilador
anterior permanece histórico e recusa cache com alterações diferentes.
