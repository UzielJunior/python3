

from random import randint

computador = randint(0,5)
jogador = int(input('\n Em que valor estou pensando?'))

print('=='*20)
if jogador==computador:
    print('Voce ganhou !')
else:
    print('Voce perdeu! Eu pensei no numero {} e nao {}'.format(computador,jogador))
print('=='*20)
