# Desenvolvimento orientado por agentes

## Entrada e fluxo
Siga a hierarquia aplicável e o roteamento por consequência em [AGENTS](../AGENTS.md).
Correção localizada começa no código, documentação e testes locais. Carregue docs
adicionais quando o impacto atingir seu domínio; a ordem de autoridade não é
uma lista universal de leitura. Se descobrir uma fronteira ou contrato afetado,
amplie o contexto antes de implementar. Comando de validação conhecido não exige
carregar a skill testing. Não execute instaladores para entender como funcionam.
No kit ativo, perfis, backups e estado são privados.

## Validações executáveis
Da raiz do projeto (ou usando caminho absoluto; os scripts resolvem sua raiz):

```bash
./scripts/verify architecture
./scripts/verify shell
./scripts/verify recovery
./scripts/verify all
./scripts/doctor
python3 scripts/test-foundation.py
```

`verify` usa Python 3.11+ e ferramentas existentes; não instala dependências.
- `architecture`: arquivos obrigatórios, skills/frontmatter, regras locais,
  links Markdown relativos da fundação e sintaxe dos novos scripts.
- `shell`: sintaxe Bash/Python/JSON/TOML nos sources do kit ativo (exclui
  work, outputs, backups e assets upstream); teste offline de ações Noctalia
  se existir fonte local compatível com commit/patch esperado e PyQt6.
- `recovery`: teste existente de capture/merge de painéis em memória; teste
  QJSEngine do efeito de janelas se PyQt6 existir. Não troca shell/compositor.
- `all`: agrega os anteriores; não significa certificação do desktop.
- `doctor`: diagnóstico somente leitura de ferramentas, pacotes via pacman,
  ambiente declarado, unidades e entrada Plasma Wayland. Nunca executa reparos.

`python3 scripts/test-foundation.py` exercita 17 cenários dos validadores em
fixture temporária, incluindo arquivos/links ausentes, erro de componente e
dependência indisponível. Não é executado recursivamente por verify.

Códigos de saída: verify 0 = checks executados passaram sem skips de dependência;
1 = alguma verificação falhou; 2 = algum check offline não pôde rodar, sem FAIL;
uso inválido também retorna 2. Ensaios live ficam sempre `NOT RUN`, fora do
escopo automático. Doctor: 0 = consultas concluídas; 2 = alguma informação
UNKNOWN; isso nunca significa desktop saudável. Nenhum comando recebe sudo.

A checagem de links cobre arquivos da fundação, README raiz e AGENTS locais,
sem percorrer todo o histórico, links externos ou validar âncoras de títulos.
Ela verifica destinos Markdown inline e referências de links; texto em blocos
de código não é link. Paths em código inline e symlinks runtime não são cobertos.
Documentos históricos preservados podem ter caminhos antigos.

## Níveis e evidência
| Nível | Quando é relevante | Limite |
|---|---|---|
| Static | Docs, regras, scripts/configs alterados | Parse/link não garante comportamento |
| Component | Lógica do componente | Rodar regressões locais apropriadas |
| Integration | Contratos D-Bus, unidades, perfil e KWin | Executar em ambiente preparado, com retorno |
| Recovery | Login, compositor, shell, defaults/arquivos | Offline não substitui ida/volta e login reais |
| Visual | Mudança de aparência/interação | Registrar captura/observação, monitores e escala |
| Environment | Dependências e versões | Presença de pacote não prova compatibilidade |

Use `PASS`, `FAIL`, `NOT RUN <motivo>` e `NOT APPLICABLE <motivo>` no relatório.
Não afirmar “This should work”, “Probably fixed” ou “Everything is working” sem
evidência. Resultados históricos devem ser atribuídos à sessão original.

## Mudanças e publicação futura
Use [CHANGELOG](CHANGELOG.md) para Model/Agent, Date, Purpose, Validation performed.
Mudança arquitetural não prevista segue
[architecture-change](../.agents/skills/architecture-change/SKILL.md).
A seleção do baseline Git local está registrada em [GIT-BASELINE](GIT-BASELINE.md).
Antes de publicação, revisar as ressalvas de privacidade, portabilidade e
licenças/atribuição ali registradas. Manter a seleção explícita de fontes e assets
separada de perfis, clipboard, backups e estado; não fazer `git add .` no kit ativo.
Nenhum remote, licença global ou release foi escolhido.
Consulte [MIGRATION-PLAN](MIGRATION-PLAN.md) para ordem e riscos.
