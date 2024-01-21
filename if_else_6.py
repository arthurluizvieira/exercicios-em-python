from datetime import date
a = int(input('Digite o ano que deseja: '))
if a == 0:
    a == date.today().year
if a == 0 % 4 == 0 and a % 100 != 0 or a % 400 ==0:
    print('O ano {} É bissexto!!'.format(a))
else:
    print('O ano {} NÃO é bissexto!!'.format(a))