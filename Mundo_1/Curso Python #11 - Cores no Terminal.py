
'''print('\033[X;X;Xm....\0333[m')

#Primeiro X: Style = estilo da letra ou fonte
0 none      _ou colar nada o stilo permanece do python
1 Bold      _ Negrito
4 Underline _Sublinha
7 Negative  _inverte o fundo com a letra

#Segund o X: Text  = Cor do texto
30 - 37 codigo de cores das letras

#Terceiro X: Back  = Cor do background ou cor de fundo
40 - 47 codigo de cores do background


print('\033[1;32;40mOla, mundo\033[m')

print('\nPrazer te conhecer\033[33mCriador\033[m')

print('\nPrazer te conhecer{}'.format('\033[35mCRIADOR\033[m'))
'''

style ={'none':     '\033[0m',
        'bold':     '\033[1m',
        'underline':'\033[4m',
        'negative': '\033[7m',}

fundo ={'clean':     '\033[m',
        'preto':     '\033[40m',
        'vermelho':  '\033[41m',
        'verde':     '\033[42m',
        'amarelo':   '\033[43m',
        'azul':      '\033[44m',
        'roxo':      '\033[45m',
        'azulclaro': '\033[46m',
        'cinza':     '\033[47m' }

letra ={'clean':     '\033[m',
        'preto':     '\033[30m',
        'vermelho':  '\033[31m',
        'verde':     '\033[32m',
        'amarelo':   '\033[33m',
        'azul':      '\033[34m',
        'roxo':      '\033[35m',
        'azulclaro': '\033[36m',
        'cinza':     '\033[37m' }

print('\n Ola {}mundo{}!  '.format(letra['vermelho'],letra['clean']))