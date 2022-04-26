from zooAnimales.animal import Animal
class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__( nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    @classmethod
    def cantidadAves(self):
        return len(Ave._listado)
    @classmethod
    def crearHalcon(self, nombre, edad , genero):
        Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
    @classmethod
    def crearAguila(self, nombre, edad , genero):
        Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1