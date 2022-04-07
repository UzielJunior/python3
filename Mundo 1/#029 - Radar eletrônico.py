

velocidade = float(input('\n Qual sua velocidade?'))
multa = (velocidade-80)*7             # multa R$7 por Km excedido

print('=='*20)
if velocidade<=80:
    print('Tenha um bom dia, dirija com cuidado !')
else:
    print('Voce excedeu o limite de velocidade de 80Km/h, '
          'sua multa é de R${:.2f}.'.format(multa))
print('=='*20)
