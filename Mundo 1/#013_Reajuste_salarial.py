
# Valor de aumento fixo
'''
salario = float(input('Qual o salario atual do funcionario?:'))
aumento = salario*1.15
print('O funcionario com salario de R${}, com aumento de 15% passa a receber R${:.2f}.'.format(salario,aumento))

'''
# Valor de aumento variavel onde o usuario informará o aumento

salario  = float(input('Qual o salario atual do funcionario?:'))
reajuste= float(input('Quantos porcento ele terá de aumento?:'))
valorf  = (salario*(100+reajuste))/100
print('O funcionario com salario de R${}, tendo um aumento de {:.0f}% passará a ganhar R${:.2f}.'.format(salario,reajuste,valorf))
#'''