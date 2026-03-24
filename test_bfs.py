from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa
from mundo.node import Node
from algoritmosBusqueda.noinformada.busCostoUni import BusquedaCosto
from algoritmosBusqueda.noinformada.busAmplitud import BusquedaAmplitud
from algoritmosBusqueda.noinformada.busProfundidad import BusquedaProfundidad
# 1. Cargar el mapa
matriz = leer_mapa()
grid   = Grid(matriz)

# 2. Crear nodo inicial
nodo_inicial = Node(
    posicion            = grid.inicio,
    pasajeros_recogidos = frozenset()
)

# 3. Definir todos los pasajeros que hay que recoger
pasajeros_totales = frozenset(grid.pasajeros)


print(f"Celda (1,0): {grid.matriz[1][0]}")
print(f"Celda (0,0): {grid.matriz[0][0]}")
print(f"Es transitable (1,0): {grid.es_transitable(1,0)}")
print(f"Vecinos del nodo inicial:")
from mundo.node import Node
nodo_prueba = Node(posicion=grid.inicio, pasajeros_recogidos=frozenset())
for v in grid.get_vecinos(nodo_prueba):
    print(f"  {v.posicion}")


# 4. Ejecutar BFS
bfs       = BusquedaAmplitud(grid)
resultado = bfs.buscar(nodo_inicial, pasajeros_totales)


# ejecutar por costo

bcu = BusquedaCosto(grid)
resultado2 = bcu.buscar(nodo_inicial, pasajeros_totales)

#Ejecutar por profundidad evitando ciclos
dfs = BusquedaProfundidad(grid)
resultado3 = dfs.buscar(nodo_inicial, pasajeros_totales)


# 5. Ver resultado
if resultado:
    print("✅ BFS - Solución encontrada!")
    print(f"Camino: {resultado['camino']}")
    print(f"Nodos expandidos: {resultado['nodos_expandidos']}")
    print(f"Profundidad: {resultado['profundidad']}")
    print(f"Costo: {resultado['costo']}")
else:
    print("❌ BFS - No se encontró solución")

if resultado2:
    print("✅ bcu - Solución encontrada!")
    print(f"Camino: {resultado2['camino']}")
    print(f"Nodos expandidos: {resultado2['nodos_expandidos']}")
    print(f"Profundidad: {resultado2['profundidad']}")
    print(f"Costo: {resultado2['costo']}")
else:
    print("❌ UCS - No se encontró solución")

if resultado3:
    print("✅ dfs - Solución encontrada!")
    print(f"Camino: {resultado3['camino']}")
    print(f"Nodos expandidos: {resultado3['nodos_expandidos']}")
    print(f"Profundidad: {resultado3['profundidad']}")
    print(f"Costo: {resultado3['costo']}")
else:
    print("❌ UCS - No se encontró solución")