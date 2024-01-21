print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

l1 = float(input('Primeira Linha: '))
l2 = float(input('Segunda Linha: '))
l3 = float(input('Terceira Linha: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('As linhas acimas PODEM formar triângulos!!')
else:
    print('As linhas acima NÃO podem formar triângulos!!')
