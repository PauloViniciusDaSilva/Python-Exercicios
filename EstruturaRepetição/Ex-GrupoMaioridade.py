import datetime

c = 0
co = 0

for i in range(7):
    nome = int(input('Em que ano a pessoa nasceu? '))
    conta = datetime.date.today().year - nome

    if conta <= 21:
        c += 1
    else:
        co += 1

print(f'{c} são menores de idade')
print(f'{co} são maiores de idade')
