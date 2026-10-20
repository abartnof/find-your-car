#!/bin/bash
# usage: tools/shot.sh out.png "#hash" [W H]
cd "$(dirname "$0")/.."
timeout 90 chromium --headless=new --no-sandbox --use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --window-size=${3:-390},${4:-800} --virtual-time-budget=${5:-7000} --screenshot="$1" "file://$PWD/docs/index.html$2" 2>&1 | tail -1
