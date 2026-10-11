# Componentes

KNOWN significa presença e responsabilidade verificadas nos arquivos citados; não
certificação runtime nesta tarefa. Todos os destinos são PLANNED. Ownership indica
manutenção, preservando licenças upstream. Cada link atual leva ao README local.

A raiz `ricy-kit/` é ativa; `docs/ricy-kit/` conserva a variante de transporte.
Leia [regras do kit](../ricy-kit/AGENTS.md) antes de editar. Réplicas não são
fontes intercambiáveis. O ciclo de patches Noctalia é cumulativo: a referência
registrada mais recente é app-icon-reordering, com window-fade-expand para janelas.

| Componente / localização atual | Responsabilidade | Destino futuro | Dependências | Status / ownership | Impacto em recovery |
|---|---|---|---|---|---|
| [noctalia-kde-integration-and-menus](../ricy-kit/contributions/noctalia-kde-integration-and-menus/README.md) | Adaptador de busca, perfil, atalhos e menus Qt | `integrations/kde/ + services/ + themes/` | Noctalia, PyGObject, D-Bus, KGlobalAccel, Kvantum | KNOWN / RICY-OWNED + assets derivados | Alta: atalhos, wallpaper e estilo compartilhados |
| [noctalia-autostart](../ricy-kit/contributions/noctalia-autostart/README.md) | Unidades de shell, busca e integração no login | `services/ + installer/` | systemd usuário, Plasma, integração | KNOWN / RICY-OWNED | Alta: iniciar somente após prontidão; retorno Plasma |
| [plasma-noctalia-switching](../ricy-kit/contributions/plasma-noctalia-switching/README.md) | Comando ricy, snapshots e restauração de painéis | `recovery/plasma/ + integrations/kde/` | systemd, Python/PyGObject, qdbus6, flock, KGlobalAccel | KNOWN / RICY-OWNED | Crítica: caminho de retorno atual |
| [notification-continuity](../ricy-kit/contributions/notification-continuity/README.md) | Patch de notificações e ativador do binário local | `shell/noctalia/` | Noctalia fixado, integração, blur | KNOWN / PATCHES + RICY-OWNED | Preservar /usr/bin/noctalia, backup e apps |
| [taskbar-menu-composition](../ricy-kit/contributions/taskbar-menu-composition/README.md) | Menu de app encaixado; variante histórica cumulativa | `shell/noctalia/` | Noctalia e patches anteriores | KNOWN / PATCHES | Risco de crash de shell; manter ativador/reversão |
| [tray-menu-composition](../ricy-kit/contributions/tray-menu-composition/README.md) | Menus DBusMenu encaixados; variante histórica | `shell/noctalia/` | Noctalia, DBusMenu | KNOWN / PATCHES | Ações pertencem aos aplicativos; não mudar sem validação |
| [app-icon-interactions](../ricy-kit/contributions/app-icon-interactions/README.md) | Hover/escala de ícones; variante histórica | `shell/noctalia/` | Noctalia Style | KNOWN / PATCHES | Não alterar hit area nem controle da sessão |
| [taskbar-app-actions](../ricy-kit/contributions/taskbar-app-actions/README.md) | Foco/minimização/fechamento por UUID; histórico | `shell/noctalia/ + integrations/kde/` | API KWin e Noctalia | KNOWN / PATCHES | Testes não devem fechar trabalho do usuário |
| [app-indicator-animations](../ricy-kit/contributions/app-indicator-animations/README.md) | Indicadores e animação anterior de janelas | `shell/noctalia/ + compositor/kwin/` | Noctalia e KWin | KNOWN / PATCHES + derivado KDE | Variante anterior; não aplicar sobre a atual |
| [app-icon-states](../ricy-kit/contributions/app-icon-states/README.md) | Movimento de ícones por ação; histórico | `shell/noctalia/` | Noctalia, efeitos KDE | KNOWN / PATCHES | Não substituir variante cumulativa atual por acidente |
| [app-icon-reordering](../ricy-kit/contributions/app-icon-reordering/README.md) | Variante cumulativa de referência: ordenação/ícones/ações | `shell/noctalia/` | Noctalia 5.2.1 fixado, Meson/Ninja/C++, KWin | KNOWN / PATCHES | Rebuild e ativação separados; preservar rollback |
| [window-fade-expand](../ricy-kit/contributions/window-fade-expand/README.md) | Animação atual ricywindowactions e Scale | `compositor/kwin/` | API script KWin, PyQt6 para testes | KNOWN / RICY-OWNED derivado KDE | Altera efeitos compartilhados com Plasma |
| [blur-continuity](../ricy-kit/contributions/blur-continuity/README.md) | ricyblur derivado do blur upstream | `compositor/kwin/` | KWin 6.7.5/headers, Qt/KF6, C++ | KNOWN / PATCHES | ABI crítica; não substituir o compositor |
| [dolphin-noctalia-identity](../ricy-kit/contributions/dolphin-noctalia-identity/README.md) | Tema/QSS e launcher Dolphin, FileManager1 | `integrations/kde/ + themes/` | Dolphin, Kvantum, helper Qt | KNOWN / RICY-OWNED + temas derivados | Alta: acesso aos arquivos no recovery |
| [dolphin-blur-corners](../ricy-kit/contributions/dolphin-blur-corners/README.md) | Helper Qt e efeito de cantos Dolphin | `integrations/kde/ + compositor/kwin/` | Qt, Kvantum, ABI KWin | KNOWN / RICY-OWNED + derivado KDE | Plugin incompatível pode afetar Dolphin |
| [dolphin-deb-rpm-installer](../ricy-kit/contributions/dolphin-deb-rpm-installer/README.md) | Integração local DEB/RPM com conversão e UI | `integrations/kde/ + installer/` | Dolphin, PyQt6, debtap, pkexec/pacman | KNOWN / RICY-OWNED + dependências upstream | Não executar instalação para testar docs |
| [target-implementation-fixes](../ricy-kit/contributions/target-implementation-fixes/README.md) | Correções versionadas para preparação do destino | `installer/` | Scripts do kit, debtap | KNOWN / PATCHES + RICY-OWNED | Aplicar só após conferir kit de destino |
| [login-lock-cursor-appearance](../ricy-kit/contributions/login-lock-cursor-appearance/README.md) | Assets e aplicadores de SDDM/Plasma/Qt/GTK | `themes/ + integrations/kde/` | SDDM, Plasma, Kvantum, fontes e temas | KNOWN / UPSTREAM assets + RICY-OWNED | Alta: login/bloqueio e configurações globais |
| [login-matched-lock-screen](../ricy-kit/contributions/login-matched-lock-screen/README.md) | Adaptação do bloqueio ao login | `themes/ + integrations/kde/` | KDE/Breeze instalado, SDDM | KNOWN / PATCHES / assets derivados | Alta: manter desbloqueio utilizável |
| [konsole-animated-cursor](../ricy-kit/contributions/konsole-animated-cursor/README.md) | Perfil e paleta de terminal | `themes/ + integrations/kde/` | Konsole, Kvantum | KNOWN / RICY-OWNED configuração | Terminal deve continuar disponível para diagnóstico |
| [keyboard-cedilla](../ricy-kit/contributions/keyboard-cedilla/README.md) | Composição XCompose e ajuste Brave | `integrations/` | Layout/XCompose, Brave opcional | KNOWN / RICY-OWNED | Preservar entrada de texto e preferências |
| [noctalia-language-and-localization](../ricy-kit/contributions/noctalia-language-and-localization/README.md) | Idioma/região/clima da shell | `shell/noctalia/ + integrations/` | Noctalia, locale, unidades systemd | KNOWN / RICY-OWNED | Não globalizar preferências de uma instalação |
| [noctalia-visual-identity](../ricy-kit/contributions/noctalia-visual-identity/README.md) | Tokens e prancha da identidade existente | `themes/tokens/` | Config/paleta/Style Noctalia e contribuições visuais | KNOWN / RICY-OWNED referência | Sem instalação; divergências visuais precisam ser registradas |
| [driver-aic8800](../ricy-kit/contributions/driver-aic8800/README.md) | Driver USB Wi-Fi/Bluetooth e pacote DKMS | `integrations/hardware/` | Kernel/headers, DKMS, fonte Radxa fixada | KNOWN / UPSTREAM + patches + empacotamento Ricy | Risco de perder rede; dependência de hardware, não de toda sessão |

## Entradas e componentes transversais

| Componente / localização atual | Responsabilidade | Destino | Dependências | Status | Recovery |
|---|---|---|---|---|---|
| [Wrappers raiz](../iniciar.sh), [voltar](../voltar.sh), [alternar](../alternar.sh) | Entradas desta instalação | core/ (a avaliar) | Caminho absoluto do kit | KNOWN / RICY-OWNED | Não mover sem revisar chamadores |
| [preparar-ambiente.py](../ricy-kit/preparar-ambiente.py), outputs/ | Preparação e seeds/templates; pode criar backups privados | installer/ + integrations/ | Python e configurações do destino | KNOWN / RICY-OWNED | Não executar no kit ativo para validar estrutura |
| [gerar-variante-kvantum.py](../ricy-kit/gerar-variante-kvantum.py) | Variante de estilo Qt | themes/ | Kvantum/tema existente | KNOWN | Estilo compartilhado com recovery |
| [Kit de transporte](ricy-kit/AGENTS.md) e archives/ | Reprodução/histórico | installer/ e arquivo histórico, após auditoria | Manifests, scripts e licenças | KNOWN: presença; UNKNOWN: publicação segura integral | Não copiar estado da instalação ativa |
| KWin / Plasma / Dolphin | Compositor, desktop compartilhado e arquivos | compositor/kwin/ + recovery/plasma/ | Pacotes do sistema | KNOWN: dependência no código; upstream externo | Não removíveis |
| [Ricy Files](../apps/file-manager/README.md) | Futuro gerenciador padrão Ricy | apps/file-manager/ | UNKNOWN: toolkit/contratos | PLANNED / RICY-OWNED | Dolphin permanece disponível |
| [Core](../core/AGENTS.md) / [Services](../services/AGENTS.md) | Futuros limites comuns; serviços atuais estão nas contribuições | core/ + services/ | UNKNOWN: novos contratos | PLANNED | Não criar novo daemon/IPC por suposição |

Leia [migração](MIGRATION-PLAN.md) antes de realocar qualquer componente. Leia
[RECOVERY](RECOVERY.md) para operações que afetam sessão, login ou arquivos.
