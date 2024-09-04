#!/bin/bash

explore_mayus=false
explore_blank_space=false

for file in *
do
    if [[ $file =~ [A-Z] ]]; then
        # Cambia el nombre del archivo a minúsculas
        new_name=$(echo "$file" | tr '[:upper:]' '[:lower:]')
        # Renombra el archivo
        mv "$file" "$new_name"
        # Cambiamos el valor de la variable
        explore_mayus=true
    fi
done

if [[ $explore_mayus == false ]]; then
    echo -e 'No encontramos mayusculas en esta carpeta!\n'
    sleep 2
fi

for folder in *
do
    if [[ $folder =~ [[:space:]] ]]; then
    
    # Cambiamos espacios vacios por underground
    new_name2=$(echo "$folder" | sed 's/__/ /g; s/_/ /g; s/ /_/g')
    # Cambiamos el nombre
    mv "$folder" "$new_name2"
    echo  "$folder" "------------" "$new_name2"
    explore_blank_space=true
    fi
done

if [[ $explore_blank_space == false ]]; then
    echo -e 'No encontramos espacios vacios en las carpetas\n'
    sleep 2
fi

# if [ -d "simplescreenrecorder*" ]; then
# desc_folder=$(basename $(pwd) | sed 's/[0-9.]//g') && echo $desc_folder