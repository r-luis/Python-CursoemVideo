'''Melhore o jogo do desafio 28, onde o computador vai "pensar" em um número de 0 e 10
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
comp = randint(0, 10) #Computador pensa um número
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
while not comp == usu:
    print('Você perdeu, o número escolhido pelo PC foi {} e não {}.'.format(comp, usu))
    usu = int(input('Escolha um novo número: '))
    comp = randint(0,10)
if comp == usu:
    print('PARABÉNS, VOCÊ VENCEU!')
