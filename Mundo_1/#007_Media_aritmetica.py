

#
n1 = float(input('Digite primeiro valor:'))
n2 = float(input('Digite segundo valor:'))
media = (n1+n2)/2
# ao usar dois pontos dentro dos couchetes{} colocamos um ponto  e a quantidade de caracteres
# que desejamos visualizar depois o f.Exemplo : {:.3f} ->teremos 3 caracteres
print('A media entre {} e {} é igual a :{:.2f}'.format(n1,n2,media))
