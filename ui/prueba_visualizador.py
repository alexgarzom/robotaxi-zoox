import sys
import os

# Agregar la carpeta raíz al path
ruta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ruta_raiz)

from ui.visualizador import Visualizador
from mundo.lectorMapa import leer_mapa
from mundo.grid import Grid
from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella

# ==================== PRUEBA DEL VISUALIZADOR ====================
if __name__ == "__main__":
    print("="*60)
    print("PRUEBA DEL VISUALIZADOR")
    print("="*60)

    # Cargar mapa
    matriz = leer_mapa()
    if not matriz:
        print("❌ No se pudo cargar el mapa")
        exit(1)

    # Crear grid
    grid = Grid(matriz)
    print(f"Inicio: {grid.inicio}")
    print(f"Destino: {grid.destino}")
    print(f"Pasajeros: {grid.pasajeros}")

    # Ejecutar A*
    print("\n🔍 Ejecutando A*...")
    resultado = a_estrella(grid, grid.inicio, grid.destino, grid.pasajeros)

    if not resultado:
        print("❌ No se encontró solución")
        exit(1)

    print(f"✅ Solución encontrada. Costo: {resultado['costo']}")
    print(f"Pasos: {len(resultado['camino'])}")
    print("\n🎬 Mostrando animación...")

    # Crear visualizador y animar
    vis = Visualizador(grid, "Robotaxi Zoox - A*")
    vis.animar_camino(resultado['camino'], delay=200)