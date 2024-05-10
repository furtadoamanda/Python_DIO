
# Entrada do usuário
peso = float(input("Insira o peso da fruta: "))
textura_input = input("Insira a textura da fruta: ")
textura = textura_input.lower()
cor_input = input("Insira a cor da fruta: ")
cor = cor_input.lower()

# Verificação dos requisitos
if peso >= 150 and textura == "smooth" and cor == "red":
    print("A fruta é um morango!")
elif peso >= 130 and textura == "rough" and cor == "red":
    print("A fruta é uma maçã!")
elif peso >= 120 and textura == "smooth" and cor == "orange":
    print("A fruta é uma laranja!")
elif peso >= 150 and textura == "rough" and cor == "yellow":
    print("A fruta é uma banana!")
else:
    print("Não foi possível classificar a fruta.")


# TODO: melhorar com funções e dicionário