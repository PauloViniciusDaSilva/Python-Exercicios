n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
op = 0
li = []

while op != 5:
    op = int(input('''
    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Qual é a sua opção?'''))

    if op == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        li = [n1, n2]
        maior = max(li)
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif op == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um novo número: '))
        print(f'Os novos números são {n1} e {n2}')
    elif op == 5:
        print('Programa encerrado.')
    elif op >= 6:
        print('Digite apenas números de 1 a 5')

print('Fim do programa!')
