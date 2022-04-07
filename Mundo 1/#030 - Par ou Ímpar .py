

from random import randint

numero = int(input('\n Digite um numero:'))
resultado =  numero % 2
print('=='*20)
if resultado==0:
    print('O número {} é par!'.format(numero))
else:
    print('O numero {} é impar'.format(numero))
print('=='*20)
