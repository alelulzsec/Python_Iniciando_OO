class Account:

    def __init__(self, number, total):
        self.number = number
        self.total = total

alexandre = Account(123, 50.00)

#print(alexandre.saldo)

def depositar(self, value): # Função de deposito
    self.total+=value

def sacar(self, value): # Função de Sacar
    self.total-=value

def get_total(self): # Função que mostra o total da conta
    return self.total