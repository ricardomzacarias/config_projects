#!/bin/bash

shopt -s dotglob # Habilitar la coincidencia de archivos ocultos

for file in *; do
    if [[ -f "$file" && ! "$file" == .* ]]; then
        # Obtener la fecha de creación del archivo en formato YYYY-MM-DD
        file_date=$(stat -c %y "$file" | cut -d ' ' -f1)

        # Verificar si el nombre del archivo ya contiene la fecha
        if [[ $file != *"$file_date"* ]]; then
            # Renombrar el archivo con la fecha de creación
            new_name="${file%.*}_${file_date}.${file##*.}"
            mv "$file" "$new_name"
            echo "Archivo $file renombrado a $new_name"
        else
            echo "El archivo $file ya contiene la fecha en su nombre"
        fi
    fi
done

