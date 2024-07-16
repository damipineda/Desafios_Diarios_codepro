from collections import deque

def bfs(grafo, nodo_inicial):
    visitados = set()
    cola = deque([nodo_inicial])
    visitados.add(nodo_inicial)

    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

# Ejemplo de uso
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
bfs(grafo, 0)  # 0 1 2 3 4
