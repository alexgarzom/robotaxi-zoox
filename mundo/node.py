class Node:

    def __init__(self, posicion, pasajeros_recogidos=None, padre=None, g=0, h=0):
        self.posicion             = posicion               # (fila, col) actual del robotaxi
        self.pasajeros_recogidos  = pasajeros_recogidos if pasajeros_recogidos is not None else frozenset()
        self.padre                = padre                  # Nodo padre (para reconstruir camino)
        self.g                    = g                      # Costo acumulado desde el inicio
        self.h                    = h                      # Heurística (estimado al destino)
        self.f                    = g + h                  # Costo total (usado por A* y Avara)
        self.profundidad          = (padre.profundidad + 1) if padre else 0  # Para el reporte

    def __eq__(self, other):
        # Dos nodos son iguales si están en la misma posición Y recogieron los mismos pasajeros
        return self.posicion == other.posicion and self.pasajeros_recogidos == other.pasajeros_recogidos

    def __lt__(self, other):
        # Necesario para que heapq (cola de prioridad) pueda comparar nodos
        return self.f < other.f

    def __hash__(self):
        # Necesario para usar nodos en sets (evitar ciclos)
        return hash((self.posicion, self.pasajeros_recogidos))

    def obtener_camino(self):
        # Reconstruye el camino desde el nodo actual hasta el inicio
        camino = []
        nodo = self
        while nodo:
            camino.append(nodo.posicion)
            nodo = nodo.padre
        return list(reversed(camino))



