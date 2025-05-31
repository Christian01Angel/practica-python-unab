#Ejercicios POO
'''
Ejercicios Básicos (Clases y Objetos simples):

1 - Clase Rectangulo:

Crea una clase Rectangulo que tenga dos atributos: ancho y alto.
Implementa un método calcular_area() que devuelva el área del rectángulo.
Implementa un método calcular_perimetro() que devuelva el perímetro del rectángulo.
Crea algunos objetos Rectangulo y prueba sus métodos.



Ejercicios Intermedios (Herencia y Encapsulamiento):





Ejercicios Avanzados (Polimorfismo, Composición, Clases Abstractas):

6 - Clase FormaGeometrica y Polimorfismo:

Define una clase base FormaGeometrica con un método calcular_area() que lance una excepción NotImplementedError.
Crea subclases como Circulo y Cuadrado que hereden de FormaGeometrica.
Implementa el método calcular_area() de forma específica para cada subclase.
Crea una lista de objetos de diferentes formas geométricas y recorre la lista llamando a calcular_area() para demostrar el polimorfismo.

7 - Sistema de Gestión de Empleados (Herencia y Composición):

Crea una clase Persona con atributos nombre y edad.
Crea una clase Empleado que herede de Persona y agregue atributos como id_empleado y salario.
Crea una clase Departamento que tenga una lista de objetos Empleado (composición).
Implementa métodos en Departamento para agregar empleados, listar empleados y calcular el salario total del departamento.

8 - Clase ReproductorMusical (Composición):

Crea una clase Cancion con atributos titulo y artista.
Crea una clase ReproductorMusical que tenga una lista de objetos Cancion.
Implementa métodos como agregar_cancion(), reproducir_siguiente(), pausar() y mostrar_playlist().
Demuestra cómo el ReproductorMusical "tiene" varias Canciones.

9 - Clase Abstracta DispositivoElectronico:

Utiliza el módulo abc para crear una clase base abstracta DispositivoElectronico con un método abstracto encender() y apagar().
Crea subclases como Telefono y Computadora que hereden de DispositivoElectronico y implementen los métodos abstractos de forma específica.
Intenta instanciar DispositivoElectronico directamente para ver el error que genera.

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