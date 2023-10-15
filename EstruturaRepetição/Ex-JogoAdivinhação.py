from random import randint

maq = randint(0, 10)
cot = 0

n = int(input('Digite um número de 0 a 10: '))

while n != maq:
    if n > maq:
        cot += 1
        n = int(input('Menos... Digite outra vez: '))
    if maq > n:
        cot += 1
        n = int(input('Mais... Digite outra vez: '))

print('Você acertou com {} tentativas'.format(cot))
print(f'A máquina escolheu o número {maq}')
print('Acabou')
