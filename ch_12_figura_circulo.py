"""Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase derivada Círculo que extienda Figura 
y sobreescriba el método imprimir.
"""
class Figura:
    def imprimir(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Soy un círculo con radio {self.radio}")

circulo = Circulo(4)
circulo.imprimir()
