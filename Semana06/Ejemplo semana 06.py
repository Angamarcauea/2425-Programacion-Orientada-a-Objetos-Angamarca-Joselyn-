# Clase base "Vehiculo"
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo  # Atributo privado (encapsulación)

    # Método para obtener la descripción (encapsulación)
    def obtener_descripcion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.__modelo}"

# Clase derivada "Automovil" que hereda de "Vehiculo"
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.tipo_motor = tipo_motor

    # Sobrescritura del método poliformismo
    def obtener_descripcion(self):
        return f"Automóvil de marca {self.marca}, modelo  {self.tipo_motor}"

# Crear instancias
vehiculo1 = Vehiculo("Toyota", "Corolla")
automovil1 = Automovil("Chevrolet", "Sail", "Gasolina")

# Mostrar descripciones
print(vehiculo1.obtener_descripcion())  # Polimorfismo: utiliza el método de la clase base
print(automovil1.obtener_descripcion())  # Polimorfismo: sobrescribe el método en la clase derivada
