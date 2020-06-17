'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
Para salários superiores a 1250, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
s = float(input('Digite o seu salário e saiba o aumento: R$'))
a1 = (s * 10) / 100
a2 = (s * 15) / 100
if s > 1250:
    print('Seu novo salário será R${}. Um aumento de 10%, ou, R${}'.format((s + a1), a1))
else:
    print('Seu novo salário será R${}. Um aumento de 15%, ou, R${}'.format((s + a2), a2))
