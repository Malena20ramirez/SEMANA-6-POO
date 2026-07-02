from modelos.producto import Producto

class Platillo(Producto):

    def __init__(self, nombre: str, precio: float, disponible: bool, tipo_platillo: str):
        # Constructor de la clase Platillo. 
        super().__init__(nombre, precio, disponible)

        # Atributo propio de Platillo
        self.tipo_platillo = tipo_platillo
        # tipo_platillo (str): Categoría del platillo (por ejemplo, "Plato fuerte", "Entrada").

    # Método para mostrar información específica del platillo

    def mostrar_información(self):
        print(f"Nombre       : {self.nombre}")
        print(f"Tipo         : {self.tipo_platillo}")
        print(f"precio       : ${self.obtener_precio():.2f}")
        print(f"Disponible   : {'Sí' if self.disponible else 'No'}")
