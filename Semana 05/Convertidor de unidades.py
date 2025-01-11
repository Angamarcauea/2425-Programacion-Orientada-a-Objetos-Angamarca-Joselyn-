"""
Programa: Conversor de Unidades de Peso
Descripción: Este programa permite convertir unidades de peso entre kilogramos y libras.
"""

def convertir_kg_a_lb(kilogramos):
    """
    Convierte kilogramos a libras.
    :param kilogramos: Peso en kilogramos (float)
    :return: Peso en libras (float)
    """
    libras = kilogramos * 2.20462
    return libras


def convertir_lb_a_kg(libras):
    """
    Convierte libras a kilogramos.
    :param libras: Peso en libras (float)
    :return: Peso en kilogramos (float)
    """
    kilogramos = libras / 2.20462
    return kilogramos


def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    print("Bienvenido al conversor de unidades de peso.")
    print("Opciones:")
    print("1. Convertir de kilogramos a libras")
    print("2. Convertir de libras a kilogramos")

    # Solicitar la elección del usuario
    eleccion = input("Ingrese el número de la opción deseada (1 o 2): ")
    if eleccion == "1":
        peso_en_kg = float(input("Ingrese el peso en kilogramos: "))
        resultado = convertir_kg_a_lb(peso_en_kg)
        print(f"{peso_en_kg} kg son equivalentes a {resultado:.2f} lb.")
    elif eleccion == "2":
        peso_en_lb = float(input("Ingrese el peso en libras: "))
        resultado = convertir_lb_a_kg(peso_en_lb)
        print(f"{peso_en_lb} lb son equivalentes a {resultado:.2f} kg.")
    else:
        print("Opción no válida. Por favor, reinicie el programa e intente nuevamente.")

    # Variable booleana para comprobar si el programa se ejecutó correctamente
    programa_correcto = True
    if programa_correcto:
        print("Gracias . ")


# Ejecutar el programa
if __name__ == "__main__":
    main()
