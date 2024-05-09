# Desafio de Código SQUADIO 2 - Intermediário II 👩🏻‍💻
### A Jornada da Classificação Frutífera

Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

- Maçã:  
    Peso mínimo: 130 gramas  
    Textura: Ápera (rough)  
    Cor: Vermelha (red)  

- Laranja:  
    Peso mínimo: 120 gramas  
    Textura: Suave (smooth)  
    Cor: Laranja (orange)  

- Morango:  
    Peso mínimo: 150 gramas  
    Textura: Suave (smooth)  
    Cor: Vermelha (red)  

- Banana:  
    Peso mínimo: 150 gramas  
    Textura: Áspera (rough)  
    Cor: Amarela (yellow)  

## Entrada
Seu código deve receber as seguintes entradas do usuário:  

- Peso da fruta (em gramas): um número real que representa o peso da fruta.  
- Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").  
- Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.  


## Saída
O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

------------
**Entrada** | **Saída**
------------|-----------
150 \n smooth \n red          | A fruta é um morango!
140 \n rough \n yellow          | Não foi possível classificar a fruta.
150 \n smooth \n orange           | A fruta é uma laranja!
------------