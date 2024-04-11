frutas = ["laranja", "maca", "uva"]

verduras = [] # lista vazia

letras = list("python") # cria uma lista onde cada letra da palavra é um elemento

numeros = list(range(10)) # cada número retornado pela função range será um elemento

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] # uma lista pode ser composta por elementos de diversos formatos

# ------------------ ACESSO DIRETO

print(frutas[0] + frutas[2] + frutas[-2])

# ----------------- LISTA ANINHADA
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# --------------- FATIAMENTO
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # a partir do índice 2 (inclusivo)
print(lista[:2]) # até o índice 2 (exclusivo)
print(lista[1:3]) # do 1 (inclusivo) até o 3 (exclusivo)
print(lista[0:3:2]) # do 0 ao 3, saltando de 2 em 2
print(lista[::]) # tudo vazio, do 0 ao fim da string, sem salto
print(lista[::-1]) # espelha a lista

# -------------- ITERAR LISTAS
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# -------------- FUNÇÃO ENUMERATE
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# ------------- LIST COMPREENSION
numbers = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numbers:
    if numero % 2 ==0:
        pares.append(numero) # insere individualmente cada item par na lista pares
        print(pares)
# Com o List compreension, a mesma ação é feita da seguinte maneira:
evens = [numero for numero in numbers if numero % 2 == 0] # a primeira parte é o retorno (o que vai compor a lista), a segunda parte é o laço. Essas duas partes são obrigatórias. Para criar o filtro, se adiciona a terceira parte, que fará o if antes de retornar o valor, que só será retornado se atendida a condição
print(evens)

quadrado = [numero ** 2 for numero in numbers] # antes de retornar o número, irá elevar ao quadrado
print(quadrado)