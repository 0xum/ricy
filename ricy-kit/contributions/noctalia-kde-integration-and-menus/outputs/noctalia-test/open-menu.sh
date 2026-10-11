#!/usr/bin/env bash
set -euo pipefail
# Super and Super+Space use the same opening by typing monitor.
exec /usr/bin/qdbus6 org.kde.krunner /App org.kde.krunner.App.toggleDisplay
