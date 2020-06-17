"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
Quantas letras ao todo, sem considerar espaços;
Quantas letras tem o primeiro nome:"""

n = str(input('Digite seu nome completo: ')).strip()
#div = n.split()

print(n.upper())
print(n.lower())
#print('Número de letras: {}'.format(len(''.join(div))))
print('Número de letras: {}'.format(len(n) - n.count(' ')))
#print('Número de letras do primeiro nome: {}'.format(len(div[0])))
print('Número de letras do primeiro nome: {}'.format(n.find(' ')))