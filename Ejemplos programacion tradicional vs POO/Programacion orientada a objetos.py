class ClimaSemanal:
    def __init__(self):
        self.lecturas_diarias = []

    # Método para registrar las temperaturas de cada día
    def registrar_temperaturas(self):
        for dia in range(7):  # 7 días de la semana
            temperatura = float(input(f"Introduce la temperatura para el día {dia + 1}: "))
            self.lecturas_diarias.append(temperatura)

    # Método para calcular el promedio de las temperaturas semanales
    def obtener_promedio(self):
        if not self.lecturas_diarias:
            print("No se han ingresado temperaturas para calcular el promedio.")
            return 0
        promedio = sum(self.lecturas_diarias) / len(self.lecturas_diarias)
        return promedio

# Función principal
def ejecutar_programa():
    print("Cálculo del promedio semanal de temperaturas - Paradigma de POO")
    clima_semanal = ClimaSemanal()
    clima_semanal.registrar_temperaturas()
    promedio = clima_semanal.obtener_promedio()
    print(f"El promedio de las temperaturas durante la semana es: {promedio:.2f}°C")

# Llamada a la función principal
ejecutar_programa()
