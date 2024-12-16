# Función para registrar las temperaturas diarias
def registrar_temperaturas():
    temperaturas_semanales = []
    for dia in range(7):  # 7 días de la semana
        temperatura = float(input(f"Introduce la temperatura del día {dia + 1}: "))
        temperaturas_semanales.append(temperatura)
    return temperaturas_semanales

# Función para calcular el promedio de las temperaturas semanales
def calcular_promedio_semanal(temperaturas_semanales):
    promedio = sum(temperaturas_semanales) / len(temperaturas_semanales)
    return promedio

# Función principal
def iniciar_programa():
    print("Promedio semanal de temperaturas - Programación Tradicional")
    temperaturas_semanales = registrar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas_semanales)
    print(f"El promedio de las temperaturas durante la semana es: {promedio:.2f}°C")

# Llamada a la función principal
iniciar_programa()
