# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print('União: {}'.format(conjunto_uniao))
# conjunto_intereccao = conjunto.intersection(conjunto2)
# print('Intersecção: {}'.format(conjunto_intereccao))
# conjunto_dif1 = conjunto.difference(conjunto2)
# conjunto_dif2 = conjunto2.difference(conjunto)
# print('Diferença entre 1 e 2: {}'.format(conjunto_dif1))
# print('Diferença entre 2 e 1: {}'.format(conjunto_dif2))
# conjunto_simet = conjunto.symmetric_difference(conjunto2)
# print('Diferença Simétrica: {}' .format(conjunto_simet))

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_sub = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_sub))
conjunto_sub_b = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_sub_b))
conjunto_super = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_super))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

#Um CONJUNTO não permite valores iguais
#.add() Para adicionar um elemento
#.discard() Para Remover um elemento
#.union() Para unir os elementos de outros conjuntos
#.intersection Pra mostrar qual elemento tem em ambos os conjuntos
#.difference Para saber quais elementos tem em um conjunto e não em outro
#symmetric_difference Mostra só os valores diferentes entre os conjuntos
#issubset Para saber se um conjunto é subconjunto de outro
#issuperset O Contrário de de issubset
#set() Para transformar uma lista em um conjunto para tirar a duplicidade da lista