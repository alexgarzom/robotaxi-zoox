class Grid:
    
    LIBRE=0
    MURO=1
    INICIO=2
    FLUJO_ALTO=3
    PASAJERO=4
    DESTINO=5

    def __init__(self,matriz):
        self.matriz=matriz                #Almacena la matriz oririgal
        self.filas=len(matriz)            #Numero de filas
        self.columnas=len(matriz[0]) if matriz else 0  #Número de columnas

        ### Encontrar posiciones especiales ###

        self.inicio=self._encontrar_posicion(Grid.INICIO)                 #Posición inicio
        self.destino=self._encontrar_posicion(Grid.DESTINO)               #Posición inicio
        self.pasajeros=self._encontrar_todas_posiciones(Grid.PASAJERO)    #Lista de pasajeros

    def _encontrar_posiciones(self,valor):  #Busca la primer celda con un valor especifico"
        for i in range(self.filas):         #Recorre filas
            for j in range(self.columnas):  #Recorre columnas
               if self.matriz[i][j]==valor: #Si encuentra el valor
                   return(i,j)              #Retorna la posición
        return None                         #Si no encuentra retorna None
        