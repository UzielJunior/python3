
# Valor de desconto fixo
'''preco   = float(input('Qual o preço do produto?:'))
promocao= preco*0.95
print('O produto que custava R${}, na promocao com desconto de 5% sai á R${:.2f}.'.format(preco,promocao))'''

# Valor de desconto variavel onde o usuario informará o desconto

preco   = float(input('Qual o preço do produto?:'))
desconto= float(input('Qual o desconto do produto?:'))
valorf  = (preco*(100-desconto))/100
print('O produto que custava R${}, na promocao com desconto de {:.0f}% sai á R${:.2f}.'.format(preco,desconto,valorf))

