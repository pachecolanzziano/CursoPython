class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha = True
    
    def parar(self):
        self.enmarcha = False
    
    def estado(self):
        if(self.enmarcha):
            return "El Coche está en marcha"
        else:
            return "El Coche está parado"

