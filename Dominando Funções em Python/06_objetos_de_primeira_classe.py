def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação entre {a} e {b} é {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

teste = somar
print(teste(1, 23))