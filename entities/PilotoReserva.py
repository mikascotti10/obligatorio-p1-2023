from entities.Empleados import Empleados

class PilotoReserva(Empleados):
    def __init__(self, id, nombre, fecha_de_nacimiento, nacionalidad, salario, score, numero_de_auto, puntaje, lesion):
        super().__init__(id, nombre, fecha_de_nacimiento, nacionalidad, salario)
        self._score = score
        self._numero_de_auto = numero_de_auto
        self._puntaje = puntaje
        self._lesion = lesion

    @property
    def score(self):
        return self.score

    @property
    def numero_de_auto(self):
        return self.monumero_de_auto
    
    @property
    def puntaje(self):
        return self.puntaje
    
    @property
    def lesion(self):
        return self.lesion
    
    
    @puntaje.setter
    def puntaje(self, valor):
        self.puntaje = valor

    @score.setter
    def score(self, valor):
        self.score = valor
    
    @lesion.setter
    def lesion(self, x):
        self.lesion = x