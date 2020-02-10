#Desafio 36, programa para aprovar um empréstimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ela
#vai pagar. 

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
#então o emprestimo sera negado.

casa = float(input('Valor da casa: R$'))
salário = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print('Para pagar um acasa de R${:.2f} em {} anos' .format(casa, anos), end='')
print(', a prestação será de R${:.2f}'.format(prestação))

##print('COMPARANDO tem que pagar {:.2f} e o minimo é de {}'.format(prestação, mínimo))
if prestação <= mínimo:
    print('Empréstimo aprovado')
else:
    print('Empréstimo recusado')    