# Polimorfismo
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

#esta es la funcion clave para que el concepto se de        
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Moto()

desplazamientoVehiculo(miVehiculo)