#Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo.
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depositaste: ${monto}")
        self.consultar_saldo()

    def consultar_saldo(self):
        print(f"Tu saldo actual es: ${self.saldo}")

cuenta = CuentaBancaria()
cuenta.depositar(100)
cuenta.depositar(200)
