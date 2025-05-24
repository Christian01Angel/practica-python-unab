# En el bloque principal del programa definir un diccionario que almacene los nombres ed los nombres de paises como
# clave y como valor la cantidad de habitantes. Implementar una funcion para mostrar cada clave valor


def imprimir(paises):
    for claves in paises:
        print(claves, paises[claves])


#main
paises = {"Argentina" : 4000000, "Chile": 2300000}
imprimir(paises)

