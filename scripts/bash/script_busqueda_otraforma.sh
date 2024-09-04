#!/bin/bash


echo "nombre del archivo: "
read File
find $File 2>/dev/null || echo "No encontramos tu archivo!"
