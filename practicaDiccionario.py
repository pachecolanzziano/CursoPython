midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino unido": "Londres", "España":"Madrid"}
print(midiccionario["Francia"])
#adiciona un elemento clave : valor a un diccionario 
midiccionario["Colombia"] = "Bogota"
print(midiccionario)
#Eliminar un elemento clave:valor con del
del midiccionario["Reino unido"]
print(midiccionario)
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

