# Desafio: A Aventura do Explorador
titulo = " A Aventura do Explorador "
print(titulo.center(40, "*") + "\n")

quantidade_passos = int(input("Indique a quantidade de passos que o explorador deve dar na floresta: "))

if quantidade_passos < 0:
    print("Número de passos inválido.")
elif quantidade_passos == 0:
        print("Nenhum passo dado na floresta.")
else:
    quantidade_passos_contagem = range(1, quantidade_passos + 1)
    for unidade in quantidade_passos_contagem:
        if unidade == 1:
            print(f"Explorador: {unidade} passo")
        else:
            print(f"Explorador: {unidade} passos")



#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.