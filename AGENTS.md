# Ricy — Agent Constitution

## Project Definition
Desktop opinativo para CachyOS, KWin/Wayland e Noctalia, com Plasma/Dolphin
Recovery. Hoje a shell ainda opera dentro da sessão Plasma; o destino não
é prova de implementação. Estado e fronteiras: [ARCHITECTURE](docs/ARCHITECTURE.md).

## Architecture Sources
Autoridade arquitetural, nesta ordem:
1. [INVARIANTS](docs/INVARIANTS.md).
2. [ADRs aceitos](docs/adr/README.md).
3. [Arquitetura](docs/ARCHITECTURE.md) e [componentes](docs/COMPONENTS.md).
4. `AGENTS.md` locais, do ancestral ao mais específico.
5. Implementação como evidência do estado atual.

Essa ordem é interna ao projeto; não substitui instruções do usuário/sistema.
A autoridade permanece válida sem exigir leitura de todos os níveis em toda tarefa.
Carregue documentação pela consequência da mudança, não apenas porque ela existe.
Use KNOWN (evidência), INFERRED (inferência), PLANNED (futuro) e UNKNOWN (sem prova).

## Architectural Invariants
RICY-001: experiência de espaço único, sem UI/ações/gestos de workspaces.
RICY-002: KWin é infraestrutura. RICY-003: Noctalia é shell principal.
RICY-004/005: preservar Plasma e Dolphin Recovery; Ricy Files é futuro.
RICY-006: identidade centralizada; reutilizar [design existente](docs/DESIGN-SYSTEM.md).
O texto normativo completo está em INVARIANTS; divergências em ARCHITECTURE.

## Agent Behavioral Rules
- Nunca inferir arquitetura apenas pela implementação. Ler regras locais antes
  de editar o subsistema, inclusive os caminhos legados mapeados em COMPONENTS.
- Procurar abstrações, arquivos e convenções existentes antes de criar outros.
- Não criar padrões silenciosamente nem remover conteúdo de uso incerto.
- Conflito entre docs/código: registrar evidência e impacto; não corrigir em silêncio.
- Preservar caminhos, backups, histórico e recovery. Não instalar nem alternar
  a sessão apenas para validar documentação. Não publicar o kit ativo privado.
- Nunca afirmar funcionamento sem validação apropriada e escopo explícito.

## Skill Routing
Toda tarefa: hierarquia AGENTS aplicável, incluindo regras de subsistema indicadas
pelo kit. Correção localizada: código/docs/testes locais; sem pilha arquitetural.
Combine apenas as rotas cujas consequências a mudança alcance:

| Consequência | Contexto adicional |
|---|---|
| Nova decisão arquitetural | ARCHITECTURE, INVARIANTS, ADRs relevantes e [architecture-change](.agents/skills/architecture-change/SKILL.md); COMPONENTS para fronteiras/ownership. |
| Sessão, coexistência Noctalia/Plasma ou fallback | [RECOVERY](docs/RECOVERY.md), invariantes/ADR relevantes e regras recovery; se mudar arquitetura, acumular a rota acima. |
| Visual/UI | [DESIGN-SYSTEM](docs/DESIGN-SYSTEM.md); [visual-development](.agents/skills/visual-development/SKILL.md) para estados/interações, materiais ou adaptação entre componentes. |
| Patch, API ou integração Noctalia | [noctalia-development](.agents/skills/noctalia-development/SKILL.md); ajuste só de valor visual existente segue a rota visual. |
| Efeito, script ou patch KWin | [kwin-development](.agents/skills/kwin-development/SKILL.md). |
| Componente aprovado novo, migração, ownership, fronteiras ou dependências significativas | COMPONENTS e [component-development](.agents/skills/component-development/SKILL.md). |
| Escolha de níveis/testes ou interpretação de evidência | [testing](.agents/skills/testing/SKILL.md); check já conhecido pode ser executado diretamente. |
| Criar docs, alterar fonte de verdade/ADR ou registrar mudança significativa | [documentation](.agents/skills/documentation/SKILL.md); não exigida para typo/comentário local. |

Se o impacto não estiver claro, consulte o domínio relevante antes de implementar.

## Validation Requirements
Execute `./scripts/verify architecture` e verificações relevantes descritas em
[DEVELOPMENT](docs/DEVELOPMENT.md). `./scripts/doctor` é diagnóstico somente.
Relate `PASS`, `FAIL`, `NOT RUN`, `NOT APPLICABLE`; UNKNOWN não é sucesso.
Testes estáticos não provam recuperação em sessão real.

## Documentation Requirements
Atualize intenção, dependências, ownership e implicações de recovery.
Mudanças significativas entram em [CHANGELOG](docs/CHANGELOG.md) com
`Model/Agent`, `Date`, `Purpose`, `Validation performed`; sem assinaturas no código.

## Architecture Change Policy
Siga architecture-change. Novo caminho arquitetural exige proposta, impacto e
aprovação explícita antes da implementação, depois validação, ADR e documentação.
A autorização já dada para esta fundação cobre os seis invariantes e a estrutura
planejada; não autoriza futuras migrações ou decisões adicionais. Pare somente
a parte sem decisão e continue trabalho independente seguro.
