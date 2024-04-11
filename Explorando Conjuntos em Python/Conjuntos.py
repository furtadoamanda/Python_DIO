# A diferença dos sets para as listas é que nos sets não existem elementos duplicados. Não seguindo a ordem dos elementos

print(set([1, 2, 3, 1, 3, 4]))

print(set("acabaxi"))

print(set(("palio", "gol", "celta", "palio")))

# CONJUNTOS NÃO SOPORTAM INDEXAÇÃO NEM FATIAMENTO

numeros = {1, 2, 3, 2} # sintaxe do conjunto {}

numeros = list(numeros)

print(numeros[0])


# ------- ITERAR CONJUNTOS
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)


# ------- ENUMERATE
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# ------- METODOS UNION, INTERSECTION, DIFFERENCE E SYMMETRIC DIFFERENCE
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))


# ------ MÉTODOS ISSUBSET (subconjunto) E ISSUPERSET (superconjunto)
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))

print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))


# ------ MÉTODO ISDISJOINT
conjunto_e = {1, 2, 3, 4, 5}
conjunto_f = {6, 7 ,8 ,9}
conjunto_j = {1, 0}

print(conjunto_e.isdisjoint(conjunto_f))
print(conjunto_e.isdisjoint(conjunto_j))


# ------- ADD
sorteio = {1, 23}

sorteio.add(25)
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25) # Como o elemento já existe, não será adicionado
print(sorteio)


# ------- CLEAR
numbers = {1, 23}

numbers.clear()
print(numbers)


# ------ COPY
sorteio1 = sorteio.copy()

print(sorteio1, sorteio)


# ------- DISCARD
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.discard(1)
print(numeros)

numeros.discard(45) # pedir que descarte um elemento que não existe não apresenta erro, ele apenas não realizará nenhuma mudança
print(numeros)


# -------- POP
# Diferença do pop da lista é que tira o primeiro valor em vez de tirar o último

numeros.pop()
print(numeros)

# -------- REMOVE
# Se chamar com um elemento que não existe ele dará erro
numeros.remove(3)
print(numeros)


# -------- LEN
print(len(numeros))


# -------- IN
print(2 in numeros)
print(10 in numeros)