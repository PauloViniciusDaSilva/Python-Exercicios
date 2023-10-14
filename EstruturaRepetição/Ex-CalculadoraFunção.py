while True:
    try:
        def cal(n):return [f'{i} x {n} = {i*n}' for i in range(1,11)]

        resu = cal(int(input('Digite número')))
    except(ValueError, TypeError, KeyboardInterrupt):
        print('Digite APENAS NÚMEROS')
    else:
        print(f'Calculadora:')
        for el in resu:
            print(el)
        break