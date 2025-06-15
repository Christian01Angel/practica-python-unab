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
            print(f'Arrancando reproducción. Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista} \n')
        else:
            print('El reproductor se encuentra vacío. Por favor seleccioná una canción\n')

    def siguiente(self):
        indice = ReproductorMusical.reproductor.index(self._cancionActual)
        if indice < len(ReproductorMusical.reproductor)-1:
            self._cancionActual = ReproductorMusical.reproductor[indice+1]
            print(f'Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista}\n')
        else:
            print('Esta es la última canción\n')

    def anterior(self):
        indice = ReproductorMusical.reproductor.index(self._cancionActual)
        if indice > 0:
            self._cancionActual = ReproductorMusical.reproductor[indice - 1]
            print(f'Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista}\n')
        else:
            print(f'Estas escuchando {self._cancionActual._titulo} del artista {self._cancionActual._artista}\n')


    def agregar_cancion(self, cancion):
        ReproductorMusical.reproductor.append(cancion)
        self._cancionActual = ReproductorMusical.reproductor[0]

    def eliminar_cancion(self, tituloCancion):
        for cancion in ReproductorMusical.reproductor:
            if tituloCancion == cancion._titulo:
                ReproductorMusical.reproductor.remove(cancion)

    def pausar(self):
        print('Has pausado el reproductor\n')

    def ver_reproductor(self):
        if self._cancionActual is not None:
            print('Playlist: {')
            for i in ReproductorMusical.reproductor:
                print(f'{i._titulo} -- {i._artista}')
            print('}\n')
        else:
            print('La playlist esta vacía.\n')

    def limpiar_playlist(self):
        ReproductorMusical.reproductor = []
        self._cancionActual = None

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
reproductor.agregar_cancion(amor_amarillo)
reproductor.agregar_cancion(cancion_animal)
reproductor.agregar_cancion(soy)
reproductor.agregar_cancion(viejo_karma)
reproductor.agregar_cancion(bohemian_rapsody)
condicion = True

while condicion:
    print(f'''Seleccione una opción:
1- Reproducción (Play)
2- Canción siguiente
3- Canción anterior
4- Agregar Canción a la playlist
5- Eliminar canción de la playlist
6- Mostrar la playlist completa
7- Vaciar la playlist
8- Detener el reproductor (Stop)
''')
    try:
        eleccion = int(input(f'Que desea hacer?: \n'))

        match eleccion:
            case 1:
                reproductor.play()
                condicion = True
            case 2:
                reproductor.siguiente()
            case 3:
                reproductor.anterior()
            case 4:
                titulo = input('Escribe el titulo de la canción: \n')
                autor = input('Indica el autor de la canción: \n')
                cancion = Cancion(titulo, autor)
                reproductor.agregar_cancion(cancion)
            case 5:
                titulo = input('Escribe el titulo de la canción: \n')
                reproductor.eliminar_cancion(titulo)
            case 6:
                reproductor.ver_reproductor()
            case 7:
                reproductor.limpiar_playlist()
            case 8:
                condicion = reproductor.stop()
                print('Gracias por compartir tu hermosa musica. Hasta la próxima.\n')
            case _:
                print('Opción ingresada invalida. Por favor intenta nuevamente\n')

    except ValueError:
        print('Valor ingresado invalido. Por favor intenta nuevamente\n')
