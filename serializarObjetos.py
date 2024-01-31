import pickle

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
        
coche1 = Vehiculos("honda", "civic")
coche2 = Vehiculos("renult", "spark")
coche3 = Vehiculos("kia", "picanto")
coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero)


fichero = open("losCoches", "rb")
listaCoches = pickle.load(fichero)
fichero.close()

for coche in listaCoches:
    print(coche.estado())

