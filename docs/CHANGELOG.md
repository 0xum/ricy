# Registro técnico de mudanças

Registre mudanças significativas em entradas curtas. Campos mínimos:
Model/Agent, Date, Purpose, Validation performed. Não assinar arquivos de código.

## 2026-10-11 — Baseline Git local

- **Model/Agent:** Codex (GPT-6), agente desta tarefa.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** estabelecer baseline Git auditável em `main`, com seleção explícita
  de fontes e assets, sem remote, publicação, reorganização ou mudança de runtime.
- **Changes:** `.gitignore` conservador, registro em [GIT-BASELINE](GIT-BASELINE.md)
  e atualização do estado Git em DEVELOPMENT. Seleção de 1.098 arquivos;
  1.939 arquivos locais excluídos do índice, preservados no disco. Backups,
  clipboard, histórico de notificações, perfil/work, bytecode e ZIP com estado
  privado não entram no baseline. Templates, patches, evidências e assets ficam.
- **Validation performed:** PASS `./scripts/verify architecture` (52 arquivos
  obrigatórios e links locais); PASS `./scripts/verify all` (83 candidatos de
  sintaxe, 17 cenários Noctalia, capture/merge de painéis e 28 cenários KWin);
  PASS `python3 scripts/test-foundation.py` (17 cenários). Todos com exit 0.
  Busca heurística nos 1.098 arquivos staged, incluindo 244 SVGZ descomprimidos,
  sem credenciais evidentes. Índice sem gitlinks; permissões executáveis preservadas.
- **Preservation:** inventário inicial com SHA-256; nenhum arquivo preexistente
  removido ou com permissões alteradas. Apenas DEVELOPMENT e este CHANGELOG
  foram editados pela tarefa. O histórico de notificações privado mudou durante
  a sessão por atividade externa; não foi escrito, revertido ou versionado.
- **Limits:** NOT RUN sessão/recovery live; NOT APPLICABLE validação visual e
  instalação, pois não houve mudança de comportamento. Licenças, referências
  pessoais/de máquina e portabilidade ainda exigem revisão para publicação;
  o baseline local não certifica publicação segura integral.

## 2026-10-11 — Fundação agent-first

- **Model/Agent:** Codex (GPT-6), agente desta tarefa.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** formalizar arquitetura solicitada em torno dos kits existentes,
  com invariantes/ADRs, mapa de 24 contribuições, regras/skills progressivas,
  diagnóstico e verificações offline, sem migrar runtime ou alterar a sessão.
- **Changes:** AGENTS/CLAUDE, docs arquiteturais, reservas documentais, sete skills,
  regras locais, scripts/verify e scripts/doctor. README recebe entrada arquitetural;
  texto preexistente é preservado. Nenhum arquivo legado removido.
- **Validation performed:** `./scripts/verify architecture` e `./scripts/verify all`
  passaram (exit 0): estrutura/links, sintaxe de 83 arquivos do kit, 17 cenários
  Noctalia, regressões de capture/merge de painéis e 28 cenários KWin isolados.
  `python3 scripts/test-foundation.py`: 17 verificações comportamentais passaram.
  As sete skills passaram em `skill-creator/scripts/quick_validate.py`, usando
  ambiente virtual temporário com PyYAML 6.0.3, sem dependência nova no runtime.
  `./scripts/doctor`: exit 2 esperado, duas informações UNKNOWN (recovery live e
  conformidade integral RICY-001); consultas de pacotes/unidades concluídas.
  O primeiro quick_validate não rodou no Python do sistema por falta de PyYAML;
  foi repetido com sucesso no ambiente isolado.
- **Limits:** não testar login, alternância ou crash recovery nesta alteração
  documental. C-001 a C-005 são divergências registradas, não correções de runtime.

- **Preservation check:** 51 arquivos novos; README foi o único arquivo
  preexistente editado pela tarefa, preservando integralmente seu texto anterior.
  Comparação SHA-256 de 2.978 arquivos iniciais encontrou também mudança no
  `notification_history.json` do perfil ativo durante a sessão. Esse estado não
  foi escrito pela tarefa e não foi revertido. Os outros 2.976 arquivos mantiveram
  hash; nenhum arquivo preexistente removido ou com permissões alteradas.

## 2026-10-11 — Contexto por consequência

- **Model/Agent:** Codex (GPT-6), agente desta tarefa.
- **Date:** 2026-10-11 (America/Sao_Paulo).
- **Purpose:** reduzir leitura universal sem alterar autoridade ou aprovação
  de arquitetura. CLAUDE importa AGENTS; raiz/DEVELOPMENT/índice e roteadores
  locais carregam fontes conforme impacto. Skills component-development, testing,
  documentation, noctalia-development e visual-development têm gatilhos mais
  específicos; KWin mantém invariantes/recovery e consulta o mapa por domínio.
  DESIGN-SYSTEM condiciona apenas o acionamento da skill visual; valores e
  garantias visuais permanecem intactos.
- **Context before → after:** ajuste visual local antes encadeava arquitetura,
  invariantes, mapa e skills gerais; agora usa hierarquia AGENTS, DESIGN-SYSTEM e
  código/docs/testes locais. Nova arquitetura continua exigindo ARCHITECTURE,
  INVARIANTS, ADRs pertinentes, mapa das fronteiras e aprovação explícita.
- **Validation performed:** `./scripts/verify architecture` e `./scripts/verify all`
  passaram (exit 0); `python3 scripts/test-foundation.py` passou nos 17 cenários;
  as sete skills passaram em quick_validate.py no ambiente virtual já existente.
  Import `@AGENTS.md` conferido estaticamente; carregamento pelo Claude Code
  não foi executado. Testes de sessão/recovery live permanecem NOT RUN.
- **Runtime Changes:** None. Invariantes, ADRs, fontes de arquitetura/recovery,
  validadores e implementação preservados; nenhum arquivo novo ou removido.
