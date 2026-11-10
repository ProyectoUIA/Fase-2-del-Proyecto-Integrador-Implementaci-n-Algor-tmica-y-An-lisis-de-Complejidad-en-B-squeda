from collections import deque
from time import perf_counter


def bfs(problema):
    """
    Busqueda en anchura (BFS).
    Utiliza una cola FIFO.
    """

    inicio = perf_counter()

    frontera = deque([(problema.estado_inicial, [])])
    visitados = {problema.estado_inicial}
    nodos_expandidos = 0

    while frontera:
        estado, camino = frontera.popleft()

        if problema.es_meta(estado):
            tiempo = (perf_counter() - inicio) * 1000

            return {
                "algoritmo": "BFS",
                "camino": camino,
                "nodos_expandidos": nodos_expandidos,
                "tiempo_ms": tiempo,
                "costo": len(camino)
            }

        nodos_expandidos += 1

        for accion in problema.acciones(estado):
            nuevo_estado = problema.resultado(estado, accion)

            if nuevo_estado not in visitados:
                visitados.add(nuevo_estado)
                nuevo_camino = camino + [accion]
                frontera.append((nuevo_estado, nuevo_camino))

    return None


def dfs(problema):
    """
    Busqueda en profundidad (DFS).
    Utiliza una pila LIFO.
    """

    inicio = perf_counter()

    frontera = [(problema.estado_inicial, [])]
    visitados = {problema.estado_inicial}
    nodos_expandidos = 0

    while frontera:
        estado, camino = frontera.pop()

        if problema.es_meta(estado):
            tiempo = (perf_counter() - inicio) * 1000

            return {
                "algoritmo": "DFS",
                "camino": camino,
                "nodos_expandidos": nodos_expandidos,
                "tiempo_ms": tiempo,
                "costo": len(camino)
            }

        nodos_expandidos += 1

        for accion in problema.acciones(estado):
            nuevo_estado = problema.resultado(estado, accion)

            if nuevo_estado not in visitados:
                visitados.add(nuevo_estado)
                nuevo_camino = camino + [accion]
                frontera.append((nuevo_estado, nuevo_camino))

    return None
