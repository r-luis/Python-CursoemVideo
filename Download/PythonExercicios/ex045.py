'''Crie um programa que faça o computador jogar Jokenpô com você'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
#Entrada
print('\033[1;30m-=\033[m'*6)
print('\033[1;31mJOKENPO GAME\033[m')
print('\033[1;30m=-\033[m'*6)
#Jogo
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
usu = int(input('Qual a sua opção? '))
#bricadeira
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*20)
print('''Você escolheu {} 
O PC escolheu {}'''.format(itens[usu], itens[pc]))
print('=-'*20)
#vitórias do pc
if pc == 0: #PEDRA
    if usu == 0:
        print('EMPATE')
    elif usu == 1:
        print('JOGADOR VENCE')
    elif usu == 2:
        print('PC VENCE')
    else: print('JOGADA INVÁLIDA')
elif pc == 1: #PAPEL
    if usu == 1:
        print('EMPATE')
    elif usu == 2:
        print('JOGADOR VENCE')
    elif usu == 0:
        print('PC VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2: #TESOURA
    if usu == 2:
        print('EMPATE')
    elif usu == 0:
        print('JOGADOR VENCE')
    elif usu == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('Erro na escolha, tente novamente.')