#Elabore um programa que calcule o valor a ser pago por 
# um produto, considerando o seu preço normal e condição de 
# pagamento:
# 
# -à vista dinheiro/cheque: 10% de desconto
# -à vista no cartão: 5% de desconto
# -em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros#

produto = float(input('Valor do produto: '))
dinheiro = produto * 10 / 100
cartao1x = produto * 5 / 100
cartao3x= produto * 20 / 100
opc1 = produto - dinheiro
opc2 = produto - cartao1x
opc3 = produto / 2
opc4 = (produto + cartao3x) / 3

pgt = float(input('''Informe o metodo de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros
'''))
if pgt == 1:
    print('O valor a ser pago à vista no dinheiro ou cheque é de R${:.2f}'.format(opc1))
elif pgt == 2: 
    print('O valor a ser pago à vista no cartão é de R${:.2f}'.format(opc2))
elif pgt == 3:
    print('Em duas parcelas de R${:.2f}, sem juros, o valor total a ser pago pelo produto é de {:.2f}'.format(opc3, produto))
elif pgt == 4:
    total = produto + cartao3x
    print('Em três parcelas de R${:.2f}, com 30% de juros, o valor total a ser pago pelo produto é de {:.2f}'.format(opc4, total))
else:
    print('Opção invalida.')