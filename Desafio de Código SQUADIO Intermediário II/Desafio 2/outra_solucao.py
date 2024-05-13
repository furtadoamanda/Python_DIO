# Resolução criada com base no meu código inicial e auxílio do Gemini
# TODO: revisar e aprimorar do meu jeito

def obter_informacoes_fruta():
    """
    Obtém as informações da fruta do usuário (peso, textura e cor).

    Retorna um dicionário com as informações da fruta.
    """
    peso = float(input("Insira o peso da fruta: "))
    textura_input = input("Insira a textura da fruta: ")
    textura = textura_input.lower()
    cor_input = input("Insira a cor da fruta: ")
    cor = cor_input.lower()

    informacoes_fruta = {
        "peso": peso,
        "textura": textura,
        "cor": cor
    }

    return informacoes_fruta

def classificar_fruta(informacoes_fruta):
    """
    Classifica a fruta com base em suas informações (peso, textura e cor).

    Retorna a classe da fruta ou uma mensagem de erro.
    """
    peso = informacoes_fruta["peso"]
    textura = informacoes_fruta["textura"]
    cor = informacoes_fruta["cor"]

    if peso >= 150 and textura == "smooth" and cor == "red":
        return "Morango"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "Maçã"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "Laranja"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "Banana"
    else:
        return "Fruta não identificada."

# Obtém as informações da fruta do usuário
informacoes_fruta = obter_informacoes_fruta()

# Classifica a fruta
classe_fruta = classificar_fruta(informacoes_fruta)

# Imprime o resultado
print(f"A fruta é um(a) {classe_fruta}")