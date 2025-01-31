import os
import subprocess

def mostrar_codigo(ruta_script):
    """Muestra el código de un script y lo retorna como string."""
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"¡Error! Archivo no encontrado: {ruta_script}")
        return None
    except Exception as e:
        print(f"¡Error! Al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script en una nueva ventana de terminal."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/c', 'start', 'python', ruta_script], shell=True)
        else:  # Unix-based systems (Linux, macOS)
            subprocess.Popen(['gnome-terminal', '--', 'python3', ruta_script])
    except FileNotFoundError:
        print(f"¡Error! No se encontró el ejecutable de Python.")
    except Exception as e:
        print(f"¡Error! Al ejecutar el código: {e}")

def mostrar_menu():
    """Muestra el menú principal y maneja la navegación."""
    opciones = {
        '1': 'Ejemplos programacion tradicional vs POO',
        '2': 'Ejemplos Mundo Real_POO',
        '3': 'Semana 05',
        '4': 'Semana 06',
        '5': 'Semana 7',
        '6': 'Tecnicas de programacion'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for clave, valor in opciones.items():
            print(f"{clave} - {valor}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in opciones:
            ruta_carpeta = os.path.abspath(opciones[eleccion])  # Obtiene la ruta absoluta
            if os.path.exists(ruta_carpeta):
                mostrar_scripts(ruta_carpeta)  # Llama a mostrar_scripts con la ruta
            else:
                print(f"¡Error! No se encontró la carpeta: {ruta_carpeta}")
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_scripts(ruta_carpeta):
    """Muestra los scripts de una carpeta y permite verlos y ejecutarlos."""
    try:
        if not os.path.exists(ruta_carpeta):  # Verifica si la carpeta existe
            print(f"¡Error! La carpeta {ruta_carpeta} no existe.")
            return

        scripts = sorted([
            f.name for f in os.scandir(ruta_carpeta)
            if f.is_file() and f.name.endswith('.py')
        ])

        while True:
            print(f"\nScripts en {ruta_carpeta}:")
            if not scripts:
                print("No hay scripts en esta carpeta.")
                break

            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar al menú principal")

            opcion = input("Elige un script para ver y ejecutar (0 para regresar): ")

            if opcion == '0':
                break

            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        else:
                            print("Script no ejecutado.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

    except Exception as e:
        print(f"¡Error! Ocurrió algo inesperado: {e}")

if __name__ == "__main__":
    mostrar_menu()
