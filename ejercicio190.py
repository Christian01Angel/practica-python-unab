class Empleado():

    def __init__(self):
        self.nombre = input('Ingrese el nombre: ')
        self.sueldo = int(input('Ingrese el sueldo: '))

    def imprimir(self):
        print(f"""
        Datos: 
        Su nombre es: {self.nombre}
        Su sueldo es: {self.sueldo}""")

    def impuestos(self):
        if self.sueldo>3000:
            print('Paga impuestos')
        else:
            print('No paga')