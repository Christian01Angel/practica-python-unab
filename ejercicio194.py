"""Plantear una clase Operaciones que solicire en el metodo init la carga de dos enteros e inmediatamente muestre
su suma, resta, multiplicaciones y division. Hacer cada operacion en otro metodo de la misma clase y llamarlo desde
el metodo init"""


class Operaciones:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print("Suma: ", self.num1 + self.num2)

    def resta(self):
        print("Resta: ", self.num1 - self.num2)

    def multiplicacion(self):
        print("Multiplicacion: ", self.num1 * self.num2)

    def division(self):
        print("Division: ", self.num1 / self.num2)


# main
operaciones = Operaciones(int(input('Ingrese un numero: ')), int(input('Ingrese otro numero: ')))
