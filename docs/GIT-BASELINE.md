# Baseline Git local

Auditoria de 2026-10-11, limitada à preparação Git. A fundação agent-first,
arquitetura, runtime, configurações visuais e organização dos arquivos foram
preservados. O baseline usa `main`, sem remote ou publicação. As regras de
inclusão são responsabilidade da manutenção do repositório; não acrescentam
dependências ao desktop nem modificam recovery.

## Seleção e preservação

KNOWN: a inspeção inicial enumerou 3.035 arquivos, incluindo arquivos ocultos,
assets binários e dois repositórios aninhados de plugins dentro do perfil ativo.
Não foram encontrados symlinks ou arquivos especiais. Não havia Git na raiz;
o único `.gitignore` encontrado pertencia a um plugin materializado em `work/`.
Esse arquivo upstream foi preservado e não rege a seleção do projeto.

O [.gitignore](../.gitignore) exclui 1.939 arquivos presentes nessa inspeção:

| Categoria | Arquivos | Decisão |
|---|---:|---|
| `ricy-kit/contributions/noctalia-kde-integration-and-menus/work/` | 1.927 | Perfil privado, configurações ativas, estado, histórico de notificações, clipboard criptografado, recentes, uso, caches e plugins/clones materializados |
| Capturas locais em `outputs/` da mesma contribuição | 8 | Dois TARs de backup KDE, manifesto do backup, estado anterior, dois atalhos originais, restauração de wallpaper com IDs do destino e marcador de teste ativo |
| `__pycache__/` | 3 | Bytecode Python regenerável |
| `archives/ricy.zip` | 1 | Archive histórico com `notification_history.json` dentro de `work/`; preservado no disco, fora do Git |

Os dois TARs contêm configurações KDE pessoais; os caminhos exatos excluídos
estão no `.gitignore`. Nenhum backup foi apagado, movido ou refeito. O ZIP pode
conter evidência histórica própria: sua eventual extração/sanitização exige
auditoria separada, sem redistribuir o archive original.

As regras também cobrem os nomes de capturas geradas pelos preparadores,
caches Python e temporários de editor, além de produtos makepkg nos diretórios
do driver. Não havia builds compilados, logs avulsos ou temporários de editor
fora das áreas privadas na inspeção inicial; os compiladores atuais usam cache
externo ao repositório. Logs e metadados Git dos plugins ficam dentro de `work/`.
Não se aplicaram exclusões genéricas de `outputs/`, assets, backups por extensão,
fontes, logs de evidência ou diretórios históricos.

Incluídos: regras/skills, documentação e ADRs, scripts/testes, as duas árvores
de kit com suas diferenças, patches cumulativos e históricos, templates,
paletas, temas, fontes, cursores, licenças e manifests `SHA256SUMS` originais.
Os arquivos de `outputs/` necessários à preparação/recriação permanecem.
A inclusão inicial usa uma lista explícita de arquivos auditados; não `git add .`.

## Limites para publicação futura

- KNOWN: wrappers raiz, alguns scripts e launchers `.desktop` contêm caminhos
  absolutos da instalação. São entradas/fontes necessárias, preservadas para
  evitar mudança de comportamento; precisam de revisão de portabilidade e
  privacidade antes de publicação.
- KNOWN: o seed `config.toml` em `outputs/noctalia-test/` da contribuição ativa
  contém uma cidade configurada. Documentação histórica também contém referências
  à máquina, ambiente e preferências. Foram preservadas como configuração e
  evidência, sem transformar esses valores em padrão genérico nesta tarefa.
- KNOWN: assets upstream e suas licenças/atribuições existentes foram preservados.
  UNKNOWN: autorização integral de redistribuição do conjunto; nenhuma licença
  global foi escolhida. Arquivos binários de fontes/cursores/imagens permanecem
  por serem assets necessários, não produtos descartáveis de compilação.
- KNOWN: `SHA256SUMS` é histórico e não foi regenerado; não representa o manifesto
  deste commit. O commit Git passa a identificar o conteúdo selecionado.
- KNOWN: a identidade de autoria usa a configuração Git existente. Nome/e-mail
  do commit também devem ser considerados numa eventual publicação.
- A busca heurística cobre chaves privadas, tokens de provedores comuns, JWT,
  URLs com credenciais e atribuições de segredo; SVGZ são inspecionados após
  descompressão. Nenhuma credencial evidente foi encontrada no conteúdo selecionado.
  UNKNOWN: ausência absoluta de segredos; não houve certificação de dados binários
  nem tentativa de descriptografar clipboard ou publicar o kit privado.

## Validação

Resultados desta preparação são registrados em [CHANGELOG](CHANGELOG.md).
Testes offline não comprovam login, alternância ou recuperação em sessão real.
