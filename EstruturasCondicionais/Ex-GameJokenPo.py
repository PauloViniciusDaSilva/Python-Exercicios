import random

op = int(input('''
[0] pedra
[1] papel
[2] tesoura
Digite sua opção: '''))

item = ('pedra', 'papel', 'tesoura')
maq = random.randint(0, 2)

if (maq == 0 and op == 2) or (maq == 1 and op == 0) or (maq == 2 and op == 1) or (op == 2 and maq == 0) or (op == 0 and maq == 1) or (op == 1 and maq == 2):
    print('MAQUINA GANHOU')
elif (maq == 0 and op == 0) or (maq == 1 and op == 1) or (maq == 2 and op == 2) or (op == 0 and maq == 0) or (op == 1 and maq == 1) or (op == 2 and maq == 2):
    print('MAQUINA E USUÁRIO EMPATOU')
else:
    print('USUÁRIO GANHOU')

print(f'A máquina escolheu {item[maq]}')
print(f'O usuário digitou {item[op]}')
