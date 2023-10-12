casa = float(input('Qual valor da casa: '))
salario = float(input('Qual o seu salário: '))
ano = int(input('Em quantos anos você quer pagar a casa: '))
lim = 30 * salario / 100
pres = casa / (ano * 12)

if pres <= lim:
    print('Sua prestação será de {:.2f}, empréstimo concedido'.format(pres))
else:
    print('Sua prestação será de {:.2f}, empréstimo negado'.format(pres))
