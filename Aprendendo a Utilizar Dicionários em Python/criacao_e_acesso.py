pessoa = {"nome": "Guilherme", "idade": 28, "profissao": "programador"} # somente aceita como chave valores imutáveis

aluno = dict(nome="Amanda", idade=27)

# ---- ACRESCENTAR UM DADO:
pessoa["telefone"] = "3333-1234"
print(pessoa)

# ---- ACESSAR UM DADO:
print(pessoa["nome"])

# ---- ALTERAR UM DADO:
pessoa["nome"] = "Maria"
print(pessoa["nome"])


# -------- Dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
    }

print(contatos["giovanna@gmail.com"]["telefone"])

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)


# -------- Iterar dicionários
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items(): # .items retorna uma lista de tuplas
    print(chave, valor)