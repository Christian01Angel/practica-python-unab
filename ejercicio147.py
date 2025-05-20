"""Desarrollar una funcion que solicite la carga del dia, mes y año y almacene dichos datos en una tupla
que luego debe retornar. La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla."""

def almanaque():
    dia = input('Ingrese el dia: ')
    mes = input('Ingrese el mes: ')
    anio = input('Ingrese el año: ')
    fecha = (dia, mes, anio)
    return fecha

def imprimir(tupla):
    fecha = ''
    for i in range(len(tupla)):
        if i<(len(tupla)-1):
            fecha += f'{tupla[i]}/'
        else:
            fecha += f'{tupla[i]}'
    print(fecha)

fecha = almanaque()
imprimir(fecha)
