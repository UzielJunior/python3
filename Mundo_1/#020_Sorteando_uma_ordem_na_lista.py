
# Importando biblioteca random
'''
import random
print('\nimforme abaixo o nome dos alunos:\n')
n1 = str(input('aluno 1:'))      # lendo especificamente no formato string(str)
n2 = str(input('aluno 2:'))      #  mas nao é necessario definir o tipo já q é string
n3 = str(input('aluno 3:'))
n4 = str(input('aluno 4:'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentacao será:\n',lista)
'''
# Importando apenas a funcao de embaralhamento(shuffle) na biblioteca random
from random import shuffle
print('\nimforme abaixo o nome dos alunos:\n')
n1 = str(input('aluno 1:'))      # lendo especificamente no formato string(str)
n2 = str(input('aluno 2:'))      #  mas nao é necessario definir o tipo já q é string
n3 = str(input('aluno 3:'))
n4 = str(input('aluno 4:'))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentacao será:\n',lista)
