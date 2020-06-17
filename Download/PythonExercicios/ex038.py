'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior;
- o segundo valor é maior;
- Não existe valor maior, os dois são iguais'''
a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))
if a > b:
    print('O primeiro valor, {}, é maior.'.format(a))
elif b > a:
    print('O segundo valor, {}, é maior.'.format(b))
else:
    print('Os dois valores são iguais.')
