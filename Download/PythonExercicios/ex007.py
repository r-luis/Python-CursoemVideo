# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
print('***Calculadora de Notas***\n')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

nf = (n1+n2)/2

print('-'*20)
print('A média do aluno é {:.1f}.'.format(nf))

if (nf>=5):
    print('O aluno foi aprovado!')
else:
    print('O aluno foi reprovado.')



