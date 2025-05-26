#Ejercicio 6. Diseñar un algoritmo que calcule el promedio de una serie de números positivos entrados por teclado.
#El ingreso del valor igual a 0 indicará el final del ingreso de datos.

nombre = input('Hola usuario, ingresá tu nombre: ')
lista_numeros = []
condicion = True
print(f'{nombre} por favor ingresá una serie de números positivos, para finalizar la carga ingresá un 0 (cero).')
while condicion:
    numero = int(input('Ingresa un numero: '))
    if numero == 0:
        condicion = False
    elif numero < 0:
        print('Número invalido, por favro verifica que el número ingresado sea mayor a cero.')
    else:
        lista_numeros.append(numero)

print(f'{nombre} ingresaste {len(lista_numeros)} números. Los números que ingresastes son: {lista_numeros}')
contador = 0
for numero in lista_numeros:
    contador += numero

promedio = contador / len(lista_numeros)

print(f'El promedio de los números ingresados es: {promedio}')
