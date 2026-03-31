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

    contador = 0
    frontera = []
    heapq.heappush(frontera, (nodo_inicial.f, contador, nodo_inicial))
    contador +=1

    visitados = {}
    nodos_expandidos=0

    while frontera:
        _,_, nodo = heapq.heappop(frontera)
        nodos_expandidos+=1

        if nodo.pasajeros_recogidos==meta_pasajeros and nodo.posicion == destino:
            return {
                'camino': nodo.obtener_camino(),
                'costo':nodo.g,
                'nodos_expandidos': nodos_expandidos,
                'profundidad':nodo.profundidad
            }
        
        estado = (nodo.posicion, nodo.pasajeros_recogidos)

        if estado in visitados and visitados[estado] <= nodo.g:
            continue
        visitados[estado] = nodo.g

        for vecino in grid.get_vecinos(nodo):
            vecino.h=heuristica_manhattan(vecino.posicion, destino)
            vecino.f=vecino.g + vecino.h
            heapq.heappush(frontera, (vecino.f, contador, vecino))
            contador +=1

            return None


        


    