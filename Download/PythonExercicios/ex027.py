'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro: Ana
último: Souza '''

nome = str(input('Digite o seu nome completo: ')).strip().title()
sp = nome.split()
print('Nice to meet you!')
print('Primeiro nome: {}'.format(sp[0]))
print('Último nome: {}'.format(sp[len(sp)-1])) #ele lê a quantidade de nomes, mostra a quantidade - 1, que é a posição do último nome
