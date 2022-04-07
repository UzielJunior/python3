
# Valor do aluguel de um carro

dias = float(input('Quantos dias alugados?:'))
km   = float(input('Quantos km rodados?:'))
valor= (0.15*km)+(dias*60)           # R$ a diaria do carro 60 e 15centavos por km rodado
print('O total a pagar é R${:.2f}'.format(valor))


