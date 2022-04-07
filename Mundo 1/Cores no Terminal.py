
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

"""print('\033[1;32;40mOla, mundo\033[m')

print('\nPrazer te conhecer\033[33mCriador\033[m')

print('\nPrazer te conhecer{}'.format('\033[35mCRIADOR\033[m'))

cor = {'azul':'\033[34m'}
caos = 3
print('\n Ola mundo de {} dimensoes '.format(cor['azul'],caos))"""
'''

style = {'Negrito' : '\033[;1m',
         'Inverte' : '\033[;7m'
         }

clean = {'0' : '\033[0;0m' }

background = {'Preto'        : '\033[1;40m',
             'Vermelho'	     :'\033[1;41m',
             'Verde'	     :'\033[1;42m',
             'Amarelo'	     :'\033[1;43m',
             'Azul'	         :'\033[1;44m',
             'Magenta'	     :'\033[1;45m',
             'Cyan'	         :'\033[1;46m',
             'Cinza Claro'   :'\033[1;47m',
             'Cinza Escuro'	 :'\033[1;100m',
             'Vermelho Claro':'\033[1;101m',
             'Verde Claro'	 :'\033[1;102m',
             'Amarelo Claro' :'\033[1;103m',
             'Azul Claro'	 :'\033[1;104m',
             'Magenta Claro' :'\033[1;105m',
             'Cyan Claro'    :'\033[1;106m',
             'Branco'    	 :'\033[1;107m'
             }

colortext = {'Preto'         :'\033[1;30m',
             'Vermelho'	     :'\033[1;31m',
             'Verde'	     :'\033[1;32m',
             'Amarelo'	     :'\033[1;33m',
             'Azul'	         :'\033[1;34m',
             'Magenta'	     :'\033[1;35m',
             'Cyan'	         :'\033[1;36m',
             'Cinza Claro'   :'\033[1;37m',
             'Cinza Escuro'	 :'\033[1;90m',
             'Vermelho Claro':'\033[1;91m',
             'Verde Claro'	 :'\033[1;92m',
             'Amarelo Claro' :'\033[1;93m',
             'Azul Claro'	 :'\033[1;94m',
             'Magenta Claro' :'\033[1;95m',
             'Cyan Claro'    :'\033[1;96m',
             'Branco'    	 :'\033[1;97m'
         }

print('{}{}\nHello word!{}'
      .format(style['Negrito'],colortext['Magenta'],clean['0']))

