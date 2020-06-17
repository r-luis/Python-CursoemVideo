#Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lido
maior = 0
maior = 0
for pess in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa (em KG): '.format(pess)))
    if pess == 1: #primeiro valor
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso que entrar for maior, ele troca pelo anterior
            maior = peso #mesmo caso do outro
        if peso < menor:
            menor = peso
print('Maior peso: {}KG'.format(maior))
print('Menor peso: {}KG'.format(menor))