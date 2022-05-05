# a = int(input('Entre com um Número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))
# Para saber se o número digitado pelo usuário é primo!
# for x in range (101):
#     print(x)

# a = int(input('Entre com um valor: '))
# for i in range(a+1):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(i)
# Para saber quais números até o número digitado é primo

# nota = int(input('Entre com a Nota: '))
# while nota > 10:
#     nota = int(input('Nota Inválida. Entre com a Nota Correta: '))


# a = 0
# while a <= 10:
#     print(a)
#     a += 1

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c= int(input('Você Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você Digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Media: {}'.format(media))
    if media > 5:
        print('O Aluno foi APROVADO')
    else:
        print('O Aluno foi REPROVADO')