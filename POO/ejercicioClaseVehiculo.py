"""
5 - Clase Vehiculo y Coche:

Crea una clase Vehiculo con atributos como marca, modelo y año.
Implementa un método mostrar_detalles() que imprima estos atributos.
Crea una subclase Coche que herede de Vehiculo y agregue un atributo numero_puertas.
Sobrescribe o extiende el método mostrar_detalles() en Coche para incluir el número de puertas.
"""


class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def mostrar_detalles(self):
        print(f'''Marca: {self._marca}
Modelo: {self._modelo}
Año de fabricación: {self._anio}''')


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self._cant_puertas = puertas

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f'Número de puertas: {self._cant_puertas}\n')


# main
auto1 = Auto('Ford', 'Fiesta', 2010, 4)
auto2 = Auto('VolksWagen', 'Gol', 2006, 2)
auto1.mostrar_detalles()
auto2.mostrar_detalles()
