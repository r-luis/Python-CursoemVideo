'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu número deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número de 0 a 20: '))

while n not in range (0, 20 + 1):
    n = int(input('Digito errado, digite novamente: '))

print('O número em extenso é', (extenso[n]))