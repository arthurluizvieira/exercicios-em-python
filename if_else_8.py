salário = float(input('Digite o salário do funcionario: '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else: novo = salário + (salário (10 / 100))
print('Quem ganhava R${} passa a ganhar R${} agora.'.format(novo))
