"""
9 - Clase Abstracta DispositivoElectronico:

Utiliza el módulo abc para crear una clase base abstracta DispositivoElectronico con un método abstracto encender() y apagar().
Crea subclases como Telefono y Computadora que hereden de DispositivoElectronico y implementen los métodos abstractos de forma específica.
Intenta instanciar DispositivoElectronico directamente para ver el error que genera.

"""
from abc import ABC, abstractmethod


class DispositivoElectronico(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class Telefono(DispositivoElectronico):
    def encender(self):
        print('Teléfono Encendido')

    def apagar(self):
        print('Teléfono apagado')


class Computadora(DispositivoElectronico):
    def encender(self):
        print('Computadora encendida')

    def apagar(self):
        print('Computadora apagada')


# main
telefono = Telefono()
computadora = Computadora()
telefono.encender()
computadora.encender()
telefono.apagar()
computadora.apagar()
