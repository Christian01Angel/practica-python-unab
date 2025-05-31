"""Escribir un programa, que tome como entrada un string del usuario, el cuál debe ser impreso por pantalla
 en orden reverso. El programa también debe imprimir la palabra "Bingo!", si el string ingresado es palíndromo."""

palabra = input(f'Ingresa una palabra: ').lower()
palabra2 = ""
i = len(palabra)-1
while i >= 0:
    palabra2 += palabra[i]
    i -=1

if palabra == palabra2:
    print("Bingo!")

print(palabra2)
