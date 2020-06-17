#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
print('Descubra a parte inteira de um número!')
n = float(input('Digite um número qualquer: '))

print('A parte inteira desse número é: {}'.format(trunc(n)))
'''print('A parte inteira desse número é: {}'.format(int(n)))'''
