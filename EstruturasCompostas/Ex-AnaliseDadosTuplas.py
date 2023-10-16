qnt = cnt = so = 0
t = ()
u = (int(input('Digite 1 número')),
   int(input('Digite 2 número:')),
   int(input('Digite 3 número:')),
   int(input('Digite o último número:')))
t += u
print(t)
ma = max(t)
mi = min(t)

for el in t:
    if el == ma:
        ma = max(t)
        cnt += 1

for el in t:
    if el % 2 == 0:
        qnt += 1
print(f'O maior número é {ma}, e apareceu {cnt} vez')
print(f'O menor número é {mi},na posição {(t.index(mi)+1)}')
print(f'Os valores pares digitados foram {qnt} ')