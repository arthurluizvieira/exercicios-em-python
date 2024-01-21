frase = str(input('Digite uma frase: ')).upper() .strip() ##ogar tudo em maiusculo ex: Arara Azul e tirar espaços
print('A A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

