
l_ida = []
nome_mu = []
qt = 0
while True:
    try:
        for p in range(1,5):
            print(f'----{p} PESSOA ----')
            nome = str(input('Nome:'))
            idade = int(input('Idade:'))
            sexo = str(input('(M/F):')).lower()
            l_ida.append(idade)
            sum_ida = sum(l_ida)
            if idade == max(l_ida) and sexo == 'm':
                nom_old = nome.split()
            elif sexo == 'f' and idade < 20:
                qt += 1
                nome_mu.append(nome.split()[0])
                nome_menor20 = ', '.join(nome_mu)
    except(ValueError, TypeError, KeyboardInterrupt):
        print('='*15)
        print('ERRO'.center(15))
        print('='*15)
    else:
        print('A média de idade do grupo é {}.'.format(sum_ida/4))
        print('O homen mais velho tem {} anos e seu nome é {}.'.format(max(l_ida), nom_old[0]))
        print('Existem {} mulheres menores de 20 anos e seu nome é {}.'.format(qt, nome_menor20))
        break