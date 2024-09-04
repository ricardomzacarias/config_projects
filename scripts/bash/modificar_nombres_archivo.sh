#!/bin/bash

ruta_carpeta=$(pwd)
file_name=$(basename "$ruta_carpeta")

folder_name=$(echo $file_name | cut -d. -f2)

#echo simplescreenrecorder-2023-10-18_12.33.50.mkv | cut -d- -f3,4

#for file in *
#do
if ls simplescreenrecorder* 1>/dev/null 2>&1 ; then
	file_name2=$(echo "simplescreenrecorder-2023-10-18_12.33.50.mkv" \
	| tr -d .mkv | cut -d- -f3,4 \
	| awk -F_ '{print $1"_"substr($2, 1, 2)}' | cut -d_ -f1 | awk '{print $0"-23"}')
#	file_name2=$(echo "simplescreenrecorder-2023-10-18_12.33.50.mkv" | tr -d .mkv | cut -d- -f3,4 | awk -F_ '{print $1"_"substr($2, 1, 2)}' | cut -d_ -f1 | awk '{print $0"-23"}')

else
	echo "no hay nada"
fi

#jb=$(ls simplescreenrecorder* 1>/dev/null 2>&1)
#p=$(echo $folder_name"-"$file_name2".mkv")
#
#mv $jb $p
#done 
jb=$(ls simplescreenrecorder* 2>/dev/null)
if [ -n "$jb" ]; then
    p="${folder_name}-${file_name2}.mkv"
    mv "$jb" "$p"
else
    echo "No file with name containing simplescreenrecorder found"
fi
