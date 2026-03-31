import heapq  #Para usar la cola de prioridad (heap)
import sys    #para modificar la ruta de busqueda de modulos
import os     # Para manejar rutas de archivos ya que tuve problemas con las rutas

ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ruta_raiz)    # Agrega la raíz al path para poder importar módulos

from mundo.node import Node  
from mundo.grid import grid
from mundo.lectorMapa import leer_mapa

def heuristica_manhattan(pos1,pos2):

    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])  #calcula la distancia de manhattan entre dos puntos

def avara(grid, inicio,destino, pasajeros):

    meta_pasajeros=frozenset(pasajeros)
