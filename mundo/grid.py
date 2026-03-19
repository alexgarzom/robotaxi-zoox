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
        