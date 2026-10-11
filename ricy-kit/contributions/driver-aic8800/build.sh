#!/usr/bin/env bash
set -euo pipefail
kernel_dir=$1
source_dir=$(cd -- "$(dirname -- "$0")" && pwd)
unset LLVM LLVM_IAS
if grep -q '^CONFIG_CC_IS_CLANG=y' "$kernel_dir/.config"; then
    toolchain=(LLVM=1)
else
    toolchain=(CC=gcc LD=ld)
fi
make -j8 "${toolchain[@]}" -C "$kernel_dir" M="$source_dir/aic8800" modules
make -j4 "${toolchain[@]}" -C "$kernel_dir" M="$source_dir/aic_btusb" modules
