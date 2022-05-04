a = int(input('Escreva o Primeiro Número: '))
b = int(input('Escreva o Segundo Número: '))
# Int para receber o valor inteiro digitado
# Input par pedir para o usuário digitar
soma = a + b
sub  = a - b
mult = a * b
div  = a / b
rest = a % b

print('Soma : {}, \nSubtração : {}, \nMultiplicação : {}, \nDivisão : {}, \nResto : {}'
      .format(soma, sub, mult, div, rest))

# Print Serve para mostrar ao Usuários mensagens que desejar
# \n para pular uma linha na Exibição
# .format Para concatenar as variáveis com o texto