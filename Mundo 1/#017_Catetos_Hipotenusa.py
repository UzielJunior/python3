
# quadrado da Hipotenusa = soma dos quadrados dos catetos
# Metodo Simples
'''
co = float(input('Cateto oposto?:'))
ca = float(input('Cateto adjacente?:'))
hi = (co**2+ca**2) **(1/2)                   # chamar a exponenncial variavel**2
print('Hipotenusa = {:.2f}'.format(hi))

# Metodo importando a biblioteca math
import math
co = float(input('Cateto oposto?:'))
ca = float(input('Cateto adjacente?:'))
hi = math.hypot(co, ca)
print('Hipotenusa = {:.2f}'.format(hi))
'''
# Metodo importando apenas a funcao da hipotenusa(hypot) da math
from math import hypot
co = float(input('Cateto oposto?:'))
ca = float(input('Cateto adjacente?:'))
hi = hypot(co, ca)
print('Hipotenusa = {:.2f}'.format(hi))
