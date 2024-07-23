#Polimorfismo: Crea una clase base Animal con un método hacerSonido y una clase derivada Perro que sobrescriba este método.
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

perro = Perro()
perro.hacer_sonido()
