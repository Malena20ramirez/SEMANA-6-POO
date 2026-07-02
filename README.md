 
Restaurante App - Sistema Metódico Modular de POO

Datos del Estudiante
Nombre: Malena Jimena Ramírez Pacho
Asignatura: Programación Orientada a Objetos (Semana 6)


Descripción del Sistema
Este proyecto es una aplicación modular en Python diseñada para gestionar el menú de un restaurante empleando los pilares fundamentales de la Programación Orientada a Objetos. Transfiere la lógica de un sistema bibliotecario base hacia un entorno gastronómico, controlando productos generales, platillos y bebidas.


Estructura del Proyecto

El proyecto se organiza bajo una estructura estrictamente modular que divide las responsabilidades en paquetes de modelos y servicios, distribuidos de la siguiente manera:

Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── platillo.py
│   │   └── bebida.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md


 Relación de Herencia Aplicada

La herencia se evidencia a través de una jerarquía limpia donde "Producto" actúa como la "clase padre" (o superclase), proveyendo los atributos comunes: nombre, precio y disponible.

Las clases "Platillo" y "Bebida" actúan como "clases hijas" (subclases) que heredan de manera directa todas las propiedades de Producto. Para reutilizar el constructor de la clase base sin duplicar código, se implementó el método super().__init__(nombre, precio, disponible), añadiendo de forma independiente los atributos específicos requeridos (como calorias para platillos y mililitros para bebidas).


Atributo Encapsulado y Métodos de Acceso

Para proteger la integridad de los datos internos, el atributo "precio" fue encapsulado declarándolo como privado mediante el prefijo de doble guion bajo (__precio), lo que restringe su modificación directa desde fuera de la clase Producto.

El control de flujo de este atributo se gestiona metódicamente mediante:
"Método de Acceso (Getter):" Utilizando el decorador "@property" para leer de forma segura el valor del precio.
"Método de Modificación (Setter):" Utilizando "@precio.setter", el cual incluye una validación lógica que impide que el precio sea modificado con un valor negativo o igual a cero, lanzando una excepción de tipo "ValueError" si las reglas de negocio no se cumplen.


 Implementación de Polimorfismo

El polimorfismo se demuestra mediante la "sobrescritura de métodos (Method Overriding)". La clase padre define el método "mostrar_informacion()", el cual es adoptado y redefinido de forma especializada dentro de "Platillo" y Bebida para adjuntar sus métricas particulares (kcal y ml respectivamente).

Al momento de recorrer la lista de productos dentro de la clase de servicio "Restaurante", un único ciclo iterativo ejecuta la instrucción "producto.mostrar_informacion()". El intérprete de Python, en tiempo de ejecución, identifica dinámicamente el tipo de objeto que se está evaluando y ejecuta el comportamiento correspondiente a su clase específica, mostrando la información correcta en pantalla sin necesidad de validar manualmente el tipo de dato.


 Reflexión sobre la Importancia de los Principios de POO
 
Desarrollar software aplicando los principios de la Programación Orientada a Objetos en entornos modulares es una práctica indispensable para el desarrollo de software profesional. La encapsulación garantiza que los componentes sean robustos y que las reglas de negocio no se rompan por accesos indebidos. La herencia minimiza la redundancia y optimiza el mantenimiento, mientras que el polimorfismo dota al sistema de flexibilidad. 

Al segmentar el código en archivos independientes, se logra un alto nivel de desacoplamiento, facilitando significativamente la detección de errores (debugging), permitiendo la escalabilidad del sistema a largo plazo y optimizando el trabajo colaborativo a través de plataformas de control de versiones como GitHub.




