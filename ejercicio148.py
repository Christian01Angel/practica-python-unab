#Desarrollar una funcion que solicite la entrada de tres enteros y almacene dichos datos en una tupla que luego debe
#retornar. La segunda funcion a implementar debe convertir la tupla en lista, modificarla segun el ingreso de un
#entero nuevo, y luego volver a convertirla en tupla.

def crear_tupla():
    ele1 = int(input("Ingrese un numero entero: "))
    ele2 = int(input("Ingrese un numero entero: "))
    ele3 = int(input("Ingrese un numero entero: "))
    tupla = (ele1, ele2, ele3)
    return tupla

def modificar_tupla(tupla):
    condicion = True;
    #Convertimos la tupla en lista
    lista = list(tupla)
    while condicion:
        print("""Modificación de la tupla.
        1-Agregar un elemento
        2-Eliminar un elemento
        3-Modificar un elemento""")
        eleccion = int(input("seleccione una opcion: "))

        match eleccion:
            case 1:
                lista.append(int(input("Ingrese el valor a agregar: ")))
                condicion = False
                return tuple(lista)
                break
            case 2:
                lista.remove(int(input('Ingrese el indice a eliminar: ')))
                condicion = False
                return tuple(lista)
                break
            case 3:
                indice = int(input("Ingrese el indice a eliminar: "))
                lista[indice] = int(input("Ingrese el nuevo valor"))
                return tuple(lista)
                break
            case _:
                print('Numero ingresado incorrecto. Por favor ingreselo nuevamente')
                break


tupla = crear_tupla()
print(tupla)
tupla = modificar_tupla(tupla)
print(tupla)
