# Cria o input e atribui como 0 a contagem inicial dos valores
numero = int(input("Insira um número: "))
positivos = 0
negativos = 0

# Cria o loop que será executado enquanto o usuário não inserir 0
while (numero != 0):
    if numero > 0:
        print("positivo!")
        positivos += 1
        
    else:
        print("negativo!")
        negativos += 1
    # Retorna para atribuir um novo valor ao numero, evita um loop infinito    
    numero = int(input("Novo número: "))

# Imprime a frase de encerramento do programa
print(f"{positivos} números positivos, {negativos} números negativos")

