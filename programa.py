from entities.Pilotos import PilotosDeReserva
from entities.Pilotos import PilotosTitulares
from entities.Autos import Autos
from entities.Equipos import Equipos
from entities.DirectorDeEquipo import DirectorDeEquipo
from entities.Mecanicos import Mecanicos
from exceptions.entidad_no_existe import EntidadNoExiste
from exceptions.entidad_ya_existe import EntidadYaExiste
from exceptions.informacion_invalida import InformacionInvalida

class ProgramaF1:
    def __init__(self):
        self._equipos=[]
        self._pilotos_titulares = []
        self._pilotos_suplentes=[]
        self._mecanicos=[]
        self._Directores_equipos=[]

        
        

        def es_vacio(self, dato):
            if dato == "" or dato < 0:
                return True

    def registrar_piloto(self,score, numero_de_auto, puntaje, lesion, titular, suplente):
        if self.es_vacio(score) or self.es_vacio(numero_de_auto) or self.es_vacio(puntaje) or self.es_vacio(lesion) or titular.type() !=bool  or suplente.type() !=bool:
                raise InformacionInvalida()
        
        if titular==True and suplente==False :
             piloto=piloto
             piloto.Set(score,numero_de_auto, puntaje, lesion, titular, suplente)
             self._pilotos_titulares.append(piloto)
        
        if titular==False and suplente==True :
             piloto=piloto
             piloto.Set(score,numero_de_auto, puntaje, lesion, titular, suplente)
             self._pilotos_suplentes.append(piloto)
        
        else:
             raise InformacionInvalida()
        
    def registrar_mecanico(self, score):
         if self.es_vacio(score) or (score is not int):
            raise InformacionInvalida()
         
         mecanico = mecanico
         mecanico.Set(score)
         self._mecanicos.append(mecanico)



                  

         




















class __name__ == "__main__"