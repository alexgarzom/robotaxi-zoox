import os

def leer_mapa():
    ruta = os.path.join("mapas","Prueba1.txt")   # Ruta hacia el mapa

    try:
        with open(ruta, 'r') as archivo:              # Abre el archivo en modo lectura
            matriz = []
            for linea in archivo:                     # Lee línea por línea
                linea = linea.strip()                  # Elimina espacios y saltos de línea
                if not linea:                           # Salta las líneas vacías
                    continue

                fila = [int(valor) for valor in linea.split()]   # Convierte la línea en lista de enteros
                matriz.append(fila)                               # Agrega filas a la matriz

            return matriz if matriz else None          # Retorna None si el archivo está vacío

    except FileNotFoundError:                           # Error si no existe el acualrchivo
        print(f"Error: No se encontró el archivo {ruta}")
        return None
    except Exception as e:                              # Muestra cualquier otro tipo de error
        print(f"Error al leer archivo: {e}")
        return None

###  PRUEBA PARA VER SI CARGA BIEN EL ARCHIVO .TXT" ###

 
if __name__ == "__main__":
    print("Probando lector de mapa...")
    matriz = leer_mapa()
    if matriz:
        print("Archivo leído correctamente")
        print(f"Dimensiones: {len(matriz)} filas x {len(matriz[0])} columnas")
        print("\nMapa completo:")
        for i, fila in enumerate(matriz):
            print(f"Fila {i}: {fila}")
    else:
        print("Error al leer el archivo")
