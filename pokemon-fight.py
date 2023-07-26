import random

VIDA_INICIAL_PIKAHCU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKAHCU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:


    #Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10

    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKAHCU)
    print("Pikachu:    [{}{}]".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu)))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}]".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle)))

    print("La vida de Pikachu es {}, la vida de Squirtle es {}".format(vida_pikachu, vida_squirtle))

    input("Enter para continuar...\n\n")

    #Turno de Squirtle
    print("Turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja\n")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9

    print("La vida de Pikachu es {}, la vida de Squirtle es {}".format(vida_pikachu, vida_squirtle))

    input("Enter para continuar...\n\n")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana")
else:
    print("Squirtle gana")
