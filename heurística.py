# 1. CLASE DEL PROBLEMA 
import heapq

# =========================================================
# IMPLEMENTACIÓN DEL ALGORITMO A* Y LA FUNCIÓN HEURÍSTICA
# =========================================================

def heuristica_documento(estado) -> float:
    """
    Función heurística h(n): Estima el costo restante hacia la meta.
    h(n) = len(estado.campos_pendientes)
    Representa exactamente el número de campos obligatorios faltantes por diligenciar.
    """
    return float(len(estado.campos_pendientes))


class NodoAStar:
    """Estructura para la frontera con cola de prioridad evaluada en f(n) = g(n) + h(n)."""
    def __init__(self, estado, padre=None, accion=None, g=0, h=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, otro):
        return self.f < otro.f


def busqueda_a_estrella(estado_inicial):
    """Implementación del algoritmo A* utilizando heapq para cola de prioridad."""
    nodo_inicial = NodoAStar(
        estado=estado_inicial, 
        padre=None, 
        accion=None, 
        g=0, 
        h=heuristica_documento(estado_inicial)
    )
    
    frontera = []
    heapq.heappush(frontera, (nodo_inicial.f, nodo_inicial))
    visitados = {estado_inicial: nodo_inicial.g}
    nodos_expandidos = 0

    while frontera:
        _, nodo_actual = heapq.heappop(frontera)
        nodos_expandidos += 1

        if nodo_actual.estado.es_meta():
            camino = []
            curr = nodo_actual
            while curr.padre is not None:
                camino.append(curr.accion)
                curr = curr.padre
            camino.reverse()
            return camino, nodo_actual.g, nodos_expandidos

        for sucesor, accion, costo_paso in nodo_actual.estado.obtener_sucesores():
            nuevo_g = nodo_actual.g + costo_paso
            if sucesor not in visitados or nuevo_g < visitados[sucesor]:
                visitados[sucesor] = nuevo_g
                h_val = heuristica_documento(sucesor)
                nuevo_nodo = NodoAStar(sucesor, nodo_actual, accion, nuevo_g, h_val)
                heapq.heappush(frontera, (nuevo_nodo.f, nuevo_nodo))
    return None




