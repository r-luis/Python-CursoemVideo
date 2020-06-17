#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
print('Cálculo de hipotenusa')
print('-'*20)
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#h = (co**2 + ca**2) ** (1/2)
h = hypot(co, ca)
print('O valor da hipotenusa dos catetos {} e {} é {:.2f}'.format(co, ca, h))
