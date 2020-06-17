#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
#pares, se for ímpar, desconsidere-o
soma = 0 #contadores dos números
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0: #só conta os números pares
        soma += num #soma = soma + num
        cont += 1 #cont = cont + 1
print('Você informou {} número(s) PARES e a soma foi {}.'.format(cont, soma))