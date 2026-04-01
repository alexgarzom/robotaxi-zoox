import sys
import os

# Agregar la carpeta raíz al path
ruta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ruta_raiz)

import pygame  # biblioteca para crear interfaz
import sys

from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa
from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella


# Colores en formato RGB
COLORES = {
    Grid.LIBRE: (255, 255, 255),      # blanco
    Grid.MURO: (0, 0, 0),             # negro
    Grid.INICIO: (0, 0, 255),         # azul
    Grid.FLUJO_ALTO: (255, 0, 0),     # rojo
    Grid.PASAJERO: (0, 255, 0),       # verde
    Grid.DESTINO: (255, 255, 0),      # amarillo
}
COLOR_CAMINO = (0, 255, 255)          # cian para el recorrido
COLOR_FONDO = (200, 200, 200)         # gris para fondo

TAM_CELDA = 60
FILAS = 10
COLUMNAS = 10

ANCHO = COLUMNAS * TAM_CELDA  # 600px
ALTO = FILAS * TAM_CELDA     # 600px


class Visualizador:

    def __init__(self, grid, titulo="robotaxi-zoox"):
        self.grid = grid
        self.tam_celda = TAM_CELDA
        self.ancho = grid.columnas * self.tam_celda
        self.alto = grid.filas * self.tam_celda

        pygame.init()
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(titulo)
        self.reloj = pygame.time.Clock()

    def dibujar_grid(self, camino=None, paso_actual=0):
        self.ventana.fill(COLOR_FONDO)

        # Dibujar cada celda
        for i in range(self.grid.filas):
            for j in range(self.grid.columnas):
                x = j * self.tam_celda
                y = i * self.tam_celda
                rect = pygame.Rect(x, y, self.tam_celda, self.tam_celda)

                tipo = self.grid.matriz[i][j]
                color = COLORES.get(tipo, COLORES[Grid.LIBRE])

                pygame.draw.rect(self.ventana, color, rect)
                pygame.draw.rect(self.ventana, (100, 100, 100), rect, 1)

        # Dibujar camino hasta el paso actual
        if camino and paso_actual < len(camino):
            for k in range(paso_actual + 1):
                i, j = camino[k]
                x = j * self.tam_celda
                y = i * self.tam_celda
                rect = pygame.Rect(x, y, self.tam_celda, self.tam_celda)
                pygame.draw.rect(self.ventana, COLOR_CAMINO, rect, 4)

        pygame.display.flip()

    def animar_camino(self, camino, delay=300):
        if not camino:
            print("No hay camino para animar")
            return

        ejecutando = True
        paso = 0

        while ejecutando:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutando = False

            # Dibujar paso actual
            self.dibujar_grid(camino, paso)

            # Avanzar al siguiente paso
            if paso < len(camino) - 1:
                paso += 1
                pygame.time.wait(delay)
            else:
                # Cuando termina, esperar a que cierren la ventana
                pygame.time.wait(500)

        pygame.quit()
        sys.exit()

    def esperar_cierre(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


