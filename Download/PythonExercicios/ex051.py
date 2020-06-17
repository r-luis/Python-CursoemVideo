#Desenvola um programa que leia o primeiro termo e a razão de uma progressão aritimética
#no fimal, mostre os 10 primeiros termos dessa progressão
print('10 TERMOS DE UMA PA')
num = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
décimo = num + (10 - 1) * razão
for c in range(num, décimo + razão, razão):
    print('{}'.format(c), end=' - ')
print('END')
