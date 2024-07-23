"""Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine
si un número está en una lista ordenada de 10 elementos."""
def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            bajo = medio + 1
        else:
            alto = medio - 1
    return False

lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_a_buscar = 7

if busqueda_binaria(lista_ordenada, elemento_a_buscar):
    print("El elemento se encuentra en la lista.")
else:
    print("El elemento no se encuentra en la lista.")
