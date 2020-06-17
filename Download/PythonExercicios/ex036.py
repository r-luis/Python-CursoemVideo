'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR da casa, o SALÁRIO do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
from time import sleep
print('\033[1;33m-='*24)
print('\033[7;30mCálculo de Empréstimo para ter sua Casa própria\033[m')
print('\033[1;33m=-\033[m'*24)

casa = float(input('Qual o valor da casa: R$'))
salário = float(input('Qual seu salário: R$'))
anos = int(input('Em quantos anos irá ser pago? '))
tri = salário - (salário * 70 / 100)
parc = casa / (anos * 12)

print('\033[1;35mCALCULANDO...\033[m')
sleep(2)

if parc > tri:
    print('\033[1;31mO empréstimo foi NEGADO\033[m, o valor máximo da parcela para você '
'deve ser de R${:.2f}, enquanto a parcela para esse financiamento é de R${:.2f}.'.format(tri, parc))
    print('Tente novamente.')
else:
    print('\033[1;34mO empréstimo foi APROVADO!\033[m')
    print('O valor do empréstimo será pago em {} parcelas de R${:.2f}.'.format(anos * 12, parc))
print('Obrigado por usar nossa ferramenta.')
