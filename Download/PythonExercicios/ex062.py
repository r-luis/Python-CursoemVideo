'''Melhore o desafio 61, perguntando se o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''
from time import sleep
print('PA Generator')
pri = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = pri
cont = 1
total = 0
sum = 10
while sum != 0:
    total += sum
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('...')
    sum = int(input('Quantos termos você quer mostrar a mais? '))
print('End. {} termos'.format(total))