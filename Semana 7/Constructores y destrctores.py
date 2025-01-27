class Producto:
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos del producto con el nombre y precio proporcionados.
        """
        self.nombre = nombre
        self.precio = precio
        print(f"Producto '{self.nombre}' creado con un precio de {self.precio}.")

    def mostrar_detalles(self):
        """
        Muestra los detalles del producto.
        """
        print(f"Producto: {self.nombre}, Precio: {self.precio}")

    def __del__(self):
        """
        Destructor de la clase Producto.
        Este metodo se llama cuando el objeto es eliminado.
        """
        print(f"Producto '{self.nombre}' destruido.")

if __name__ == "__main__":
    # Crear dos productos
    producto1 = Producto("Laptop", 1200)
    producto1.mostrar_detalles()

    producto2 = Producto("Teléfono", 800)
    producto2.mostrar_detalles()

    # Eliminar los productos
    del producto1
    del producto2

    print("Fin del programa.")


