'''
Exercício Python 034: Escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para
os inferiores ou iguais, o aumento é de 15%.
'''

salario_atual = int(input('Qual salario atual do empregado: R$ '))



if salario_atual >= 1250:
    salario_reajustado = salario_atual + (salario_atual * 0.1)
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'
    .format(salario_atual,salario_reajustado))
else:
    salario_reajustado = salario_atual + (salario_atual * 0.15)
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'
          .format(salario_atual, salario_reajustado))


