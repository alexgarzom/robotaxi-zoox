import heapq
from mundo.node import Node
from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa


def heuristica_manhattan(pos1,pos2):

    return abs(pos1[0] - pos2[1] + abs(pos1[1] - pos2[1]))     #Distancia de manhattan

def a_estrella(grid,inicio,destino,pasajeros):    #Algoritmo A* comnbina costo real g + la heuristica

    meta_pasajeros=frozenset(pasajeros)

    nodo_inicial= Node(
        posicion=inicio,
        pasajeros_recogidos=frozenset(),
        padre=None,
        g=0,
        h=heuristica_manhattan(inicio,destino)
    )



    