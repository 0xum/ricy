# Noctalia iniciado automaticamente no KDE

Os nomes `noctalia-teste.service` e `iniciar-teste.sh` são históricos: depois deste instalador, o Noctalia é permanente e inicia no login. As entradas de menu e mensagens não usam mais o rótulo de teste.

Esta contribuição substitui o modo de início manual pelo início no login,
conforme o pedido posterior à reinicialização. O Plasma continua ativo para
desktop/wallpaper; a integração inicia Noctalia, adaptador e atalhos e recolhe
os painéis somente após o IPC estar pronto.

## Instalar

Prepare primeiro `noctalia-kde-integration-and-menus` e aplique as correções da
contribuição `target-implementation-fixes`. Nesta cópia preparada do kit:

```bash
python contributions/noctalia-autostart/instalar-inicio-automatico.py
```

Execute como usuário do desktop em Plasma Wayland. O instalador guarda os
archives anteriores em `$HOME/.local/state/ricy-inicio-automatico-backups/`,
instala três unidades em `.config/systemd/user`, atualiza cinco scripts da
integração, valida as unidades e habilita/inicia a integração.

- `ricy-noctalia-integracao.service` é habilitada em `plasma-workspace.target`.
  Aguarda plasmashell e KGlobalAccel e executa a integração, com recuperação
  do Plasma em caso de erro durante a execução.
- `noctalia-teste.service` passa a ser permanente, usando o perfil isolado
  preparado. Reinicia em falha e inicia também o adaptador.
- `noctalia-busca-desktop.service` é permanente e acompanha a shell. Usa
  `Type=exec` e verifica a propriedade efetiva de `org.kde.krunner`; não
  declara `BusName`, evitando conflito com a unidade nativa do KRunner.

As unidades acompanham `graphical-session.target`. O adaptador reinicia ao
reiniciar a shell. A recuperação antiga de login não restaura o Plasma
enquanto o início automático estiver habilitado.

O registro de Super aguarda até dois segundos pela criação efetiva da ação
no KGlobalAccel. Isso cobre a criação dos desktop entries no login. Os JSON
de atalhos e backups originais continuam sendo os capturados no destino.

## Voltar ao Plasma

```bash
contributions/noctalia-kde-integration-and-menus/outputs/noctalia-test/voltar-ao-plasma.sh
```

Essa operação também desabilita o início automático para os próximos logins.
Para voltar ao Noctalia e reativar a preferência:

```bash
systemctl --user enable ricy-noctalia-integracao.service
systemctl --user restart ricy-noctalia-integracao.service
```

Nesta instalação, `$HOME/Projects/ricy/voltar.sh` e `$HOME/Projects/ricy/iniciar.sh` oferecem
essas operações. O backup de estilo e o de layout existentes foram mantidos.

## Verificação executada

Unidades verificadas por `systemd-analyze --user verify`; integração habilitada
com symlink no target KDE; início pela unidade terminou com sucesso. Ciclo de
volta ao Plasma (dois painéis, autostart desabilitado) e reinício automático
testado. Reinício da shell reiniciou também o adaptador; o PID do dono D-Bus
coincidiu com o adaptador e a consulta Query abriu a busca. Configuração TOML
inválida foi introduzida temporariamente: a integração restaurou os dois
painéis/KRunner, e o perfil original foi reposto e iniciado com sucesso.

A habilitação no login foi conferida. Uma nova reinicialização completa após
esta alteração não foi executada pelo agente durante a sessão do usuário.
