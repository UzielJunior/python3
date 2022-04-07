'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.
'''

casa = int(input('digite o valor da casa?:'))
salario   = int(input('digite o valor do seu salário?:'))
tempo = int(input('Quantos anos de financiamento?:'))

parcela = casa/(tempo*12)

print('Para pagar um casa de R${:.2f} em {} anos '
      'a parcela será de R${:.2f}'.format(casa,tempo,parcela))

if parcela <= salario*0.3 :
   print('\nParabens !!! O emprestimo pode ser consedido !')
else:
    print('\nNao é possivel efetuar a compra da casa nessas condiçoes')


