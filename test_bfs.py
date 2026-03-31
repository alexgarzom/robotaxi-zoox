from mundo.grid import Grid
from mundo.lectorMapa import leer_mapa
from mundo.node import Node
from algoritmosBusqueda.noinformada.busCostoUni import BusquedaCosto
from algoritmosBusqueda.noinformada.busAmplitud import BusquedaAmplitud
from algoritmosBusqueda.noinformada.busProfundidad import BusquedaProfundidad
from algoritmosBusqueda.informada.algoritmoAestrella import a_estrella

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

    #---------------------- PRUEBA DE A* -------------

    # Bloque principal que se ejecuta solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    print("="*60)
    print("PRUEBA DEL ALGORITMO A*")
    print("="*60)

    # Lee el mapa desde el archivo
    matriz = leer_mapa()
    if not matriz:
        print("❌ No se pudo cargar el mapa")
        exit(1)

    # Crea el grid (mundo) con la matriz leída
    grid = Grid(matriz)

    # Prueba: verifica que get_vecinos funciona correctamente
    print("\n🔍 Probando get_vecinos...")
    nodo_prueba = Node(posicion=grid.inicio, pasajeros_recogidos=frozenset())
    vecinos = grid.get_vecinos(nodo_prueba)
    print(f"Vecinos desde inicio ({grid.inicio}): {len(vecinos)}")
    for v in vecinos:
        print(f"  {v.posicion}, g={v.g}")

    # Muestra información del grid
    print(f"Inicio: {grid.inicio}")
    print(f"Destino: {grid.destino}")
    print(f"Pasajeros: {grid.pasajeros}")

    # Ejecuta el algoritmo A*
    resultado = a_estrella(grid, grid.inicio, grid.destino, grid.pasajeros)

    # Muestra el resultado
    if resultado:
        print("\n✅ SOLUCIÓN ENCONTRADA")
        print(f"Costo: {resultado['costo']}")
        print(f"Nodos expandidos: {resultado['nodos_expandidos']}")
        print(f"Profundidad: {resultado['profundidad']}")
        print(f"Pasos: {len(resultado['camino'])}")

        # Verifica que se recogieron todos los pasajeros
        recogidos = []
        for pos in resultado['camino']:
            if pos in grid.pasajeros:
                recogidos.append(pos)

        print(f"\nPasajeros recogidos: {recogidos}")
        if set(recogidos) == set(grid.pasajeros):
            print("✅ Todos los pasajeros fueron recogidos")
        else:
            print("❌ Faltan pasajeros")

        # Verifica que termina en el destino correcto
        if resultado['camino'][-1] == grid.destino:
            print("✅ Termina en destino correcto")
        else:
            print("❌ Termina en otro lugar")
    else:
        print("\n❌ No se encontró solución")