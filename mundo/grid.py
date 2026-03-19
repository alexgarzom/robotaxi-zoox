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
        
    def _encontrar_todas_posiciones(slef, valor):
        posiciones=[]                       #Guarda las posiciones
        for i in range(self.filas):         #Recorre filas
            for j in range(self.columnas):  #Recorre las columnas
                posiciones.append((i,j))
        return posiciones
    
    def es_valida(self,fila,col):   #Verifica si una coordenada está dentro del grid

        return 0 <= fila < self.filas and 0 <= col < self.columnas #Dentro de los limites
    
    def es_transitable(self,fila,col):   #Verifica si una cleda puede ser transitada, osea que no sea un muro
        if not self.es_valida(fila,col): #Esta grueda del grid
            return False                 #No transitable
        return self.matriz[fila][col] != Grid.MURO     #True si no es un muro
    
    def costo_movimiento(self,fila,col):  #Obtiene el costo de estar en una casilla especifica
        tipo=self.matriz[fila][col]       #Obtiene el tipo de celda

        #Segun el tipo retorna el costo

        if tipo in[Grid.LIBRE,Grid.INICIO,Grid.PASAJERO,Grid.DESTINO]:
            return 1                                                        #Costo 1 para flujo bajo
        elif tipo == Grid.FLUJO_ALTO:
            return 7                                                        #Costo 7 para flujo alto
        return 1                                                            #Valor por defecto



            