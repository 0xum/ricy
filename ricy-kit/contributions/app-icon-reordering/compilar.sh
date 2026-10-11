#!/usr/bin/env bash
set -euo pipefail
base=$(cd -- "$(dirname -- "$0")" && pwd)
src="${XDG_CACHE_HOME:-$HOME/.cache}/ricy-noctalia-src-5.2.1"
commit=6ef43e2bf2f3d5b4205ec72a72e34a2ab76ce3b4
if [[ ! $(/usr/bin/noctalia --version) =~ ^noctalia[[:space:]]v5\.2\.1([[:space:]]|$) ]]; then
  echo 'Este patch corresponde ao Noctalia 5.2.1. Revise para a versão instalada.' >&2
  exit 1
fi
if [[ ! -d "$src" ]]; then
  git clone --depth 1 --branch v5.2.1 https://github.com/noctalia-dev/noctalia.git "$src"
fi
[[ $(git -C "$src" rev-parse HEAD) == "$commit" ]] || { echo 'Fonte com commit inesperado.' >&2; exit 1; }
if git -C "$src" diff --quiet; then
  git -C "$src" apply --check "$base/noctalia-ricy.patch"
  git -C "$src" apply "$base/noctalia-ricy.patch"
  # O patch acrescenta um header; incluí-lo no diff permite validar o cache nas próximas execuções.
  git -C "$src" add -N src/shell/bar/widgets/taskbar_icon_motion.h src/shell/bar/widgets/taskbar_order.h
else
  git -C "$src" diff --binary | cmp - "$base/noctalia-ricy.patch"
fi
if [[ ! -f "$src/build-ricy/build.ninja" ]]; then
  meson setup "$src/build-ricy" "$src" --buildtype=release -Dtests=disabled --prefix=/usr
fi
ninja -C "$src/build-ricy" -j "${RICY_BUILD_JOBS:-6}" noctalia
printf 'Binário pronto: %s\n' "$src/build-ricy/noctalia"
