#!/usr/bin/env bash
set -euo pipefail
base_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$base_dir/teste-ativo" ] && ! systemctl --user is-active --quiet noctalia-teste.service; then
 "$base_dir/return-to-plasma.sh"
fi
