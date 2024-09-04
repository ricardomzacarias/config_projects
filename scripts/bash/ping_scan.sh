#!/bin/bash

if [ "$#" -ne "1" ]

then

echo "Modo de uso: ./ping_scan.sh [subnet]"
echo "Ejemplo: ./ping_scan.sh 104.21.93"

else 

for ip in `seq 1 254`;do
 
ping $1.$ip -c 1 | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1 &

done

fi
