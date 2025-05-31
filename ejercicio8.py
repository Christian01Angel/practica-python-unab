"""Escribir un algoritmo que muestre por pantalla las tablas de multiplicacion, desde el 1 hasta el 9."""

for x in range(1, 10):
    print(f'--- Tabla del {x} ---')
    for i in range(1, 11):
        print(f'{x} x {i} = {x*i}')
