
v = float(input('Qual é a velocidade atual do carro: '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (v-80) * 7
    print('Você deve pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
