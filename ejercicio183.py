"""Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raiz cuadrada
del numero y el valor elevado al cubo

Para resolver este problema utilizaremos dos funcionalidades qye nos provee el modulo math
de la bibliioteca estandar de python. Debemos importar el modulo math"""

from math import sqrt as raiz, pow as potencia

valor = int(input("Ingrese un valor entero: "))
raiz_cuadrada = raiz(valor)
potencia_cubica = pow(valor, 3)

print(f'La raíz cuadrada del numero ingresado es: {raiz_cuadrada}. Y la potencia cubica del valor ingresado es: {potencia_cubica}')

valor = int(input("Ingrese un valor entero: "))
raiz_cuadrada = raiz(valor)
potencia_cubica = potencia(valor, 3)
print(f'La raíz cuadrada del numero ingresado es: {raiz_cuadrada}. Y la potencia cubica del valor ingresado es: {potencia_cubica}')

