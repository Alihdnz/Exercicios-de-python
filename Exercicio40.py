#Crie um programa que leia duas notas de um aluno e 
# calcule sua média, mostrando uma mensagem no final, de 
# acordo com a média atingida:
# 
# - Média abaixo de 5,0: REPROVADO
# - Média entre 5,0 e 6,9: RECUPERAÇÃO
# - Méda 7,0 ou superior: APROVADO#

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2

print('A primeira nota foi {:.2f} e a segunda nota foi {:.2f}, então a media foi {:.1f}'.format(nota1, nota2, media)) 
if media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')