import heapq #se utiliza como cola de prioridad. Garantiza que el elemento más pequeño este en la raíz

class BusquedaCosto:

    def __init__(self,grid):
        self.grid = grid
    
    def buscar(self,nodo_inicial,pasajeros_totales):

        frontera = [] #nodos por explorar
        heapq.heappush(frontera,(nodo_inicial.g,nodo_inicial))

        visitados = set()

        nodos_expandidos = 0

        while frontera: #explorando nodos
            _, nodo = heapq.heappop(frontera)

            if (nodo.posicion, nodo.pasajeros_recogidos) in visitados:
                continue 

            visitados.add((nodo.posicion,nodo.pasajeros_recogidos))
            nodos_expandidos+=1

            if nodo.posicion == self.grid.destino and nodo.pasajeros_recogidos == pasajeros_totales:
                return{
                    "camino": nodo.obtener_camino(),
                    "nodos_expandidos":nodos_expandidos,
                    "profundidad": nodo.profundidad,
                    "costo": nodo.g
                }
            
            for vecino in self.grid.get_vecinos(nodo):
                heapq.heappush(frontera,(vecino.g,vecino)) #se agregan a la frontera segun su costo

        return None
        



