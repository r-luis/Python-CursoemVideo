#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Dólar considere - R$3.27
print('Conversor de moeda dólar-real')
m = float(input('Digite o valor em reais que você tem na carteira: R$'))
d = float(m/3.27)

print('R${:.2f} é equivalente a US${:.2f}.'.format(m, d))
