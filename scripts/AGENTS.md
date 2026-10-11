# Validação e diagnóstico

Leia [DEVELOPMENT](../docs/DEVELOPMENT.md). verify/doctor devem permanecer somente
leitura em relação à sessão e aos sources; testes temporários isolados são permitidos.
Não iniciar/reparar serviços, instalar pacotes ou esconder skips como PASS.
Erros de checks devem propagar; dependência ausente produz NOT RUN/UNKNOWN.
Mantenha raiz relativa ao próprio script e teste detecção de arquivo/link faltante.
