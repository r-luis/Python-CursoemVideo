#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
n = int(input('Digite um número: '))

print('\033[7;30mO sucessor do número {} é {}, e o antecessor é {}\033[m'.format(n, n+1, n-1))
