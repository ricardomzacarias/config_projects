#!/bin/bash
for file in *
do
    # Reemplaza los espacios vacíos con "_"
    mv "$file" "${file// /_}"
done
