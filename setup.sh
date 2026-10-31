#!/usr/bin/env bash
# One-time install for a fresh cloud container. Safe to re-run.
set -euo pipefail
cd "$(dirname "$0")"
need=()
command -v ffmpeg >/dev/null || need+=(ffmpeg)
[ -f /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf ] || need+=(fonts-noto-color-emoji)
[ -f /usr/share/fonts/opentype/inter/Inter-Bold.otf ] || need+=(fonts-inter)
dpkg -s espeak-ng >/dev/null 2>&1 || true
if [ ${#need[@]} -gt 0 ]; then (sudo -n true 2>/dev/null && S=sudo || S=""; $S apt-get update -qq && $S apt-get install -y -qq --no-install-recommends "${need[@]}"); fi
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q kokoro-onnx==0.6.1 soundfile pillow numpy
(cd engine && npm ci --silent --no-audit --no-fund)
mkdir -p models
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s models/$f ] || curl -fsSL --retry 4 -o models/$f "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
done
echo "setup ok"
