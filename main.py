import sys
import os
import time

# Agregar la carpeta actual al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mundo.lectorMapa import leer_mapa
from mundo.grid import Grid
from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella
from ui.visualizador import Visualizador


def main():

    print("="*60)
    print("ROBOTAXI ZOOX - BÚSQUEDA INFORMADA CON A*")
    print("="*60)
    
    # 1. Cargar el mapa
    print("\n📖 Cargando mapa...")
    matriz = leer_mapa()
    if not matriz:
        print("❌ No se pudo cargar el mapa")
        return
    
    # 2. Crear el grid
    grid = Grid(matriz)
    print(f"✅ Mapa cargado: {grid.filas}x{grid.columnas}")
    print(f"🚀 Inicio: {grid.inicio}")
    print(f"🎯 Destino: {grid.destino}")
    print(f"👥 Pasajeros: {grid.pasajeros}")
    
    # 3. Ejecutar A*
    print("\n🔍 Ejecutando algoritmo A*...")
    
    tiempo_inicio = time.time()
    resultado = a_estrella(grid, grid.inicio, grid.destino, grid.pasajeros)
    tiempo_total = time.time() - tiempo_inicio
    
    # 4. Mostrar reporte
    print("\n" + "="*60)
    print("REPORTE DE BÚSQUEDA")
    print("="*60)
    
    if not resultado:
        print("❌ No se encontró una ruta válida")
        return
    
    print(f"✅ Solución encontrada")
    print(f"  Algoritmo: A* (informada)")
    print(f"  Heurística: Distancia Manhattan")
    print(f"  Costo total: {resultado['costo']}")
    print(f"  Nodos expandidos: {resultado['nodos_expandidos']}")
    print(f"  Profundidad: {resultado['profundidad']}")
    print(f"  Longitud del camino: {len(resultado['camino'])} pasos")
    print(f"  Tiempo de cómputo: {tiempo_total:.4f} segundos")
    
    # Verificar pasajeros recogidos
    recogidos = []
    for pos in resultado['camino']:
        if pos in grid.pasajeros:
            recogidos.append(pos)
    print(f"  Pasajeros recogidos: {recogidos}")
    
    # 5. Mostrar animación
    print("\n🎬 Mostrando animación del recorrido...")
    print("   (Cierra la ventana para salir)")
    
    vis = Visualizador(grid, "Robotaxi Zoox - A*")
    vis.animar_camino(resultado['camino'], delay=200)


if __name__ == "__main__":
    main()