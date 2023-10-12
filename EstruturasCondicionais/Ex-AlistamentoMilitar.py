ano = int(input('Digite o Ano que você nasceu: '))
idade = (2023 - ano)

if idade > 18:
    alist = ano + 18
    falta = idade - 18
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023')
    print(f'Você já se alistou e deveria se alistar há {falta} anos, e seu alistamento foi em {alist}')

elif idade < 18:
    alist = ano + 18
    falta = 18 - idade
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023')
    print(f'Faltam {falta} anos para você fazer o alistamento')
    print(f'Seu alistamento será em {alist}')

elif idade == 18:
    print(f'Você nasceu em {ano} e tem {idade} anos em 2023')
    print('Você deve se alistar rapidamente')