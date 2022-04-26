from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__( nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(self):
        return len(Reptil._listado)
    @classmethod
    def crearIguana(self, nombre, edad , genero):
        Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
    @classmethod
    def crearSerpiente(self, nombre, edad , genero):
        Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1