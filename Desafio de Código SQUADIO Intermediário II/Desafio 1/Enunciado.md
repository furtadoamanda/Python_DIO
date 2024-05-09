# Desafio de Código SQUADIO 1 - Intermediário II 👩🏻‍💻
### O robô inteligente 

Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

## Entrada:
A entrada deve receber valores inteiros.

- numero: valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.  


## Saída:
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

#### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

------------
**Entrada** | **Saída**
------------|-----------
1 \n -1 \n 2 \n 0          | positivo! \n negativo! \n positivo! \n 2 números positivos, 1 números negativos
1 \n -1 \n 0          | positivo! \n negativo! \n 1 números positivos, 1 números negativos
1 \n 1 \n -1 \n -1 \n 0          | positivo! \n positivo! \n negativo! \n negativo! \n 2 números positivos, 2 números negativos
------------