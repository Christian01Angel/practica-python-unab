class Cliente:
    def __init__(self, nombre, monto):
        self._nombre = nombre
        self._monto = monto

    def __add__(self, other):
        return self._monto + other._monto


# main
cliente1 = Cliente('Ana', 2000)
cliente2 = Cliente('Pepe', 400)

print(f'La suma de los montos es: {cliente1 + cliente2}')
