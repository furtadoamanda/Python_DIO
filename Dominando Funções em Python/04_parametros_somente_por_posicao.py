def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # funciona porque depois da barra pode ser nomeado ou não

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # INVÁLIDO, porque modelo, ano e placa só podem ser passados por posição, não nomeados

# SOMENTE POR POSIÇÃO / POSIÇÃO OU NOME * SOMENTE POR NOME