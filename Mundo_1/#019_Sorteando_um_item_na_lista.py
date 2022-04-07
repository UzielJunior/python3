
# Importando biblioteca random
'''
import random
print('\nimforme abaixo o nome dos alunos:\n')
n1 = str(input('aluno 1:'))      # lendo especificamente no formato string(str)
n2 = str(input('aluno 2:'))      #  mas nao é necessario definir o tipo já q é string
n3 = str(input('aluno 3:'))
n4 = str(input('aluno 4:'))
lista=[n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi : {}'.format(escolhido))
'''
# Importando apenas a funcao de escolha(choice) na biblioteca random
from random import choice
print('\nimforme abaixo o nome dos alunos:\n')
n1 = str(input('aluno 1:'))      # lendo especificamente no formato string(str)
n2 = str(input('aluno 2:'))      #  mas nao é necessario definir o tipo já q é string
n3 = str(input('aluno 3:'))
n4 = str(input('aluno 4:'))
lista=[n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi : {}'.format(escolhido))
