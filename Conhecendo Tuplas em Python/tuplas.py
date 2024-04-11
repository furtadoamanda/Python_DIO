frutas = ("laranja", "pera", "uva",) # vírgula no final como boa prática para indicar que é uma tupla

pais = ("Brasil",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

print(frutas, pais, letras, numeros)

print(frutas[0])
print(frutas[-1])

# ------- TUPLAS ANINHADAS
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

# ------- FATIAMENTO

print(letras[2:])
print(letras[0:3:2])

# Tuplas têm o mesmo comportamento de uma lista, a diferença é que elas não podem ser alteradas. O fatiamento, a iteração e a função enumerate funcionam da mesma maneira.

# Os métodos que as tuplas aceitam são: count, index e len