from zooAnimales.animal import Animal
class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    
    @classmethod
    def cantidadPeces(self):
        return len(Pez._listado)
    @classmethod
    def crearSalmon(self, nombre, edad , genero):
        Pez( nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
    @classmethod
    def crearBacalao(self, nombre, edad , genero):
        Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1