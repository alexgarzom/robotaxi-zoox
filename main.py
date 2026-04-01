import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import filedialog

import pygame
import time
from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa
from mundo.node import Node
from ui.menu import mostrar_menu, mostrar_submenu
from ui.visualizador import Visualizador

from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella
from algoritmosBusqueda.informada.algoritmoAvara import avara
from algoritmosBusqueda.noinformada.busAmplitud import BusquedaAmplitud
from algoritmosBusqueda.noinformada.busCostoUni import BusquedaCosto
from algoritmosBusqueda.noinformada.busProfundidad import BusquedaProfundidad


def seleccionar_archivo():
    tk.Tk().withdraw()
    ruta = filedialog.askopenfilename(
        title="Selecciona el mapa",
        filetypes=[("Archivos de texto", "*.txt")],
        initialdir="mapas/"
    )
    return ruta if ruta else None


def ejecutar_algoritmo(nombre, grid):
    pasajeros = frozenset(grid.pasajeros)
    nodo_inicial = Node(posicion=grid.inicio, pasajeros_recogidos=frozenset())

    if nombre == "a_estrella":
        return a_estrella(grid, grid.inicio, grid.destino, grid.pasajeros)
    elif nombre == "avara":
        return avara(grid, grid.inicio, grid.destino, grid.pasajeros)
    elif nombre == "amplitud":
        return BusquedaAmplitud(grid).buscar(nodo_inicial, pasajeros)
    elif nombre == "costo":
        return BusquedaCosto(grid).buscar(nodo_inicial, pasajeros)
    elif nombre == "profundidad":
        return BusquedaProfundidad(grid).buscar(nodo_inicial, pasajeros)


if __name__ == "__main__":

    # PASO 1: seleccionar archivo
    ruta = seleccionar_archivo()
    if not ruta:
        print(" No se seleccionó ningún archivo")
        sys.exit()

    matriz = leer_mapa(ruta)
    if not matriz:
        print(" Error al leer el mapa")
        sys.exit()

    grid = Grid(matriz)

    # PASO 2: iniciar pygame
    pygame.init()
    ventana = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Robotaxi Zoox")

    # PASO 3: mostrar estado inicial del mapa
    vis = Visualizador(grid, "Robotaxi Zoox")
    vis.dibujar_grid()  # sin camino, solo el mapa
    pygame.time.wait(2000)  # pausa para que se vea

    # PASO 4: seleccionar algoritmo
    categoria = mostrar_menu(ventana, 600, 600)
    algoritmo = mostrar_submenu(ventana, 600, 600, categoria)

    # PASO 5: ejecutar algoritmo
    print(f"Ejecutando: {algoritmo}...")
    tiempo_inicio = time.time()
    resultado = ejecutar_algoritmo(algoritmo, grid)
    tiempo_fin = time.time()

    if not resultado:
        print("No se encontró solución :c ")
        pygame.quit()
        sys.exit()

    resultado['tiempo'] = round((tiempo_fin - tiempo_inicio)*1000, 2) #en milisegundos

    print(f"✅ Solución encontrada. Costo: {resultado['costo']}")
    print(f"Pasos: {len(resultado['camino'])}")
    print(f"camino: {resultado['camino']}")
    print(f"nodos expandidos: {resultado['nodos_expandidos']}")
    print(f"profundidad: {resultado['profundidad']}")
    print("\n🎬 Mostrando animación...")


    # PASO 6: animar + éxito + reporte
    vis.animar_camino(resultado['camino'], resultado, algoritmo, delay=200)

