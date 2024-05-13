# Código realizado a partir do meu código original, com auxílio do Gemini
# NÃO TESTADO !
# TODO: testar, revisar e melhorar

def obter_informacao_usuario(pergunta, tipo_dado):
  """
  Obtém a informação do usuário com base na pergunta e no tipo de dado.

  Args:
      pergunta: A pergunta a ser apresentada ao usuário.
      tipo_dado: O tipo de dado esperado (string ou inteiro).

  Returns:
      O valor digitado pelo usuário.
  """

  if tipo_dado == "int":
    return int(input(pergunta))
  else:
    return input(pergunta).lower()

def converter_resposta_booleana(resposta):
  """
  Converte a resposta do usuário ("sim" ou "não") para um valor booleano.

  Args:
      resposta: A resposta do usuário ("sim" ou "não").

  Returns:
      O valor booleano equivalente à resposta (True ou False).
  """

  return resposta == "sim"

def determinar_afinidade_elemental(intensidade_feitico, fase_lunar, idade_feiticeiro, componente_raro, afinidade_animais):
  """
  Analisa as informações do usuário e determina a afinidade elemental do feiticeiro.

  Args:
      intensidade_feitico: A intensidade do feitiço (inteiro).
      fase_lunar: A fase lunar (string).
      idade_feiticeiro: A idade do feiticeiro (inteiro).
      componente_raro: Presença de componente raro (booleano).
      afinidade_animais: Afinidade com animais mágicos (booleano).

  Returns:
      Uma string indicando a afinidade elemental ("Fogo", "Água", "Terra" ou "Ar").
  """

  if intensidade_feitico >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100 and componente_raro and afinidade_animais:
    return "Fogo"
  elif intensidade_feitico >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and not afinidade_animais:
    return "Água"
  elif intensidade_feitico >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and afinidade_animais:
    return "Terra"
  else:
    return "Ar"

# Obter informações do usuário
intensidade_feitico = obter_informacao_usuario("Qual a intensidade do feitiço? ", "int")
componente_raro_input = obter_informacao_usuario("Presença de componente raro? ", "string")
fase_lunar = obter_informacao_usuario("Qual a fase lunar? ", "string")
idade_feiticeiro = obter_informacao_usuario("Qual a idade do feiticeiro? ", "int")
afinidade_animais_input = obter_informacao_usuario("Afinidade com animais mágicos? ", "string")

# Converter respostas para booleanos
componente_raro = converter_resposta_booleana(componente_raro_input)
afin