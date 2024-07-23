"""Piloto de eventos (Priority Queue): Implementa una cola de
prioridad utilizando una lista para insertar y eliminar 5 elementos."""
class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def agregar(self, elemento, prioridad):
        self.cola.append((elemento, prioridad))
        self.cola.sort(key=lambda x: x[1])

    def eliminar(self):
        if len(self.cola) > 0:
            return self.cola.pop(0)
        else:
            return None

cola_prioridad = ColaPrioridad()
cola_prioridad.agregar("Elemento 1", 3)
cola_prioridad.agregar("Elemento 2", 1)
cola_prioridad.agregar("Elemento 3", 5)
cola_prioridad.agregar("Elemento 4", 2)
cola_prioridad.agregar("Elemento 5", 4)

while True:
    elemento = cola_prioridad.eliminar()
    if elemento is None:
        break
    print(elemento[0])
