t = ('zero um dois três quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis dezessete dezoito dezenove vinte').split()

while True:
    d = int(input('Digite um número de 0 a 20: '))
    if 0 <= d <= 20:
        oi = t[d]
        print(oi)
        break
    else:
        print('Número inválido. Digite apenas um número entre 0 e 20.')
