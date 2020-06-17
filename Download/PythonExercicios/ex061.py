'''Refaça o desafio 51, lendo o primeiro termo e a razão da PA, mostrando os 10
primeiros termos da progressão usando while.'''
print('10 TERMOS DE UMA PA')
num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
décimo = num + (10 - 1) * razão
cont = 0
while cont < 10:
    cont += 1
    num += razão
    print('{} '.format(num), end='- ')
print('END')