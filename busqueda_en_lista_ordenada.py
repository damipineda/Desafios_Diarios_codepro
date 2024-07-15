def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(busqueda_binaria(lista_ordenada, 7))  # True
print(busqueda_binaria(lista_ordenada, 2))  # False


