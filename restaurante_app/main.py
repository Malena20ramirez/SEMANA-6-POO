from modelos. platillo import Platillo
from modelos.bebida import Bebida
from servicios. restaurante import Restaurante

def main():
    # CREACIÓN DE OBJETOS PLATILLO

    platillo1 = Platillo(
        "Pollo asado",
        10.99,
        True,
       "Plato fuerte"
    )

    platillo2 = Platillo(
        "Encocado",
        8.99,
        True,
        "Plato fuerte"
    )

    platillo3 = Platillo(
        "Sopa de pollo",
        6.99,
        True,
        "Sopa"
    )

    # CREACIÓN DE OBJETOS BEBIDA


    bebida1 = Bebida(
        "Agua",
        2.99,
        True,
        "Refrescos"
    )

    bebida2 = Bebida(
        "Coca Cola",
        3.99,
        True,
        "Refrescos"
    )

    bebida3 = Bebida(
        "Jugo de naranja",
        4.99,
        True,
        "Jugos"
    )
    
    # CREACIÓN DE OBJETO RESTAURANTE

    restaurante = Restaurante()
    # Registro de los productos en el restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(platillo3)

    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)
    restaurante.agregar_producto(bebida3)

    # Visualización de la información registrada 
    # Se demuestra el polimorfismo: cada objeto ejecuta
    # su propia versión del método mostrar_información()
    print("=== MENÚ MANJAR MJR ===")
    restaurante. mostrar_productos()

    # ENCAPSULACIÓN
    # Se accede y modifica el precio mediante métodos, no directamente sobre el atributo 
    
    print("\n=== CAMBIO DE PRECIO ===")
    print(f"Precio actual del pollo asado: ${platillo1.obtener_precio():.2f}")
    platillo1.cambiar_precio(9.99)
    print(f"Precio actualizado Pollo asado: ${platillo1.obtener_precio():.2f}")

    print("\nIntento con precio inválido:")
    try:
        platillo1.cambiar_precio(-5.00)
    except ValueError as e:
        print(f"❌ Validación correcta: {e}")

# Punto de inicio del programa
if __name__ == "__main__":
    main()   