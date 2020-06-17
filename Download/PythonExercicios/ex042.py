'''Refaça o desafio 35 dos triângulos. Acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
print('-'*20)
print('Cálculo de triângulo'.upper())
print('-'*20)
a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))
print('='*20)

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('\033[33mÉ possível haver um triângulo com essas retas e ele é: \033[m', end='')
    if a == b == c:
        print('\033[31mEQUILÁTERO\033[m')
    #elif a == b != c or a == c != b or b == c != a:
        #print('\033[31mISÓSCELES\033[m')
    elif a != b != c != a:
        print('\033[31mESCALENO\033[m')
    else:
        print('\033[31mISÓSCELES\033[m')
else:
    print('\033[31mNão é possível haver um triângulo com essas retas.\033[m')