class Producto:

    def __init__(self, nombre: str, precio: float, disponible: bool):

        # Tipo str: nombre del producto
        self.nombre = nombre

        # atributo encapsulado: el precio no debe ser modificado directamente desde fuera de la clase
        self.__precio = precio

        # Tipo bool: indica si el producto está disponible para la venta
        self.disponible = disponible
    # Método de acceso para obtener el precio encapsulado.

    def obtener_precio(self) -> float:
        return self.__precio
    
    # Método de modificación con validación.

    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio 
        else:
            print(f"Precio no válido para {self.nombre}. Debe ser mayor que cero.")

        # Muestra la información general del producto. 
        
        def mostrar_información(self):
            print(f"Nombre       : {self.nombre}")
            print(f"Precio       : ${self.__precio:.2f}")
            print(f"Disponible   : {'Sí' if self.disponible else 'No'}")