# ------------- APPEND
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 32, 20])

print(lista)


# ------------ CLEAR
lista.clear()

print(lista)


# ---------- COPY
# Cria uma lista igual, com os mesmos valores, mas que tem um id diferente, ou seja, é armazenada em outro local de memória
lista = [1, "Python", [40, 30, 20]]
lista2 = lista.copy()

print(lista2)
print(id(lista2), id(lista)) # são elementos diferentes, alterações na cópia não irão alterar a lista inicial


# ---------- COUNT
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul")) # conta a quantidade de vezes que o objeto aparece na lista


# --------- EXTEND
# Acrescenta itens na lista, mas por meio de um "merge" com outra lista, sem eliminar itens duplicados
linguagens = ["Python", "JS", "C"]

linguagens.extend(["Java", "CSharp", "C"])

print(linguagens)


# ---------- INDEX
# Informa a *primeira* ocorrência do elemento
print(linguagens.index("Java"))
print(linguagens.index("C"))


# --------- POP
# Retira o último elemento da lista. Se passar um índice, ele vai retirar o elemento presente no índice indicado
print(linguagens.pop())
print(linguagens)

print(linguagens.pop())
print(linguagens)

print(linguagens.pop(1))
print(linguagens)


# -------- REMOVE
# Outra forma de retirar elementos da lista, passando o objeto em si em vez do seu índice. Se houver mais de um elemento igual na lista, removerá apenas a sua primeira ocorrência
linguagens = ['Python', 'JS', 'C', 'Java', 'CSharp', 'C']
print(linguagens)

linguagens.remove("CSharp")
print(linguagens)

linguagens.remove("C")
print(linguagens)


# ----------- REVERSE
linguagens.reverse() # faz o espelhamento da lista
print(linguagens)

# ----------- SORT
linguagens = ['Python', 'JS', 'C', 'Java', 'CSharp', 'C']

linguagens.sort() # Ordena alfabeticamente
print(linguagens)

linguagens.sort(reverse=True) # Ordena alfabeticamente e inverte
print(linguagens)

linguagens.sort(key=lambda x: len(x)) # Ordena pelo tamanho das strings
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


# ------------ LEN
print(len(linguagens)) # Informa o tamanho da lista, quantos elementos ela tem


# ------------ SORTED
# Método built-in do Python que ordena da mesma maneira que o sort
print(sorted(linguagens))

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))