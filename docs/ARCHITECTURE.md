# Arquitetura do Ricy

## Evidência e autoridade
Snapshot da investigação: 2026-10-11. **KNOWN**: confirmado em arquivo/script
citado, não necessariamente revalidado em runtime. **INFERRED**: conclusão
razoável da evidência. **PLANNED**: decisão aceita ainda não implementada.
**UNKNOWN**: evidência insuficiente; não completar lacunas por plausibilidade.

[Invariantes](INVARIANTS.md) → [ADRs](adr/README.md) → arquitetura/componentes →
regras locais → implementação. Em conflito, registrar a divergência e seu escopo.

## CURRENT — KNOWN
[README anterior e histórico](ricy.md) e os wrappers `iniciar.sh`, `voltar.sh`,
`alternar.sh` apontam para `ricy-kit/contributions/plasma-noctalia-switching/ricy`.
`ricy-kit/` é o kit ativo; `docs/ricy-kit/` é a cópia de transporte preservada,
não um espelho automaticamente sincronizado. `archives/ricy.zip` é histórico.
Nenhum `.git` foi encontrado na raiz durante a investigação; não há histórico
versionado local confirmado. Esta etapa não inicializa Git nem publica arquivos.

```text
CachyOS / sessão Plasma Wayland
└── KWin (composição e janelas)
    ├── plasmashell (desktop/wallpaper compartilhados)
    ├── Noctalia + adaptador de busca + integração Ricy
    │   └── painéis Plasma recolhidos após a shell ficar pronta
    └── retorno Plasma: painéis/atalhos/KRunner restaurados
```

Evidência: [integração](../ricy-kit/contributions/plasma-noctalia-switching/integracao.py),
[autostart](../ricy-kit/contributions/noctalia-autostart/README.md) e
[comando de alternância](../ricy-kit/contributions/plasma-noctalia-switching/ricy).
A alternância muda a shell dentro da sessão existente, não troca compositor.
O helper de status observa uma unidade systemd; não comprova saúde da sessão.

## TARGET — PLANNED
```text
CachyOS
└── KWin / Wayland
    ├── Ricy Desktop
    │   ├── Noctalia Shell
    │   ├── Ricy Core / Services (responsabilidades ainda a definir)
    │   └── Ricy Files e futuras aplicações
    └── Plasma Recovery
        └── plasmashell, Dolphin, System Settings e ferramentas KDE
```

A divisão em `core/`, `shell/noctalia/`, `compositor/kwin/`, `apps/file-manager/`,
`services/`, `themes/`, `integrations/`, `recovery/plasma/`, `installer/` e `tools/`
é uma reserva documental. Os executáveis continuam nos locais atuais.
Novos contratos de Core/Services, IPC e sessão dedicada são UNKNOWN, não APIs
implicitamente aprovadas. Ver [migração](MIGRATION-PLAN.md).

## Ownership e fronteiras
- **UPSTREAM**: Noctalia, KWin, Plasma, Dolphin, Qt, Kvantum e temas de terceiros.
- **PATCHES**: diffs Noctalia cumulativos e blur KWin; preservar versão, commit,
  licenças, build e reversão junto ao patch. As variantes antigas são histórico.
- **RICY-OWNED**: scripts de integração/alternância, adaptadores e políticas
  locais. Ownership de manutenção não elimina licenças de código derivado KDE.
- **PLANNED RICY-OWNED**: Ricy Files. Não há aplicação implementada nesta fundação.

As fontes upstream são obtidas pelos compiladores em caches externos ao projeto.
[app-icon-reordering/compilar.sh](../ricy-kit/contributions/app-icon-reordering/compilar.sh)
fixa Noctalia 5.2.1/commit `6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4`;
[blur-continuity/compilar.py](../ricy-kit/contributions/blur-continuity/compilar.py)
fixa KWin 6.7.5/commit `ab7df7ccb7c6af20f4b279cd6220f7cd3d2267d7`.
São bases do kit, não afirmações sobre as versões upstream mais recentes.

## Divergências registradas — não resolvidas nesta etapa
| ID | Evidência atual | Consequência / tratamento |
|---|---|---|
| C-001 | Config taskbar contém `only_active_workspace=true`; patches retêm grupos/badges upstream; identidade menciona workspaces | RICY-001 é normativo. UNKNOWN: exposição efetiva em todos os menus, atalhos e gestos. Auditar e remover exposição em tarefa própria; o identificador KWin `workspace` não é por si só multi-desktop. |
| C-002 | `integracao.py` usa plasmashell/wallpaper e recupera via scripts Ricy | Recovery separado e independente é PLANNED. Não alegar isolamento já obtido. |
| C-003 | Launcher e integração FileManager1 usam Dolphin personalizado | Preservar até existir Ricy Files validado; não trocar MIME/defaults nesta etapa. |
| C-004 | Tokens existem, mas configs/QSS/scripts também contêm valores | Referenciar tokens existentes; consumo central automático é PLANNED. |
| C-005 | Duas árvores de kit e caminhos absolutos nos wrappers | INFERRED: mover diretórios pode quebrar unidades e atalhos. Manter e mapear referências antes de migrar. |

UNKNOWN: recuperação após falha completa do login/compositor, conformidade de
workspaces da sessão inteira, portabilidade integral e prontidão para publicação.
Os testes históricos em READMEs são evidência histórica, não testes desta tarefa.

## Navegação por necessidade
[Componentes](COMPONENTS.md), [design](DESIGN-SYSTEM.md),
[desenvolvimento](DEVELOPMENT.md), [recovery](RECOVERY.md),
[índice de evidências](../.agents/references/README.md).
