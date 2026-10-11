# Datas em inglês e localização Cosmópolis/SP no Noctalia

A integração usa `shell.lang = "en"`, `LC_TIME=en_US.UTF-8` e
`TZ=America/Sao_Paulo` apenas na unidade Noctalia. A região do desktop e as
regras de composição do teclado continuam nas configurações existentes.
`LC_ALL` é removida do ambiente dessa unidade para não sobrepor LC_TIME.
A locale en_US.UTF-8 precisa estar gerada no destino.

Localização fixa com `auto_locate = false` e
`address = "Cosmopolis, Sao Paulo, Brazil"`. O endereço completo evita a
cidade homônima nos Estados Unidos. A API nativa resolveu o destino como
Cosmópolis, Brazil, latitude -22.64583, longitude -47.19611.

Clima habilitado em unidades métricas (°C); Noctalia consulta Open-Meteo.
O calendário/eventos fica habilitado, sem adicionar conta, fontes de eventos
ou feriados. Eventos pessoais exigem conectar Google, CalDAV, ICS ou vdir
posteriormente nas configurações Noctalia. A localização é usada pelo clima;
o calendário utiliza o fuso da sessão e os eventos de suas fontes.

## Aplicar

Depois de preparar a integração permanente e a contribuição de notificações:

```bash
cd "$HOME/Projects/ricy/ricy-kit"
python contributions/noctalia-language-and-localization/aplicar.py
```

O script ajusta somente as chaves listadas em PREFERENCES no perfil e em seu
settings.toml privado (as preferências da interface podem sobrepor o template).
Preserva contas e outras opções, valida a configuração e instala
`60-ricy-idioma-localizacao.conf` na unidade noctalia-teste.service.
Reinicia apenas shell/adaptador com o helper existente de preservação de
aplicativos. Não instala pacotes nem altera a locale global do sistema.
Os templates públicos do kit já incluem idioma, localização, clima e calendário;
o aplicador adiciona o ambiente necessário às datas e corrige overrides locais.

## Verificação e reversão

Nesta instalação: configuração validada; calendário exibiu Saturday/October;
geocodificação confirmou Brasil; clima recebeu dados e sete dias de previsão,
com timezone America/Sao_Paulo. Não foi sincronizada conta de calendário,
conforme escolha do usuário. Não foi feita instalação em outra máquina.

Backups anteriores do perfil, settings e drop-in ficam em
`$HOME/.local/state/ricy-idioma-localizacao-backups/DATA-HORA/`, com manifest
indicando archives que não existiam. Para restaurar, revise esse manifest,
restaure somente os archives desejados e remova o drop-in se antes era ausente.
Restaurar settings.toml inteiro também reverte outras preferências posteriores.
Recarregue systemd e reinicie shell/adaptador pelo helper com preservação de
aplicativos usado por aplicar.py; não use um restart comum da shell se houver
aplicativos filhos que deseja manter. Os templates são independentes do estado
local; ajuste suas chaves também se quiser manter a reversão em reinstalações.

Fonte da localização: [geocodificação usada pelo Noctalia](https://api.noctalia.dev/geocode?city=Cosmopolis%2C%20Sao%20Paulo%2C%20Brazil).
