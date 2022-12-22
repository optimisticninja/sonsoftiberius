#!/bin/bash

for img in "$@"; do
	mkdir "$img-analysis" && cd "$img-analysis"
	zsteg -av "../$img" > "zsteg-all.txt"
	stegoveritas "../$img"
	cd ..
done
