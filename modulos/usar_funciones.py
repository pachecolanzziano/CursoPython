#primera manera de importar
# import funciones_matematicas
# funciones_matematicas.sumar(2,3)
# funciones_matematicas.restar(2,3)
# funciones_matematicas.multiplicar(2,3)

#segunda forma de importar -> especificamos que queremos importar
# from funciones_matematicas import sumar, restar, multiplicar 

#tercera forma de importar -> especificamos que importe todo con el comodin *
from funciones_matematicas import *
from moduloCoche import *
#acá trabajamos con el modulo de funciones matematicas
sumar(2,3)
restar(2,3)
multiplicar(2,3)

#acá trabajamos con la clase Coche para instanciar objetos tipo coche

miCoche = Coche()
print(miCoche.estado())

