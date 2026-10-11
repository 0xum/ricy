---
name: testing
description: Definir níveis ou combinação de testes Ricy, planejar validação de integração/recovery ou distinguir PASS, UNKNOWN e NOT RUN; dispensável para executar um check já conhecido.
---

# testing

Consulte a seção “Níveis e evidência” de [DEVELOPMENT](../../../docs/DEVELOPMENT.md)
e as regras do componente para escolher Static, Component, Integration, Recovery,
Visual e Environment. Leia os validadores selecionados antes de executá-los.

Use verify para checks seguros, doctor para diagnóstico somente leitura.
Não instale/reinicie serviços ou execute aplicadores como se fossem testes.
Dependência ausente é NOT RUN/UNKNOWN, nunca PASS. Exit 0 do doctor não
certifica saúde. Não transcreva testes históricos como se tivessem sido rodados.
Corrija problemas causados pela mudança; registre problemas preexistentes.

No encerramento, use o formato abaixo, com comandos e resultados concretos:
```text
Validation:
PASS <check e escopo>
FAIL <check e erro, quando houver>
NOT RUN <check e motivo>
NOT APPLICABLE <nível e motivo>
```

Proibido concluir “This should work.”, “Probably fixed.” ou “Everything is
working.” sem evidência. Um teste offline aprovado não prova toda a sessão.
