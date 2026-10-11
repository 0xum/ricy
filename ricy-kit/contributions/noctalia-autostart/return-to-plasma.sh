#!/usr/bin/env bash
set -euo pipefail
if [[ "${RICY_RECUPERACAO_INTERNA:-0}" == 1 ]]; then
 exec python "/home/delta/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/integration.py" restaurar
fi
exec "/home/delta/Projects/ricy/ricy-kit/contributions/plasma-noctalia-switching/ricy" plasma
