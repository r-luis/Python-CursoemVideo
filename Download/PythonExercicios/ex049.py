#Refaça o desafio 009, mostrando a tabuada que o usuário escolher
n = int(input('Digite um número inteiro e descubra sua tabuada: '))
print('-'*13)
print('tabuada do {}'.format(n).upper())
print('-'*13)
for c in range(1, 11):
    print('{} x {:>2} = {}'.format(n, c, (n*c)))
