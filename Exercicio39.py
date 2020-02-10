#Faça um programa que leia o ano de nascimento de um jovem e informe
# de acordo com sua idade:
# 
# - se ele ainda vai se alistar ao serviço militar
# - se ja é hora de se alista.
# - se ja passou do tempo de alistamento 
# 
# seu programa também devera mostra o tempo que falta que 
# passou do prazo #

nasc = int(input('Ano de nascimento: '))
atual = 2020
alistamento = nasc + 18

if 2020 - nasc == 18:
    print('Você deve se alistar imediatamente!')
elif 2020 - nasc > 18: 
    print('Você deveria ter se alistado em {}'.format(alistamento))
elif 2020 - nasc < 18: 
    print('Você deve se alistar somente em {}'.format(alistamento))


