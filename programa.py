from entities.Pilotos import Pilotos
from entities.Autos import Autos
from entities.Equipos import Equipos
from entities.DirectorDeEquipo import DirectorDeEquipo
from entities.Mecanicos import Mecanicos
from exceptions.entidad_no_existe import EntidadNoExiste
from exceptions.entidad_ya_existe import EntidadYaExiste
from exceptions.informacion_invalida import InformacionInvalida
from entities.Empleados import Empleados

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

        def registrar_piloto(self, score, nombre, nacimiento, nacionalidad, numero_de_auto, puntaje, lesion, titular, suplente, salario, id):
            if self.es_vacio(score) or self.es_vacio(numero_de_auto) or self.es_vacio(puntaje) or self.es_vacio(lesion) or titular.type() !=bool  or suplente.type() !=bool:
                    raise InformacionInvalida()
            new_piloto = Pilotos(id, nombre, nacimiento, nacionalidad, salario, score, numero_de_auto, puntaje, lesion, titular, suplente)
            if titular==True and suplente==False :
                self._pilotos_titulares.append(new_piloto)
            
            if titular==False and suplente==True :
                self._pilotos_suplentes.append(new_piloto)
            
            else:
                raise InformacionInvalida()
        

                
        def registrar_equipo(self, nombre, pilotos: list, mecanicos: list, director: list, auto):
            new_equipo = Equipos(nombre, pilotos, mecanicos, director, auto)
            self._equipos.append(new_equipo)

            
        def registrar_mecanico(self, score, id, nombre, nacimiento, nacionalidad, salario):
            if self.es_vacio(score) or (score is not int):
                raise InformacionInvalida()
            new_mecanico = Mecanicos(id, nombre, nacimiento, nacionalidad, salario, score)
            self._mecanicos.append(new_mecanico)

        def registrar_director(self, id, nombre, nacimiento, nacionalidad, salario):
            new_director = DirectorDeEquipo(id, nombre, nacimiento, nacionalidad, salario)
            self._Directores_equipos.append(new_director)

        


                  

         
















def alta_empleado():
    cedula = int(input("Ingrese cedula:"))
    nombre = input("Ingrese nombre:")
    nacimiento = input("Ingrese fecha de nacimiento:")
    nacionalidad = input("Ingrese nacionalidad:")
    salario = int(input("Ingrese salario:"))
    cargo = int(input("Ingrese cargo: (1-piloto titular, 2-piloto de reserva, 3-mecanico, 4-jefe de equipo)"))
    if (cargo == 1) or (cargo == 2)
        numero_de_auto = int(input("Ingrese numero de auto:"))
        score = int(input("Ingrese score:"))
    if cargo == 2:
        score = int(input("Ingrese score:"))

def alta_auto():
    modelo = input("Ingrese modelo:")
    anio = int(input("Ingrese año:"))
    score = int(input("Ingrese score:"))

def alta_equipo():
    nombre = input("Ingrese nombre del equipo:")
    modelo = input("Ingrese modelo de auto:")
    cedula1 = int(input("Ingrese cédula de piloto titular:"))
    cedula2 = int(input("Ingrese cédula de piloto titular:"))
    cedula3 = int(input("Ingrese cédula de piloto suplente:"))
    cedula4 = int(input("Ingrese cédula de director de equipo:"))
    cedula5 = int(input("Ingrese cédula de mecánico:"))
    cedula6 = int(input("Ingrese cédula de mecánico:"))
    cedula7 = int(input("Ingrese cédula de mecánico:"))
    cedula8 = int(input("Ingrese cédula de mecánico:"))
    cedula9 = int(input("Ingrese cédula de mecánico:"))
    cedula10 = int(input("Ingrese cédula de mecánico:"))
    cedula11 = int(input("Ingrese cédula de mecánico:"))
    cedula12 = int(input("Ingrese cédula de mecánico:"))


if __name__ == "__main__":
    while(True):
        print("- 1 alta de piloto")
        print("- 2 alta de ")
        opcion = input()
        if(opcion == 1):
