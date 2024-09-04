#!/bin/bash
for file in *
do
    # Reemplaza los dobles guiones bajos con un solo guión bajo
    new_name=$(echo "$file" | sed 's/__/ /g; s/_/ /g; s/ /_/g')
    # Renombra el archivo
    mv "$file" "$new_name"
done
