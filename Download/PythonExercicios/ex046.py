#Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import emoji
from time import sleep
for c in range (10, 0, -1):
    print('\033[1;31m{}\033[m'.format(c))
    sleep(1)
print(emoji.emojize('\033[1;34mBOOM!!!\033[m :fireworks:', use_aliases=True))
