'''Faça um programa que leia um número qualquer e mostre o seu fatorial;
Ex: 5! = 5x4x3x2x1 = 120'''
'''n = int(input('Digite um número e calcule seu fatorial: ')) #while
mult = n #CONTADOOOOOOOOOOOOOOOOOOR
f = 1
print('Calculando {}!: '.format(n), end='')
while mult > 0:
    print('{}'.format(mult), end='')
    print(' x ' if mult > 1 else ' = ', end='')
    f *= mult
    mult -= 1
print('{}'.format(f))'''

n = int(input("Fatorial de: ")) #for
resultado = 1
print("{}! = ".format(n), end="")
for c in range(n, 0, -1):
    resultado *= c
    if(c != 1):
        print("{} X ".format(c), end="")
    else:
        print("{} ".format(c), end="")
print("= {}".format(resultado))