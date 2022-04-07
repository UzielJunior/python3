

frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1)) #busca leta a no texto
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))  # rfind busca a direita

