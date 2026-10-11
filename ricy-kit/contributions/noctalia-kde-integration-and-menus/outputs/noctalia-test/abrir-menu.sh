#!/usr/bin/env bash
set -euo pipefail
# Super e Super+Espaço usam a mesma abertura por monitor da digitação.
exec /usr/bin/qdbus6 org.kde.krunner /App org.kde.krunner.App.toggleDisplay
