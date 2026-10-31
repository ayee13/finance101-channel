#!/usr/bin/env bash
# Render one episode: ./make_episode.sh ep002   -> build/ep002/{video.mp4,thumbnail.png,chapters.txt,captions.srt,sheet.jpg}
set -euo pipefail
cd "$(dirname "$0")"; ROOT=$PWD; EP=$1; OUT=$ROOT/build/$EP
mkdir -p "$OUT"
.venv/bin/python -I engine/engine.py "$ROOT/episodes/$EP/beats.py" "$OUT" "$ROOT/models" "$ROOT/engine" "$ROOT/fonts"
.venv/bin/python -I engine/thumb.py "$ROOT/episodes/$EP" "$OUT" "$ROOT/engine" "$ROOT/fonts"
.venv/bin/python -I engine/sheet.py "$OUT/stills" "$OUT/sheet.jpg"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/video.mp4"
