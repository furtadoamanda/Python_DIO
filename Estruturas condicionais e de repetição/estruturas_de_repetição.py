# -------------- FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: # não muito usado
    print() # adiciona uma quebra de linha


# ------------- RANGE
for numero in range(11):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")
# não vão funcionar nesse código porque um conflita o outro

# ------------ WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n: "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# ----------- BREAK
while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break # corta o laço da repetição / condição de parada

    if numero % 2 == 0:
        continue # pula a execução

    print(numero)

# ---------- CONTINUE
for numero in range(100):

    if numero % 2 == 0:
        continue # pula a execução

    print(numero, end=" ")