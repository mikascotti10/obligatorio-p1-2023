from Empleados import Empleados

class DirectorDeEquipo(Empleados):
    def __init__(self, id, nombre, fecha_de_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_de_nacimiento, nacionalidad, salario)
        pass


    