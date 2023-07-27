from sumar import *
from restar import *
from multiplicar import *
from dividir import *

operacion = input("Que operacion deseas hacer? (S/R/M/D): ")

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if operacion=="S":
    print(sumar(num1, num2))
elif operacion=="R":
    print(restar(num1, num2))
elif operacion=="M":
    print(multiplicar(num1, num2))
elif operacion=="D":
    print(dividir(num1, num2))
else:
    print("No existe esa operacion")
