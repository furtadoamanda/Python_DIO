valor = float(input("Digite o valor do depósito: "))
saldo = 0

if valor > 0:
    saldo += valor
    print(f"Depósito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}")
elif valor < 0:
    print("Valor inválido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")