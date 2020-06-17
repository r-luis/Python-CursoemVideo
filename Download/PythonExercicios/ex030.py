'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.'''
from time import sleep
print('Descubra se o número é par ou ímpar:')
print('-='*20)
num = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1)
if (num % 2) == 0:
    print('Seu número é par.')
else:
    print('Seu número é impar.')
