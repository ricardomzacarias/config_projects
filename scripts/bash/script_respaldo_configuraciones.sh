#!/bin/bash

# declaramos las variables de nuestro script

aplicaciones=("terminator" "polybar" "i3" "pcmanfm")
folder_config="/media/$USER/"


if [ -d "$folder_config" ]; then
	echo "el directorio .config ya existe"
else
	mkdir -p $folder_config
	echo "la carpeta .config ha sido creada exitosamente!"
fi
###############################################################################################
for i in "${aplicaciones[@]}"; do
    if [ -d "/media/$USER/config/$i" ]; then
        echo "$i ya existe en el directorio."
    else
        cp -r "$HOME/.config/$i" "/media/$USER/config/"
        echo "$i ha sido copiado exitosamente."
    fi
    sleep 3
done


