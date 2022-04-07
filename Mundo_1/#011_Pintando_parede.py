
largura = float(input('Qual a largura da parede:'))
altura  = float(input('Qual a altura da parede:'))

area = largura*altura
tinta= area/2        # Cada dois m² de parede precisa de 1l de tinta

print('Sua parede tem a dimensao de {}x{} e sua are é de {}m².'.format(largura,altura,area))
print('Para pintar parede, voce precisara de {}l de tinta.'.format(tinta))
