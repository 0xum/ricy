#!/usr/bin/env bash
set -euo pipefail
curl() {
    local arg
    local -a args=()
    for arg in "$@"; do
        [[ "$arg" == '-k' ]] && continue
        case "$arg" in
            http://ftp.debian.org/*|http://archive.ubuntu.com/*|http://ports.ubuntu.com/*) arg="https://${arg#http://}" ;;
        esac
        args+=("$arg")
    done
    /usr/bin/curl -4 --fail --location --retry 2 --connect-timeout 15 --max-time 180 "${args[@]}"
}
export -f curl
export TERM=dumb LC_ALL=C
/usr/bin/bash /usr/bin/debtap -u
# Upstream may continue after a failed Debian download: verify every index.
for index in debian-main-packages-files debian-non-free-packages-files debian-contrib-packages-files ubuntu-packages-files virtual-packages aur-packages extended-base-packages-list; do
    [[ -s "/var/cache/debtap/$index" ]] || { echo "Índice ausente/vazio: $index" >&2; exit 1; }
done
