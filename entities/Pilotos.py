from Empleados import Empleados

class Pilotos(Empleados):
    def __init__(self, id, nombre, fecha_de_nacimiento, nacionalidad, salario, score, numero_de_auto, puntaje, lesion, titular, suplente):
        super().__init__(id, nombre, fecha_de_nacimiento, nacionalidad, salario)
        self._score = score
        self._numero_de_auto = numero_de_auto
        self._puntaje = puntaje
        self._lesion = lesion
        self._titular = titular
        self._suplente = suplente

        

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
    
    @property
    def titular(self):
        return self.titular
    
    @property
    def suplente(self):
        return self.suplente
    
    @puntaje.setter
    def puntaje(self, valor):
        self.puntaje = valor

    @score.setter
    def score(self, valor):
        self.score = valor
    
    @lesion.setter
    def lesion(self, x):
        self.lesion = x







