

a= int(input('digite um valor:'))
b= int(input('digite outro valor:'))
c= int(input('digite outro valor:'))
#Verificando menor
menor = a
if b < a and b < c:
    menor = b
if  c < a and c < b:
    menor = c


# Verificando maior
maior = a
if b>a and b>c:
    maior=b
if  c>a and c>b:
    maior=c

print('O manor valor digitado foi:{} e o maior é:{}'.format(menor,maior))

