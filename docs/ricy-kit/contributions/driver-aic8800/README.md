# AIC8800 USB — Wi-Fi and Bluetooth on CachyOS

This destination has the USB adapter `a69c:8800`, which after loading the firmware passes to `a69c:8801`: two Bluetooth interfaces and a Wi-Fi. The local package `aic8800-usb-dkms-ricy` includes firmware, source of the three modules `aic_load_fw`, `aic8800_fdrv` and `aic_btusb`, and DKMS configuration.

Primary source: [Radxa aic8800](https://github.com/radxa-pkg/aic8800), fixed on the commit `d13d07963cd15d731e2895e8288a04cca6152ac9`, with SHA256 from the original file in PKGBUILD. The preparation normalizes the line endings and applies the patch series maintained by Radxa itself, including kernel compatibility 7.2 and BlueZ mode for Bluetooth. The compiled code is USB; PCIe/SDIO are not installed. DKMS selects Clang or GCC according to the configuration of each kernel.

The package includes firmware in `/usr/lib/firmware/aic8800_fw/USB`. The modprobe configuration logs the Bluetooth driver before the firmware charge restarts the device and gives priority to the AIC driver over btusb. It does not block btusb globally. It does not include Wi-Fi credentials, paired devices or NetworkManager profiles of the original machine.

## Play in CachyOS

Check out the hashes of the kit before running. Install the headers corresponding exactly to the target kernels and the tools listed below. When updating kernel/headers, update the system as a set and restart in the new kernel before validating the adapter.

```bash
sudo pacman -S --needed dkms base-devel clang llvm lld python bluez bluez-utils
# Linux-cachyos-headers and linux-cachyos-lts-headers were used in this destination.
# Use kernel header packages effectively installed in the new destination.
cd "$HOME/ricy-kit/contributions/driver-aic8800"
makepkg --noconfirm
sudo pacman -U aic8800-usb-dkms-ricy-5.0.20260123.9-3-any.pkg.tar.zst
sudo modprobe aic_load_fw
sudo systemctl enable --now bluetooth.service
dkms status
lsusb -t
nmcli device
bluetoothctl list
```

The USB launcher/modalias automatically loads the modules on the next adapter connections. DKMS recompiles after kernel updates with available headers. Review upstream compatibility for future kernels: there is no guarantee that the fixed source will continue to work in any version.

Use the network panel to connect to the Wi-Fi and Bluetooth panel to pair. The driver installation does not choose a network or provide password.

## Verification and reversal

In the destination, wlan0 and hci0 interfaces were recognized, without rfkill lock; Wi-Fi found networks and BlueZ started discovery of devices. Connection to a network and matching need to be performed by the user.

To remove the driver and firmware:

```bash
sudo pacman -R aic8800-usb-dkms-ricy
```

DKMS removes the installed modules. Reconnect the adapter or restart to close the modules that are still loaded. DKMS and BlueZ can be maintained for other devices. The Bluetooth service of this destination was already enabled before installation; it was only started.

Local implementation logs: `$HOME/.local/state/ricy-aic8800/`. Compilation logs and caches are not part of the portable kit.

Compilation and installation DKMS verified for CachyOS 7.2.9-2 (Clang) and CachyOS LTS 6.18.55-2 (GCC) The functional test was in the session with 7.2; there was no boot on the LTS. Upstream code still emits build notices and debug strokes; they were not treated as installation failure.
