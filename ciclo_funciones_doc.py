# Ciclos
frutas = ['Fresa', 'Pera', 'Piña', 'Naranja']

for fruta in frutas:
    print(fruta, len(fruta))

# funciones
def suma(num1, num2):
    print(num1 + num2)
    
def resta(num1, num2):
    return (num1 - num2)

# Documentacion
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#consejo: 78 caracteres max por linea segun la PEP8