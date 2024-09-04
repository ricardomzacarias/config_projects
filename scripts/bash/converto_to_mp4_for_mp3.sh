#!/bin/bash

carpeta=""

for archivo in "$carpeta"/*.mp4; do
	nombre=$(basename "$archivo" .mp4)

	ffmpeg -i "$archivo" -vn -acodec libmp3lame -q:a 2 "$carpeta/$nombre.mp3"
done
