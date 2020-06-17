'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('\033[31mDigite um número: \033[m'))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('{} soma. {} números. {} maior. {} menor. {} média'.format(soma, quant, maior, menor, media))