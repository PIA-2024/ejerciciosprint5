from datetime import datetime

class Account:# escribe tu código aquí
    
    def __init__(self, bank:str, acc_id:str, holder_id:str, balance:float=0.0): # escribe tu código aquí
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = balance
        self.start_date = datetime.now()
# Ejemplo de uso
# Crear una instancia de la clase Account
mi_cuenta = Account(bank="Mi Banco", acc_id="123456", holder_id="ABC123")

# Acceder a los atributos de la cuenta
print("Banco:", mi_cuenta.bank)
print("ID de cuenta:", mi_cuenta.acc_id)
print("ID del titular:", mi_cuenta.holder_id)
print("Saldo inicial:", mi_cuenta.balance)
print("Fecha de apertura de la cuenta:", mi_cuenta.start_date)
