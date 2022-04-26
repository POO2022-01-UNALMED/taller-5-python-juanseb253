class Zoologico:
    def __init__(self, nombre, ubiacion):
        self._nombre = nombre
        self._ubicacion = ubiacion
        self._zonas = []

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getZonas(self):
        return self._zonas
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        e = 0
        for i in self._zonas:
            e += i.cantidadAnimales()
        return e

