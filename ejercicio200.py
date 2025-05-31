"""Plantear una clase persona que contenga dos atributos: nombre y edad. Definir la carga por teclado y la impresion
de los datos. En el bloque principal del programa definir un objeto Persona y llamar a sus metodos.

Luego crear una clase empleado que herede de la clase Persona y agregue un atributo sueldo que debe mostrar si debe
paar impuestos (si su sueldo es mayor a 3000). Tambien en el bloque principal se debe crear un objeto Empleado y
llamar a sus metodos"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Nombre: {self.nombre} -- Edad: {self.edad}'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def impuestos(self):
        if self.sueldo > 3000:
            print('Usted debe pagar impuestos')
        else:
            print('Usted no paga impuestos.')


# main
persona1 = Persona('Christrian', 31)
persona2 = Persona('Leonel', 7)
empleado1 = Empleado(persona1.nombre, persona1.edad, 1500)
empleado2 = Empleado('Raul', 44, 3700)

print(persona1)
print(persona2)
empleado1.impuestos()
empleado2.impuestos()
