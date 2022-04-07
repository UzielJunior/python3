
''' Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
    de até 200Km e R$0,45 parta viagens mais longas.  '''

distancia = float(input('\n Digite uma distancia:'))
'''
if distancia<=200:
    perto= distancia * 0.50
    print('Perto_O valor da passagem é R${:.2f}!'.format(perto))
else:
    longe = distancia * 0.45
    print('Longe _O valor da passagem é R${}!'.format(longe))
    '''

# forma compacta

preco= distancia*0.50 if distancia <=200 else distancia*0.45
print('O valor da passagem é R${:.2f}!'.format(preco))

