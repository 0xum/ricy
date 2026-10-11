# Migração incremental

## Current structure — KNOWN
- Raiz: README e wrappers com caminhos absolutos para o kit ativo.
- `ricy-kit/`: contribuições, outputs/scripts, manifests e materiais da instalação.
- `docs/ricy-kit/`: variante transportável preservada; não é espelho automático.
- `docs/ricy.md`, `REINSTALAR.md`, `IDENTIDADE-VISUAL.md`: história e referências.
- `archives/ricy.zip`: arquivo original preservado. Nenhum histórico Git confirmado.

Fontes e dependências por contribuição estão em [COMPONENTS](COMPONENTS.md).
A fundação criou diretórios documentais e validadores; não realocou runtime.

## Target structure — PLANNED
| Atual | Destino esperado | Condição antes da migração |
|---|---|---|
| Patches Noctalia e perfil público | shell/noctalia/ | Identificar variante cumulativa e consumidores; não transportar perfil privado |
| Blur/ricywindowactions/cantos | compositor/kwin/ | Preservar versão/ABI, licenças, build/instalação/reversão |
| Tokens e assets de temas | themes/ e themes/tokens/ | Definir migração dos consumidores mantendo valores e aparência |
| Adaptador busca/atalhos/KDE/Dolphin | integrations/kde/ | Mapear D-Bus, units, desktops e paths nos dois kits |
| Units de autostart e integração | services/ | Preservar ordem/prontidão, nomes e política de retorno |
| Alternância e snapshots | recovery/plasma/ | Validar restore e reduzir dependência Ricy sem perder painéis |
| Preparação/aplicadores | installer/ | Separar materiais públicos de backups/estado por allowlist |
| Driver AIC8800 | integrations/hardware/ | Manter opcional, pin/licenças e suporte de kernel |
| Wrappers/helpers comuns | core/ se justificado | Procurar duplicação real; não criar framework |
| Nenhuma aplicação Files atual | apps/file-manager/ | Nova proposta de implementação, toolkit/contratos aprovados |
| Verificações desta etapa | scripts/ | Manter offline; tools/ só para ferramentas necessárias |

## Safe migrations
Documentar fronteiras, acrescentar regras/links e testes somente leitura são
seguros nesta etapa. Consolidar referências pode preceder movimentação de fontes.
Mesmo uma mudança de caminho aparentemente simples exige busca de chamadores.
Antes de cada migração: inventário → referências → backup → mudança mínima →
validação apropriada → atualização de docs/manifests afetados → rollback claro.

## Risky migrations — não executadas
Renomear contributions/outputs; unificar os kits; mover perfis/snapshots; mudar
caminhos gravados em unidades, symlinks, desktop entries e wrappers; reorganizar
patches cumulativos; alterar ativadores; separar sessão Plasma/Noctalia; remover
Dolphin; trocar gerenciador de login. Exigem plano próprio e testes de recovery.
Não regenerar SHA256SUMS históricos para disfarçar divergências da instalação.

## Deprecated concepts — preservados como história
Os nomes `noctalia-teste.service`/`iniciar-teste.sh` não significam sessão temporária
hoje. “Transportar configuração” permanece útil para reprodução, mas não define
mais todo o produto. Compiladores cumulativos anteriores continuam históricos.
Workspaces herdados não definem a experiência futura. Nenhum arquivo foi removido
por aparentar obsolescência.

## Migration order
1. Auditar RICY-001 em configs, UI, menus, atalhos e gestos, distinguindo API KWin
   de exposição ao usuário; propor ajuste mínimo sem alterar fallback.
2. Inventariar referências e preparar baseline pública revisada: fontes/licenças,
   paths portáveis, ausência de dados privados; escolher versionamento antes de publicar.
3. Centralizar consumo de tokens, um componente por vez, com comparação visual.
4. Extrair patches/builds e integrações por componente com compatibilidade de paths.
5. Projetar isolamento de Plasma Recovery e só então uma sessão Ricy independente.
6. Propor implementação de Ricy Files mantendo Dolphin como recovery.

## Architecture Decisions Required — somente partes futuras bloqueadas

ARCHITECTURE DECISION REQUIRED

**Problem:** como separar a futura sessão Ricy sem perder wallpaper/desktop e a
recuperação que hoje dependem de plasmashell e scripts Ricy?

**Evidence:** `plasma-noctalia-switching/integracao.py` mantém plasmashell,
usa D-Bus/KGlobalAccel e lê snapshots Ricy ao restaurar. Ver
[ARCHITECTURE C-002](ARCHITECTURE.md) e [RECOVERY](RECOVERY.md).

**Options:** A. conservar a integração atual enquanto se especifica e testa uma
rota independente; B. criar sessões dedicadas e definir ownership de wallpaper,
login e recuperação antes de migrar.

**Recommended:** A nesta fundação; elaborar proposta comparativa antes de B.

**Impact:** units, login, wallpaper, atalhos, compositor e retorno após crash.
A separação runtime fica PLANNED e não é implementada sem aprovação explícita.
A reserva documental já solicitada continua válida e independente dessa decisão.
