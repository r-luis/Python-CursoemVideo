#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'nº {pess}, digite seu ano de nascimento: '))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas são maiores de idade e {} são menores: '.format(totmaior, totmenor))
