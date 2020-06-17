'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
all = (n1, n2, n3, n4)
vezes = all.count(9)
#primeiro = all.index(3)
pares = 0
qpares = ''

if all.count(3) > 0:
    tres = all.index(3)
    frase = f'O valor 3 aparece na {tres + 1}ª posição.'
else:
    frase = 'O valor 3 não aparece em menhuma posição.'

if vezes == 1:
    desc = 'vez'
else:
    desc = 'vezes'

for n in all:
    if n %2 == 0:
        pares += 1
        qpares += ' ' + str(n)

if pares > 0:
    frasepares = f'Os valores pares digitados foram: {qpares}'
else:
    frasepares = 'Não há nenhum número par'

print(f'Os valores foram {all}')
print(f'O valor 9 apareceu {vezes} {desc}')
print(frase)
print(frasepares)

