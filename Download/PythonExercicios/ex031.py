'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 por
km para viagens de até 200km e 0,45 para viagens mais longas.'''
print('-=' * 15)
print('Saiba o custo da sua viagem')
print('-=' * 15)

d = int(input('Digite a distância da sua viagem: '))
if d <= 200:
    print('O custo da viagem de {}km será de R${:.2f}'.format(d, d * 0.5))
else:
    print('O custo da viagem de {}km será de R${:.2f}'.format(d, d * 0.45))

print('Obrigado por usar nossa ferramenta!')
