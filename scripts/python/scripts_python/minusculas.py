#!/usr/bin/python

import os
path=os.getcwd()
#print(path)
working_directory=os.listdir(path)

def cambiar_a_minusculas(working_directory):

    # Iterar sobre cada archivo en el directorio
    for I in working_directory:
        # Crear la ruta completa del archivo
        full_path = os.path.join(path,I)
        if os.path.isfile(full_path):
            new_name = I.lower()
            new_path=os.path.join(path,new_name)
            os.rename(full_path,new_path)
#            print('full path ' + full_path + ' new path ' + new_path)
#            print(f'Renombrando fichero: {I} -> {new_name}')

# Ejecutamos nuestra funcion
cambiar_a_minusculas(working_directory)

# Fin del programa!
