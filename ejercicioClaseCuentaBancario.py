"""
4 - Clase CuentaBancaria (Encapsulamiento):

Define una clase CuentaBancaria con un atributo privado _saldo (para encapsularlo).
Implementa un constructor que inicialice el saldo.
Crea un método depositar(cantidad) que sume la cantidad al saldo.
Crea un método retirar(cantidad) que reste la cantidad si hay suficiente saldo.
Crea un método obtener_saldo() que devuelva el saldo actual.
Asegúrate de que el saldo no pueda ser modificado directamente desde fuera de la clase.

"""


class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, ingreso):
        self._saldo += ingreso

    def retirar(self, retiro):
        if retiro >= self._saldo:
            saldo._saldo -= retiro
            print(f'Has retirado: ${retiro}, saldo restante: {self._saldo}')
        else:
            print(f'No dispone de esa cantidad de dinero en su cuenta. Monto mámixo a retirar: {self._saldo}')

    def obtener_saldo(self):
        print(f'El saldo disponible en su cuenta bancaraia es de: ${self._saldo}')


# main
cuenta1 = Cuenta(15000)
