# listas
# se crea la lista
miLista = ['texto', 5, True]
print(miLista)

# se agrega un dato
miLista.append("datoNuevo")
print(miLista)

# se inserta un dato en una posicion determinada
miLista.insert(0, False)
print(miLista)

# se quita el primer item de la lista 
miLista.remove(False)
print(miLista)

# Tuplas
miTupla = (1, 2, 3, 4, 5)

# desempaquetado de tupla
mitupla = ("luis", "pacheco", 13, 1, 2024 )
nombre, apellido, dia, mes, agno = mitupla
# pasa variable valor en el orden que se de.
print(F"Bienvenido {nombre} {apellido}, hoy {dia}/{mes}/{agno}, ha sido registrado con exito")


# Diccionarios
agenda = {'danilo': 3156669999, 'camilo': 3105556666}
print(agenda)
print(agenda['danilo'])
print('camilo' in agenda)
print(sorted(agenda))




