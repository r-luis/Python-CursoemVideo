'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor da reta b: '))
c = float(input('Digite o valor da reta c: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo.')
