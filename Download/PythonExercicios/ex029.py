'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar 7,00 por cada km acima do limite.'''
from time import sleep
v = int(input('Digite a velocidade do carro: '))
multa = (v - 80) * 7
if v < 80:
    print('O carro está no limite de velocidade.')
else:
    print('O carro está fora do limite de velocidade.')
    print('Calculando multa...')
    sleep(2)
    print('Multa: R${:.2f}.'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
