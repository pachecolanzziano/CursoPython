#codificar una lista a codigo binario
import pickle

# lista_nombre = ["Pedro", "Ana", "Maria", "Isabel"]
# fichero_binario = open("listaNombre", "wb")
# pickle.dump(lista_nombre, fichero_binario)
# fichero_binario.close()
# del(fichero_binario)

#leer la lista codificada
fichero_binario = open("listaNombre", "rb")
lista = pickle.load(fichero_binario)
print(lista)