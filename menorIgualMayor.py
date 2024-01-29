def suma( a, b ):
    return (a + b)
    
numero1 =int(input("Ingresa el primer valor: ")) 
numero2 =int(input("Ingresa el segundo valor: ")) 
rta = suma(numero1, numero2)

if rta > 10:
    print(f'{rta} es mayor a 10')
elif rta == 10:
    print(f'{rta} es igual a 10')
else:
    print(f'{rta} es menor a 10')
    