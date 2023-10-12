peso = float(input('Digite seu peso? '))
altura = float(input('Digite sua altura? '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    v = 'Abaixo peso'
elif imc <= 24.9:
    v = 'EUTROFIA (PESO IDEAL)'
elif imc <= 29:
    v = 'SOBREPESO'
elif imc <= 34:
    v = 'OBESIDADE GRAU 1'
elif imc <= 39.9:
    v = 'OBESIDADE GRAU 2'
else:
    v = 'OBESIDADE MÓRBIDA'

print('Com a altura de {}m e pesando {}Kg, seu IMC é {:.2f} e você está {}.'.format(altura, peso, imc, v))
