from collections import deque

class BusquedaAmplitud:

    def __init__(self,grid):
        self.grid = grid

    def buscar(self, nodo_inicial, pasajeros_totales):

        frontera = deque([nodo_inicial]) #doble cola, nodo inicial el primero de la lista

        visitados = set() #La clase Node en node.py, hace uso del __hash__ para verificar si ya se estuvo en un nodo.

        nodos_expandidos = 0

        while frontera: #Nodos a explorar
            nodo = frontera.popleft()

            if (nodo.posicion,nodo.pasajeros_recogidos)in visitados:
                continue #sirve para saltar de un nodo al siguiente. 

            visitados.add((nodo.posicion,nodo.pasajeros_recogidos)) #se agrega el nodo visitado
            nodos_expandidos+=1 #nodos expandido  + 1

            if nodo.posicion == self.grid.destino and nodo.pasajeros_recogidos == pasajeros_totales:
                return{
                    "camino": nodo.obtener_camino(),
                    "nodos_expandidos": nodos_expandidos,
                    "profundidad": nodo.profundidad,
                    "costo": nodo.g
                }
        
            for vecino in self.grid.get_vecinos(nodo):
                frontera.append(vecino)

        return None
