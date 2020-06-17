'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
r = 0
while r != 5:
    print('''[1] SOMA
[2] MULTIPLICAÇÃO
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    r = int(input('Qual sua opção? '))
    if r == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif r == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, mult))
    elif r == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = n1
            print('Os dois são iguais, ou seja:')
        print('Entre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif r == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif r == 5:
        print('FINALIZANDO...')
        sleep(1)
    else:
        print('Opção INVÁLIDA. Tente de novo.')
    print('-='*20)
    sleep(2)
print('Finalizado, obrigado por usar!')