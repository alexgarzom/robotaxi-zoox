<<<<<<< HEAD


class Grid:
    
    LIBRE = 0
    MURO = 1
    INICIO = 2
    FLUJO_ALTO = 3
    PASAJERO = 4
    DESTINO = 5

    def __init__(self, matriz):
        self.matriz = matriz                # Almacena la matriz original
        self.filas = len(matriz)            # Número de filas
        self.columnas = len(matriz[0]) if matriz else 0  # Número de columnas

        ### Encontrar posiciones especiales ###

        self.inicio = self._encontrar_posicion(Grid.INICIO)                 # Posición inicio
        self.destino = self._encontrar_posicion(Grid.DESTINO)               # Posición destino
        self.pasajeros = self._encontrar_todas_posiciones(Grid.PASAJERO)    # Lista de pasajeros

    def _encontrar_posicion(self, valor):  # Busca la primer celda con un valor específico
        for i in range(self.filas):         # Recorre filas
            for j in range(self.columnas):  # Recorre columnas
                if self.matriz[i][j] == valor:  # Si encuentra el valor
                    return (i, j)              # Retorna la posición
        return None                         # Si no encuentra retorna None

    def _encontrar_todas_posiciones(self, valor):
        posiciones = []                       # Guarda las posiciones
        for i in range(self.filas):           # Recorre filas
            for j in range(self.columnas):    # Recorre las columnas
                if self.matriz[i][j] == valor:  # Si encuentra el valor
                    posiciones.append((i, j))   # Agrega la posición
        return posiciones

    def es_valida(self, fila, col):   # Verifica si una coordenada está dentro del grid
        return 0 <= fila < self.filas and 0 <= col < self.columnas  # Dentro de los límites

    def es_transitable(self, fila, col):   # Verifica si una celda puede ser transitada, osea que no sea un muro
        if not self.es_valida(fila, col):  # Esta fuera del grid
            return False                    # No transitable
        return self.matriz[fila][col] != Grid.MURO  # True si no es un muro

    def costo_movimiento(self, fila, col):  # Obtiene el costo de estar en una casilla específica
        tipo = self.matriz[fila][col]       # Obtiene el tipo de celda

        # Según el tipo retorna el costo

        if tipo in [Grid.LIBRE, Grid.INICIO, Grid.PASAJERO, Grid.DESTINO]:
            return 1                                                        # Costo 1 para flujo bajo
        elif tipo == Grid.FLUJO_ALTO:
            return 7                                                        # Costo 7 para flujo alto
        return 1         
    
    def get_vecinos(self,nodo):
        vecinos = []
        fila,col = nodo.posicion
        
        #4 Movimientos posibles
        movimientos = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for df, dc in movimientos:
            nueva_fila = fila + df
            nueva_col = col + dc
            
            if self.es_transitable(nueva_fila,nueva_col):
                #se calcula el costo de entrada en esa celda
                costo = nodo.g + self.costo_movimiento(nueva_fila,nueva_col)
                
                #ahora ver si hay un pasajero en esa celda y recogerlo automáticamente
                nuevos_pasajeros = set(nodo.pasajeros_recogidos)
                if self.matriz[nueva_fila][nueva_col] == Grid.PASAJERO:
                    nuevos_pasajeros.add((nueva_fila,nueva_col))
                    
                from mundo.node import Node
                
                vecino = Node(
                    posicion = (nueva_fila,nueva_col),
                    pasajeros_recogidos = frozenset(nuevos_pasajeros),
                    padre = nodo,
                    g = costo
                )
                vecinos.append(vecino)  
        return vecinos                                                 # Valor por defecto


if __name__ == "__main__":
    from lectorMapa import leer_mapa
    
    matriz = leer_mapa()
    if matriz:
        grid = Grid(matriz)
        print("Grid creado correctamente")
        print(f"Inicio: {grid.inicio}")
        print(f"Destino: {grid.destino}")
        print(f"Pasajeros: {grid.pasajeros}")
=======
class Grid:
    def __init__(self, matriz):
        self.matriz = matriz
        self.rows = len(matriz)
        self.cols = len(matriz[0])
        self.start = None
        self.goal = None
        self.passengers = []
        self._extraer_elementos()
    


    #extraer elemenetos de la matriz e idenfiticarlos



    def _extraer_elementos(self):
        for i, fila in enumerate(self.matriz):
            for j, valor in enumerate(fila):
                if valor == 2:
                    self.start = (i, j)
                elif valor == 5:
                    self.goal = (i, j)
                elif valor == 4:
                    self.passengers.append((i, j))


    #moverse
    def get_neighbors(self, i, j):
        vecinos = []
        movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
        for di, dj in movimientos:
            ni = i + di
            nj = j + dj
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                if self.matriz[ni][nj] != 1:
                    vecinos.append((ni, nj))
        return vecinos
   
   
   
   
    #costo del trafico
    def get_cost(self, i, j):
        if self.matriz[i][j] == 3:
            return 7
        return 1







>>>>>>> 94993da (modificacion de grid)

