from Empleados import Empleados

class Mecanicos(Empleados):
    def __init__(self, id, nombre, fecha_de_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_de_nacimiento, nacionalidad, salario)
        self._score = score

    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, valor):
        self.score = valor

    
    