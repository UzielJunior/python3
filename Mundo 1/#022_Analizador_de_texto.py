

nome = str(input('Digite seu nome completo: ')).strip()   #strip corta os espacos vazios
print('Analizando seu nome')

#---------------------------------------------------------------------------------
print('Seu nome em maiúculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'
      .format(len(nome)-nome.count(' ')))  # len conta a quantidade de letras
                                           # variavel.cont('x') conta quantas daquele
                                           #tipo entre parenteses existem
print('Seu primeiro nome tem:{} letras'
      .format(nome.find(' ')))            # busca dentro da variavel o termo entre parenteses
#--------------------- Usando uma lista (split) --------------------------------------
'''
separa = nome.split()                                     # split cria uma lista separando palavras inteiras
print(separa)                                             # (separa) é uma lista
print('Seu primeiro nome é {} e ele tem {} letras'        # busca primeira palavra da lista [0]
      .format(separa[0], len(separa[0])))                 # len conta quantas letras tem a primeira palavra
'''