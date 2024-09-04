#!/bin/bash

# Inicializar la variable para almacenar los nombres de archivos
non_crp_season_files=""
filtered_files=""

# Obtener todos los nombres de archivos que no contengan "crp_season"
for file in *; do
#    if [[ $file != *"crp_season"* ]]; then
    if [[ $file != *"crp_season"* && $file != *.sh && $file != *crp.sh* ]]; then
        # Agregar el nombre del archivo a la variable
        non_crp_season_files="$non_crp_season_files$file "
    
        # Fichero que contiene el nombre que voy a tratar
        echo "El archivo que vas a tratar es $file"
        sleep 2
        
        echo "Ingrese un número (N):"
        read number

        echo "Ingrese un título (T):"
        read title

#        echo "Ingrese la extensión del archivo (E):"
#        read extension
        extension=".pdf"

        new_filename="crp_season${number}_${title}${extension}"
        mv "$file" "$new_filename"
        echo "El archivo se ha renombrado a $new_filename"

    fi
done

# Imprimir los nombres de archivos que no contienen "crp_season"
echo "Archivos que no contienen 'crp_season':"
echo "$non_crp_season_files"

