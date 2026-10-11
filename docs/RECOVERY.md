# Recovery

## Contrato e estado
Primary Session (TARGET / PLANNED): **Ricy + Noctalia**.
Recovery Session (TARGET / PLANNED): **Plasma + Dolphin** e ferramentas KDE.
Princípio: recovery deve ter tão poucas dependências de componentes específicos
Ricy quanto razoavelmente possível. Leia [ADR-0002](adr/0002-plasma-recovery.md).

CURRENT / KNOWN: a alternância ocorre dentro de Plasma Wayland. Plasmashell
continua responsável pelo wallpaper/desktop; a volta usa scripts Ricy,
systemd de usuário, D-Bus, KGlobalAccel e snapshots de painéis/atalhos.
Não existe isolamento comprovado contra falha de KWin, login ou scripts Ricy.

## Retorno existente — sessão acessível
No terminal da própria sessão, como o usuário do desktop, a partir da raiz:

```bash
./voltar.sh
# Alternativa instalada pelo kit:
ricy plasma
```

Execute uma alternativa, não ambas por rotina. Esses comandos **mudam** a sessão:
desabilitam a integração Noctalia no login, encerram shell/adaptador e restauram
painéis, atalhos e KRunner. Plasmashell pode reiniciar brevemente. KWin e apps
são preservados pela intenção do código; a tarefa de fundação não testa a troca.
[Comando](../ricy-kit/contributions/plasma-noctalia-switching/ricy) e
[implementação](../ricy-kit/contributions/plasma-noctalia-switching/integracao.py)
são as evidências. Wrappers raiz atuais usam caminho absoluto desta instalação.

Diagnóstico somente leitura:
```bash
./scripts/doctor
systemctl --user is-active plasma-plasmashell.service
journalctl --user -u ricy-noctalia-integracao.service
```

Serviço ativo não garante painéis visíveis, login ou Dolphin funcional.
`ricy status` retorna Plasma quando a unidade Noctalia não está ativa, inclusive
em falhas: não usar esse resultado isolado como prova de recovery.

## Falhas e dependências críticas
| Ponto | Comportamento conhecido / limite |
|---|---|
| Config Noctalia inválida | Integração valida antes de recolher painéis; falhas nessa etapa não comprovam recovery de toda a sessão. |
| Shell/adaptador falha durante a troca | Bloco protegido de `start()` chama `restore()`; comando desabilita preferência se restart falhar. Nem toda exceção fica no bloco protegido. |
| Shell cai depois da troca | Unidades têm política de reinício; UNKNOWN: fallback garantido após falha persistente. |
| Snapshot ausente/corrompido ou D-Bus indisponível | Retorno pode falhar; manter backups e investigar erro, não sobrescrever layout por suposição. |
| Falha KWin/login/sessão de usuário | UNKNOWN: roteiro independente ainda não validado. Sessão de recovery desacoplada é PLANNED. |
| Dolphin personalizado / plugin incompatível | Há launcher, QSS, plugin Qt e efeito KWin; consultar restauradores das contribuições, não remover Dolphin. |

Snapshots atuais ficam em `${XDG_STATE_HOME:-$HOME/.local/state}/ricy-alternancia/`.
O instalador documenta backups e restauração em
[plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md).
O seed histórico `plasma-antes.tar.gz` não deve ser substituído. Não restaurar
archives completos antigos para alternar: poderiam sobrescrever wallpaper/widgets.
Para Dolphin, consultar [identidade](../ricy-kit/contributions/dolphin-noctalia-identity/README.md)
e [plugins](../ricy-kit/contributions/dolphin-blur-corners/README.md).
Não inventar caminhos de backup; usar o caminho emitido pelo instalador real.

## Superfícies protegidas
Pacotes Plasma/Dolphin, KWin e ABI de plugins, display manager, units/targets,
D-Bus, KGlobalAccel, atalhos, appletsrc/plasmashellrc, defaults MIME/FileManager1,
launchers e backups exigem análise explícita de recovery antes de mudanças.
O teste `./scripts/verify recovery` cobre merge de painéis em memória; não
abre janelas, não altera a sessão e não comprova recovery end-to-end.
Um ensaio posterior deve conferir painéis/atalhos, Dolphin, System Settings,
apps abertos e login, com backup e plano de retorno.
