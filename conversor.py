
euro_dolar = 1.00
dolar_euro = 1.00
libra_euro = 1.19
euro_libra = 0.84
libra_dolar = 1.19
dolar_libra = 0.84

divisa = input("Que divisa es la que tienes? E, euro; L, libra; D, dolar \n")
divisa_cambio = input("A que divisa deseas cambiar? EU, LI, DO \n")

#Conversiones de misma divisa
if (divisa == "E" and divisa_cambio == "EU"):
    print("No puedes convertir la misma divisa")
    exit()

elif (divisa == "L" and divisa_cambio == "LI"):
    print("No puedes convertir la misma divisa")
    exit()

elif (divisa == "D" and divisa_cambio == "DO"):
    print("No puedes convertir la misma divisa")
    exit()

cantidad = int(input("Cuanta cantidad tienes? \n"))


#Euros a lib/dol
if (divisa == "E" and divisa_cambio == "LI"):
    print("Tu cantidad de libras es: {}" .format(cantidad * euro_libra))

elif (divisa == "E" and divisa_cambio == "DO"):
    print("Tu cantidad de dolares es: {}" .format(cantidad * euro_dolar))

#Libras a eur/dol
elif (divisa == "L" and divisa_cambio == "EU"):
    print("Tu cantidad de euros es: {}" .format(cantidad * libra_euro))

elif (divisa == "L" and divisa_cambio == "DO"):
    print("Tu cantidad de dolares es: {}" .format(cantidad * libra_dolar))

#Dolares a eur/lib
elif (divisa == "D" and divisa_cambio == "EU"):
    print("Tu cantidad de euros es: {}" .format(cantidad * dolar_euro))

elif (divisa == "D" and divisa_cambio == "LI"):
    print("Tu cantidad de libras es: {}" .format(cantidad * dolar_libra))

