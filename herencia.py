# que caracteristicas y comportamientos tienen en comun los objetos? clase padre u super clases

class Vehiculos():
 
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo} \nEnmarcha: {self.enmarcha} \nAcelerando: {self.acelera}\nFrenando: {self.frena}\n ")

#herencia
class Moto(Vehiculos):

    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
        self.cantidadPasajeros = 2
        self.hcaballito = False
    
    def caballito(self):
        self.hcaballito = True
#sobreescritura de metodos
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo} \nEnmarcha: {self.enmarcha} \nAcelerando: {self.acelera}\nFrenando: {self.frena}\nCaballito: {self.hcaballito} ")

class furgoneta(Vehiculos):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
        self.cargado = False

    def carga(self):
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Velectricos(Vehiculos):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True



miMoto = Moto("honda", "cbr")
miMoto.estado()
miMoto.frenar()
miMoto.estado()
miMoto.caballito()
miMoto.estado()
print(f"Pasajeros:{miMoto.cantidadPasajeros}")

furgoneta1 = furgoneta("Ford", "kidw")
print(furgoneta1.carga())
furgoneta1.estado()

class BicicletaElectrica(Velectricos, Vehiculos):
    pass
# esto genera un error por que toma el constructor de la clase que esta a la izquierda en este caso Velectricos, la cual no pide parametros al momento de crear el objeto
miBici = BicicletaElectrica("marca", "modelo")
# miBici = BicicletaElectrica()
miBici.estado()

# principio de sustitucion "es siempre un/a"
# un empleado es una persona, pero una persona NO siempre es un empleado.
# para verificar que una objeto pertenece a una clase podemos usar isinstance
print(isinstance(miBici, BicicletaElectrica))