import heapq                     # Para usar la cola de prioridad (heap)
import sys                       # Para modificar la ruta de búsqueda de módulos
import os                        # Para manejar rutas de archivos ya que tuve problemas con las rutas

# Obtiene la ruta de la carpeta raíz del proyecto (robotaxi-zoox)

ruta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ruta_raiz)    # Agrega la raíz al path para poder importar módulos

from mundo.node import Node    
from mundo.grid import Grid        
from mundo.lectorMapa import leer_mapa  


def heuristica_manhattan(pos1, pos2):
    
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) #Calcula la distancia de manhattan


def a_estrella(grid, inicio, destino, pasajeros):

                                             
    meta_pasajeros = frozenset(pasajeros) # Esto permite comparar si ya recogió todos los pasajeros

    # Crea el nodo inicial: en la posición de inicio, sin pasajeros recogidos
    nodo_inicial = Node(
        posicion=inicio,                       # Posición inicial (fila, col)
        pasajeros_recogidos=frozenset(),       # Conjunto vacío de pasajeros
        padre=None,                            # No tiene padre (es raíz)
        g=0,                                   # Costo acumulado = 0
        h=heuristica_manhattan(inicio, destino)  # Heurística al destino
    )

    contador = 0                               # Contador para desempate en la cola
    frontera = []                              # Cola de prioridad (heap)
                                               # Agrega el nodo inicial a la frontera con prioridad f = g + h
    heapq.heappush(frontera, (nodo_inicial.f, contador, nodo_inicial))
    contador += 1                              # Incrementa el contador

    visitados = {}                             # Diccionario: estado -> mejor costo g
    nodos_expandidos = 0                       # Contador de nodos expandidos

   
    while frontera:                            # Bucle principal: mientras haya nodos por explorar
                                                
        _, _, nodo = heapq.heappop(frontera)   # Extrae el nodo con menor valor f (prioridad)
        nodos_expandidos += 1                  # Incrementa contador de expandidos

        # CONDICIÓN DE META: si recogió todos los pasajeros Y está en el destino
        if nodo.pasajeros_recogidos == meta_pasajeros and nodo.posicion == destino:
            # Retorna el resultado con toda la información
            return {
                'camino': nodo.obtener_camino(),       # Lista de posiciones
                'costo': nodo.g,                       # Costo total acumulado
                'nodos_expandidos': nodos_expandidos,  # Nodos explorados
                'profundidad': nodo.profundidad        # Profundidad del nodo
            }

       
        estado = (nodo.posicion, nodo.pasajeros_recogidos)

        
        if estado in visitados and visitados[estado] <= nodo.g:  # Si ya visitamos este estado con un costo menor o igual, lo saltamos
            continue
      
        visitados[estado] = nodo.g                   # Guarda este estado con su costo g (el mejor encontrado hasta ahora)

       
        for vecino in grid.get_vecinos(nodo):        # Genera todos los vecinos del nodo actual
          
            if vecino.pasajeros_recogidos == meta_pasajeros:   # Calcula la heurística según si ya recogió todos los pasajeros o no

                vecino.h = heuristica_manhattan(vecino.posicion, destino)    # Si ya recogió todos, la heurística es distancia al destino
            else:
                # Si aún faltan pasajeros, busca el pasajero más cercano
                pasajeros_faltantes = [p for p in pasajeros if p not in vecino.pasajeros_recogidos]
                if pasajeros_faltantes:
                    # Heurística = distancia al pasajero más cercano
                    vecino.h = min(heuristica_manhattan(vecino.posicion, p) for p in pasajeros_faltantes)
                else:
                    # Por si acaso, si no hay pasajeros faltantes (nunca debería pasar)
                    vecino.h = heuristica_manhattan(vecino.posicion, destino)
            
            # Calcula f = g + h
            vecino.f = vecino.g + vecino.h
            # Agrega el vecino a la frontera con prioridad f
            heapq.heappush(frontera, (vecino.f, contador, vecino))
            contador += 1

   
    return None  # Si la frontera se vacía sin encontrar solución


