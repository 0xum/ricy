#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
/usr/lib/qt6/moc $(pkg-config --cflags Qt6Qml Qt6Gui) -I/usr/include/kwin -I/usr/include/KF6/KConfigCore -I/usr/include/KF6/KConfig windowsequence.cpp -o windowsequence.moc
g++ -std=c++20 -fPIC -shared windowsequence.cpp -o libwindowsequence.so -I/usr/include/kwin -I/usr/include/KF6/KConfigCore -I/usr/include/KF6/KConfig $(pkg-config --cflags --libs Qt6Qml Qt6Gui) -lkwin -lKF6ConfigCore
