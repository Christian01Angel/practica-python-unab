"""2 - Clase Libro:

Define una clase Libro con atributos como titulo, autor y año_publicacion.
Crea un método mostrar_informacion() que imprima todos los detalles del libro.
Instancia varios objetos Libro y llama al método mostrar_informacion() para cada uno.
"""

class Libro:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self):
        return self._titulo


    def mostrar_informacion(self):
        print(f'''Libro: {self._titulo}
Autor: {self._autor}
Año de publicación: {self._anio}
''')
    # @titulo.setter
    # def titulo(self, titulo):
    #     self._titulo = titulo
    #
    # @property
    # def autor(self):
    #     return self._autor
    #
    # @autor.setter
    # def autor(self, autor):
    #     self._autor = autor
    #
    # @property
    # def anio(self):
    #     return self._anio
    #
    # @anio.setter
    # def anio(self, anio):
    #     self._anio = anio


#main
harry_potter = Libro('Harry Potter y la pieda filosofal', "J. K. Rowling", 1997)
el_eternauta = Libro('El Eternauta', 'Héctor Germán Oesterheld', 1959)
don_quijote = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes Saavedra', 1605)

harry_potter.mostrar_informacion()
el_eternauta.mostrar_informacion()
don_quijote.mostrar_informacion()
