ano = int(input('Digite o ano em que você nasceu: '))
idade = 2023 - ano

if idade > 18:
    alist = ano + 18
    falta = idade - 18
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023.')
    print(f'Você já se alistou e deveria ter se alistado há {falta} anos. Seu alistamento foi em {alist}.')

elif idade < 18:
    alist = ano + 18
    falta = 18 - idade
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023.')
    print(f'Faltam {falta} anos para você se alistar.')
    print(f'Seu alistamento será daqui a {alist} anos.')

elif idade == 18:
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023.')
    print('Você deve se alistar imediatamente.')
