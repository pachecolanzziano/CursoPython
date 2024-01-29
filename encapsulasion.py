class Articulo():
    def __init__(self):
        self.nombre = ""
        self.__precio = 10
        self.estado = False
    
    def cambiarNombre(self, nombre):
        self.nombre = nombre
        
    def cambiarPrecio(self, precio):
        self.__precio = precio
        
    def cambiarEstado(self, estado):
        self.estado = estado
    
    def estadoActual(self):
        if self.estado:
            print("articulo disponible")
        else:
            print("Articulo no disponible")
    
    def getPrecio(self):
        return self.__precio
            
pc = Articulo()
print(pc.nombre)
pc.nombre = "PC"
print(pc.nombre)
print(pc.getPrecio())

print("----------- Objeto 2 -------")

teclado = Articulo()
teclado.nombre = "Teclado"
print(teclado.nombre)
teclado.cambiarPrecio(1000)
print(teclado.getPrecio())

