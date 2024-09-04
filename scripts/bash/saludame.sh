#!/bin/bash -li
function saludame() {
    echo "Hola $USER"; # comillas normales acepta variables
    echo "Este es tu path $PATH";
    echo 'Tus alias son: '; # comillas simples es un comentario
    alias ;
	echo "#===================#"
    export alias prueba="date";
    alias
	echo "#===================#"	
}
saludame 
alias 
