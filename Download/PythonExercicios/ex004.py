#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ela
n = (input('Digite algo: '))

print('O tipo é: \033[1;30m{}\033[m'.format(type(n)))
print('É numérico? \033[1;31m{}\033[m'.format(n.isnumeric()))
print('É escrito? \033[1;32m{}\033[m'.format(n.isalpha()))
print('É alfanumérico? \033[1;33m{}\033[m'.format(n.isalnum()))
print('É decimal? \033[1;34m{}\033[m'.format(n.isdecimal()))