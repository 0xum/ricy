#!/usr/bin/env bash
set -euo pipefail
if ! /usr/bin/noctalia msg status | /usr/bin/python -c 'import json,sys; s=json.load(sys.stdin); sys.exit(0 if s.get("activePanelId")=="launcher" else 1)'; then
 /usr/bin/noctalia msg bar-show search_edge >/dev/null
 sleep 0.25
fi
exec /usr/bin/noctalia msg panel-toggle launcher
