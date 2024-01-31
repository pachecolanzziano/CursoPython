from io import open_code
# Modo escritura
# archivo_texto = open("archivo.txt", "w")
# frase = "Hola mundo \n Mi nombre es Lucas \n Estoy aprendiendo Python"
# archivo_texto.write(frase)
# archivo_texto.close()

#Modo escritura
# archivo_texto = open("archivo.txt", "r")
# texto = archivo_texto.read()
# archivo_texto.close()
# print(texto)

# readLines -> lee y crea una lista con el contenido del archivo
# archivo_texto = open("archivo.txt", "r")
# texto = archivo_texto.readlines()
# archivo_texto.close()
# print(texto[0])

# añade una linea
archivo_texto = open("archivo.txt", "a")
archivo_texto.write("\n siempre es una buena ocasión para aprender Python")
archivo_texto = open("archivo.txt", "r")
texto = archivo_texto.readlines()
archivo_texto.close()
print(texto)


