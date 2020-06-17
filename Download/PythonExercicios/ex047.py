#Crie um programa que mosre na tela todos os numeros pares que estão no intervalo entre 1 e 50
print('números pares entre 1 e 50:'.upper())
'''for c in range(1, 51):
    if c % 2 == 0:
        print('{}'.format(c), end=' ')'''
for n in range(2, 51, 2):
    print(n, end=' ')
print('fim')