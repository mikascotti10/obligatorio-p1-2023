from entities.Equipos import Equipos
from entities.Pilotos import Pilotos
from entities.PilotoReserva import PilotoReserva
from entities.Mecanicos import Mecanicos
from entities.DirectorDeEquipo import DirectorDeEquipo
from entities.Autos import Autos
from random import random

class ProgramaF1:
    def __init__(self):
        self.empleados = []
        self.autos = []
        self.equipos = []

    def mostrar_menu(self):
        print("----- Menú -----")
        print("1. Alta de empleado")
        print("2. Alta de auto")
        print("3. Alta de equipo")
        print("4. Simular carrera")
        print("5. Realizar consultas")
        print("6. Finalizar programa")

    def alta_empleado(self):
        try:
            cedula = int(input("Ingrese cedula:"))
            nombre = input("Ingrese nombre:")
            nacimiento = input("Ingrese fecha de nacimiento:")
            nacionalidad = input("Ingrese nacionalidad:")
            salario = int(input("Ingrese salario:"))
            cargo = int(input("Ingrese cargo: (1-piloto titular, 2-piloto de reserva, 3-mecanico, 4-jefe de equipo)"))
            if (cargo == 1) or (cargo == 2):
                numero_de_auto = int(input("Ingrese numero de auto:"))
                score = int(input("Ingrese score:"))
            if cargo == 2:
                score = int(input("Ingrese score:"))
        except Exception as e:
            print(f"Error: {e}")

    def alta_auto(self):
        try:
            modelo = input("Ingrese modelo:")
            anio = int(input("Ingrese año:"))
            score = int(input("Ingrese score:"))
        except Exception as e:
            print(f"Error: {e}")

    def alta_equipo(self):
        try:
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
        except Exception as e:
            print(f"Error: {e}")

    def simular_carrera(self):
        try:
            # Lógica para simular la carrera
            pilotos_carrera = []
            for equipo in self.equipos:
                if not equipo.pilotos_titulares[0].lesionado:
                    pilotos_carrera.append(equipo.pilotos_titulares[0])
                elif not equipo.pilotos_titulares[1].lesionado:
                    pilotos_carrera.append(equipo.pilotos_titulares[1])
                elif equipo.piloto_reserva:
                    pilotos_carrera.append(equipo.piloto_reserva)

            for piloto in pilotos_carrera:
                # Simulación de imprevistos
                if random() < 0.1:  # Probabilidad de lesión
                    piloto.lesionado = True
                if random() < 0.2:  # Probabilidad de abandono
                    pilotos_carrera.remove(piloto)
                if random() < 0.15:  # Probabilidad de error en pits
                    piloto.score -= 5
                if random() < 0.1:  # Probabilidad de penalidad
                    piloto.score -= 8

            # Calcular puntaje final
            for piloto in pilotos_carrera:
                suma_score_mecanicos = sum([mecanico.score for mecanico in piloto.equipo.mecanicos])
                score_final = suma_score_mecanicos + piloto.equipo.modelo_auto.score + piloto.score

                if piloto.lesionado or piloto not in pilotos_carrera:
                    score_final = 0

                piloto.score_final = score_final

            # Ordenar pilotos por score_final en orden descendente
            pilotos_carrera.sort(key=lambda x: x.score_final, reverse=True)

            # Asignar puntos a los pilotos según su posición en la carrera
            puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
            for i, piloto in enumerate(pilotos_carrera):
                if i < len(puntos):
                    piloto.puntaje_campeonato += puntos[i]

            # Restaurar estado de lesiones
            for piloto in pilotos_carrera:
                piloto.lesionado = False

            return pilotos_carrera

        except Exception as e:
            print(f"Error: {e}")

#Consultas
    def top_10_pilotos_mas_puntos(pilotos):
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.puntaje_campeonato, reverse=True)
        return pilotos_ordenados[:10]

    def resumen_campeonato_constructores(equipos):
        resumen = {}
        for equipo in equipos:
            puntos_equipo = sum(piloto.puntaje_campeonato for piloto in equipo.pilotos_titulares + [equipo.piloto_reserva] if piloto)
            resumen[equipo.nombre] = puntos_equipo
        return dict(sorted(resumen.items(), key=lambda x: x[1], reverse=True))

    def top_5_pilotos_mejor_pagados(pilotos):
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.salario, reverse=True)
        return pilotos_ordenados[:5]

    def top_3_pilotos_mas_habilidosos(pilotos):
        pilotos_ordenados = sorted(pilotos, key=lambda piloto: piloto.score, reverse=True)
        return pilotos_ordenados[:3]

    def retornar_jefes_de_equipo(equipos):
        jefes = [(equipo.director.nombre, equipo.nombre) for equipo in equipos]
        return sorted(jefes, key=lambda x: x[0])

    def realizar_consultas(self):
        print("1. Top 10 pilotos con más puntos en el campeonato")
        print("2. Resumen campeonato de constructores (equipos).")
        print("3. Top 5 pilotos mejores pago")
        print("4. Top 3 pilotos más habilidosos")
        print("5. Retornar jefes de equipo")
        opcion = int(input("Seleccionar consulta: "))
        if opcion == 1:
            print(top_10_pilotos_mas_puntos(pilotos_carrera))
        if opcion == 2:
            print(resumen_campeonato_constructores(pilotos_carrera))
        if opcion == 3:
            print(top_5_pilotos_mejor_pagados(pilotos_carrera))
        if opcion == 4:
            print(top_3_pilotos_mas_habilidosos(pilotos_carrera))
        if opcion == 5:
            print(retornar_jefes_de_equipo(self.equipos))



    def ejecutar_programa(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.alta_empleado()
            elif opcion == '2':
                self.alta_auto()
            elif opcion == '3':
                self.alta_equipo()
            elif opcion == '4':
                resultado_carrera = self.simular_carrera()
                print("Posiciones finales en la carrera:")
                for i, piloto in enumerate(resultado_carrera):
                    print(f"{i+1}. {piloto.nombre} - Puntos: {piloto.puntaje_campeonato}")
            elif opcion == '5':
                self.realizar_consultas()
            elif opcion == '6':
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Ingrese un número del 1 al 6.")


if __name__ == "__main__":
    programa = ProgramaF1()
    programa.ejecutar_programa()
