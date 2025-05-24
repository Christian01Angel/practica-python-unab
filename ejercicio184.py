"""Calcular el factorial de un número ingresado por teclado. El factorial de un número es la cantidad que resulta
de la multiplicación de determinado número natural por todos los números naturales que le anteceden
excluyendo el cero. Por ejemplo el factorial de 4 es 24, que resulta de multiplicar 432*1. Implementar el algoritmo
para calcular el factorial por un lado. El módulo math tiene una función llamada factorial que recibe como parámetro
un entero del que necesitamos que nos retorne el factorial. Solo importar la funcionalidad factorial del módulo
math de la biblioteca estándar de Python."""

def factorial(num):
    factorial = 1
    for x in range(1, num+1):
        factorial *= x
    return factorial
condicion = True

while (condicion):
    entrada = int(input('Ingrese el valor a calcular: '))
    if entrada==0:
        print('Ingrese un valor mayor a cero')
    elif entrada<0:
        condicion = False
    else:
        print(f'El factorial de {entrada} es: {factorial(entrada)}')
