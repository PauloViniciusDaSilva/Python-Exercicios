f = str(input('Digite uma frase: ')).lower()
f1 = f.replace(' ', '')

for ele in f1:
    ele = f1[::-1]
    frase_principal = f[0:].replace(' ', '')

print(ele)

if ele == frase_principal:
    print('É um palíndromo')
else:
    print('Esta frase não é um palíndromo')
