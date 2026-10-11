# Ricy

Desktop opinativo para CachyOS, baseado em KWin/Wayland, com Noctalia como
shell principal e Plasma/Dolphin como fallback e recovery.

**Estado atual:** Noctalia está integrado à sessão Plasma, que ainda fornece
wallpaper/desktop. Sessão independente e Ricy Files são planejados; esta fundação
não migrou o runtime nem implementou novas aplicações.

**Arquitetura:** KWin permanece infraestrutura; a experiência Ricy usa um único
espaço de trabalho. Preservar acesso ao Plasma e ao Dolphin é um requisito.
As divergências legadas e limites de recuperação estão documentados.

**Desenvolvimento:** orientado por agentes, com evidência e mudanças incrementais.
Comece em [AGENTS.md](AGENTS.md); [CLAUDE.md](CLAUDE.md) reutiliza as mesmas regras.

- [Arquitetura](docs/ARCHITECTURE.md), [invariantes](docs/INVARIANTS.md) e [ADRs](docs/adr/README.md).
- [Componentes](docs/COMPONENTS.md) e [design system](docs/DESIGN-SYSTEM.md).
- [Desenvolvimento e validação](docs/DEVELOPMENT.md), [recovery](docs/RECOVERY.md) e [migração](docs/MIGRATION-PLAN.md).

`./scripts/verify all` executa checks offline; `./scripts/doctor` diagnostica sem
alterar configurações. Isso não certifica o funcionamento da sessão inteira.

## Organização e registro existentes

Projeto organizado em 11/10/2026.

- `iniciar.sh`: seleciona Noctalia para a sessão e próximos logins.
- `voltar.sh`: volta ao Plasma.
- `alternar.sh`: alterna entre Plasma e Noctalia.
- `ricy-kit/`: kit ativo desta máquina, com perfil, estado e backups locais.
- `docs/`: registro, identidade visual, instruções de reinstalação e kit transportável preservado.
- `archives/ricy.zip`: arquivo original de transporte, preservado.

Os comandos `ricy`, `voltar-ao-noctalia` e `voltar-ao-plasma` continuam disponíveis em `~/.local/bin`.
Os atalhos e serviços foram atualizados para os caminhos deste projeto.
Para levar o Ricy para outro computador, use a documentação e o kit transportável;
o kit ativo contém estado e backups privados desta instalação.

O registro histórico conserva os caminhos usados nas sessões anteriores.
Registro da organização e cópias dos archives alterados:
`~/.local/state/profile-organization/2026-10-11/`.

Correção dos atalhos em 11/10/2026: as entradas de menu e clipboard foram recarregadas
no cache da sessão KDE (locale en_US.UTF-8), preservando Super e Super+Espaço.
O serviço Noctalia usa `KillMode=process`, para manter os aplicativos que ele abriu
quando a shell é encerrada. A proteção também consta nos modelos dos dois kits.
Durante essa correção o Noctalia e o adaptador de busca permaneceram em execução.
Registro: `~/.local/state/profile-organization/2026-10-11/shortcut-repair/`.
