#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Digite o preço do produto (em reais): R$'))
d = p - ((p*5)/100)
#f = p-d

print('O preço final com 5% de desconto é de R${:.2f}.'.format(d))
