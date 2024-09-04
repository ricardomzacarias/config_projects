#!/bin/bash

DIR_LIBROS="$"
#DIR_LIBROS="$HOME/Documents/"
DIR_LISTOS="$"
TOTAL_FICHEROS=$(ls -p $DIR_LIBROS | grep -v / | wc -l)
CONDITION=0

while [ $CONDITION -eq 0 ]; do
	FICHERO=""
	FICHERO="$(ls -p $DIR_LIBROS | grep -v / | tail -1)"
	EXTENSION=$(echo "$FICHERO" | rev | cut -d . -f1 | rev)
	if [ $TOTAL_FICHEROS != 0 ]; then
		printf "NOMBRE FICHERO = $FICHERO selecciona el prefijo \n"

		printf "1 selecciona -  ctf_htb_walkthrough_ \n"
		printf "2 selecciona -  incibe_curso_basico_ \n"
		printf "3 selecciona -  forensics_directrices_ \n"
		printf "4 selecciona -  formarte_curso_marketing_ \n"
		printf "5 selecciona -  windows_comandos_ \n"
		printf "6 selecciona -  computing_research_project \n"
		printf "7 selecciona -  linux_ \n"
		printf "8 selecciona -  python_ \n"
		printf "9 selecciona -  bussiness_process_support_ \n"
		printf "10 selecciona - information_security_management_ \n"
		printf "11 selecciona - big_data_ \n"
		printf "12 selecciona - criptography_ \n"
		printf "13 selecciona - network_security_ \n"
		printf "/ escoge una variable!! \n"

		read SELECTION
		case $SELECTION in
		1) PREFIJO="ctf_htb_walkthrough_" ;;
		2) PREFIJO="incibe_curso_basico_" ;;
		3) PREFIJO="forensics_" ;;
		4) PREFIJO="formarte_curso_" ;;
		5) PREFIJO="windows_comandos_" ;;
		6) PREFIJO="computing_research_project_" ;;
		7) PREFIJO="linux_" ;;
		8) PREFIJO="python_" ;;
		9) PREFIJO="bussiness_process_support_" ;;
		10) PREFIJO="information_security_management_" ;;
		11) PREFIJO="big_data_" ;;
		12) PREFIJO="criptography_" ;;
		13) PREFIJO="network_security_" ;;
		/) read -p "cualquier prefijo " PREFIJO ;;
		*) echo "No has escogido ninguna opcion" ;;
		esac

		printf "PREFIJO: $PREFIJO, FICHERO: $FICHERO, continuemos con la mineria de texto \n"

		read -p "Introduce el nuevo nombre despues del prefijo de $PREFIJO" SUFIJO

		OLD_NAME="$DIR_LIBROS$FICHERO"
		NEW_NAME="$DIR_LIBROS$PREFIJO$SUFIJO.$EXTENSION"

		printf "\n Cambiando fichero de nombre!! \n"
		mv "$OLD_NAME" "$NEW_NAME"

		NOMBRE_BASE=$(basename "$NEW_NAME")

		printf "\n el nuevo nombre de tu fichero es $NOMBRE_BASE \n"

		printf "\n Vamos a mover tu fichero a la carpeta Listos \n"

		mv "$NEW_NAME" "$DIR_LISTOS"

		printf "listo!! \n"
	else
		CONDITION=1
	fi
done
