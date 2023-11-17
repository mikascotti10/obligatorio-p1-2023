from entities.Empleados import Empleados
from entities.Autos import Autos 

class Equipos:
    def __init__(self, nombre, pilotos: list, mecanicos: list, director: list, auto):
        self._nombre = nombre
        self._pilotos = [pilotos]
        self._mecanicos = [mecanicos]
        self._director = [director]
        self._auto = auto
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def asignar_auto(self, auto):
        self.auto = auto


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

    
    
    