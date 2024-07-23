#Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.
def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

lista_con_duplicados = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)
