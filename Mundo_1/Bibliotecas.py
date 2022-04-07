
from time import sleep
import math
from datetime import datetime

n = int(input('digite um numero:'))
r = math.sqrt(n)
print('a raiz quadrada de {} é {}'.format(n,r))

from math import sqrt

n = int(input('digite um numero:'))
r = sqrt(n)
print('a raiz quadrada de {} é {}'.format(n,r))
# sleep
for c in range(10, 0,-1): # decrementa de um em um
    print(c)
    sleep(0.5)
print('\nBUUM! BUUMM POOW!!!')

# data time

t = datetime.now()
print('data time atual é {}'.format(t))