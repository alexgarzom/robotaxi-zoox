import pygame #biblioteca para crear interfaz

from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa


#colores en formate RGB

COLORES = {
    Grid.LIBRE      : (255,255,255),  # blanco
    Grid.MURO       : (0,0,0),  # negro
    Grid.INICIO     : (0,0,255),  # azul
    Grid.FLUJO_ALTO : (255,0,0),  # naranja o rojo
    Grid.PASAJERO   : (0,255,0),  # verde
    Grid.DESTINO    : (255,255,0),  # morado o amarillo
}

TAM_CELDA = 60
FILAS     = 10
COLUMNAS  = 10

ANCHO = COLUMNAS * TAM_CELDA  # 600px
ALTO  = FILAS * TAM_CELDA     # 600px


pygame.init()

ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Robotaxi Zooz")