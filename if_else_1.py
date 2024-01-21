t = int(input('Digite quantos anos tem seu carro: '))
if t <= 3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')

nome = str(input('Qual seu nome? '))
if nome == 'arthur':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é normal.')
print('--FIM--')

n1 = int(input('Digite sua nota 1: '))
n2 = int(input('Digite sua nota 2: '))
m = (n1 + n2) / 2
if m <=60:
    print('Reprovado. Sua média foi de: {}.'.format(m))
else:
    print('Aprovado. Sua média foi de: {}.'.format(m))