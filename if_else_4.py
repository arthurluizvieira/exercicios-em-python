n = int(input('Digite um número: '))
r = n % 2
print('O resultado foi {}'.format(r))
if r == 0:
    print('O número {] é PAR.'.format(r))
else:
    print('O número {} é ÍMPAR.'.format(r))
