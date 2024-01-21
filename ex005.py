n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
dr = n1 % n2

print('A soma vale {} , a multiplicação vale {} e a divisão vale {}'.format(s, m , d))
print('A divisão inteira vale {}, potenciação {} e resto da div {}'.format(di, p , dr))

# exercicio 05

n = int(input('Digite um valor aleatório: '))
a = n - 1
s = n + 1

print('O antecessor do número {} é {} e o sucessor é {}'.format(n, a, s))

# exercicio

n3 = int(input('Digite um numero aleatorio: '))
d = n3 * 2
t = n3 * 3
r = n3 ** (1/2)

print('O dobro do número {} é de {}, seu triplo é {} e sua raiz quadrada é {}'.format(n3 , d , t ,r))
