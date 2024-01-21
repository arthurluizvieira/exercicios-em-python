# desafio continuação do ex005

nome = input('Digite seu nome: ')
n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
sm = n1 + n2
mf = sm / 2

print('Olá {}, sua média final foi de {}'.format(nome,mf))

# desafio 4

m = float(input('Digite um valor em metros: '))
c = m * 100
mm = c * 1000

print('A quantidade em metros definida equivale a \n{} centímetros e \n{} milímetros'.format(c, mm))

#desafio 5

ni = int(input('Digite um numero inteiro: '))
t = ni * 1 , ni * 2 , ni * 3
print('A tabuada de 1 a 3 desse número é de {}'.format(t))

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} x {} = {:2}'.format(num, 1, num*1))
print('{} x {} = {:2}'.format(num, 2, num*2))
print('{} x {} = {:2}'.format(num, 3, num*3))
print('{} x {} = {:2}'.format(num, 4, num*4))
print('{} x {} = {:2}'.format(num, 5, num*5))
print('-' * 12)



#desafio 6

