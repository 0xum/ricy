#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# The persistent onset makes its own recovery in case of failure.
if systemctl --user is-enabled --quiet ricy-noctalia-integracao.service; then
 exit 0
fi
if [ -f "$base_dir/teste-ativo" ] && ! systemctl --user is-active --quiet noctalia-teste.service; then
 "$base_dir/return-to-plasma.sh"
fi
