#Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar(nodo, valor):
    if not nodo:
        return Nodo(valor)

    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    else:
        nodo.derecho = insertar(nodo.derecho, valor)

    return nodo

def recorrer_en_orden(nodo):
    if nodo is None:
        return

    recorrer_en_orden(nodo.izquierdo)
    print(nodo.valor)
    recorrer_en_orden(nodo.derecho)

valores = [5, 3, 7, 2, 4]
arbol = None

for valor in valores:
    arbol = insertar(arbol, valor)

print("Recorrido en orden:")
recorrer_en_orden(arbol)

