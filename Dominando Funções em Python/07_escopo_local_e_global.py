salario = 2000

def salario_bonus(bonus, lista):
    global salario # se não definir como global dará erro, porque a variável foi definida fora do escopo da função

    lista_aux = lista.copy() # criar uma cópia porque se alterar dentro da função irá alterar toda a lista
    lista_aux.append(2)
    print(f"lista auxiliar - {lista_aux}")

    salario += bonus
    return salario
    
lista = [1] # o objeto mutável não tem o mesmo problema do imutável, pode ser acessado em qualquer escopo
print(salario_bonus(500, lista))
print(lista)


# CÓDIGO INICIAL SEM A LISTA:
#salario = 2000
#def salario_bonus(bonus):
#    global salario
#    salario += bonus
#    return salario

#salario_bonus(500)