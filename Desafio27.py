nome = str(input('digite seu nome: ')) .strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

#split pra separar o nome