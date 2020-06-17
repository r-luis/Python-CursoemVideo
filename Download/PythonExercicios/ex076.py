'''Desafio 76 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
produto = ('25 coins', 25, '50 coins', 50, '75 coins', 75, '80 coins', 80, '100 coins', 100, '250 coins', 250)

i, f = 0, 1
sep = '-' * 40
tam = len(produto)

print(sep)
print(f'{"TIBIA COINS":^40}')

print(sep)
while f < tam:
    print(f'{produto[i]:.<31}R$ {produto[f]:.2f}', end='\n')
    i += 2
    f += 2
print(sep)








