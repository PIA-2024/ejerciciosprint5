import datetime as dt

class Account:
    def __init__(self, bank, acc_id, holder_id, balance:float=0.0):
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = balance
        self.start_date = dt.datetime.now()

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
            print(f"Se depositaron {amount} unidades. Nuevo saldo: {self.balance}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def withdraw(self, amount:float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Se retiraron {amount} unidades. Nuevo saldo: {self.balance}")
        elif amount > self.balance:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El monto a retirar debe ser mayor que 0.")

# Ejemplo de uso
mi_cuenta = Account(bank="Mi Banco", acc_id="123456", holder_id="ABC123")
print("Saldo inicial:", mi_cuenta.balance)

mi_cuenta.deposit(100.0)
mi_cuenta.withdraw(50.0)
mi_cuenta.withdraw(70.0)
