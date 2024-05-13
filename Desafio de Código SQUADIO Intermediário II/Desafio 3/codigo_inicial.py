# Coletar as informações do usuário
intensidade_feitico = int(input("Qual a intensidade do feitiço? "))

componente_raro_input = input("Presença de componente raro? ")
componente_raro = componente_raro_input.lower()

fase_lunar_input = input("Qual a fase lunar? ")
fase_lunar = fase_lunar_input.lower()

idade_feiticeiro = int(input("Qual a idade do feiticeiro? "))

afinidade_animais_input = input("Afinidade com animais mágicos? ")
afinidade_animais = afinidade_animais_input.lower()

# Definir a presença de componente e afinidade animais como booleano
if componente_raro == "sim":
    componente_raro = True
else:
    componente_raro = False

if afinidade_animais == "sim":
    afinidade_animais = True
else:
    afinidade_animais = False

# OBS: divergência entre o enunciado apresentado e os testes usados como exemplo. Código feito de acordo com os exemplos e testes.
# Atribuir os inputs aos elementos:
if intensidade_feitico >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100 and componente_raro and afinidade_animais:
    print("A afinidade elemental do feiticeiro é com o elemento Fogo!")
elif intensidade_feitico >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and not afinidade_animais:
    print("A afinidade elemental do feiticeiro é com o elemento Água!")
elif intensidade_feitico >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and afinidade_animais:
    print("A afinidade elemental do feiticeiro é com o elemento Terra!")
else:
    print("A afinidade elemental do feiticeiro é com o elemento Ar!")

# TODO: refazer usando funções e dicionários