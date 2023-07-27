import re

cadena="Estoy trabajando con Python en domingo y Semana Santa"

busqueda="domingo"

if re.search(busqueda,cadena) is not None:
    
    print("Se encontro el termino ", busqueda)
    
else:
    
    print("No se encontro el termino ", busqueda)
    
# -----------------------------------------------------

import re

cadena="Estoy trabajando con Python en domingo y Semana Santa. El proximo domingo no pienso grabar ningun video"

busqueda="domingo"

print(re.findall(busqueda, cadena))

print(len(re.findall(busqueda, cadena)))

text_encontrado=re.search(busqueda, cadena)

print(text_encontrado.start())

print(text_encontrado.end())

print(text_encontrado.span())

# --------------------------------------------------

import re

lista_nombres=["Antonio Banderas", "Salma Hayek", "Tomas Cruceros", "Antonio Resines", "Friedrich Hayek"]

for nombre in lista_nombres:
    if re.findall("^Antonio", nombre):
        print(nombre)
        
for nombre in lista_nombres:
    if re.findall("Hayek$", nombre):
        print(nombre)

# --------------------------------------------------

import re

lista_nombres=["http://www.pildorasinformaticas.es", "ftp://www.pildorasinformaticas.es", "http://www.pildorasinformaticas.com", "ftp://www.pildorasinformaticas.com",]

for nombre in lista_nombres:
    if re.findall("^ftp", nombre):
        print(nombre)
        
for nombre in lista_nombres:
    if re.findall(".es$", nombre):
        print(nombre)
        
# --------------------------------------------------

import re

lista_terminos=["camión", "camion", "niños", "niñas", "ejemplo"]

for termino in lista_nombres:
    if re.findall("cami[oó]n", termino):
        print(termino)
        
for termino in lista_nombres:
    if re.findall("niñ[oa]s", termino):
        print(termino)
        
for termino in lista_nombres:
    if re.findall("[p-z]", termino):
        print(termino)
        
for termino in lista_nombres:
    if re.findall("^[a-f]", termino):
        print(termino)
        
for termino in lista_nombres:
    if re.findall("^[A-F]", termino):
        print(termino)
        
for termino in lista_nombres:
    if re.findall("^[l-p]$", termino):
        print(termino)
        
# ----------------------------------------------------

import re

lista_terminos=["Ma:1", "Se1", "Ma2", "Va1", "Ba1", "Se2", "Ma.3", "Ma4", "Se3", "SeA", "SeB", "Va2", "SeC"]

for termino in lista_terminos:
    if re.findall("Ma[1-3]", termino):
        print(termino)

for termino in lista_terminos:
    if re.findall("Se[0-2A-B]", termino):
        print(termino)
        
for termino in lista_terminos:
    if re.findall("Ma[.:]", termino):
        print(termino)

# -----------------------------------------------------

import re

nombre1="Lara Lopez"

nombre2="Juan Diaz"

nombre3="Jara Martin"

if re.match("Juan", nombre3, re.IGNORECASE):
    
    print("He encontrado la persona")
    
else:
    
    print("No he encontrado la persona")
    
if re.match(".ara", nombre3, re.IGNORECASE):
    
    print("He encontrado la persona2")
    
else:
    
    print("No he encontrado la persona2")
    
if re.search("Lopez", nombre1):
    
    print("He encontrado la persona3")
    
else:
    
    print("No he encontrado la persona3")
    
# --------------------------------------------------

import re

codigo1="efbounhsfuoibnnfgdgsuio255sdfvbnkjlbsf"

codigo2="khjbvsdckhjbvsdk133svjlkbnnvsfbsdvnlsv"

codigo3="iuhbsdv255ojnvdskjvbndsojlvbodsbnosdv"

if re.search("255", codigo1):
    
    print("He encontrado el numero")
    
else:
    
    print("No he encontrado el numeero")
    
    
