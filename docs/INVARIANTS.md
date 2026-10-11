# Invariantes arquiteturais

Status: Accepted, decisão do projeto em 2026-10-11. São contratos normativos;
conformidade atual parcial documentada em [ARCHITECTURE](ARCHITECTURE.md).

| ID | Contrato | Limite de implementação |
|---|---|---|
| RICY-001 — Single Workspace | Experiência em um único espaço; proibir switchers, indicadores, move-to-workspace, gestos e navegação entre desktops. | KWin pode possuir APIs internas; não confundir seu objeto `workspace` com autorização de UI. Auditar legado sem apagar fallback. |
| RICY-002 — KWin é infraestrutura | KWin/Wayland compõe e gerencia janelas; Ricy não o substitui. | Patches conservadores, compatíveis com a versão instalada. |
| RICY-003 — Noctalia principal | Noctalia é a shell visual Ricy, com patches próprios identificáveis. | Não presumir APIs upstream nem transformar Plasma na experiência principal do destino. |
| RICY-004 — Plasma Recovery | Plasma deve continuar instalado, utilizável e acessível quando Ricy/Noctalia falhar. | Não remover dependências, ferramentas KDE, login ou rotas de retorno. Isolamento atual é incompleto. |
| RICY-005 — Dolphin Recovery | Ricy Files será padrão da futura sessão; Dolphin permanece para recovery. | Não implementar Files agora nem retirar o gerenciador atualmente funcional. Reserva: `apps/file-manager/`. |
| RICY-006 — Design centralizado | Uma fonte de verdade para identidade; reutilizar cores, raios, espaços, movimento, transparência, blur e fontes. | Preservar valores existentes; não criar design paralelo nem migrar todos os consumidores agora. |

Mudanças nos contratos exigem [architecture-change](../.agents/skills/architecture-change/SKILL.md)
e decisão explícita do usuário, seguida de ADR. Conhecer a divergência não
concede permissão para enfraquecer o contrato. Veja [RECOVERY](RECOVERY.md) e
[DESIGN-SYSTEM](DESIGN-SYSTEM.md) para sua aplicação.
