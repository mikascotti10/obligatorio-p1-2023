from Empleados import Empleados
from Autos import Autos 

class Equipos:
    def __init__(self, nombre, pilotos: list, mecanicos: list, director: list, auto):
        #empleado 1, empleado 2, empleado 3, empleado 4, ..., empleado 8 (?)
        self._nombre = nombre
        self._pilotos = [pilotos]
        self._mecanicos = [mecanicos]
        self._director = [director]
        self._auto = auto


    @property
    def nombre(self):
        return self.nombre
    
    @property
    def empleados(self):
        return self.empleados
    
    @property
    def auto(self):
        return self.auto
    
    @empleados.setter
    def empleados(self, nuevoempleado):
        self.empleados = nuevoempleado

    
    @auto.setter
    def auto(self, nuevoauto):
        self.auto = nuevoauto

    
    
    