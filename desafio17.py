c = float(input('Digite comprimento cateto oposto: '))
ca = float(input('Digite comprimento cateto adjacente: '))
h = (c ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))

## Segunda forma mais fácil hipotenusa

import math

caa = float(input('Cateto adjacente: '))
co = float(input('Cateto oposto: '))
hi = math.hypot(caa, co)
print('A hipotenusa mede {:.2f}'.format(hi))
