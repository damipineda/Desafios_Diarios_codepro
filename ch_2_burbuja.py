"""Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros
utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección)."""
def ordenamiento_por_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista_para_ordenar = [5, 2, 8, 3, 1]
ordenamiento_por_burbuja(lista_para_ordenar)
print("Lista ordenada:", lista_para_ordenar)
