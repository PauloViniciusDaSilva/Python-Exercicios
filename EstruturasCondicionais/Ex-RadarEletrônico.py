velocidade = int(input('Digite sua velocidade: '))

if velocidade <= 80:
    print('Você está andando dentro do limite da rodovia')
else:
    conta = (velocidade - 80) * 7
    print('Você foi multado no valor de {:.2f} por exceder o limite da via (80 km/h)'.format(conta))
