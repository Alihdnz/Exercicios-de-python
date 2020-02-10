#escreva um programa que leia um numero inteiro qualquer 
#e peça para o usuárui escolhar qual será a base de conversão:

# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal

num = int(input('digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para binario
[2] Converter para octal
[3] Converter para hexadecima''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2: 
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')