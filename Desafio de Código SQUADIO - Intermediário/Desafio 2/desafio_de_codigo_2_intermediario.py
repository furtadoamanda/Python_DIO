ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Digite a quantidade de ativos: "))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input("Ativo: ")
    ativos.append(codigoAtivo)

ativos.sort()

for ativo in ativos:
    print(f"{ativo}")



