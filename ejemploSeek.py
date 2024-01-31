from io import open

# archivo_texto = open("archivo.txt", "r")
# print(archivo_texto.read())
# # archivo_texto.seek(0)
# archivo_texto.seek(2)
# print(archivo_texto.read())

archivo_texto = open("archivo.txt", "r+")
lista_texto = archivo_texto.readlines()
lista_texto[1] = "esta linea ha sido incluida dede el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()