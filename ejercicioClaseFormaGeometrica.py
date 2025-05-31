"""
6 - Clase FormaGeometrica y Polimorfismo:

Define una clase base FormaGeometrica con un método calcular_area() que lance una excepción NotImplementedError.
Crea subclases como Circulo y Cuadrado que hereden de FormaGeometrica.
Implementa el método calcular_area() de forma específica para cada subclase.
Crea una lista de objetos de diferentes formas geométricas y recorre la lista llamando a calcular_area() para demostrar el polimorfismo.
"""
import math

class FormaGeometrica():
    def calcular_area(self):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print('Método no implementado')


class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    def calcular_area(self):
        return (self._radio**2)*math.pi


class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self._lado = lado

    @property
    def lado(self):
        return self._lado

    def calcular_area(self):
        return self._lado * self._lado


# main
figura = FormaGeometrica()
figura.calcular_area()
circulo1 = Circulo(5)
circulo2 = Circulo(7)
cuadrado1 = Cuadrado(7)
cuadrado2 = Cuadrado(9)
print(f'Circulo 1 -- Radio: {circulo1.radio} -- Area: {circulo1.calcular_area()}')
print(f'Circulo 2 -- Radio: {circulo2.radio} -- Area: {circulo2.calcular_area()}')
print(f'Cuadrado 1 -- Lado: {cuadrado1.lado} -- Area: {cuadrado1.calcular_area()}')
print(f'Cuadrado 2 -- Lado: {cuadrado2.lado} -- Area: {cuadrado2.calcular_area()}')
