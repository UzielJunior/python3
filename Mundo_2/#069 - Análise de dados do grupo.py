'''
Exercício Python 045: Crie um programa que
faça o computador jogar Jokenpô com você.'''

import random

while True:

    tipo = ' '
    sexo = ' '
    cont = 0
    print('-' * 20, '\nCADASTRE UMA PESSOA\n', '-' * 20)

    idade = int(input('Idade: '))

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    cont += 1

    cond = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cond in 'N':
        print('\nPrograma Encerrado')
        break









