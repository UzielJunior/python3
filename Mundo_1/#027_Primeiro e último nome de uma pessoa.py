

n = str(input('Digite um nome completo:')).strip().upper()
nome = n.split()
print(nome[0])
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))


