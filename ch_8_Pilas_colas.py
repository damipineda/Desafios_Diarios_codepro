#Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        else:
            return None

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop(0)
        else:
            return None

pila = Pila()
pila.apilar("Elemento 1")
pila.apilar("Elemento 2")
pila.apilar("Elemento 3")

while True:
    elemento = pila.desapilar()
    if elemento is None:
        break
    print(elemento)

cola = Cola()
cola.encolar("Elemento 1")
cola.encolar("Elemento 2")
cola.encolar("Elemento 3")

while True:
    elemento = cola.desencolar()
    if elemento is None:
        break
    print(elemento)
