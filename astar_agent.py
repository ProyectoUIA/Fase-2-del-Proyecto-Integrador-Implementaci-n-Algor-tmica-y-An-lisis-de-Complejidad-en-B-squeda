import heapq
import time

def heuristica_documento(estado: tuple) -> float:
    """
    Función heurística h(n): Estima el costo restante hacia la meta.
    Cuenta los ceros (0) en la tupla de estado, que representan los campos pendientes.
    """
    return float(estado.count(0))

class NodoAStar:
    """Estructura de nodo para la frontera evaluada en f(n) = g(n) + h(n)."""
    def _init_(self, estado, padre=None, accion=None, g=0, h=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.g = g
        self.h = h
        self.f = g + h

    def _lt_(self, otro):
        return self.f < otro.f

def busqueda_a_estrella(problema_instancia):
    """
    Algoritmo A* preparado como módulo importable.
    Compatible con la estructura de main.py y ProblemaDocumentos.
    """
    start_time = time.perf_counter()
    estado_inicial = problema_instancia.estado_inicial
    
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

        # Se verifica la meta sin contar el nodo como expandido
        if problema_instancia.es_meta(nodo_actual.estado):
            end_time = time.perf_counter()
            camino = []
            curr = nodo_actual
            while curr.padre is not None:
                camino.append(curr.accion)
                curr = curr.padre
            camino.reverse()
            
            return {
                "algoritmo": "A*",
                "camino": camino,
                "nodos_expandidos": nodos_expandidos,
                "tiempo_ms": (end_time - start_time) * 1000,
                "costo": nodo_actual.g
            }

        # Incremento de nodos expandidos al evaluar sucesores
        nodos_expandidos += 1

        for accion in problema_instancia.acciones(nodo_actual.estado):
            nuevo_estado = problema_instancia.resultado(nodo_actual.estado, accion)
            costo_paso = problema_instancia.costo(nodo_actual.estado, accion, nuevo_estado)
            nuevo_g = nodo_actual.g + costo_paso
            
            if nuevo_estado not in visitados or nuevo_g < visitados[nuevo_estado]:
                visitados[nuevo_estado] = nuevo_g
                h_val = heuristica_documento(nuevo_estado)
                nuevo_nodo = NodoAStar(
                    estado=nuevo_estado,
                    padre=nodo_actual,
                    accion=accion,
                    g=nuevo_g,
                    h=h_val
                )
                heapq.heappush(frontera, (nuevo_nodo.f, nuevo_nodo))

