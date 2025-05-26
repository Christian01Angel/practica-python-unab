"""Dado un número de 2n + 1 cifras decir si el mismo es palíndromo (capicúa)."""

nombre = input('Hola usuario, ingresá tu nombre: ')

condicion = True
while condicion:
    numero = input(f'{nombre} ingresá un número de cifras impares (3 cifras, 5 cifras, 7 cifras, etc): ')
    if int(numero) % 2 == 0:
        print(f'{nombre} la cantidad de cifras es par, ingresa otro número por favor')
    else:
        condicion = False

i = 0
x = len(numero)-1
medio = int(len(numero)/2)
while i < medio and x> medio:
    palindromo = int(numero[i]) == int(numero[x])
    i+=1
    x-=1

if palindromo:
    print(f'El número {numero} es palindromo')
else:
    print(f'El número {numero} no es palindromo')
