"""Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, 
escribe una función que encuentre el camino más corto entre dos nodos 
especificados usando cualquier método que prefieras."""
from collections import deque

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 10},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 2},
    'F': {'C': 10, 'E': 2},
}

def camino_mas_corto(grafo, nodo_inicial, nodo_final):
    cola = deque([(nodo_inicial, [nodo_inicial], 0)])
    visitados = set()

    while cola:
        nodo_actual, camino, distancia = cola.popleft()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            if nodo_actual == nodo_final:
                return camino, distancia

            for vecino, peso in grafo[nodo_actual].items():
                if vecino not in visitados:
                    nueva_distancia = distancia + peso
                    nuevo_camino = camino + [vecino]
                    cola.append((vecino, nuevo_camino, nueva_distancia))

    return None, float('inf')

nodo_inicial = 'A'
nodo_final = 'F'
camino, distancia = camino_mas_corto(grafo, nodo_inicial, nodo_final)
print(f"Camino más corto: {camino}, Distancia: {distancia}")
