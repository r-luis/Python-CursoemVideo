'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''
a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite mais um número: '))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
        menor = c
#verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor é {menor}.')
print(f'O maior valor é {maior}.')
