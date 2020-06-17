'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Qual o seu sexo? [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dadós inválidos, digite novamente: ')).strip().upper()[0]
print('Obrigado! Sexo {} registrado.'.format(sexo))
