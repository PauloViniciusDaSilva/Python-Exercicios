conversao = int(input('Digite um número inteiro: '))
opcao = int(input('''
[1] Binário
[2] Octal
[3] Hexadecimal
Escolha a opção para conversão: '''))

if opcao == 1:
    print('O número {} em Binário é {}'.format(conversao, bin(conversao)[2:]))
elif opcao == 2:
    print('O número {} em Octal é {}'.format(conversao, oct(conversao)[2:]))
elif opcao == 3:
    print('O número {} em Hexadecimal é {}'.format(conversao, hex(conversao)[2:]))
else:
    print('Digite apenas as opções marcadas acima!')

