#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math
a = float(input('Digite o valor de um ângulo e descubra o seno, cosseno e a tangente: '))
s = math.sin(math.radians(a))
print('O ângulo de {}º tem o seno {:.2f};'.format(a, s))
cs = math.cos(math.radians(a))
print('O cosseno {:.2f};'.format(cs))
tg = math.tan(math.radians(a))
print('E a tangente {:.2f}.'.format(tg))
