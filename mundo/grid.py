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








