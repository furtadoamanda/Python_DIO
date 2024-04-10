def sacar(self, valor: float) -> None: # início do bloco do método
    if self.saldo >= valor: # início do bloco do if
        self.saldo -= valor
    # fim do bloco do if
# fim do bloco do método

# ----------------------------

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print("Retire seu dinheiro na boca do caixa")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)