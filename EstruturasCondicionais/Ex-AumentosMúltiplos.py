salario = float(input('Digite seu salario: R$'))
print('Salários inferiores a R$1.250 terão desconto de 15% de aumento')
if salario <= 1250:
    aumen = (salario * 15) / 100
else:
    aumen = (salario * 10) / 100
print('O valor de {} terá o aumento de R${:.2f}'.format(salario, aumen + salario))
