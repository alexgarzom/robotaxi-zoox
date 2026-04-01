import sys
import os


ruta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #Agrega la raiz al path de python para importar modulos
sys.path.insert(0, ruta_raiz)

import pygame
import sys

from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa
from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella


# Colores en formato RGB
COLORES = {
    Grid.LIBRE: (255, 255, 255),      # blanco para flujo
    Grid.MURO: (128, 128, 128),       # gris no transitable
    Grid.INICIO: (0, 0, 255),         # azul punto de partida
    Grid.FLUJO_ALTO: (255, 0, 0),     # rojo para trafico alto
    Grid.PASAJERO: (0, 255, 0),       # verde pasa el pasajero
    Grid.DESTINO: (255, 165, 0),      # Naranja para el destino finak
}


COLOR_CAMINO = (0, 255, 255)          # cian para el recorrido
COLOR_CAMINO_RESALTE = (128, 0, 128)  # morado para resaltar más
COLOR_FONDO = (200, 200, 200)         # gris para fondo

##Config de las ventanas

TAM_CELDA = 60   #Tamaño de celdas en px
FILAS = 10       #Num de filas del mapa
COLUMNAS = 10    #Num de col del mapa

ANCHO = COLUMNAS * TAM_CELDA    #Ancho 600px
ALTO = FILAS * TAM_CELDA        #Alto 600px


class Visualizador:

    def __init__(self, grid, titulo="robotaxi-zoox"):
        self.grid = grid                                   #Guarda el grid del mundo
        self.tam_celda = TAM_CELDA                         #Tamaño de la celda
        self.ancho = grid.columnas * self.tam_celda        #Calcu el ancho
        self.alto = grid.filas * self.tam_celda            #Calcu el alto

        pygame.init()                                      #Inicializa pygame
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(titulo)                 #Titulo de la ventana
        self.reloj = pygame.time.Clock()                   #Controla los fps con un reloj
        
      
        self.pasajeros_originales = set(grid.pasajeros)    # Guarda los pasajeros originales para saber dónde están

    def dibujar_grid(self, camino=None, paso_actual=0):
        self.ventana.fill(COLOR_FONDO)                     #Limpia la pantalla

        pasajeros_recogidos = set()                        # Obtener los pasajeros que ya han sido recogidos hasta este paso
        if camino and paso_actual < len(camino):
            for k in range(paso_actual + 1):
                pos = camino[k]
                if pos in self.pasajeros_originales:
                    pasajeros_recogidos.add(pos)            #Se marca como recogido

                                                           #Dibuja cada celda
        for i in range(self.grid.filas):
            for j in range(self.grid.columnas):
                x = j * self.tam_celda                      #Coordenada X
                y = i * self.tam_celda                      #Coodenada Y
                rect = pygame.Rect(x, y, self.tam_celda, self.tam_celda)

                tipo = self.grid.matriz[i][j]               #Tipo de celda
                
              
                if tipo == Grid.PASAJERO and (i, j) in pasajeros_recogidos:   #Si es un pasajero y ya fue recogido, mostrarlo como celda libre
                    color = COLORES[Grid.LIBRE]
                else:
                    color = COLORES.get(tipo, COLORES[Grid.LIBRE])  #Desaparece el pasajero

                pygame.draw.rect(self.ventana, color, rect)
                pygame.draw.rect(self.ventana, (100, 100, 100), rect, 1)

        if camino and paso_actual < len(camino):     #Dibuja el camino hasta el paso actual (con resalte)
            for k in range(paso_actual + 1):
                i, j = camino[k]
                x = j * self.tam_celda
                y = i * self.tam_celda
                rect = pygame.Rect(x, y, self.tam_celda, self.tam_celda)
                
                
                pygame.draw.rect(self.ventana, COLOR_CAMINO_RESALTE, rect, 6)  #Dibuja un borde grueso en color morado para resaltar
                
                             
                if k == paso_actual:                             #Dibuja un círculo en la posición actual (para más énfasis)
                    centro = (x + self.tam_celda // 2, y + self.tam_celda // 2)
                    pygame.draw.circle(self.ventana, (255, 255, 255), centro, self.tam_celda // 3)
                    pygame.draw.circle(self.ventana, COLOR_CAMINO_RESALTE, centro, self.tam_celda // 3, 3)

        pygame.display.flip()                          #Actualiza la pantalla

    def animar_camino(self, camino, delay=300):
        if not camino:
            print("No hay camino para animar")
            return

        ejecutando = True
        paso = 0

        while ejecutando:                                #Maneja los eventos de pygames, cierre de ventana
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutando = False

           
            self.dibujar_grid(camino, paso)             #Dibuja el paso actual

            if paso < len(camino) - 1:                  #Avanza al siguiente paso      
                paso += 1
                pygame.time.wait(delay)
            else:
                pygame.time.wait(500)                      #Cuando termina, y espera a que cierren la ventana

        pygame.quit()
        sys.exit()

    def esperar_cierre(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

#### PRUEBA ###########


if __name__ == "__main__":
    print("="*60)
    print("PRUEBA DEL VISUALIZADOR")
    print("="*60)

    matriz = leer_mapa()
    if not matriz:
        print("❌ No se pudo cargar el mapa")
        exit(1)

    grid = Grid(matriz)
    print(f"Inicio: {grid.inicio}")
    print(f"Destino: {grid.destino}")
    print(f"Pasajeros: {grid.pasajeros}")

    print("\n🔍 Ejecutando A*...")
    resultado = a_estrella(grid, grid.inicio, grid.destino, grid.pasajeros)

    if not resultado:
        print("❌ No se encontró solución")
        exit(1)

    print(f"✅ Solución encontrada. Costo: {resultado['costo']}")
    print(f"Pasos: {len(resultado['camino'])}")
    print("\n🎬 Mostrando animación...")

    vis = Visualizador(grid, "Robotaxi Zoox - A*")
    vis.animar_camino(resultado['camino'], delay=200)

    #### PRUEBA ###########