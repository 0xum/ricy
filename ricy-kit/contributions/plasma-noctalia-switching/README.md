# Alternar Plasma e Noctalia preservando o Ricy

Esta contribuição substitui a restauração integral do backup antigo usada
pelos scripts anteriores. O wallpaper, os widgets do desktop e as configurações
gerais continuam compartilhados no Plasma. Cada entrada no Noctalia salva os
painéis Plasma mais recentes e seus grupos de geometria; o retorno repõe
somente esses grupos, sem restaurar archives completos de uma instalação antiga.
O perfil privado, binário personalizado, estado e drop-ins Noctalia existentes
continuam em uso. Não restaura cores, fontes, efeitos ou aparência de aplicativos.

## Instalar em um destino preparado

Depois de preparar Noctalia/KDE e instalar `noctalia-autostart`:

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/instalar.py"
```

Requer a sessão Plasma Wayland, suas três unidades já instaladas, Python/PyGObject,
qdbus6, systemctl, flock e kbuildsycoca6. O instalador não troca o ambiente atual.
Executar novamente após reinstalar os scripts antigos de início automático.
Os caminhos são calculados a partir da localização do kit e do usuário de destino.

## Usar

```bash
ricy noctalia   # selecionar Noctalia e habilitar no próximo login
ricy plasma     # selecionar Plasma e desabilitar início automático Noctalia
ricy alternar   # trocar para o outro; também é a ação padrão de `ricy`
ricy status     # mostrar Plasma ou Noctalia
```

Os comandos ficam em `$HOME/.local/bin`; se esse diretório não estiver no PATH,
use o caminho completo. Também existem `voltar-ao-noctalia`, `voltar-ao-plasma`,
`$HOME/Projects/ricy/iniciar.sh`, `voltar.sh`, `alternar.sh` e três entradas no menu:
**Voltar ao Noctalia**, **Voltar ao Plasma**, **Alternar Plasma e Noctalia**.

Os wrappers antigos do kit ativo passam a encaminhar para esta implementação.
Cada troca roda numa unidade transitória separada da shell, para continuar
mesmo quando o comando foi aberto pelo menu do Noctalia e a shell é encerrada.
Os nomes de serviços e perfil permanecem os mesmos. Plasmashell reinicia
brevemente para sincronizar o KConfig e repor painéis; KWin e aplicativos
continuam abertos. Só recolhe painéis depois de confirmar shell, busca e atalhos.
Falha durante essa etapa recupera Plasma; falha pelo comando também desabilita
a preferência Noctalia no login. Os atalhos Super, Super+Espaço e Super+V são
capturados antes da transferência e devolvidos no retorno, a cada ciclo.

Backups privados, atalhos e grupos de painéis ficam em
`${XDG_STATE_HOME:-$HOME/.local/state}/ricy-alternancia/`; não distribua essa
pasta. O snapshot de painéis se atualiza quando existem painéis vivos; entrar
novamente numa sessão já Noctalia não o substitui por um layout vazio.
Colisões com IDs de widgets/desktops criados posteriormente são remapeadas.
O backup original `plasma-antes.tar.gz` nunca é modificado; só serve de seed
de painéis quando a migração começa numa sessão antiga já sem painéis.

## Verificar

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/verificar.py"
ricy status
systemctl --user is-active plasma-plasmashell.service
```

Noctalia deve ter shell/adaptador ativos e zero painéis Plasma; Plasma deve
ter seus painéis e KRunner. O wallpaper deve permanecer nos dois sentidos.
O instalador imprime o backup; erros da integração aparecem em
`journalctl --user -u ricy-noctalia-integracao.service`.

## Desfazer a instalação da alternância

Primeiro execute `ricy plasma`. Depois use o caminho do backup emitido:

```bash
python "$HOME/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/restaurar-instalacao.py" \
  "$HOME/.local/state/ricy-alternancia/backups/DATA-HORA"
```

O restaurador só repõe wrappers/entradas de comando e o estado da alternância.
Não repõe appletsrc/plasmashellrc capturados para diagnóstico, preservando o
desktop atual. Não apaga o perfil Noctalia, efeitos, aparência nem os backups.
Os scripts antigos recolocados voltam a ter a limitação original: podem
restaurar um wallpaper/layout antigo. Para continuar alternando, mantenha
esta contribuição instalada.

Não é uma troca de sessão/compositor: Noctalia segue integrado ao KDE/KWin.
Alterações no próprio desktop são compartilhadas. Aparência de login/bloqueio
permanece independente; seus restauradores continuam em outras contribuições.
