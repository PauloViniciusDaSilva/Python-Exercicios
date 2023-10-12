nome = str(input('Digite uma frase:'))
print('A letra A  aparece {} vezes na frase'.format(nome.upper().count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.upper().strip().find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.upper().strip().rfind('A')+1))