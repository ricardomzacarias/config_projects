#!/bin/bash

# localiza archivos

echo "Nombre del directorio: "

read DIR

echo "Nombre del archivo: "

read ARCHIVO

X=$(find $DIR -name "$ARCHIVO")

#
[ -n "$X" ] && echo "Archivo Encontrado" || echo "Archivo no encontrado"
