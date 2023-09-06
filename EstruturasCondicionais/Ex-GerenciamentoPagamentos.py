p = float(input('Qual é o preço do produto escolhido: R$ '))
con = int(input('Escolha uma opção de pagamento:\n'
                '1 - À vista em dinheiro/cheque\n'
                '2 - À vista no cartão\n'
                '3 - Parcelado em 2x no cartão\n'
                '4 - Parcelado em 3x ou mais no cartão\n'
                'Qual é a sua opção? '))

if con == 1:
    conta = (p * 10) / 100
    print('O produto de R${:.2f} com 10% de desconto custará R${:.2f}'.format(p, (p - conta)))
elif con == 2:
    conta = (p * 5) / 100
    print('O produto de R${:.2f} com 5% de desconto custará R${:.2f}'.format(p, (p - conta)))
elif con == 3:
    parcela = p / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('O produto custará R${:.2f} e não terá desconto'.format(p))
elif con == 4:
    par = int(input('Digite o número de parcelas: '))
    conta = (p * 20) / 100
    parcela1 = (p + conta) / par
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(par, parcela1))
    print('O produto de R${:.2f} com 20% de juros custará R${:.2f}'.format(p, (p + conta)))
else:
    print('Digite apenas os números indicados acima!')
