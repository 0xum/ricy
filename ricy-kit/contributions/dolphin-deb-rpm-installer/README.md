# Dolphin: instalador local DEB/RPM no CachyOS

Esta contribuição é uma cópia de reprodução do instalador criado nesta sessão,
não uma ferramenta oficial do CachyOS. Abra um pacote no Dolphin: a janela
prepara a conversão, apresenta os metadados e oferece **Instalar**. O botão
chama `pkexec /usr/bin/pacman -U --noconfirm`; a confirmação é o próprio botão
e o Polkit pede autenticação. Não usa `dpkg -i` nem `rpm -i`.

## Instalação no destino

Use CachyOS x86_64 com KDE Plasma, Python 3.14 observado, Qt 6 e agente Polkit
da sessão. As versões exatas observadas estão em `versoes-observadas.txt`;
não são versões obrigatórias para sistemas futuros. Faça os comandos em Bash.
Execute os scripts de integração como o usuário do desktop, sem sudo.

Confira os hashes do kit antes de preparar:

```bash
cd "$HOME/Projects/ricy/ricy-kit"
sha256sum -c SHA256SUMS
```

Antes de instalar dependências, gere um registro dos pacotes DO DESTINO:

```bash
umask 077
backup_pacotes=$(mktemp -d "$HOME/ricy-pacotes-antes-XXXXXXXX")
pacman -Q > "$backup_pacotes/pacotes.txt"
pacman -Qqe > "$backup_pacotes/explicitos.txt"
printf '%s\n' "$backup_pacotes"
sudo pacman -Syu
sudo pacman -S --needed dpkg rpm-tools binutils fakeroot pkgfile namcap python-pyqt6 desktop-file-utils
```

`bash`, `pacman`, `python`, `libarchive` (bsdtar), `zstd`, `curl`, `gawk`, `grep`,
`sed`, `coreutils`, `tar`, `gzip`, `binutils`, `fakeroot`, `pkgfile`, `namcap`
são usados pelo conversor. Polkit fornece pkexec e KDE fornece kbuildsycoca6.
Git/base-devel são usados apenas para construir o pacote AUR abaixo.

Instale o Debtap pelo AUR, após ler seu PKGBUILD e o arquivo de instalação:

```bash
sudo pacman -S --needed git base-devel
build_debtap=$(mktemp -d "$HOME/debtap-build-XXXXXXXX")
git clone https://aur.archlinux.org/debtap.git "$build_debtap/debtap"
cd "$build_debtap/debtap"
cat PKGBUILD debtap.install
makepkg --verifysource
makepkg -si
```

Nesta sessão foi construído `debtap 3.6.3-1`, fontes com SHA-512 verificado.
O AUR pode mudar: os scripts distribuídos incluem a cópia local da versão 3.6.3
com as correções aplicadas, mas a atualização da base continua necessária.

```bash
# Inicialização da base: downloads de índices Debian/Ubuntu/AUR, cerca de
# 1,1 GiB descompactado observado em /var/cache/debtap nesta máquina.
# IPv4 e limites de espera resolvem o bloqueio observado no acesso ao Ubuntu.
sudo bash -c 'curl() { /usr/bin/curl -4 --connect-timeout 15 --max-time 180 "$@"; }; export -f curl; /usr/bin/debtap -u'
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-deb-rpm-installer"
python instalar-integracao.py
```

A base do upstream usa URLs HTTP e `curl -k`, como no código original;
o wrapper de IPv4/timeout não corrige esse comportamento. Requer acesso à
rede. A cópia `app/debtap` usa a base de `/var/cache/debtap` e `/var/cache/pkgfile`.

O preparador cria backup local com diretório 0700 em
`$HOME/.local/state/cachyos-package-installer-backups/<data-hora>/`, incluindo
archives anteriores, ausências, defaults MIME e lista de pacotes. Não reutilize
backups de outro usuário. Uma nova execução cria um novo backup, sem apagar os
anteriores. O script substitui seus próprios scripts e duas entradas de desktop;
ajusta apenas os três defaults solicitados, mantendo os demais valores MIME.

Arquivos finais:

- `$HOME/.local/share/cachyos-package-installer/{backend.py,installer.py,normalize_control.py,debtap}`.
- `$HOME/.local/share/applications/cachyos-local-package-installer.desktop`.
- `$HOME/.local/share/kio/servicemenus/cachyos-install-package.desktop`, executável.
- `$HOME/.config/mimeapps.list`: `application/vnd.debian.binary-package`,
  `application/x-debian-package`, `application/x-rpm` apontam para
  `cachyos-local-package-installer.desktop`.
- Cache: `$HOME/.cache/cachyos-package-installer/conversion-*` e
  `last-conversion.log`. Conversões são serializadas por `conversion.lock`.
- Nenhum serviço, autostart, daemon, regra Polkit ou configuração do Fish
  foi criado. O shell Bash só é imposto aos processos do conversor.

Os modelos `.desktop.in` usam `@INSTALLER@`; o preparador escreve os caminhos
absolutos do usuário de destino com escape. O Debtap portável resolve o script
normalizador ao lado do próprio arquivo. O kit não contém nomes de usuário
da origem, backups pessoais, caches, logs de aplicativos ou executáveis Parsec.

## Conversão, limitações e correções

DEB é convertido pelo Debtap. `normalize_control.py` remove CRLF e desdobra
campos de dependências; identifica bibliotecas comuns pela ABI em `/usr/lib`
e pelo dono no pacman/pkgfile, escolhendo alternativas declaradas. Evita os
provedores privados do Proton e ferramentas de outra arquitetura observados
na tentativa do Parsec. Há mapeamento explícito para bibliotecas comuns e
libavcodec/libavformat/libavutil; ele não cobre todos os nomes Debian.
Versões Debian com epoch/revision são comparadas pelo upstream, com `vercmp`;
somente limites `>=`/`>>` são aceitos para esse mapeamento. Isso é uma heurística,
não uma equivalência universal entre versões de distribuições.

RPM é consultado com rpmdb temporária local, extraído por rpm2archive para
arquivo binário e por tarfile com filtro `data`; gera DEB intermediário e usa
o mesmo fluxo. RPMs com scriptlets/gatilhos são recusados, sem ignorá-los.
Dependências de archives precisam de um provedor identificado; outras
dependências complexas e arquiteturas incompatíveis são recusadas. A captura
binária evita mostrar bytes gzip como texto. Conversão ocorre sem root.

`app/debtap` preserva copyright e licença GPL-2.0; licença completa incluída.
`debtap-alteracoes.patch` descreve diferenças contra `/usr/bin/debtap 3.6.3`:
regex dos índices pkgfile atuais, normalizador, resolução nativa, tamanho
sem pressupor diretórios de 4096 bytes no Btrfs, intervalo de `cut`, Bash
explícito no fakeroot e verificação de falhas de tar/zstd. TERM=dumb evita
avisos tput. A versão `/usr/bin/debtap` não é sobrescrita.

**Pendência observada:** `pacman -Qkk parsec` relatou UID/GID divergentes em
15 entradas do pacote instalado, embora não tenha relatado divergência de
conteúdo nessa execução. As correções atuais não normalizam explicitamente
UID/GID em tar/mtree. O kit preserva esse estado, sem afirmar que está resolvido.
Antes de ampliar uso, audite o pacote gerado e seus metadados de ownership.
Não corrigimos essa pendência durante a documentação, conforme solicitado.

Não há garantia para todos os pacotes, scripts Debian, dependências dinâmicas
carregadas via dlopen ou configurações da distribuição de origem. Pacman -Up
confere resolução/arquitetura mas não comprova que o programa funciona nem
substitui a verificação de conflitos no momento da instalação. Conversões
nunca usam `--nodeps` ou `--overwrite`. Atualizações de aplicativos convertidos
exigem novos archives; não acompanham repositórios Debian/Fedora automaticamente.

## Verificação no destino (a executar)

```bash
python -c 'from PyQt6.QtWidgets import QApplication; print("PyQt6 disponível")'
gio mime application/vnd.debian.binary-package
gio mime application/x-rpm
desktop-file-validate "$HOME/.local/share/applications/cachyos-local-package-installer.desktop"
```

Abra um DEB confiável no Dolphin; deve chegar a **Instalar**, apresentando
metadados nativos. Antes de confirmar, confira nome, versão e dependências.
Para RPM com scripts, espere uma recusa explicativa. Depois da instalação,
`pacman -Q nome`, `pacman -Qkk nome` e abertura do app são verificações separadas.
Para inspecionar sem instalar: `pacman -Qip arquivo.pkg.tar.zst`,
`pacman -Up arquivo.pkg.tar.zst`, `bsdtar -tvf arquivo.pkg.tar.zst` e
`bsdtar -xOf arquivo.pkg.tar.zst .PKGINFO`.

Testes realmente realizados na origem: sintaxe Python/Bash, desktop-file,
GUI offscreen, DEB/RPM mínimos de teste sem instalar, recusa de RPM com
scriptlet, Parsec real reproduzido em ambiente Fish/TERM ausente chegando ao
botão Instalar sem erros tput/cut e sem Proton/cross compiler; verificação de
MIME defaults e hash do arquivo Parsec. A instalação posterior é confirmada
no estado atual/pacman.log, não uma nova instalação feita para documentar.
Não há confirmação neste chat de streaming/login do Parsec ou migração real
em outra máquina. Os scripts novos de instalação/restauração foram validados
estaticamente, não executados sobre a sessão atual.

## Desfazer no destino

Feche o instalador após concluir a operação. Use o caminho impresso pelo
preparador (os backups anteriores são mantidos):

```bash
cd "$HOME/Projects/ricy/ricy-kit/contributions/dolphin-deb-rpm-installer"
python restaurar-integracao.py "$HOME/.local/state/cachyos-package-installer-backups/<data-hora>"
```

Isso restaura archives completos do backup e remove alvos que antes não
existiam, atualizando caches KDE. Pode substituir outras edições posteriores
nesses archives MIME; revise o backup se quiser restaurar só as três entradas.
Não remove pacotes, apps convertidos, cache ou backup. Sem backup, voltar ao
Ark é possível se ele estiver instalado:

```bash
xdg-mime default org.kde.ark.desktop application/vnd.debian.binary-package
xdg-mime default org.kde.ark.desktop application/x-debian-package
xdg-mime default org.kde.ark.desktop application/x-rpm
```

Aplicativos convertidos são removidos pelo pacman, por exemplo `sudo pacman -R parsec`.
Consulte o registro de pacotes antes da mudança para remover somente o que foi
adicionado e não é usado por outros programas. Não remova automaticamente
binutils/fakeroot/pkgfile/Python/Qt: alguns já existiam ou agora são compartilhados.
`sudo pacman -Rns dpkg rpm-tools debtap namcap` é uma possibilidade apenas se
esses pacotes foram adicionados no destino e não forem mais necessários;
revise a transação. Não execute isso indiscriminadamente.
O cache do conversor pode ser apagado depois de fechar a janela; isso perde
os archives convertidos e logs. `/var/cache/debtap` permanece mesmo após
remover debtap, e pode ser removido manualmente se não houver outros usuários
do conversor. Índices `/var/cache/pkgfile` são compartilhados e devem ser mantidos.

## Histórico resumido

Primeiro foram instaladas ferramentas de terminal, interpretação incompleta
do pedido de duplo clique. Discover/PackageKit, Alien e rpmtoarch foram
consultados, mas não instalados. A implementação final é local PyQt6.
A primeira atualização debtap ficou presa no Ubuntu; foi interrompida e
repetida com IPv4/timeout. Os primeiros testes mínimos não cobriram Fish,
CRLF ou dependências do Parsec; falhas reais motivaram as correções incluídas.
Nenhum dos pacotes de teste foi instalado. Scripts/materiais de investigação
permanecem na origem em `~/.cache/package-support`, mas não são necessários
ao kit e não foram copiados.
