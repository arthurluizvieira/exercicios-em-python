#desafio 6

s = float(input('Qual seu saldo disponível em R$?: '))
d = s / 3.27

print('Você pode comprar {:.2f} doláres!!'.format(d))

#desafio 07

da = float(input('Digite a altura de sua parede em metros: '))
dl = float(input('Agora digite a largura em metros: '))
a = da * dl

ptd = a / 2


print('A quantida necessária de tinta para pintar completamente a parede , é de {:.2f} litros.'.format(ptd))

#desafio 08

preco = float(input('Digite o preço do produto: '))
np = float(input('Digite a porcentagem de desconto: '))
d = preco * np / 100
pa = preco - d



print('O valor atual do produto com desconto é de {}!'.format(pa))

#desafio 09

salario = float(input('Digite seu salário: '))
a = salario * 0.15
ns = salario + a

print('Seu novo salário com 15% de aumento é de {}!!'.format(ns))

precoum = float(input('Digite o preco'))
nvp = precoum - (precoum * 5 / 100)
print('o produto que custava {}, na promocao com 5% vai custar {}'.format(precoum, nvp))

