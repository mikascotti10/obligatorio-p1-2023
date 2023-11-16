from abc import ABC, abstractmethod

class Empleados(ABC):
    def __init__(self, id, nombre, fecha_de_nacimiento, nacionalidad, salario):
        if (id is int) and (len(id) == 8):
            self._id = id
        self._fecha_de_nacimiento = fecha_de_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario

    @property
    def id(self):
        return self.id
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def fecha_de_nacimiento(self):
        return self.fecha_de_nacimiento
    
    @property
    def nacionalidad(self):
        return self.nacionalidad
    
    @property
    def salario(self):
        return self.salario
    
    @salario.setter
    def salario(self, valor):
        self.salario = valor

    
    
    
    
    
    
        

