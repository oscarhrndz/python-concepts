# import os 

# os.makedirs("PruebaDirectorio")     # crea un directorio/carpeta

# os.chdir("PruebaDirectorio")        # nos mueve al directorio PruebaDirectorio
# print(os.getcwd())      # imprime el nombre del directorio donde estamos

# ----------------------------------

# crea un directorio y un archivo .txt

# import os
# import io

# os.makedirs("PracticaDirectorio")

# os.chdir("PracticaDirectorio")

# archivo_externo=open("Ejemplo.txt", "w")

# archivo_externo.write("Texto de ejemplo...")

# print(os.getcwd())

# print(os.listdir("./"))

# --------------------------------------

# cambia el nombre Ejemplo.txt a Archivo a eliminar.txt

# import os
# import io

# os.chdir("PracticaDirectorio2")

# os.rename("Ejemplo.txt", "Archivo a eliminar.txt")

# print(os.getcwd())

# print(os.listdir("./"))

# -----------------------------------------------

# elimina el archivo

# import os
# import io

# os.chdir("PracticaDirectorio2")

# os.remove("Archivo a eliminar.txt")

# print(os.getcwd())

# print(os.listdir("./"))

# -------------------------------------------------

# elimina el directorio (solo si esta vacio/sin archivos)

# import os
# import io

# os.chdir("PracticaDirectorio2")

# os.remove("Ejemplo.docx")

# os.chdir("../")

# os.rmdir("PracticaDirectorio2")

# ------------------------------------------------------

# muestra los archivos de el directorio y elimina tirar.py

import os
import io

listaArchivos=os.listdir("./")

for archivo in listaArchivos:
    
    if archivo=="tirar.py":
        
        os.remoev(archivo)