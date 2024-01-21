n = int(input('Digite um valor: '))

print('O antecessor do {} é {} e o sucessor {}'.format(n, (n-1), (n+1)))

#menos variaveis menos memoria utilizada, se precisasse mais pra frente , ai usa com variaveis

# convertendo temperaturas

celsius = float(input('Digite a temperatura em °C: '))
fahrenheit = ((9*celsius) / 5) + 32

print('A temperatura de {} em °C corresponde a {}°F'.format(celsius, fahrenheit))

# aluguel carros

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}!!'.format(pago))

