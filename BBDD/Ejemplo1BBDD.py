import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()
#esta instruccion no se debe ejecutar varias veces ya que estaria creando la tabla repetidamente, lo que genera un error
# miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

# variosProductos = [
#     ("CAMISETA", 10, "DEPORTES"),
#     ("JARRON", 90, "CERAMICA"),
#     ("CAMIÓN", 20, "JUGUETERÍA")
# ]
#INSERTAR VARIOS DATOS DE UN ITERABLE
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
#se genera la consulta o la query
miCursor.execute("SELECT * FROM PRODUCTOS")
#con el metodo fetchall se generea una LISTA de los resultados de la query
variosProductos = miCursor.fetchall()

for item in variosProductos:
    print(item[0])
    print(item[1])
    print(item[2])





#Confirmar los cambios de la tabla
miConexion.commit()

miConexion.close()