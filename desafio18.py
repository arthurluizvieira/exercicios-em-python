import math
ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o Seno de {:.2f}'.format(ângulo, seno))

cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem Cosseno de {:.2f}'.format(ângulo, cosseno))

tangente = math.tan(math.radians(ângulo))
print('O ângulo {} tem Tangente de {:.2f}'.format(ângulo, tangente))

## desafio 19

import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluo: '))
lista = [n1 ,  n2 , n3 , n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
