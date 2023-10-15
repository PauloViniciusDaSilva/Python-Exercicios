# NOT IN signfica  nao estiver em ....
sexo = str(input('Digite F/M'))[0].replace(' ', '')
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalaidos,Digite novamente seu sexo[M/F]:'))[0].replace(' ', '')
print('Acabou')