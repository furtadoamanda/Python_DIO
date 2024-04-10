curso = "pYtHon"

print(curso.upper())

print(curso.lower())

print(curso.title())

# -----
curso1 = "   Python  "

print(curso1.strip() + ".")

print(curso1.lstrip() + ".")

print(curso1.rstrip() + ".")

# -----
curso2 = "Python"

print(curso2.center(14, "#")) #caracteres totais, caractere que quer inserir nos espaços (se não informar serão espaços em branco)
print(curso2.center(14))

print(".".join(curso2))