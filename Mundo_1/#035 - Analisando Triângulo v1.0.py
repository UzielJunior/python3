'''
Exercício Python 035: Desenvolva um programa que leia o
comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo
'''

r1= int(input('digite um valor para uma reta:'))
r2= int(input('digite outro valor para uma reta:'))
r3= int(input('digite outro valor para uma reta:'))

#Verificando menor

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
   print('\nÉ possivel formar uma reta')
else:
    print('\nNao é possivel formar uma reta')