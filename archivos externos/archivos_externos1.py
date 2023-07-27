
# Para crear y escribir en un archivo por primera vez

from io import open

archivo_externo=open("primeroArchivo.txt", "w")

archivo_externo.write("Bienvenidos a los archivos externos")

archivo_externo.close()

# ------------------------------------------

# Para anadir/escribir texto/informacion en un documento ya creado

from io import open

archivo_externo=open("primeroArchivo.txt", "a")

archivo_externo.write("\n Guardamos informacion de forma permanente")

archivo_externo.close()

# -----------------------------------------------

# Para leer archivos

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

informacion=archivo_externo.read()

archivo_externo.close()

print(informacion)

# ------------------------------------------------

# Imprime por la terminal la primera linea

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

informacion_lineas=archivo_externo.readline()

archivo_externo.close()

print(informacion_lineas)

# --------------------------------------------------

# Imprime por la terminal todas las lineas // Las guarda como una lista

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

informacion_lineas=archivo_externo.readlines()

archivo_externo.close()

print(informacion_lineas)

# --------------------------------------------------

# Imprime por la terminal la linea/s que deseas entre todas las lineas

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

informacion_lineas=archivo_externo.readlines()

archivo_externo.close()

print(informacion_lineas[0])

# ------------------------------------------------

# seek mueve el cursor al caracter que deseemos, cada numero es un caracter

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

print(archivo_externo.read())

archivo_externo.seek(4)

print(archivo_externo.read())

# ------------------------------------------------

# read con un numero mostrara por pantalla el numero de caracteres que desees en este caso los 6 primeros, "bienve"

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

print(archivo_externo.read(6))

# ------------------------------------------------

# el logaritmo del seek hara que el cursor empiece en la mitad del archivo/texto

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

archivo_externo.seek(len(archivo_externo())/2)

print(archivo_externo.read())

# ------------------------------------------------

# suprimira la primera linea e imprimira el resto

from io import open

archivo_externo=open("primeroArchivo.txt", "r")

archivo_externo.seek(len(archivo_externo.readline()))

print(archivo_externo.read())

# ------------------------------------------------

# r+ hara que puedas leer y escribir en el documento

from io import open

archivo_externo=open("primeroArchivo.txt", "r+")

lista_archivo=archivo_externo.readlines()

lista_archivo[1]="Hoy es viernes y ya llega el ansiado fin de semana \n"

archivo_externo.seek(0)

archivo_externo.writelines(lista_archivo)

archivo_externo.close()

print(archivo_externo)






