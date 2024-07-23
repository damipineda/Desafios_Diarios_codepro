"""Formas geométricas: Define una clase base FormaGeometrica con métodos
calcular_area y calcular_perimetro. Crea clases derivadas Rectangulo y Circulo que sobrescriban estos métodos."""
class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

rectangulo = Rectangulo(5, 3)
area_rectangulo = rectangulo.calcular_area()
perimetro_rectangulo = rectangulo.calcular_perimetro()
print(f"Área del rectángulo: {area_rectangulo}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")

circulo = Circulo(4)
area_circulo = circulo.calcular_area()
perimetro_circulo = circulo.calcular_perimetro()
print(f"Área del círculo: {area_circulo}")
print(f"Perímetro del círculo: {perimetro_circulo}")
