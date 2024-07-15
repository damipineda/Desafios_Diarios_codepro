def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
lista = [64, 34, 25, 12, 22]
print(ordenamiento_burbuja(lista))  # [12, 22, 25, 34, 64]