# ------ Solução enviada para a plataforma

#capacidade_atual, aumento_percentual = map(int, input().split())

#nova_capacidade = int(capacidade_atual + (capacidade_atual * (aumento_percentual / 100)))

#print(nova_capacidade)

#TODO: Calcule a nova capacidade do disco de Mithril

#TODO: Imprima a nova capacidade

# ------ Minha solução:
titulo = " CodeMiners "
print(titulo.center(40, "*") + "\n")

capacidade_atual = int(input("Capacidade atual: "))
aumento_percentual = int(input("Aumento percentual da capacidade: "))

nova_capacidade = int(capacidade_atual + (capacidade_atual * (aumento_percentual / 100)))

print(f"A capacidade atual da CodeMiners é {capacidade_atual}, com o aumento percentual de {aumento_percentual}%, passará a ser {nova_capacidade}.")