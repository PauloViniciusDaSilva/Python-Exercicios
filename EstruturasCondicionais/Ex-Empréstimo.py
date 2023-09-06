casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário: '))
ano = int(input('Em quantos anos você quer pagar a casa: '))
lim = 30 * salario / 100
pres = casa / (ano * 12)

if pres <= lim:
    print('Sua prestação será de R$ {:.2f}. Empréstimo concedido.'.format(pres))
else:
    print('Sua prestação será de R$ {:.2f}. Empréstimo negado.'.format(pres))
