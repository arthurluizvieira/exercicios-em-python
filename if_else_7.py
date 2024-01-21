v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
v3 = int(input('Digite o valor 3:' ))
#verificando quem é menor
menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v1 and v3<v2:
    menor = v3
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O menor valor foi {}.'.format(menor))
print('O maior valor foi {}.'.format(maior))