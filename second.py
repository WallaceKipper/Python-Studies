# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a > c:
#     print('O Maior Número é {}' .format(a))
# elif b > a and b > c:
#     print('O Maior Número é {}' .format(b))
# else:
#     print('O Maior Número é {}'.format(c))
# print('Final do Programa')

# a = int(input('Entre com o Primeiro Valor: '))
# b = int(input('Entre com o Segundo Valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número digitado é par')

# Operador AND para usar quando quer saber se um resultado E outro são verdadeiros
# Operador OR para usar quando quer saber se UM OU O OUTRO é verdadeiro
# Operador OR NOT para saber se um for verdadeiro e O OUTRO NÂO

a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c= int(input('Você Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você Digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Media: {}'.format(media))
    if media > 5:
        print('O Aluno foi APROVADO')
    else:
        print('O Aluno foi REPROVADO')
else:
    print('Foi Informado uma nota Invalida')