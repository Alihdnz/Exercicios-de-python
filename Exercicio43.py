#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# 
# -Abaixo de 18,5: ABAIXO DO PESO
# -Entre 18.5 e 25: PESO IDEAL
# -25 até 30: SOBREPESO
# -30 até 40: OBESIDADE 
# -Acima de 40: Obesidade mórbida #
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

print('Seu peso é {:.2f} e sua altura é {:.2f}, seu IMC é {:.1f}'.format(peso, altura, imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')