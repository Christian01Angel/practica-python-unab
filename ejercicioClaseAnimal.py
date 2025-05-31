"""
3 - Clase Animal y sus subclases:

Crea una clase base Animal con un atributo nombre y un método hacer_sonido() (que imprima "Sonido genérico").
Crea dos subclases, Perro y Gato, que hereden de Animal.
Sobrescribe el método hacer_sonido() en cada subclase para que impriman el sonido específico de cada animal ("Guau!" o "Miau!").
Crea instancias de Perro y Gato y llama a su método hacer_sonido().

"""

class Animal:
    def __init__(self, nombre):
        self._nombre = nombre

    def hacer_sonido(self):
        print('Grrrrr')


class Perro(Animal):
    def __init__(self, nombre):
        self._nombre = nombre
        super()

    def hacer_sonido(self):
        print('Guau Guau')


class Gato(Animal):
    def __init__(self, nombre):
        self._nombre = nombre
        super()

    def hacer_sonido(self):
        print('Miau Miau')


# main
perro1 = Perro('Perla')
perro1.hacer_sonido()
perro2 = Perro('Celeste')
perro2.hacer_sonido()
gato1 = Gato('Caracono')
gato1.hacer_sonido()
gato2 = Gato('Michini')
gato2.hacer_sonido()
