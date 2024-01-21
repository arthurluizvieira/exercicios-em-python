#strip pra nao contar os espaços antes e depois
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome minusculo é: {}'.format(nome.lower()))
# retirar espaços #
print('Seu nome tem {} letras!!'.format(len(nome) -nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print('Seu segundo nome é {} e ele tem {} letras.'.format(separa[1], len(separa[1])))
print('Seu terceiro nome é {} e ele tem {} letras.'.format(separa[2], len(separa[2])))