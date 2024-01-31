import pickle

class Persona:

    
    def __init__(self, nombre, genero, edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("se ha creado una persona nueva con el nombre de ",self.nombre)

#esto se muestra al instanciar un objeto tipo persona        
    def __str__(self) -> str:
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []
    
    def __init__(self) -> None:
        listaPersonas = open("ficheroExterno","ab+")
        listaPersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaPersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
            
        except:
            print("El fichero esta vacio")
        
        finally:
            listaPersonas.close()
            del(listaPersonas)
    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
    
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)
    
    def guardarPersonasEnFicheroExterno(self):
        #abre el documento y lo prepara para escribir bit
        listaDePersonas = open("ficheroExterno","wb")
        #con la libreria pickle serializa el objeto personas(la lista)
        #y la almacena en binarios en listaDePersonas
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
        
    def mostrarInfoFicheroExterno(self):
        print("la información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)
                    
miLista = ListaPersonas()
p = Persona("Nadia", "Femenino", "34")
miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()





