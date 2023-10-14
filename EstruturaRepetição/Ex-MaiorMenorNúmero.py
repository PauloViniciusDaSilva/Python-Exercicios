pesos = []
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    pesos.append(peso)

print(f'O maior peso é {max(pesos):.2f} Kg')
print(f'O menor peso é {min(pesos):.2f} Kg')

