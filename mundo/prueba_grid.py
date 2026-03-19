import sys
import os

# Agregar la carpeta robotaxi-zoox al path de Python
# Esto permite importar mundo, algoritmos, etc.
ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ruta_base)

# Ahora podemos importar desde mundo
from mundo.lectorMapa import leer_mapa
from mundo.grid import Grid

def probar_grid():
    print("="*50)
    print("PRUEBA DE LA CLASE GRID")
    print("="*50)
    
    # 1. Leer mapa
    print("Leyendo mapa...")
    matriz = leer_mapa()
    
    if not matriz:
        print("ERROR, No se pudo cargar el mapa")
        return
    
    # 2. Crear grid
    print("Creando Grid...")
    grid = Grid(matriz)
    
    # 3. Mostrar información
    print("\n Grid creado correctamente")
    print(f" Dimensiones: {grid.filas} filas x {grid.columnas} columnas")
    print(f" Inicio: {grid.inicio}")
    print(f" Destino: {grid.destino}")
    print(f" Pasajeros: {grid.pasajeros}")
    
    # 4. Probar métodos
    print("\n Probando métodos:")
    
    pruebas = [
        ("es_valida(0,0)", grid.es_valida(0,0), True),
        ("es_valida(10,10)", grid.es_valida(10,10), False),
        ("es_transitable(0,0)", grid.es_transitable(0,0), True),
        ("es_transitable(0,1)", grid.es_transitable(0,1), False),
        ("costo_movimiento(0,0)", grid.costo_movimiento(0,0), 1),
        ("costo_movimiento(1,6)", grid.costo_movimiento(1,6), 7),
    ]
    
    for nombre, obtenido, esperado in pruebas:
        estado = "✅" if obtenido == esperado else "❌"
        print(f"{estado} {nombre}: {obtenido} (esperado: {esperado})")
    
    # 5. Información de depuración
    print("\n Información de rutas:")
    print(f"Archivo actual: {__file__}")
    print(f"Ruta base agregada: {ruta_base}")
    print(f"Python path: {sys.path[:3]}")  # Muestra las primeras 3 rutas

if __name__ == "__main__":
    probar_grid()