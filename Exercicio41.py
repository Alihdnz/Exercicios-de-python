#A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de 
# acordo com a idade:
# 
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER#

nasc = int(input('Ano de nascimento: '))
atual = 2020
idade = 2020 - nasc

if idade <= 9:
    print("O atleta tem {} anos, e esta na categoria MIRIM".format(idade))

elif idade > 9 and idade <= 14:
    print("o atleta tem {} anos, e esta na categoria INFANTIL".format(idade))

elif idade > 14 and idade <= 19:
    print('o atleta tem {} anos, e esta na categoria JUNIOR'.format(idade))

elif idade == 20:
    print('o atleta tem {} anos, e esta na categoria SÊNIOR'.format(idade))

else:
    print('o atleta tem {} anos, e esta na categoria MASTER'.format(idade))