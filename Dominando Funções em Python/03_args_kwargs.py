def exibir_poema(data_extenso, *args, **kwargs): # poderiam se chamar *poema e **dados, por exemplo, o que importa são os asteriscos
    texto = "\n".join(args) # concatena todos os argumentos do *args com o \n, de modo que cada um ficará em uma linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de agosto, 2022", # primeira linha será considerada como data_extenso
    "Zen of Python", # tudo o que vier depois do data_extenso e for apenas um argumento separado por vírgula, isto é, uma tupla, será considerado como *args
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters", # sabe que acabou o *args porque acabaram os argumentos separados por vírgula, sendo iniciado um argumento de chave/valor, que serão **kwargs
    ano=1999,
)