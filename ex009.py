n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 0.5

print('O dobro do número {} é de {},\nseu triplo é de {} \ne sua raiz quadrada {:.3f}'.format(n , d , t, r))

n1 = int(input('Digite um número: '))
d1 = n * 2
t1 = n * 3
r1 = n ** 0.5

print('O dobro de {} é de {}'.format(n1, (n1*2)))
print('O triplo de {} é de {} \nE sua raiz é de {}'.format(n1, (n1*3), pow(n1, (1/2))))
