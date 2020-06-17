"""O mesmo professor do ex. anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

list = [a1, a2, a3, a4]
random.shuffle(list)

print('A sequência de apresentação é: {}'.format(list))