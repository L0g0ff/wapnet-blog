#!/bin/sh
set -eu

PATH="/opt/data/home/.local/bin:$PATH"
xml="source/wordpress.xml"
cache="${TMPDIR:-/opt/data/cache/scratch}/wp2hugo-media"

[ -f "$xml" ] || gzip -cd source/wordpress.xml.gz > "$xml"
rm -rf import-output "$cache"
mkdir -p "$cache"

wp2hugo \
  --source "$xml" \
  --output import-output \
  --download-media \
  --download-all \
  --continue-on-media-download-error \
  --content-date-folder-structure year-month \
  --media-cache-dir "$cache" \
  --font system-ui

find import-output -mindepth 1 -maxdepth 1 -type d -name 'generated-*' -print
