# AIC8800 USB — Wi-Fi e Bluetooth no CachyOS

Este destino possui o adaptador USB `a69c:8800`, que após carregar o firmware
passa a `a69c:8801`: duas interfaces Bluetooth e uma Wi-Fi. O pacote local
`aic8800-usb-dkms-ricy` inclui firmware, fonte dos três módulos
`aic_load_fw`, `aic8800_fdrv` e `aic_btusb`, e configuração DKMS.

Fonte primária: [Radxa aic8800](https://github.com/radxa-pkg/aic8800), fixada no
commit `d13d07963cd15d731e2895e8288a04cca6152ac9`, com SHA256 do arquivo original
no PKGBUILD. A preparação normaliza os finais de linha e aplica a série de
patches mantida pelo próprio Radxa, incluindo compatibilidade com kernel 7.2
e modo BlueZ para Bluetooth. O código compilado é USB; PCIe/SDIO não são
instalados. DKMS seleciona Clang ou GCC conforme a configuração de cada kernel.

O pacote inclui o firmware em `/usr/lib/firmware/aic8800_fw/USB`. A configuração
de modprobe registra o driver Bluetooth antes de a carga de firmware
reinicializar o dispositivo e dá prioridade ao driver AIC sobre btusb. Não bloqueia btusb
globalmente. Não inclui credenciais Wi-Fi, dispositivos pareados ou perfis
NetworkManager da máquina de origem.

## Reproduzir em CachyOS

Confira os hashes do kit antes de executar. Instale os headers correspondentes
exatamente aos kernels do destino e as ferramentas indicadas abaixo. Ao atualizar
kernel/headers, atualize o sistema como conjunto e reinicie no kernel novo antes
de validar o adaptador.

```bash
sudo pacman -S --needed dkms base-devel clang llvm lld python bluez bluez-utils
# Neste destino foram usados linux-cachyos-headers e linux-cachyos-lts-headers.
# Use os pacotes de headers dos kernels efetivamente instalados no novo destino.
cd "$HOME/Projects/ricy/ricy-kit/contributions/driver-aic8800"
makepkg --noconfirm
sudo pacman -U aic8800-usb-dkms-ricy-5.0.20260123.9-3-any.pkg.tar.zst
sudo modprobe aic_load_fw
sudo systemctl enable --now bluetooth.service
dkms status
lsusb -t
nmcli device
bluetoothctl list
```

O launcher/modalias USB carrega os módulos automaticamente nas próximas
conexões do adaptador. DKMS recompila após atualizações de kernel com headers
disponíveis. Reveja a compatibilidade upstream para kernels futuros: não existe
garantia de que a fonte fixada continuará funcionando em qualquer versão.

Use o painel de rede para conectar ao Wi-Fi e o painel Bluetooth para parear.
A instalação do driver não escolhe uma rede nem fornece senha.

## Verificação e reversão

No destino foram reconhecidas as interfaces wlan0 e hci0, sem bloqueio rfkill;
Wi-Fi encontrou redes e BlueZ iniciou descoberta de dispositivos. A conexão
a uma rede e o pareamento precisam ser realizados pelo usuário.

Para remover o driver e o firmware:

```bash
sudo pacman -R aic8800-usb-dkms-ricy
```

DKMS remove os módulos instalados. Reconecte o adaptador ou reinicie para
encerrar os módulos que ainda estejam carregados. DKMS e BlueZ podem ser
mantidos para outros dispositivos. O serviço Bluetooth deste destino já
estava habilitado antes da instalação; ele apenas foi iniciado.

Logs locais da implementação: `$HOME/.local/state/ricy-aic8800/`.
Os logs e caches de compilação não fazem parte do kit portátil.

Compilação e instalação DKMS verificadas para CachyOS 7.2.9-2 (Clang) e
CachyOS LTS 6.18.55-2 (GCC). O teste funcional foi na sessão com 7.2; não
houve boot no LTS. O código upstream ainda emite avisos de compilação e
traces de debug; eles não foram tratados como falha de instalação.
