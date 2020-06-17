#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
tot = 0 #PRECISA DE CONTADOR PORRA
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('\n\033[mO número {} foi divisível {} vezes e é PRIMO.'.format(num, tot))
else:
    print('\n\033[mO número {} foi divisível {} vezes e NÃO É PRIMO'.format(num, tot))
