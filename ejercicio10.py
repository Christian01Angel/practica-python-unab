"""Ejercicio: Supongamos que hacemos una tirada de 10 dados
Ganaremos $200 si la suma de los valores esta entre 10 y 23
Perderemos $1600 si la suma de los valores esta entre 24 y 48
Ganaremos $2500 si la suma de los valores es 42
Perderemos $500 en cualquier otro caso. Deberíamos jugar este juego?"""

import random

saldo = 10000

nombre = input('Ingresa tu nombre: ')
print(f'Bienvenido {nombre} al casino virtual. Tu saldo es de ${saldo}. Las reglas ya fueron explicadas.')
condicion = input('Deseas jugar? (si/no)').lower() == 'si'

while condicion:
    suma = 0
    for x in range(10):
        valorDado = random.randint(1, 6)
        print(f'El valor del dado es: {valorDado}')
        suma += valorDado

    print(f'La suma de los valores es: {suma}')
    if 10 <= suma <= 23:
        saldo += 200
        print(f'Ganaste $200. Ahora tu saldo es de {saldo}')
    elif 24 <= suma <= 48 and suma != 42:
        saldo -= 1600
        print(f'Perdiste $1600. Ahora tu saldo es de {saldo}')
    elif suma == 42:
        saldo += 2500
        print(f'Ganaste $2500. Ahora tu saldo es de {saldo}')
    else:
        saldo -= 500
        f'Perdiste $500. Ahora tu saldo es de {saldo}'

    if saldo <= 0:
        print('Te quedaste sin saldo.')
        condicion = input('Deseas hacer una recarga? (si/no)') == 'si'
        if condicion:
            saldo += int(input('Ingresa la cantidad de dinero que deseas recargar: '))
    else:
        condicion = input('Deseas seguir jugando? (si/no)').lower() == 'si'

print('Gracias por jugar, vuelva pronto.')