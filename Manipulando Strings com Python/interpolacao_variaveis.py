# -------- Old style
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Paulo", "idade": 20}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. \n" % (nome, idade, profissao, linguagem))

# -------- Format
print("Oi, eu sou o {}, tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {} \n" .format(nome, idade, profissao, linguagem))
print("Oi, eu sou o {1}, tenho {2} anos de idade, trabalho como {3} e estou matriculado no curso de {0}. Gosto muito de estudar {0}. \n" .format(linguagem, nome, idade, profissao))
print("Oi, eu sou o {name}, tenho {age} anos de idade, trabalho como {job} e estou matriculado no curso de {language} \n" .format(name=nome, age=idade, job=profissao, language=linguagem))
print("Oi, eu sou o {nome}, tenho {idade} anos de idade \n" .format(**pessoa))


# ---------- F-STRING
print(f"Opa! Eu sou o {nome}, tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem} \n")

PI = 3.14159
print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}") # tamanho . numero de casas decimais