
# Quebrando numeros
'''
# Método simples
numero = float(input('Digite um numero:'))
print('O valor digitado foi {} e sua porção inteira é {:.0f}'.format(numero,numero))

# Método importando biblioteca de matematica (math)
import math
numero = float(input('Digite um numero:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(numero, math.trunc(numero)))

#Método importando apenas o trunc da biblioteca de matematica (math)
from math import trunc
numero = float(input('Digite um numero:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(numero,trunc(numero)))
'''
# Método utilizando a propriedade int como funcao para chamar apenas a parte inteira
numero = float(input('Digite um numero:'))
print('O valor digitado foi {} e sua porção inteira é {:.0f}'.format(numero,int(numero)))
