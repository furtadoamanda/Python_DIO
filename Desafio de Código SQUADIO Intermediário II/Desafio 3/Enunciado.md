# Desafio de Código SQUADIO 3 - Intermediário II 👩🏻‍💻
### A Questão Intrincada da Magia Preditiva

No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.  

Aqui estão os critérios mágicos para cada elemento:

- Elemento Fogo:  
    Intensidade do feitiço maior ou igual a 5.   
    Fase lunar durante o feitiço é crescente.  
    Idade do feiticeiro é superior a 100 anos.  

- Elemento Água:  
    Intensidade do feitiço maior ou igual a 7.  
    Presença de componente raro.  
    Fase lunar durante o feitiço é cheia.  
    Idade do feiticeiro é igual ou inferior a 100 anos.  
    Afinidade com animais mágicos.  

- Elemento Terra:  
    Intensidade do feitiço maior ou igual a 7.  
    Presença de componente raro.  
    Fase lunar durante o feitiço é cheia.  
    Idade do feiticeiro é igual ou inferior a 100 anos.  
    Afinidade com animais mágicos.  

- Elemento Ar:  
    Caso não se encaixe nos critérios anteriores.  


## Entrada
Seu código deve receber as seguintes entradas do usuário:  

- Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.  
- Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.  
- Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do feitiço.  
- Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.  
- Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com animais mágicos.  


## Saída
O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

------------
**Entrada** | **Saída**
------------|-----------
6 \n sim \n crescente \n 110 \n sim          | A afinidade elemental do feiticeiro é com o elemento Fogo!
8 \n sim \n cheia \n 80 \n não          | A afinidade elemental do feiticeiro é com o elemento Água!
9 \n sim \n cheia \n 80 \n sim           | A afinidade elemental do feiticeiro é com o elemento Terra!
------------