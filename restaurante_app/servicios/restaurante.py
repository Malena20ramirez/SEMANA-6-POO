class Restaurante:
    # Administra los productos registrados en el sistema
    # Utiliza una lista para alamacenar objetos de tipo  Producto y sus clases hijas
     
    def __init__(self): # Constructor de la clase Restaurante
        self.productos = []# Inicia una lista vacía para almacenar los productos del restaurante

    # Agrega un objeto Producto (o sus clases hijas) a la lista 

    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Recorre la lista y ejecuta  mostrar_informacion() según el tipo de objeto
    # Demuestra el polimorfismo.
    
    def mostrar_productos(self):
        for producto in self.productos:
            producto.mostrar_información()