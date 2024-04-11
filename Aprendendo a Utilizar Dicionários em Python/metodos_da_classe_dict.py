contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# -------- CLEAR
contatos.clear()
print(contatos)


# -------- COPY
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

copia = contatos.copy()
print(copia["guilherme@gmail.com"])

copia["guilherme@gmail.com"] = {"nome": "Gui"} # Altera o valor do dicionário vinculado

print(contatos["guilherme@gmail.com"])
print(copia["guilherme@gmail.com"])

# ------- FROMKEYS
dicionario = dict.fromkeys(["nome", "telefone"])
print(dicionario)

dicionario = dict.fromkeys(["nome", "telefone"], "vazio")
print(dicionario)


# ------- GET
# Busca a chave passada dentro do dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

print(contatos.get("chave"))
print(contatos.get("chave", {})) # Se não encontrar a chave "chave", retorna o valor default atribuído, {}
print(contatos.get("guilherme@gmail.com", {}))


# ------- ITEMS
# Retorna uma lista de tuplas com os valores do dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
}

print(contatos.items())


# ------ KEYS
# Retorna apenas as chaves do diconário
print(contatos.keys())


# ------ VALUES
# Retorna apenas os valores do dicionário
print(contatos.values())


# ------ POP
# Remove uma chave do dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

print(contatos.pop("guilherme@gmail.com"))
print(contatos)

print(contatos.pop("guilherme@gmail.com", {})) # Se não encontrar, retorna {} -> sem passar o default, se não encontrar o elemento o código vai apresentar uma Key Error


# ----- POPITEM
# Não informa qual a chave, sendo retirados os itens em sequencia
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}
}

contatos.popitem()
print(contatos)

contatos.popitem()
print(contatos)

# Se acabarem os itens e tentar fazer mais um popitem vai ocorrer um Key Erros novamente


# ----- SETDEFAULT
contato = {'nome': 'Guilherme', 'telefone': '3333-1234'}

contato.setdefault("nome", "Giovanna") # Existindo um valor atribuído a essa chave no dicionário, não há alteração. A função retorna o valor atribuído originalmente à chave
print(contato)

contato.setdefault("idade", 28) # Se a chave não existir no dicionário, será adicionada
print(contato)


# ----- UPDATE
# Atualiza o dicionário com outro dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # Atualiza uma chave já existente, alterando seu valor
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}}) # Como a chave do novo dicionário não existe no inicial, será adicionada
print(contatos)


# ------ IN
print("guilherme@gmail.com" in contatos)
print("idade" in contatos["guilherme@gmail.com"])


# ------ DEL
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"] # Remove o atributo telefone

del contatos["chappie@gmail.com"] # Remove TODA a chave

print(contatos)

del contatos #apaga o dicionário inteiro, o print abaixo vai dar erro
print(contatos)
