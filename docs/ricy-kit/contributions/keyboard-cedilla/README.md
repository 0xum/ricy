# Cedilha no teclado US internacional

O destino usa `us(alt-intl)` e interface em inglês. A composição inglesa
original interpreta acento agudo seguido de c/C como ć/Ć. Este aplicador
configura `$HOME/.XCompose` para produzir ç/Ç, mantendo o layout, o idioma
e as demais composições. Em arquivo novo inclui `"%L"`; em arquivo existente
preserva as regras do usuário e acrescenta o bloco Ricy ao final.

```bash
cd "$HOME/ricy-kit"
python contributions/keyboard-cedilla/aplicar.py
python contributions/keyboard-cedilla/aplicar-brave.py
```

Execute sem sudo. Reabra completamente Konsole e Brave: processos existentes
podem manter a tabela anterior. No Brave, feche também o processo em segundo
plano; sair e entrar na sessão é outra forma de recarregar os aplicativos.
Teste a tecla de acento agudo seguida de `c` e de `Shift+C`: `ç`, `Ç`.

O aplicador é idempotente e guarda o arquivo anterior (ou marcador de ausência)
em `$XDG_STATE_HOME/ricy-teclado-backups/DATA-HORA`, com padrão
`$HOME/.local/state`. Para desfazer, restaure `XCompose` do backup em
`$HOME/.XCompose`; se houver `XCompose.ausente`, remova o arquivo criado.
Reabra os aplicativos depois. Se houver alterações posteriores, remova somente
o bloco delimitado `BEGIN/END Ricy` para preservar essas alterações.

Isso corrige a composição da sessão gráfica; o teclado do console virtual e
a conta separada do SDDM continuam usando suas próprias configurações.
O layout físico ABNT2 exige a configuração `br`, não este ajuste de US.

Referência: [libxkbcommon — Compose e dead keys](https://xkbcommon.org/doc/current/group__compose.html).

## Brave no KDE Wayland

O usuário confirmou a cedilha no Konsole, mas o Brave nativo Wayland ainda
produziu ć. O compositor interno de caracteres do Chromium usa uma tabela
própria para os eventos que não foram consumidos por um IME. Não basta reabrir
o navegador para fazê-lo usar .XCompose nessa rota.

`aplicar-brave.py` seleciona `--ozone-platform=x11` em
`$XDG_CONFIG_HOME/brave-flags.conf` (padrão `$HOME/.config`). O launcher do
pacote CachyOS/Arch lê esse arquivo; a seleção usa XWayland dentro da sessão
KDE Wayland. O script preserva outras flags e guarda o estado anterior em
`ricy-teclado-backups`. Reabra completamente o Brave após aplicar.
Esta rota pode mudar a escala/renderização do navegador em telas HiDPI.

Para desfazer, restaure `brave-flags.conf` do backup; se houver o marcador
`brave-flags.conf.ausente`, remova o arquivo criado. Para preservar alterações
posteriores, remova apenas a linha `--ozone-platform=x11`. Reabra o Brave.

Referências primárias Chromium:
[rota de entrada Wayland](https://chromium.googlesource.com/chromium/src/+/HEAD/ui/ozone/platform/wayland/host/wayland_input_method_context.cc) e
[compositor de caracteres](https://chromium.googlesource.com/chromium/src/+/HEAD/ui/base/ime/character_composer.cc).
