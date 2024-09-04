#!/bin/bash
for file in *
do
    # Cambia el nombre del archivo a minúsculas
    new_name=$(echo "$file" | tr '[:upper:]' '[:lower:]')
    # Renombra el archivo
    mv "$file" "$new_name"
done
