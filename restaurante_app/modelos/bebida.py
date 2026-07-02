from modelos.producto import Producto

class Bebida(Producto):

    def __init__(self, nombre: str, precio: float, disponible: bool, tipo_bebida: str):
        super().__init__(nombre, precio, disponible)

        # Atributo propio de Bebida
        self.tipo_bebida = tipo_bebida

    def mostrar_información(self):
        print("\n=== BEBIDA ===")
        print(f"Nombre       : {self.nombre}")
        print(f"Tipo         : {self.tipo_bebida}")
        print(f"Precio       : ${self.obtener_precio():.2f}")
        print(f"Disponible   : {'Sí' if self.disponible else 'No'}")