class BusquedaProfundidad:

    def __init__(self,grid):
        self.grid = grid

    def buscar(self,nodo_inicial,pasajeros_totales):
        
        frontera = [(nodo_inicial)] #se usa una lista comun, partiendo del nodo inicial

        visitados = set() #evitar ciclos

        nodos_expandidos = 0

        while frontera:
            nodo = frontera.pop()

            if (nodo.posicion, nodo.pasajeros_recogidos) in visitados:
                continue

            visitados.add((nodo.posicion, nodo.pasajeros_recogidos))
            nodos_expandidos+=1

            if nodo.posicion == self.grid.destino and nodo.pasajeros_recogidos == pasajeros_totales:
                return{
                    "camino": nodo.obtener_camino(),
                    "nodos_expandidos":nodos_expandidos,
                    "profundidad": nodo.profundidad,
                    "costo": nodo.g
                }
            
            for vecino in self.grid.get_vecinos(nodo):
                frontera.append(vecino)

        return None

        





