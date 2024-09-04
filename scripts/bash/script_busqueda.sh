#!/bin/bash

# localiza archivos

read -p "Nombre del directorio: " DIR ; read -p "Nombre del archivo: " ARCHIVO

X=$(find $DIR -name "$ARCHIVO")

[ -n "$X" ] && echo "Archivo $ARCHIVO Encontrado en $DIR/$ARCHIVO" || echo "Archivo no encontrado"
