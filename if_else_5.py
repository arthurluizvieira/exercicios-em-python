d = float(input('Digite a distância da viajem em km: '))
if d <=200:
    p = d * 0.5
else:
    p = d * 0.45
print('O preço da sua passagem é de R${}!!'.format(p))
