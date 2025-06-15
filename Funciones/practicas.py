#Ejercicios POO
'''
Ejercicios Básicos (Clases y Objetos simples):

1 - Clase Rectangulo:

Crea una clase Rectangulo que tenga dos atributos: ancho y alto.
Implementa un método calcular_area() que devuelva el área del rectángulo.
Implementa un método calcular_perimetro() que devuelva el perímetro del rectángulo.
Crea algunos objetos Rectangulo y prueba sus métodos


Ejercicios Avanzados (Polimorfismo, Composición, Clases Abstractas):

10 - Simulación de Tienda Online (Múltiples clases y relaciones):

Crea clases para representar:
Producto (nombre, precio, stock)
Cliente (nombre, email)
CarritoDeCompras (contiene una lista de Producto y cantidades)
Pedido (contiene un Cliente, un CarritoDeCompras y un estado)
Implementa métodos para:
Agregar productos al carrito.
Calcular el total del carrito.
Realizar un pedido (vacía el carrito y crea un Pedido).
Actualizar el stock de los productos al realizar un pedido.
'''


"""
Ejercicios de Programación Funcional en Python
Nivel Básico

1 - Transformación de Lista con map:

Dada una lista de números [1, 2, 3, 4, 5], usa map y una función lambda para obtener una nueva lista donde cada número esté elevado al cuadrado.
Variante: Haz lo mismo, pero usando una función definida normalmente (no lambda).

2 - Filtrado de Lista con filter:

Dada una lista de palabras ["manzana", "banana", "cereza", "dátil"], usa filter y una función lambda para obtener una nueva lista que contenga solo las palabras que empiezan con la letra 'b'.

3 - Reducción con reduce (Necesitarás functools):

Dada una lista de números [1, 2, 3, 4, 5], usa reduce para calcular la suma de todos los elementos.
Pista: from functools import reduce

4 - Función Pura Sencilla:

Crea una función pura multiplicar(a, b) que tome dos números y devuelva su producto. Asegúrate de que no modifique nada fuera de su ámbito ni tenga efectos secundarios.

5 - Lista de Tuplas a Diccionario:

Dada una lista de tuplas [("a", 1), ("b", 2), ("c", 3)], usa una combinación de funciones (posiblemente dict y algo más) para transformarla en un diccionario {"a": 1, "b": 2, "c": 3}. Intenta hacerlo de la manera más "funcional" posible.


Nivel Intermedio

6 - Composición de Funciones:

Crea dos funciones: sumar_cinco(x) que suma 5 a x, y duplicar(x) que multiplica x por 2.
Ahora, escribe una función componer(f, g) que tome dos funciones f y g y devuelva una nueva función que aplique f y luego g al resultado.
Usa componer para crear una función duplicar_y_sumar_cinco y pruébala con un número.

7 - Map en Listas Anidadas:

Dada una lista de listas [[1, 2], [3, 4], [5, 6]], usa map para obtener una nueva lista donde cada sublista sea la suma de sus elementos (por ejemplo, [3, 7, 11]).

8 - Fibonacci Recursivo:

Implementa una función fibonacci(n) que calcule el n-ésimo número de Fibonacci utilizando recursión. Asegúrate de que sea lo más pura posible. (Considera la inmutabilidad de los argumentos).

9 - Currying (Parcialmente):

Crea una función sumador_parcial(numero_base) que devuelva una nueva función. La nueva función devuelta debería tomar otro número y sumarlo a numero_base.
Ejemplo: sumar_a_diez = sumador_parcial(10), luego sumar_a_diez(5) debería devolver 15.

10 - Procesamiento de Cadenas con map y filter:

Dada una lista de frases ["Hola mundo", "Python es genial", "Programacion funcional"].
Usa map para convertir cada frase a mayúsculas.
Luego, usa filter en el resultado para quedarte solo con las frases que contengan la palabra "FUNCIONAL" (ignorando mayúsculas/minúsculas).


Nivel Avanzado

11 - reduce para Concatenar Cadenas:

Dada una lista de palabras ["Hola", "mundo", "funcional", "Python"], usa reduce para concatenarlas en una sola cadena, separadas por un espacio. El resultado debería ser "Hola mundo funcional Python".

12 - Memoización para Fibonacci (Optimización de Recursión):

La función Fibonacci recursiva puede ser ineficiente. Modifica tu función fibonacci para incluir memoización (caché). Puedes usar un diccionario o el decorador @functools.lru_cache. Esto ayuda a la performance sin perder la naturaleza funcional.

13 - Función pipe o compose_all:

Implementa una función pipe(*funciones) que tome un número variable de funciones y devuelva una nueva función. Esta nueva función debe aplicar el resultado de la primera función como argumento a la segunda, el resultado de la segunda a la tercera, y así sucesivamente (como un "pipeline" de datos).
Ejemplo: pipeline = pipe(funcion1, funcion2, funcion3)
resultado = pipeline(valor_inicial)

14 - Procesamiento de Datos con map, filter, reduce y Lambdas:

Tienes una lista de diccionarios representando usuarios:
Python

usuarios = [
    {"nombre": "Alice", "edad": 30, "activo": True},
    {"nombre": "Bob", "edad": 24, "activo": False},
    {"nombre": "Charlie", "edad": 35, "activo": True},
    {"nombre": "David", "edad": 28, "activo": True}
]
Utiliza una combinación de map, filter y reduce (o funciones equivalentes) para:
Filtrar solo los usuarios activo: True.
Obtener una lista con la edad de estos usuarios activos.
Calcular la edad promedio de los usuarios activos.

15 - Generadores (Un toque funcional pero también eficiente):

Aunque no son estrictamente "programación funcional pura", los generadores son muy útiles en un contexto funcional por su inmutabilidad y evaluación perezosa.
Crea un generador pares(n) que genere los primeros n números pares.
Luego, usa map y este generador para obtener una lista con el doble de estos números pares.
Consejos para los ejercicios:

Prioriza la inmutabilidad: Intenta no modificar las estructuras de datos originales. Siempre devuelve nuevas estructuras de datos con los cambios.
Piensa en funciones puras: Cada función debería hacer una cosa y hacerla bien, sin efectos secundarios.
Usa funciones de orden superior: Acostúmbrate a map, filter, reduce.
Lambdas para simplicidad: Para funciones pequeñas y de una sola línea.
Comprende la recursión: Es fundamental en programación funcional.
"""
