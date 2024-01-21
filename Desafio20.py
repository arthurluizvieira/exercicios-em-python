from random import shuffle
n1 = input('Digite o nome do primeiro: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2 , n3 , n4]
ordem = shuffle(lista)
print('A ordem de apresentação dos alunos será de {}!!'.format(lista))
##ñ precisava do ordem, shuffle direto
