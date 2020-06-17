'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
comp = randint(0, 5) #Computador pensa um número
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'roxo':'\033[1;35m'}

print('{}-*{}'.format(cores['azul'], cores['limpa'])*12)
txt = '{}JOGO DA ADVINHAÇÃO 1.0v{}'.format(cores['vermelho'], cores['limpa'])
print('{:^30}'.format(txt))
print('{}*-{}'.format(cores['azul'], cores['limpa'])*12)
usu = int(input('''Digite um número entre 0 e 5 e tente descobrir
se é o mesmo número escolhido pelo computador: ''')) #O usuário pensa em um número
print('{}PROCESSANDO...{}'.format(cores['roxo'], cores['limpa']))
sleep(2)
if comp == usu:
    print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('Você perdeu, o número escolhido pelo PC foi {} e não {}.'.format(comp, usu))
