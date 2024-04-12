titulo = " Itens do Personagem "
print(titulo.center(40, "*") + "\n")

itens = []

adicionar_item = input("Insira um item que o personagem possui: ")
itens.append(adicionar_item)

adicionar_item = input("Insira outro item que o personagem possui: ")
itens.append(adicionar_item)

adicionar_item = input("Insira outro item que o personagem possui: ")
itens.append(adicionar_item)


print("Lista de itens:")
for item in itens:
    print(f"- {item}")