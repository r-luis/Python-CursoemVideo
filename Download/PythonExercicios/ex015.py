#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('Cálculo de aluguel de carro\n', '-'*25)
d = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos KM rodados? '))
v = (d*60) + (km*0.15)
print('-'*20)
print('O valor a pagar pelo aluguel é de R${:.2f}'.format(v))
