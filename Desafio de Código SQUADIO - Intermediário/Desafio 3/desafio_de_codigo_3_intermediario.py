import string

caracteres_especiais = list(string.punctuation)
# caracteres_especiais = "!@#$%^&*()-_+=}{[]:;'\"\\<>,.?/~"
letras_maiusculas = list(string.ascii_uppercase)
# letras_maiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letras_minusculas = list(string.ascii_lowercase)
# letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numerais = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


senha = input("Insira sua senha: ").strip()

def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificar se possui caractere especial
    for char in senha:
        if char in caracteres_especiais:
            tem_caractere_especial = True
    
    # Verificar se possui letra maiscula
    for char in senha:
        if char in letras_maiusculas:
            tem_letra_maiuscula = True

    # Verificar se possui letra minuscula
    for char in senha:
        if char in letras_minusculas:
            tem_letra_minuscula = True

    # Verificar se possui numero
    for char in senha:
        if char in numerais:
            tem_numero = True

    # Verificando se atende todos os criterios
    if (tem_numero) and (tem_caractere_especial) and (tem_letra_maiuscula) and (tem_letra_minuscula) and (len(senha) > comprimento_minimo):
        print("Sua senha atende aos requisitos de seguranca. Parabéns!")
    elif len(senha) < comprimento_minimo:
        print(f"Sua senha é muito curta. Recomenda-se no mínimo {comprimento_minimo} caracteres.")
    else:
        print("Sua senha não atende aos requisitos de segurança.")
    
    # Verificando se a senha contém sequências comuns
    # sequencias_comuns = ["123456", "abcdef"]
    # for sequencia in sequencias_comuns:
    #     if sequencia in senha:
    #         print("Sua senha contem uma sequencia comum. Tente uma senha mais complexa.")

    # # Verificando se a senha contém palavras comuns
    # palavras_comuns = ["password", "123456", "qwerty"]
    # if senha in palavras_comuns:
    #     print("Sua senha e muito comum. Tente uma senha mais complexa.")


# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
#print(resultado)

