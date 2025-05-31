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
        print(f'Realizaste el deposito de ${ingreso} exitosamente. Tu nuevo saldo es de {self._saldo}')

    def retirar(self, retiro):
        if retiro <= self._saldo:
            self._saldo -= retiro
            print(f'Has retirado: ${retiro}, saldo restante: {self._saldo}')
        else:
            print(f'No dispone de esa cantidad de dinero en su cuenta. Monto mámixo a retirar: {self._saldo}')

    def obtener_saldo(self):
        print(f'El saldo disponible en su cuenta bancaraia es de: ${self._saldo}')


# main
cuenta1 = CuentaBancaria(15000)
cuenta2 = CuentaBancaria(500000)

cuenta1.retirar(5000)
cuenta2.retirar(250000)
cuenta1.obtener_saldo()
cuenta1.depositar(2000)
cuenta2.depositar(50000)
cuenta2.obtener_saldo()
