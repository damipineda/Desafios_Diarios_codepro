#Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.
from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

def bfs(grafo, nodo_inicial):
    visitados = set()
    cola = deque([nodo_inicial])

    while cola:
        nodo_actual = cola.popleft()
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            print(nodo_actual)

            for vecino in grafo[nodo_actual]:
                cola.append(vecino)

bfs(grafo, 'A')
