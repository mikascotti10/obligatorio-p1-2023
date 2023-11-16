class Autos():
    def __init__(self, modelo, anio, score):
        self.modelo = modelo
        self.anio = anio
        self.score = score
    
    @property
    def modelo(self):
        return self.modelo
    
    @property
    def anio(self):
        return self.anio
    
    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, valor):
        self.score = valor

    