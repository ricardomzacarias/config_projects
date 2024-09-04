#!/bin/bash

# rsycn_no_touch="rsync -r -n -t -p -o -g -v --progress --delete --size-only -s" # PRUEBAS
rsycn_no_touch="rsync -r -t -p -o -g -v --progress --delete --size-only -s"
base_learn="/"
base_hdd_2tb="/"
base_personales="/"
base_personales_hdd_2tb="/"
folders_learn=("libros_todos/" "msmk/" "obsidian/" "proyectos/" "learn_with_videos/")

for i in "${folders_learn[@]}"; do
	# if [ -d "$base_learn$i" ] && [ -d "$base_hdd_2tb$i" ]; then
	if [ -d "$base_learn$i" ] && [ -d "$base_hdd_2tb$i" ]; then
		$rsycn_no_touch "$base_learn$i" "$base_hdd_2tb$i"
		sleep 3
	else
		# $rsycn_no_touch "$videos_folder" "$base_hdd_2tb$i"
		echo -e "\n$i no lo hemos conseguido!!!"
	fi
done

if [ -d $base_personales ] && [ -d $base_personales_hdd_2tb ]; then
	echo -e "\nCONSEGUIDOS"
	sleep 3
	$rsycn_no_touch "$base_personales" "$base_personales_hdd_2tb"
fi

# rsync -r -v --progress --delete --ignore-existing --size-only -s /home/ricardolmz/particion_respaldo/respaldo_rlmz/personales_ricardo/musica/ /run/user/1000/gvfs/afc:host=00008110-000C6D2111C2801E,port=3/org.videolan.vlc-ios/
