# Sistema de control de inventario
class Articulo:
    def __init__(self, codigo, nombre, cantidad, precio_unitario):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def obtener_codigo(self):
        return self.codigo

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio_unitario

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio_unitario = nuevo_precio

    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio Unitario: ${self.precio_unitario}"


class GestionInventario:
    def __init__(self):
        self.lista_productos = []

    def agregar_articulo(self, articulo):
        for a in self.lista_productos:
            if a.obtener_codigo() == articulo.obtener_codigo():
                print("El artículo ya existe con este código.")
                return
        self.lista_productos.append(articulo)
        print(f"Artículo '{articulo.obtener_nombre()}' añadido correctamente.")

    def eliminar_articulo(self, codigo):
        for a in self.lista_productos:
            if a.obtener_codigo() == codigo:
                self.lista_productos.remove(a)
                print(f"Artículo con código {codigo} ha sido eliminado.")
                return
        print("No se encontró el artículo con ese código.")

    def modificar_articulo(self, codigo, nueva_cantidad=None, nuevo_precio=None):
        for a in self.lista_productos:
            if a.obtener_codigo() == codigo:
                if nueva_cantidad is not None:
                    a.actualizar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    a.actualizar_precio(nuevo_precio)
                print(f"Artículo con código {codigo} ha sido actualizado.")
                return
        print("No se encontró el artículo con ese código.")

    def buscar_articulo(self, nombre):
        encontrados = [a for a in self.lista_productos if nombre.lower() in a.obtener_nombre().lower()]
        if encontrados:
            print(f"Artículos encontrados con el nombre '{nombre}':")
            for a in encontrados:
                print(a)
        else:
            print(f"No se encontraron artículos con el nombre '{nombre}'.")

    def mostrar_lista(self):
        if self.lista_productos:
            print("Inventario completo:")
            for a in self.lista_productos:
                print(a)
        else:
            print("El inventario está vacío.")


def interfaz():
    inventario = GestionInventario()

    while True:
        print("\n--- Menú de Control de Inventarios ---")
        print("1. Agregar artículo")
        print("2. Eliminar artículo")
        print("3. Modificar artículo")
        print("4. Buscar artículo")
        print("5. Ver inventario")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                codigo = int(input("Introduce el código del artículo: "))
                nombre = input("Introduce el nombre del artículo: ")
                cantidad = int(input("Introduce la cantidad: "))
                precio = float(input("Introduce el precio unitario: "))
                articulo = Articulo(codigo, nombre, cantidad, precio)
                inventario.agregar_articulo(articulo)
            except ValueError:
                print("Error: Los datos introducidos no son válidos.")

        elif opcion == "2":
            try:
                codigo = int(input("Introduce el código del artículo a eliminar: "))
                inventario.eliminar_articulo(codigo)
            except ValueError:
                print("Error: El código debe ser un número.")

        elif opcion == "3":
            try:
                codigo = int(input("Introduce el código del artículo a modificar: "))
                cantidad = input("Introduce la nueva cantidad (deja en blanco si no deseas cambiarla): ")
                precio = input("Introduce el nuevo precio (deja en blanco si no deseas cambiarlo): ")

                if cantidad:
                    cantidad = int(cantidad)
                if precio:
                    precio = float(precio)

                inventario.modificar_articulo(codigo, cantidad if cantidad else None, precio if precio else None)
            except ValueError:
                print("Error: Los datos introducidos no son válidos.")

        elif opcion == "4":
            nombre = input("Introduce el nombre del artículo a buscar: ")
            inventario.buscar_articulo(nombre)

        elif opcion == "5":
            inventario.mostrar_lista()

        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    interfaz()
