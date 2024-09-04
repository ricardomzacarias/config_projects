#!/bin/bash

# Tratamos el nombre del archivo
# El nombre del archivo, sera el nombre de la carpeta, tomamos la ruta absoluta.
ruta_carpeta=$(pwd)
# A partir de la ruta absoluta tomamos solo la base, el ultimo nombre
file_name=$(basename "$ruta_carpeta")
# Nos quedamos solo con el nombre de la carpeta.
folder_name=$(echo $file_name | cut -d. -f2)

# Bucle que recorre todos los simplescreenrecorder
for I in `find . -name "simplescreenrecorder*mkv"`
do
	echo $I
# TRATAMOS TODAS LAS VARIABLES PARA EL NOMBRE
    SIMPLE=$(echo $I | cut -d / -f2)
    FECHA_DIA=$(echo $SIMPLE | cut -d'-' -f4 | cut -d '_' -f1)
    echo "FECHA DIA " $FECHA_DIA
    FECHA_MES=$(echo $SIMPLE | cut -d'-' -f3)
    echo "FECHA MES " $FECHA_MES
    FECHA_ANO=$(echo $SIMPLE | cut -d'-' -f2)
    echo "FECHA A*O " $FECHA_ANO
#    sleep 2
#    mv $I $folder_name"-"$FECHA_MES"-"$FECHA_DIA"-"$FECHA_ANO".mkv"

# Si existe un archivo cumple la condicion.
if [ -e $folder_name"-"$FECHA_MES"-"$FECHA_DIA"-"$FECHA_ANO".mkv" ] ; then
# Si existe un archivo con el mismo nombre, hacemos una secuencia de ellos
	CONSECUTIVO=1
	while [ -e $folder_name"-"$FECHA_MES"-"$FECHA_DIA"-"$FECHA_ANO".$CONSECUTIVO.mkv" ]
	do
	CONSECUTIVO=$((CONSECUTIVO+1))
	done
		mv $I $folder_name"-"$FECHA_MES"-"$FECHA_DIA"-"$FECHA_ANO".$CONSECUTIVO.mkv"
# mantenemos el archivo si no se cumple la condicion
else
		mv $I $folder_name"-"$FECHA_MES"-"$FECHA_DIA"-"$FECHA_ANO".mkv"
fi
done
