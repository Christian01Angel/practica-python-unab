"""
8 - Clase ReproductorMusical (Composición):

Crea una clase Cancion con atributos titulo y artista.
Crea una clase ReproductorMusical que tenga una lista de objetos Cancion.
Implementa métodos como agregar_cancion(), reproducir_siguiente(), pausar() y mostrar_playlist().
Demuestra cómo el ReproductorMusical "tiene" varias Canciones.

"""


class Cancion:
    def __init__(self, titulo, artista):
        self._titulo = titulo
        self._artista = artista


class ReproductorMusical(Cancion):
    reproductor = []

    def __init__(self, cancion = None):
        if cancion is not None:
            super().__init__(cancion._titulo, cancion._artista)
            ReproductorMusical.reproductor.append(cancion)
            self._cancionActual = ReproductorMusical.reproductor[0]

    def play(self):
        if ReproductorMusical.reproductor:
            print(f'Arrancando reproducción. Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista}')
        else:
            print('El reproductor se encuentra vacío. Por favor seleccioná una canción')

    def siguiente(self):
        indice = ReproductorMusical.reproductor.index(self._cancionActual)
        print(indice)
        self._cancionActual = ReproductorMusical.reproductor[indice+1]
        print(f'Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista}')

    def agregar_cancion(self, cancion):
        ReproductorMusical.reproductor.append(cancion)
        self._cancionActual = ReproductorMusical.reproductor[0]

    def eliminar_cancion(self, cancion):
        ReproductorMusical.reproductor.pop(cancion)

    def pausar(self):
        print('Has pausado el reproductor')

    def ver_reproductor(self):
        print('Playlist: {')
        for i in ReproductorMusical.reproductor:
            print(f'{i._titulo} -- {i._artista}')
        print('}')

    def stop(self):
        return False


# main
cancion_animal = Cancion('Canción Animal', 'Soda Stereo')
arrancarmelo = Cancion('Arrancarmelo', 'WOS')
jijiji = Cancion('Jijiji', 'Los Redondos')
amor_amarillo = Cancion('Amor Amarillo', 'Soda Stereo')
crimen = Cancion('Crimen', 'Gustavo Cerati')
seminare = Cancion('Seminare', 'Serú Girán')
doctora_2 = Cancion('La Docotora II', 'Las Pastillas del Abuelo')
soy = Cancion('Soy', 'Cruzando el Charco')
viejo_karma = Cancion('Viejo Karma!', 'Las Pastillas del Abuelo')
bohemian_rapsody = Cancion('Bohemian Rapsody', 'Queen')

reproductor = ReproductorMusical()
condicion = True

while condicion:
    print(f'''Seleccione una opción:
1- Reproducción (Play)
2- Siguiente canción
3- Agregar Canción a la playlist
4- Eliminar canción de la playlist
5- Mostrar la playlist completa
6- Detener el reproductor (Stop)
''')
    try:
        eleccion = int(input(f'Que desea hacer?: '))

        match eleccion:
            case 1:
                reproductor.play()
                condicion = True
            case 2:
                reproductor.siguiente()
            case 3:
                titulo = input('Escribe el titulo de la canción: ')
                autor = input('Indica el autor de la canción: ')
                cancion = Cancion(titulo, autor)
                reproductor.agregar_cancion(cancion)
            case 4:
                titulo = input('Escribe el titulo de la canción: ')
                autor = input('Indica el autor de la canción: ')
                cancion = Cancion(titulo, autor)
                reproductor.eliminar_cancion(cancion)
            case 5:
                reproductor.ver_reproductor()
            case 6:
                condicion = reproductor.stop()
                print('Gracias por compartir tu hermosa musica. Hasta la próxima.')
            case _:
                print('Opción ingresada invalida. Por favor intenta nuevamente')

    except ValueError:
        print('Valor ingresado invalido. Por favor intenta nuevamente')
