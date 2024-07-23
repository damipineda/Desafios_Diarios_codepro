#Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

def dfs(grafo, nodo_inicial, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo_inicial)
    print(nodo_inicial)

    for vecino in grafo[nodo_inicial]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

dfs(grafo, 'A')
