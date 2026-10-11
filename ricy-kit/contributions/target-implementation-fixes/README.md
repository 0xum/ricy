# Correções verificadas na implementação do destino

Esta contribuição complementa os archives históricos sem substituir suas cópias
no kit distribuído. Foi aplicada à cópia ativa em `$HOME/Projects/ricy/ricy-kit`.

## Aplicar antes de preparar outro destino

Na raiz do kit, confira os hashes e então aplique as correções:

```bash
sha256sum -c SHA256SUMS
python contributions/target-implementation-fixes/aplicar-correcoes.py
```

O aplicador valida todos os archives antes de escrever. Aceita somente a versão
original ou a versão corrigida; repetir a aplicação é permitido. Depois de
aplicar, os hashes originais dos dois archives alterados deixam de corresponder
ao pacote, como já acontece com os `.desktop` após preparar o destino.

Continue pelo README de `noctalia-kde-integration-and-menus` e pelo README de
`dolphin-deb-rpm-installer`. Use somente a contribuição Noctalia indicada:
a cópia antiga em `outputs/` da raiz não recebe estas correções.

## Mudanças

- `configurar-super.py`: chama `doRegister` e `setShortcut` antes de
  `setForeignShortcut`. No destino, a chamada estrangeira sozinha não registrava
  Super. Foram verificados os registros de Super e Super+Espaço, a abertura do
  launcher e o ciclo de restauração/reinício.
- `debtap`: gera `.MTREE` com UID/GID zero, inclui `.INSTALL` somente quando
  existe, interrompe em erro de geração e grava o arquivo final com ownership
  numérico zero. Exclui `namcap-*` e `pkgbuildinstallations*` do pacote, do mtree
  e do cálculo de tamanho. DEB e RPM de teste foram convertidos, instalados,
  conferidos por `pacman -Qkk` (zero archives alterados) e removidos.
- `atualizar-indices.sh`: wrapper para executar o Debtap instalado com IPv4,
  limites de conexão/tempo, retries, TLS verificado e URLs HTTPS dos índices
  Debian/Ubuntu. Verifica que todos os índices necessários são não vazios após
  o comando. Não altera `/usr/bin/debtap`.

Depois de instalar o pacote AUR Debtap, atualize os índices:

```bash
sudo bash contributions/target-implementation-fixes/atualizar-indices.sh
```

O teste de interface chegou ao botão **Instalar** com `SHELL=fish` e `TERM`
ausente, sem clicar no botão. RPM com scriptlet foi recusado. Isso não demonstra
compatibilidade universal de pacotes externos. Não foi instalado Parsec nesta
implementação; seu binário não faz parte do kit.

As cópias completas corrigidas e seus diffs estão nesta pasta. Código Debtap de
George Savvidis, GPL-2.0 ou posterior, licença preservada. O conteúdo das bases
continua dependendo dos servidores externos e da heurística do upstream.
