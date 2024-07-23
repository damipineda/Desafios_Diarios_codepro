#Auto y Motor: Implementa una clase Auto que contenga una instancia de una clase Motor con un método para describir el motor.

class Motor:
    def __init__(self, cilindros):
        self.cilindros = cilindros

    def describir_motor(self):
        print(f"Este motor tiene {self.cilindros} cilindros.")

class Auto:
    def __init__(self, motor):
        self.motor = motor

    def mostrar_motor(self):
        self.motor.describir_motor()

motor = Motor(4)
auto = Auto(motor)
auto.mostrar_motor()
