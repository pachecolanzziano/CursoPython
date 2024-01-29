import math

def calcularRaiz(num1):
    if num1<0:
        raise ValueError ("el numreo no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("introduce un número: "))

try:
    print(calcularRaiz(op1))
except ValueError as errorDeNumeroNegativo:
    print(errorDeNumeroNegativo)

print("Programa Terminado")