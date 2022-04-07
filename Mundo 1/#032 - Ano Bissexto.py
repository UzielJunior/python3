
from datetime import date      # importando a data na  biblioteca de data time

ano = int(input('Que ano deseja analisar? Coloque 0 para analisar o ano atual:'))
data=ano
mes=ano

mes = date.today().month
data = date.today().day

if ano ==0:
    ano= date.today().year  # atribuindo o ano do computador á variavel ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # ano deve ser divisivel por 4
    print('O ano {} é Bissexto'.format(ano))          # e nao pode ser divisivel por 100
                                                      # ou multiplo de 400
else:
    print('O ano {} nao é Bissexto'.format(ano))
print('Hoje é dia {} do {}'.format(data,mes))

