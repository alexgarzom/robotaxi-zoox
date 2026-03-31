import heapq  # Para usar la cola de prioridad (heap)
import sys    # para modificar la ruta de busqueda de modulos
import os     # Para manejar rutas de archivos ya que tuve problemas con las rutas

ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ruta_raiz)    # Agrega la raíz al path para poder importar módulos

from mundo.node import Node  
from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa


def heuristica_manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])  # calcula la distancia de manhattan entre dos puntos


def avara(grid, inicio, destino, pasajeros):
    meta_pasajeros = frozenset(pasajeros)  # Compara si ya recogió a todos los pasajeros

    nodo_inicial = Node(
        posicion=inicio,                              # posicion inicial (fila, col)
        pasajeros_recogidos=frozenset(),              # Conjunto vacío de pasajeros
        padre=None,                                   # No tiene padre (es raíz)
        g=0,                                          # Costo acumulado = 0
        h=heuristica_manhattan(inicio, destino)       # Heurística al destino
    )

    contador = 0            # Contador para desempate en la cola
    frontera = []           # cola de prioridad heap

    # En Avara, la prioridad es solo la heuristica (h), no considera el costo real
    heapq.heappush(frontera, (nodo_inicial.h, contador, nodo_inicial))
    contador += 1           # incrementa el contador

    visitados = set()       # conjunto de estados visitados (evita ciclos)
    nodos_expandidos = 0    # contador de nodos expandidos

    while frontera:         # Bucle principal mientras haya nodos por explorar
        _, _, nodo = heapq.heappop(frontera)
        nodos_expandidos += 1        # Incrementa contador de expandidos

        # Condición de META: Si recogió todos los pasajeros y esta en el destino
        if nodo.pasajeros_recogidos == meta_pasajeros and nodo.posicion == destino:
            # Retorna el resultado con toda la info
            return {
                'camino': nodo.obtener_camino(),        # Lista de posiciones
                'costo': nodo.g,                        # Costo total acumulado
                'nodos_expandidos': nodos_expandidos,   # Nodos explorados
                'profundidad': nodo.profundidad         # Profundidad del nodo
            }

        estado = (nodo.posicion, nodo.pasajeros_recogidos)  # Clave unica del estado actual

        # Si ya visitamos este estado, se salta
        if estado in visitados:
            continue
        visitados.add(estado)  # marca el estado como visitado

        # Genera todos los vecinos del nodo actual
        for vecino in grid.get_vecinos(nodo):
            # Calcula la heuristica de acuerdo a si ya recogio todos los pasajeros o no
            if vecino.pasajeros_recogidos == meta_pasajeros:
                # Si ya recogio todos, la heuristica es distancia al destino
                vecino.h = heuristica_manhattan(vecino.posicion, destino)
            else:
                # Si aún faltan pasajeros, busca el pasajero más cercano
                pasajeros_faltantes = [p for p in pasajeros if p not in vecino.pasajeros_recogidos]
                if pasajeros_faltantes:
                    # Heuristica = distancia al pasajero más cercano
                    vecino.h = min(heuristica_manhattan(vecino.posicion, p) for p in pasajeros_faltantes)
                else:
                    # Por si acaso, si no hay pasajeros faltantes
                    vecino.h = heuristica_manhattan(vecino.posicion, destino)
            
            # Agrega el vecino a la frontera con prioridad h
            heapq.heappush(frontera, (vecino.h, contador, vecino))
            contador += 1

    return None  # Si la frontera se vacía sin encontrar solución


