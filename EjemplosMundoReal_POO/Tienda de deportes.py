class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False

    def __str__(self):
        return f"{self.nombre} - ${self.precio}, Stock: {self.stock}"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.reducir_stock(cantidad):
                    print(f"Venta: {cantidad} x {producto.nombre} = ${producto.precio * cantidad}")
                else:
                    print(f"Stock insuficiente para {producto.nombre}. Disponible: {producto.stock}")
                return
        print(f"{nombre} no encontrado.")


# Ejemplo de uso
tienda = Tienda()
tienda.agregar_producto(Producto("Pelota", 20, 15))
tienda.agregar_producto(Producto("Camiseta", 35, 10))

print("Inventario:")
tienda.mostrar_productos()
tienda.vender_producto("Pelota", 3)
tienda.mostrar_productos()