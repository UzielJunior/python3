
# Calculos de Angulo desejado para Seno, Cosseno e Tangente
# Metodo importando a biblioteca math
'''
import math
an = float(input('\nDigite um angulo:'))
seno= math.sin(math.radians(an))    #chama sin dentro da math e depois converte o angulo para radianos
cos = math.cos(math.radians(an))
tang= math.tan(math.radians(an))
print('O angulo de {}°graus tem o valor do seno:{:.2}, cosseno:{:.2} e tangente:{:.2}'.format(an,seno,cos,tang))
'''
# Metodo importando apenas as funcoes utilizadas
from math import radians,sin,cos,tan
an = float(input('\nDigite um angulo:'))
seno= sin(radians(an))    #chama sin dentro da math e depois converte o angulo para radianos
cos = cos(radians(an))
tang= tan(radians(an))
print('O angulo de {}°graus tem o valor do seno:{:.2}, cosseno:{:.2} e tangente:{:.2}'.format(an,seno,cos,tang))