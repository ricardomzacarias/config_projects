#!/bin/bash
if [ -z $1 ]
then
  echo "Error: debes introducir un nombre de usuario"
  echo "Ejemplo: ./añadir_usuario nombre"
  exit 1
fi
NOMBRE="$1"
sudo useradd -m $NOMBRE
