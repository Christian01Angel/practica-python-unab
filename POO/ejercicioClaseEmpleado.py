"""
7 - Sistema de Gestión de Empleados (Herencia y Composición):

Crea una clase Persona con atributos nombre y edad.
Crea una clase Empleado que herede de Persona y agregue atributos como id_empleado y salario.
Crea una clase Departamento que tenga una lista de objetos Empleado (composición).
Implementa métodos en Departamento para agregar empleados, listar empleados y calcular el salario total del departamento.

"""

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):
    id_empleado = 1

    def __init__(self, persona, salario):
        super().__init__(persona.nombre, persona.edad)
        self._salario = salario
        self._id = Empleado.id_empleado
        Empleado.id_empleado += 1

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def __str__(self):
        return f'Empleado n°: {self._id} -- Nombre: {self._nombre} -- Edad: {self._edad} -- Sueldo: {self._salario}\n'

    def __eq__(self, other):
        if self._salario > other._salario:
            print(f'{self._nombre} gana más que {other._nombre}')
        elif self._salario < other._salario:
            print(f'{other._nombre} gana más que {self._nombre}')
        else:
            print(f'{self._nombre} y {other._nombre} ganan lo mismo')


# main
juan = Persona('Juan', 25)
ana = Persona('Ana', 58)
christian = Persona('Christian', 31)
valeria = Persona('Valeria', 34)
empleado1 = Empleado(valeria, 30000)
empleado2 = Empleado(christian, 45000)
empleado3 = Empleado(ana, 15000)
empleado4 = Empleado(juan, 120000)
empleado5 = Empleado(ana, 30000)

print(empleado1)
print(empleado2)
print(empleado3)
print(empleado4)

empleado1 == empleado5
