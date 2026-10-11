# Konsole: cursor de texto animado

Esta contribuição atende à correção do usuário: o cursor solicitado é o
cursor de texto animado do Konsole. O ponteiro Bibata da contribuição de
aparência permanece como uma preferência adicional capturada.

Estado observado no Konsole 26.08.2-1.1:

- `konsolerc`: perfil padrão `PlasmaBlur.profile`; barra de menus desativada.
- Perfil Plasma Blur: `[Terminal Features] AnimatingCursorEnabled=true`.
- Fonte: JetBrainsMono Nerd Font 10 pt; paleta `PlasmaBlur`.
- Paleta Catppuccin Mocha, `Opacity=0.85` e `Blur=true`.
- Wrapper e entrada de aplicativo usam `QT_STYLE_OVERRIDE=kvantum`.

A propriedade foi confirmada no executável local por
`/usr/bin/konsole --list-profile-properties` e no [código oficial dessa
versão](https://github.com/KDE/konsole/blob/v26.08.2/src/profile/Profile.cpp).
O perfil não define explicitamente BlinkingCursorEnabled, CursorShape ou
CustomCursorColor: seus valores permanecem herdados do perfil FALLBACK.
Não foi inventada uma configuração adicional de piscada ou cor de cursor.

## Reproduzir no destino

```bash
sudo pacman -S --needed konsole kvantum ttf-jetbrains-mono-nerd
cd "$HOME/ricy-kit/contributions/konsole-animated-cursor"
python aplicar.py
```

Execute como usuário do desktop, sem sudo. O script confere se o Konsole do
destino reconhece a opção de animação antes de alterar preferências. Instala
somente perfil/paleta, wrapper e launcher; mescla DefaultProfile e MenuBar em
konsolerc, preservando outras chaves e grupos. Os archives anteriores e
ausências são guardados em pasta privada 0700 sob
`$HOME/.local/state/ricy-konsole-backups/DATA-HORA/`.

Feche e abra o Konsole para carregar as configurações. Na próxima instalação,
o shell vem do usuário de destino; o perfil não fixa usuário, diretório,
comando de inicialização ou histórico. O blur também depende do compositor.
O restante do Ricy já inclui Kvantum e a fonte necessária.

## Conferir e restaurar

```bash
kreadconfig6 --file konsolerc --group 'Desktop Entry' --key DefaultProfile
kreadconfig6 --file "$HOME/.local/share/konsole/PlasmaBlur.profile" --group 'Terminal Features' --key AnimatingCursorEnabled
/usr/bin/konsole --profile PlasmaBlur
```

O resultado esperado dos dois primeiros comandos é `PlasmaBlur.profile` e
`true`. Para desfazer, use o backup impresso pelo aplicador:

```bash
python aplicar.py --restaurar "$HOME/.local/state/ricy-konsole-backups/DATA-HORA"
```

A reversão repõe os archives afetados e remove os que antes não existiam.
Pode substituir edições posteriores nesses archives; não remove o Konsole.

Verificação: suporte da opção no executável instalado, cópia exata do perfil
e paleta ativos, sintaxe Python/desktop/Bash e aplicação/restauração em HOME
descartável, preservando outras preferências. Não houve alteração de janelas
ou configurações do Konsole em uso, nem teste visual novo da animação.
