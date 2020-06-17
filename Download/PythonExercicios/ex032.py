'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
from datetime import date
print('Cálculo de ano bissexto'.upper())
ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print('''O ano {} foi ou será ano bissexto, já que:
- É múltiplo de 4 e;
- É múltiplo de 100 e de 400'''.format(ano))
else:
    print('''O ano {} não é ano bissexto já que:
- Não é múltiplo de 4 ou;
- É múltiplo de 4, mas é múltiplo de 100 mas não de 400.'''.format(ano))


'''if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Ano Bissexto")
else:
    print("Não é um ano Bissexto!")'''

#Ano bissexto são anos múltiplos de 4, exceto anos múltiplos de 100 que não são múltiplos de 400.