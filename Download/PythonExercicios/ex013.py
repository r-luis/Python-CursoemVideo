#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
print('Parabéns, você terá aumento de salário!')
s = float(input('Digite o seu salário atual: R$'))
a = s*15/100
sf = s + a

print('O seu novo salário será de R${}. Um aumento de R${:.2f}. Parabéns!'.format(sf, a))
