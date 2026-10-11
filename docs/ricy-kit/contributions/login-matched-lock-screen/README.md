# Bloqueio com a apresentação do login

Contribuição para Plasma 6.7 e o login local `mocha-limine`. Usa o wallpaper
configurado no SDDM, relógio, usuário e campo de senha dos mesmos componentes
Breeze. O formulário aparece imediatamente e permanece visível por um minuto,
como no login. Controles de mídia ficam desativados e o campo de senha não
exibe o botão de revelar senha, seguindo o tema de login.

```bash
python aplicar.py
```

A adaptação copia somente o bloqueio do KDE instalado para um pacote local de
mesmo ID. Os demais componentes do shell apontam para os archives do sistema.
Autenticação, sincronização da senha, biometria, teclado virtual e tratamento
de erros continuam usando a implementação nativa. O SDDM não é modificado.
O script interrompe antes de escrever caso exista outro shell local ou o QML
tenha mudado. Após atualizar o Plasma, reaplique para usar seu bloqueio novo.

O backup privado fica em `~/.local/state/ricy-lockscreen-backups/`. Para voltar:

```bash
python restaurar.py /caminho/do/backup/informado
```

Prévia sem bloquear a sessão: `/usr/lib/kscreenlocker_greet --testing`.
Na sessão normal, a mudança vale no próximo bloqueio. Botões de sessão
permanecem apropriados para uma sessão já aberta; não se oferece desligamento
ou escolha de sessão do SDDM dentro do bloqueio.

Scripts desta contribuição: MIT. Os QML gerados mantêm seus avisos de licença
originais do KDE (GPL-2.0-or-later / LGPL-2.0-or-later).

## Correção da inicialização da autenticação (08/10/2026)

O campo fica visível por uma transição de `uiVisible` após a montagem do QML
(`Qt.callLater`), preservando o estado inicial `false` do KDE. Inicializar
diretamente com `true` impedia o disparo de `onUiVisibleChanged`, que inicia
a autenticação; o formulário aparecia, mas a senha não era processada.

A regressão foi reproduzida em cópia temporária da versão anterior: nenhum
início de autenticação e timeout. A versão corrigida passou pelo formulário
nativo até o PAM real (`kde`): resultado 0 / Success e saída do greeter.
Foram exercitados os modos imediato e com tolerância de 1200 ms, em
`--testing`, com renderização offscreen, sem bloquear a sessão. A senha
foi fornecida apenas por um descritor em memória, sem entrar no kit ou logs.
