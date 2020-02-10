#DESAFIO dos triângulos, acrescentando o recurso
#de mostrar que tipo de triangulo será formado:
# 
# -Equilátero: todos os lados iguais
# -isósceles: dois lados iguais
# -Escaleno: todos os lados diferentes#

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
    
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES') 
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
    